"""Start a schema-v2 assessment record and locate exact quotations.

Standard library only. Writes only the new record file it is asked to
create and never overwrites an existing file. Judgments stay with the
assessor: results, explanations, subject quotations, findings and summary.
"""
import hashlib
import json
import os
from pathlib import Path

INPUT_FIELDS = ('id', 'asset', 'kind', 'file', 'label')
OPTIONAL_FIELDS = ('context', 'derivedFrom')
MAX_QUOTE_LINES = 50


def fail(engine, message):
    raise engine.RetrievalError(message)


def relative_to(path, folder):
    try:
        return os.path.relpath(path, folder)
    except ValueError:  # Different Windows drive
        return str(path)


def manifest_inputs(engine, manifest, output_dir):
    try:
        rows = json.loads(Path(manifest).read_text('utf-8-sig'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise engine.RetrievalError('Cannot read the inputs manifest') from exc
    if not isinstance(rows, list) or not rows:
        fail(engine, 'Inputs manifest must be a nonempty list')
    base = Path(manifest).resolve().parent
    result = []
    for row in rows:
        if not isinstance(row, dict) or any(not isinstance(row.get(f), str) or not row[f].strip() for f in INPUT_FIELDS):
            fail(engine, 'Each input needs id, asset, kind, file and label')
        path = Path(row['file']) if Path(row['file']).is_absolute() else base / row['file']
        try:
            raw = path.resolve().read_bytes()
        except OSError as exc:
            raise engine.RetrievalError('Cannot read input file: ' + row['id']) from exc
        entry = {f: row[f] for f in INPUT_FIELDS}
        entry.update({f: row[f] for f in OPTIONAL_FIELDS if f in row})
        entry['file'] = relative_to(path.resolve(), output_dir)
        entry['sha256'] = hashlib.sha256(raw).hexdigest()
        result.append(entry)
    return result


def guidance(engine, criterion):
    unit = next((u for u in engine.corpus('assessment') if u['file'] == 'assessment/criteria.md'
                 and criterion['guidanceHeading'] in u['headings']), None)
    if unit is None:
        fail(engine, 'Criterion explanation is missing: ' + criterion['checkId'])
    return {'unitId': unit['unitId'], 'fileSha256': unit['fileSha256'], 'quote': criterion['positive']}


def coverage_row(engine, assessment, criterion, manifest):
    missing = [req for req in criterion['requirements']
               if not assessment.available(req, criterion['asset'], manifest)]
    row = {'checkId': criterion['checkId'], 'result': '', 'explanation': '',
           'knowledge': [guidance(engine, criterion)], 'subject': []}
    if missing:
        reason = 'Unavailable inspection input: ' + ', '.join(missing) + '.'
        row.update(result='insufficient-evidence', explanation=reason, reason=reason,
                   missingEvidenceType='missing-input', missingInputs=missing)
    return row


def scaffold(engine, assessment, asset, mode, manifest, output):
    output = Path(output).resolve()
    if output.exists():
        fail(engine, 'Output record already exists. Choose a new file')
    inputs = manifest_inputs(engine, manifest, output.parent)
    # Reuse the checker's own input rules before anything is written.
    checked = assessment.inputs(engine, {'inputs': inputs}, output.parent)
    plan = assessment.criteria(engine, asset, mode)
    coverage = [coverage_row(engine, assessment, c, checked) for c in plan['criteria']]
    record = {'schemaVersion': 2, 'asset': asset, 'mode': mode, 'catalogueSha256': plan['catalogueSha256'],
              'inputs': inputs, 'coverage': coverage, 'findings': [],
              'summary': {'purpose': '', 'conclusions': [], 'strengths': []}}
    rows_needed = mode == 'target-role' and assessment.available('target', None, checked)
    if mode == 'target-role':
        record['requirements'] = []
    try:
        with open(output, 'x', encoding='utf-8') as handle:
            json.dump(record, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    except OSError as exc:
        raise engine.RetrievalError('Cannot write the new record') from exc
    prefilled = [row['checkId'] for row in coverage if row['result']]
    return {'record': str(output), 'checks': len(coverage), 'prefilledUnavailable': prefilled,
            'toComplete': [row['checkId'] for row in coverage if not row['result']],
            'requirementRowsNeeded': rows_needed, 'sections': plan['sections']}


def locate(engine, file, quote):
    engine.require_text(quote, 'quote')
    try:
        raw = Path(file).read_bytes()
        lines = engine.subject_lines(raw.decode('utf-8-sig'))
    except (OSError, UnicodeError) as exc:
        raise engine.RetrievalError('Cannot read the supplied text') from exc
    matches = []
    for start in range(len(lines)):
        for end in range(start, min(start + MAX_QUOTE_LINES, len(lines))):
            window = ''.join(lines[start:end + 1])
            if quote in window:
                # Keep only the smallest window: a later start must not also contain it.
                if quote not in ''.join(lines[start + 1:end + 1]):
                    matches.append({'startLine': start + 1, 'endLine': end + 1})
                break
    if not matches:
        fail(engine, 'Quote not found in the supplied text')
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'matches': matches}
