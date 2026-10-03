"""Criteria, evidence-bearing coverage and deterministic report rendering.

Standard library only. Input files and records are read, never modified.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
from types import SimpleNamespace

ASSETS = ('resume', 'linkedin', 'both')
MODES = ('general', 'target-role', 'consistency')
KINDS = ('resume-text', 'profile-text', 'live-profile-capture', 'original-file',
         'extraction-observation', 'target-requirements', 'portfolio-text', 'user-fact')
RESULTS = ('meets-criterion', 'needs-attention', 'insufficient-evidence', 'not-applicable')
PRIORITIES = ('address-first', 'improve-next', 'optional')
ASSET_NAMES = {'resume': 'Résumé', 'linkedin': 'LinkedIn'}
REQUIREMENT_TYPES = ('required', 'preferred')
REQUIREMENT_STATUS = {'demonstrated': 'Demonstrated', 'transferable': 'Transferable',
                      'not-shown': 'Not shown', 'contradicted': 'Contradicted'}
LABELS = {'meets-criterion': 'Meets criterion', 'needs-attention': 'Needs attention',
          'insufficient-evidence': 'Insufficient evidence', 'not-applicable': 'Not applicable'}


def fail(engine, message):
    raise engine.RetrievalError(message)


def text(engine, value, name):
    engine.require_text(value, name)


def transaction(engine):
    """Reuse parsed passages within one validation, still checking live bytes.

    No persistent index or cross-call cache. The original read command remains
    unchanged. Exact references are checked against their current file bytes.
    """
    units = engine.corpus()
    by_id = {u['unitId']: u for u in units}
    proxy = SimpleNamespace(**vars(engine))
    proxy.corpus = lambda area=None: [u for u in units if area is None or u['area'] == area]

    def read(ident, expected, offset=0, max_chars=6000):
        unit = by_id.get(ident)
        if unit is None:
            fail(engine, 'Evidence unit is not in the current knowledge collection')
        _, digest = engine.load(engine.ROOT / unit['file'])
        if digest != expected or unit['fileSha256'] != expected:
            fail(engine, 'Source changed since search. Search again before reading')
        body = unit['text']
        stop = min(offset + max_chars, len(body))
        return {**unit, 'text': body[offset:stop], 'offset': offset,
                'nextOffset': stop if stop < len(body) else None}

    proxy.read = read

    def verify_refs(record):
        return engine.verify_assessment(record, reader=read)

    proxy.verify_assessment = verify_refs
    return proxy


def catalogue(engine):
    try:
        raw = engine.CATALOGUE.read_bytes()
        value = json.loads(raw.decode('utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise engine.RetrievalError('Criteria catalogue is missing or invalid') from exc
    if not isinstance(value, dict) or value.get('schemaVersion') != 1:
        fail(engine, 'Invalid criteria catalogue version')
    rows = value.get('criteria')
    sections = value.get('sections')
    if not isinstance(rows, list) or not rows or not isinstance(sections, list) or len(sections) != 8:
        fail(engine, 'Invalid criteria or report sections')
    units = engine.corpus()
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            fail(engine, 'Invalid criterion')
        for field in ('id', 'title', 'purpose', 'positive', 'problem', 'evidenceType', 'guidanceHeading'):
            text(engine, row.get(field), 'criterion.' + field)
        ident = row['id']
        if ident in seen or not re.fullmatch(r'[a-z]+\.[a-z]+', ident):
            fail(engine, 'Duplicate or invalid criterion ID')
        seen.add(ident)
        if type(row.get('section')) is not int or row['section'] not in range(2, 7):
            fail(engine, 'Invalid criterion section')
        for field, allowed in (('assets', ('resume', 'linkedin', 'cross')), ('modes', MODES),
                               ('requirements', ('content', 'original', 'extraction', 'target', 'comparison'))):
            choices = row.get(field)
            if not isinstance(choices, list) or not choices or len(set(choices)) != len(choices) or any(x not in allowed for x in choices):
                fail(engine, 'Invalid criterion ' + field)
        if type(row.get('allowNotApplicable')) is not bool:
            fail(engine, 'Invalid non-applicability policy')
        for field in ('adequate', 'problematic', 'uncertain'):
            text(engine, row.get('examples', {}).get(field), 'criterion example')
        route = row.get('route', {})
        if not any(u['file'] == route.get('file') and route.get('heading') in u['headings'] for u in units):
            fail(engine, 'Criterion owning route does not resolve: ' + ident)
        guidance = next((u for u in units if u['file'] == 'assessment/criteria.md'
                         and row['guidanceHeading'] in u['headings']), None)
        if guidance is None or any(row[field] not in guidance['text'] for field in ('purpose', 'positive', 'problem')):
            fail(engine, 'Criterion guidance disagrees with catalogue: ' + ident)
        if any(example not in guidance['text'] for example in row['examples'].values()):
            fail(engine, 'Criterion examples disagree with catalogue: ' + ident)
    return value, hashlib.sha256(raw).hexdigest()


def criteria(engine, asset, mode):
    if asset not in ASSETS or mode not in MODES:
        fail(engine, 'Invalid assessment asset or mode')
    value, digest = catalogue(engine)
    assets = ('resume', 'linkedin') if asset == 'both' else (asset,)
    checks = []
    for row in value['criteria']:
        if mode not in row['modes']:
            continue
        owners = ('cross',) if 'cross' in row['assets'] else assets
        for owner in owners:
            if owner not in row['assets']:
                continue
            checks.append({'checkId': owner + ':' + row['id'], 'asset': owner, **row})
    return {'asset': asset, 'mode': mode, 'catalogueSha256': digest,
            'sections': value['sections'], 'criteria': checks}


def path_at(value, base):
    path = Path(value)
    return (path if path.is_absolute() else base / path).resolve()


def inputs(engine, record, base):
    rows = record.get('inputs')
    if not isinstance(rows, list) or not rows:
        fail(engine, 'Assessment requires inspected inputs')
    result = {}
    for row in rows:
        if not isinstance(row, dict):
            fail(engine, 'Invalid input record')
        for field in ('id', 'file', 'sha256', 'label'):
            text(engine, row.get(field), 'input.' + field)
        ident = row['id']
        if ident in result or row.get('kind') not in KINDS or row.get('asset') not in ('resume', 'linkedin', 'portfolio', 'target', 'context'):
            fail(engine, 'Duplicate input or invalid input kind/asset')
        compatible = {'resume-text': ('resume',), 'profile-text': ('linkedin',),
                      'live-profile-capture': ('linkedin',), 'original-file': ('resume', 'linkedin', 'portfolio'),
                      'extraction-observation': ('resume',), 'target-requirements': ('target',),
                      'portfolio-text': ('portfolio',), 'user-fact': ('context',)}
        if row['asset'] not in compatible[row['kind']]:
            fail(engine, 'Input kind is incompatible with its asset')
        try:
            raw = path_at(row['file'], base).read_bytes()
            if row['kind'] != 'original-file':
                raw.decode('utf-8-sig')
        except (OSError, UnicodeError) as exc:
            raise engine.RetrievalError('Cannot read inspected input') from exc
        if hashlib.sha256(raw).hexdigest() != row['sha256']:
            fail(engine, 'Inspected input changed since assessment')
        if row['kind'] in ('live-profile-capture', 'extraction-observation', 'user-fact'):
            text(engine, row.get('context'), 'input.context')
        result[ident] = row
    for row in rows:
        if row['kind'] == 'extraction-observation':
            original = result.get(row.get('derivedFrom'))
            if original is None or original['kind'] != 'original-file' or original['asset'] != row['asset']:
                fail(engine, 'Extraction observation requires its inspected original')
    return result


def available(requirement, owner, manifest):
    rows = list(manifest.values())
    content_kinds = ('resume-text', 'profile-text', 'live-profile-capture', 'portfolio-text')
    if requirement == 'comparison':
        return len({x['asset'] for x in rows if x['kind'] in content_kinds}) >= 2
    if requirement == 'target':
        return any(x['kind'] == 'target-requirements' for x in rows)
    if requirement == 'content':
        return any(x['asset'] == owner and x['kind'] in content_kinds for x in rows)
    wanted = 'original-file' if requirement == 'original' else 'extraction-observation'
    return any(x['asset'] == owner and x['kind'] == wanted for x in rows)


def evidence(engine, entry, manifest, base, require_subject=True):
    # The legacy checker remains the single exact-attribution implementation.
    probe = {'kind': 'evidence-clarification', 'finding': 'Coverage evidence',
             'consequence': 'Inspect supporting passages', 'nextStep': 'Apply the criterion',
             'knowledge': entry.get('knowledge'), 'subject': copy.deepcopy(entry.get('subject', [])),
             'missingSubjectEvidence': entry.get('reason', 'Input not supplied')}
    if require_subject and not probe['subject']:
        fail(engine, 'Assessed check requires subject evidence')
    for ref in probe['subject']:
        if not isinstance(ref, dict):
            fail(engine, 'Invalid subject evidence')
        row = manifest.get(ref.get('inputId'))
        if row is None or row['kind'] == 'original-file':
            fail(engine, 'Subject evidence requires a registered inspected text input')
        if path_at(ref.get('file', ''), base) != path_at(row['file'], base) or ref.get('sha256') != row['sha256']:
            fail(engine, 'Subject evidence disagrees with inspected input')
        ref['file'] = str(path_at(ref['file'], base))
    return engine.verify_assessment({'schemaVersion': 1, 'findings': [probe]})


def relevant(engine, check, refs):
    route = check['route']
    for ref in refs:
        unit = engine.read(ref['unitId'], ref['fileSha256'], max_chars=50000)
        if ((unit['file'] == route['file'] and route['heading'] in unit['headings']) or
            (unit['file'] == 'assessment/criteria.md' and check['guidanceHeading'] in unit['headings'])):
            return
    fail(engine, 'Check lacks its owning knowledge or criterion explanation: ' + check['checkId'])


def inspect_assertions(engine, assertions, checks, positive=False):
    if not isinstance(assertions, list):
        fail(engine, 'Conclusion and strengths must be lists')
    for assertion in assertions:
        if not isinstance(assertion, dict):
            fail(engine, 'Invalid summary assertion')
        text(engine, assertion.get('text'), 'summary text')
        refs = assertion.get('checkIds')
        if not isinstance(refs, list) or not refs or any(not isinstance(x, str) for x in refs) or len(set(refs)) != len(refs) or any(x not in checks for x in refs):
            fail(engine, 'Summary assertion requires valid checked criteria')
        allowed = ('meets-criterion',) if positive else ('meets-criterion', 'needs-attention', 'insufficient-evidence')
        if any(checks[x]['result'] not in allowed for x in refs):
            fail(engine, 'Summary assertion uses an unsupported check result')


def inspect_requirements(engine, record, checks, manifest, record_dir):
    """One row per posting requirement, quoted exactly from the supplied target."""
    rows = record.get('requirements')
    if record['mode'] != 'target-role' or not available('target', None, manifest):
        if rows not in (None, []):
            fail(engine, 'Requirement rows need target-role mode with supplied target requirements')
        return 0
    if not isinstance(rows, list) or not rows:
        fail(engine, 'Target-role assessment requires one row per posting requirement')
    owner = next(x for ident, x in checks.items() if ident.endswith(':target.requirements'))
    selected = ('resume', 'linkedin') if record['asset'] == 'both' else (record['asset'],)
    ids = set()
    for row in rows:
        if not isinstance(row, dict):
            fail(engine, 'Invalid requirement row')
        for field in ('id', 'text', 'explanation'):
            text(engine, row.get(field), 'requirement ' + field)
        if row['id'] in ids:
            fail(engine, 'Duplicate requirement ID')
        ids.add(row['id'])
        if row.get('type') not in REQUIREMENT_TYPES or row.get('status') not in REQUIREMENT_STATUS:
            fail(engine, 'Invalid requirement type or status')
        subject = row.get('subject')
        if not isinstance(subject, list) or not subject or any(not isinstance(x, dict) for x in subject):
            fail(engine, 'Requirement requires subject evidence')
        # Exact attribution reuses the target check's validated knowledge.
        evidence(engine, {'knowledge': owner['knowledge'], 'subject': subject}, manifest, record_dir)
        sources = [(ref, manifest[ref['inputId']]) for ref in subject]
        if not any(x['kind'] == 'target-requirements' and ref['quote'] == row['text'] for ref, x in sources):
            fail(engine, 'Requirement text must be quoted exactly from the supplied target')
        if row['status'] != 'not-shown' and not any(x['asset'] in selected + ('portfolio',) for _, x in sources):
            fail(engine, 'Requirement status needs evidence from the assessed material')
    return len(rows)


def verify(engine, record, record_dir):
    if not isinstance(record, dict) or record.get('schemaVersion') != 2:
        fail(engine, 'Structured assessments require schemaVersion 2')
    live_engine = engine
    engine = transaction(engine)
    plan = criteria(engine, record.get('asset'), record.get('mode'))
    if record.get('catalogueSha256') != plan['catalogueSha256']:
        fail(engine, 'Criteria catalogue changed. Retrieve criteria again')
    manifest = inputs(engine, record, record_dir)
    selected = ('resume', 'linkedin') if record['asset'] == 'both' else (record['asset'],)
    for owner in selected:
        if not available('content', owner, manifest):
            fail(engine, 'Selected asset requires inspected content: ' + owner)
    expected = {x['checkId']: x for x in plan['criteria']}
    rows = record.get('coverage')
    if not isinstance(rows, list) or any(not isinstance(x, dict) for x in rows):
        fail(engine, 'Coverage must be a list of checks')
    for row in rows:
        text(engine, row.get('checkId'), 'check ID')
    checks = {x.get('checkId'): x for x in rows}
    if len(checks) != len(rows) or set(checks) != set(expected):
        fail(engine, 'Required coverage omitted, duplicated or unknown')
    totals = {'knowledge': 0, 'subject': 0}
    limited = []
    for ident, row in checks.items():
        definition = expected[ident]
        if row.get('result') not in RESULTS:
            fail(engine, 'Invalid check result')
        text(engine, row.get('explanation'), 'check explanation')
        missing = [req for req in definition['requirements'] if not available(req, definition['asset'], manifest)]
        result = row['result']
        if missing and (result != 'insufficient-evidence' or row.get('missingEvidenceType') != 'missing-input'):
            fail(engine, 'Unavailable inspection cannot be passed or marked not applicable: ' + ident)
        if result == 'not-applicable':
            if not definition['allowNotApplicable']:
                fail(engine, 'Foundational check cannot be skipped: ' + ident)
            text(engine, row.get('reason'), 'non-applicability reason')
        if result == 'insufficient-evidence':
            text(engine, row.get('reason'), 'missing evidence reason')
            if row.get('missingEvidenceType') not in ('missing-input', 'unestablished-claim'):
                fail(engine, 'Distinguish missing input from unestablished claim')
            if row['missingEvidenceType'] == 'missing-input':
                requests = row.get('missingInputs')
                if not isinstance(requests, list) or not requests or any(not isinstance(x, str) or not x.strip() for x in requests):
                    fail(engine, 'Name the unavailable inspection inputs')
                limited.append(ident)
        observed = not (result == 'insufficient-evidence' and row['missingEvidenceType'] == 'missing-input')
        counted = evidence(engine, row, manifest, record_dir, require_subject=observed)
        relevant(engine, definition, row['knowledge'])
        kinds = {manifest[r['inputId']]['kind'] for r in row.get('subject', [])}
        owners = {manifest[r['inputId']]['asset'] for r in row.get('subject', [])}
        if observed:
            if definition['asset'] != 'cross' and definition['asset'] not in owners:
                fail(engine, 'Check evidence must inspect its selected asset')
            if 'target' in definition['requirements'] and 'target-requirements' not in kinds:
                fail(engine, 'Target comparison requires target evidence')
            if 'comparison' in definition['requirements'] and len(owners.intersection(('resume', 'linkedin', 'portfolio'))) < 2:
                fail(engine, 'Consistency check requires evidence from two assets')
            if 'extraction' in definition['requirements'] and 'extraction-observation' not in kinds:
                fail(engine, 'Extraction check requires its observation evidence')
        totals['knowledge'] += counted['validatedKnowledgeReferences']
        totals['subject'] += counted['validatedSubjectReferences']
    findings = record.get('findings')
    if not isinstance(findings, list):
        fail(engine, 'Findings must be a list, possibly empty')
    ids = set()
    linked = set()
    for finding in findings:
        if not isinstance(finding, dict):
            fail(engine, 'Invalid finding')
        text(engine, finding.get('id'), 'finding ID')
        if finding['id'] in ids:
            fail(engine, 'Duplicate finding ID')
        ids.add(finding['id'])
        if finding.get('kind') not in engine.KINDS or finding.get('priority') not in PRIORITIES or finding.get('certainty') not in ('demonstrated', 'conditional'):
            fail(engine, 'Invalid finding classification, priority or certainty')
        if finding['kind'] == 'material-correction' and finding['certainty'] != 'demonstrated':
            fail(engine, 'Material correction requires a demonstrated problem')
        if finding['kind'] == 'optional-preference' and finding['priority'] != 'optional':
            fail(engine, 'Optional preference must remain optional')
        if finding['kind'] == 'presentation-improvement' and finding['priority'] == 'address-first':
            fail(engine, 'Presentation improvement cannot be ranked address-first')
        refs = finding.get('checkIds')
        if not isinstance(refs, list) or not refs or any(not isinstance(x, str) for x in refs) or len(set(refs)) != len(refs) or any(x not in checks for x in refs):
            fail(engine, 'Finding requires valid check references')
        for ident in refs:
            result = checks[ident]['result']
            if result not in ('needs-attention', 'insufficient-evidence'):
                fail(engine, 'Finding contradicts its check result')
            if result == 'insufficient-evidence' and finding['kind'] != 'evidence-clarification':
                fail(engine, 'Insufficient evidence supports clarification, not a demonstrated defect')
        for field in ('finding', 'consequence', 'nextStep'):
            text(engine, finding.get(field), field)
        evidence(engine, finding, manifest, record_dir,
                 require_subject=finding['kind'] != 'evidence-clarification')
        for ident in refs:
            relevant(engine, expected[ident], finding['knowledge'])
        if not finding.get('subject'):
            text(engine, finding.get('missingSubjectEvidence'), 'missingSubjectEvidence')
        linked.update(refs)
        supersedes = finding.get('supersedes', [])
        if not isinstance(supersedes, list) or any(not isinstance(x, str) or not x.strip() for x in supersedes):
            fail(engine, 'Invalid superseded finding IDs')
    if any(row['result'] == 'needs-attention' and ident not in linked for ident, row in checks.items()):
        fail(engine, 'Needs-attention check requires a linked finding')
    requirement_count = inspect_requirements(engine, record, checks, manifest, record_dir)
    summary = record.get('summary')
    if not isinstance(summary, dict) or not summary.get('conclusions'):
        fail(engine, 'Assessment requires supported conclusions')
    text(engine, summary.get('purpose'), 'assessment purpose')
    inspect_assertions(engine, summary['conclusions'], checks)
    inspect_assertions(engine, summary.get('strengths'), checks, positive=True)
    summarized = {ident for assertion in summary['conclusions'] for ident in assertion['checkIds']}
    if any(finding['priority'] == 'address-first' and not summarized.intersection(finding['checkIds']) for finding in findings):
        fail(engine, 'Overall assessment must include address-first findings')
    changes = record.get('reassessment', [])
    if not isinstance(changes, list):
        fail(engine, 'Reassessment must be a list')
    for change in changes:
        if not isinstance(change, dict):
            fail(engine, 'Invalid reassessment entry')
        for field in ('previousFindingId', 'explanation'):
            text(engine, change.get(field), 'reassessment.' + field)
        if change.get('state') not in ('resolved', 'remaining', 'new'):
            fail(engine, 'Invalid reassessment state')
        inspect_assertions(engine, [{'text': change['explanation'], 'checkIds': change.get('checkIds')}], checks)
    before = {u['file']: u['fileSha256'] for u in engine.corpus()}
    after = {u['file']: u['fileSha256'] for u in live_engine.corpus()}
    if before != after or hashlib.sha256(live_engine.CATALOGUE.read_bytes()).hexdigest() != plan['catalogueSha256']:
        fail(engine, 'Knowledge or criteria changed during validation. Retrieve current evidence again')
    return {'validationScope': 'coverage-and-attribution', 'assessmentCompleteness': 'limited' if limited else 'complete',
            'unavailableChecks': limited, 'validatedChecks': len(checks), 'validatedFindings': len(findings),
            'validatedKnowledgeReferences': totals['knowledge'], 'validatedSubjectReferences': totals['subject'],
            'validatedRequirements': requirement_count,
            'asset': record['asset'], 'mode': record['mode']}


def display(engine, value):
    # Do not turn private record paths/fingerprints into public chat prose.
    if re.search(r'(?i)\b[A-Z]:[\\/]|\\\\[^\s]+|(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])|/(?:Users|home|tmp|var|private|mnt)/', value):
        fail(engine, 'Report text contains a machine path or fingerprint. Keep it in private records')
    return ' '.join(value.split()).replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;')


def report(engine, record, record_dir, detail='concise'):
    result = verify(engine, record, record_dir)
    plan = criteria(engine, record['asset'], record['mode'])
    if plan['catalogueSha256'] != record['catalogueSha256']:
        fail(engine, 'Criteria changed before report rendering')
    checks = {x['checkId']: x for x in record['coverage']}
    safe = lambda value: display(engine, value)
    lines = ['# ' + ('Résumé' if record['asset'] == 'resume' else 'LinkedIn' if record['asset'] == 'linkedin' else 'Résumé and LinkedIn') + ' assessment', '']
    for number, title in enumerate(plan['sections'], 1):
        if number == 5:
            title = {'resume': 'Résumé-specific checks', 'linkedin': 'LinkedIn-specific checks', 'both': 'Résumé and LinkedIn checks'}[record['asset']]
        lines.extend(['## ' + str(number) + '. ' + title, ''])
        if number == 1:
            lines.extend([safe(record['summary']['purpose']), '', 'Inspected material: ' + ', '.join(safe(x['label']) for x in record['inputs']) + '.', ''])
            if result['assessmentCompleteness'] == 'limited':
                lines.extend(['This assessment is limited by unavailable inspection inputs.', ''])
                for ident in result['unavailableChecks']:
                    lines.append('- ' + safe(checks[ident]['reason']))
                lines.append('')
            for assertion in record['summary']['conclusions']:
                lines.extend([safe(assertion['text']), ''])
        elif 2 <= number <= 6:
            rows = [x for x in plan['criteria'] if x['section'] == number]
            if not rows:
                lines.extend(['No target-role comparison was requested.' if number == 6 else 'No checks apply in this assessment mode.', ''])
                continue
            lines.extend(['| Check | Result | Assessment |', '| --- | --- | --- |'])
            for criterion in rows:
                check = checks[criterion['checkId']]
                title = criterion['title']
                if record['asset'] == 'both' and criterion['asset'] != 'cross':
                    title = ASSET_NAMES[criterion['asset']] + ': ' + title
                explanation = safe(check['explanation'])
                if check['result'] in ('not-applicable', 'insufficient-evidence'):
                    reason = safe(check['reason'])
                    if reason != explanation:
                        explanation += ' ' + reason
                lines.append('| ' + title + ' | ' + LABELS[check['result']] + ' | ' + explanation + ' |')
            lines.append('')
            if number == 6 and record.get('requirements'):
                ordered = sorted(record['requirements'], key=lambda x: REQUIREMENT_TYPES.index(x['type']))
                lines.extend(['| Posting requirement | Type | Status | Assessment |', '| --- | --- | --- | --- |'])
                lines.extend('| ' + safe(x['text']) + ' | ' + x['type'].capitalize() + ' | ' + REQUIREMENT_STATUS[x['status']]
                             + ' | ' + safe(x['explanation']) + ' |' for x in ordered)
                lines.append('')
        elif number == 7:
            findings = sorted(record['findings'], key=lambda x: (PRIORITIES.index(x['priority']), x['id']))
            if not findings:
                lines.extend(['No changes are recommended from the inspected evidence.', ''])
            for finding in findings:
                lines.extend(['### ' + safe(finding['id']) + '. ' + safe(finding['finding']), '',
                              finding['kind'].replace('-', ' ').capitalize() + ' · ' + finding['priority'].replace('-', ' ') + ' · ' + finding['certainty'], ''])
                quotes = [safe(ref['quote']) for ref in finding.get('subject', [])]
                if quotes:
                    lines.extend(['Inspected evidence: ' + ' / '.join('“' + q + '”' for q in quotes), ''])
                else:
                    lines.extend([safe(finding['missingSubjectEvidence']), ''])
                lines.extend([safe(finding['consequence']), '', 'Next step: ' + safe(finding['nextStep']), ''])
            for change in record.get('reassessment', []):
                lines.extend([safe(change['previousFindingId']) + ' (' + change['state'] + '): ' + safe(change['explanation']), ''])
        else:
            strengths = record['summary']['strengths']
            lines.extend(['- ' + safe(x['text']) for x in strengths] or ['No supported strength has been established in the supplied material.'])
            lines.append('')
    if detail == 'evidence':
        lines.extend(['## Supporting evidence', ''])
        seen = set()
        for entry in record['coverage'] + record['findings']:
            for ref in entry.get('knowledge', []):
                key = (ref['unitId'], ref['quote'])
                if key in seen:
                    continue
                seen.add(key)
                lines.extend(['- ' + ref['unitId'] + ': “' + safe(ref['quote']) + '”'])
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'
