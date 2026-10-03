"""Hypothetical inputs only. Helpers write into caller-owned temporary folders."""
import hashlib
import json
from pathlib import Path

RESUME = ('Product Designer\nExample Studio | Senior Product Designer | 2021-2025\n'
          'Owned interaction design and component governance for operator software.\n'
          'Engineers deployed the service. Evaluated an earlier prototype with five users.\n'
          'Case: the supplied operator-workflow example explains my design decisions.\n')
PROFILE = ('Headline: Product Designer | Design Systems\nAbout: I design operator workflows and reusable components.\n'
           'Experience: Example Studio | Senior Product Designer | 2021-2025\n'
           'Owned interaction design and component governance. Engineers deployed the service.\n'
           'Skills: interaction design, design systems.\nFeatured: supplied operator-workflow case.\n')
PORTFOLIO = ('Operator-workflow case. Owned interaction design and component governance.\n'
             'Engineers deployed the service after an earlier prototype evaluation with five users.\n')
TARGET = ('Product Designer. Required: interaction design and evidence of individual decisions.\n'
          'Preferred: production deployment ownership. Design systems experience is relevant.\n')


def build(engine, mod, folder, asset='resume', mode='general', original=True, target=True, comparison=True):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    plan = mod.criteria(engine, asset, mode)
    manifest = []
    refs = {}

    def add(ident, owner, kind, body, **extra):
        file = folder / (ident + '.txt')
        file.write_bytes(body.encode('utf-8'))
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        row = {'id': ident, 'asset': owner, 'kind': kind, 'file': file.name,
               'sha256': digest, 'label': ident.replace('-', ' '), **extra}
        manifest.append(row)
        if kind != 'original-file':
            refs[ident] = {'inputId': ident, 'file': file.name, 'sha256': digest,
                           'startLine': 1, 'endLine': len(body.splitlines()), 'quote': body}
    if asset in ('resume', 'both'):
        add('resume', 'resume', 'resume-text', RESUME)
        if original:
            add('resume-original', 'resume', 'original-file', RESUME)
            add('extraction', 'resume', 'extraction-observation',
                'The supplied plain-text original was read as UTF-8. Its extracted text preserves all five lines in order.\n',
                context='Local observation of the supplied plain-text original, not a proprietary ATS test.', derivedFrom='resume-original')
    if asset in ('linkedin', 'both'):
        add('profile', 'linkedin', 'profile-text', PROFILE)
    if mode == 'target-role' and target:
        add('target', 'target', 'target-requirements', TARGET)
    if mode == 'consistency' and comparison and asset != 'both':
        other = ('profile', 'linkedin', 'profile-text', PROFILE) if asset == 'resume' else ('resume', 'resume', 'resume-text', RESUME)
        add(*other)
    add('portfolio', 'portfolio', 'portfolio-text', PORTFOLIO)
    coverage = []
    units = engine.corpus('assessment')
    for criterion in plan['criteria']:
        guidance = next(u for u in units if u['file'] == 'assessment/criteria.md' and criterion['id'] in u['headings'])
        knowledge = [{'unitId': guidance['unitId'], 'fileSha256': guidance['fileSha256'], 'quote': criterion['positive']}]
        owner = criterion['asset']
        subject = [refs['resume' if owner == 'resume' else 'profile']] if owner != 'cross' else [refs[x] for x in ('resume', 'profile') if x in refs]
        if 'target' in criterion['requirements'] and 'target' in refs:
            subject.append(refs['target'])
        if 'extraction' in criterion['requirements'] and 'extraction' in refs:
            subject.append(refs['extraction'])
        missing = [r for r in criterion['requirements'] if not mod.available(r, owner, {x['id']: x for x in manifest})]
        row = {'checkId': criterion['checkId'], 'result': 'meets-criterion',
               'explanation': criterion['examples']['adequate'], 'knowledge': knowledge, 'subject': subject}
        # Fixture observations describe this supplied plain-text original,
        # not the catalogue's illustrative PDF example.
        if criterion['id'] == 'resume.extraction':
            row['explanation'] = 'The supplied plain-text original preserves its five lines in extraction order.'
        if criterion['id'] == 'shared.chronology':
            row['explanation'] = 'The supplied employment dates and role are identifiable and consistent.'
        if missing:
            row.update(result='insufficient-evidence', missingEvidenceType='missing-input', missingInputs=missing,
                       reason='Unavailable inspection inputs: ' + ', '.join(missing))
        coverage.append(row)
    positive = [x['checkId'] for x in coverage if x['result'] == 'meets-criterion']
    return {'schemaVersion': 2, 'asset': asset, 'mode': mode, 'catalogueSha256': plan['catalogueSha256'],
            'inputs': manifest, 'coverage': coverage, 'findings': [],
            'summary': {'purpose': 'Assess the supplied hypothetical professional material.',
                        'conclusions': [{'text': 'The inspected material identifies design work and contribution.', 'checkIds': positive[:1]}],
                        'strengths': [{'text': 'The professional identity is connected to design responsibilities.', 'checkIds': positive[:1]}]}}


def finding(record, criterion='shared.claims', kind='material-correction', certainty='demonstrated'):
    check = next(x for x in record['coverage'] if x['checkId'].endswith(':' + criterion))
    check['result'] = 'needs-attention'
    row = {'id': 'F1', 'checkIds': [check['checkId']], 'kind': kind, 'priority': 'optional' if kind == 'optional-preference' else 'address-first',
           'certainty': certainty, 'finding': 'Clarify the project responsibility.',
           'consequence': 'The reader could confuse design responsibility with engineering deployment.',
           'nextStep': 'Name the part personally owned.', 'knowledge': check['knowledge'], 'subject': check['subject']}
    record['findings'] = [row]
    if row['priority'] == 'address-first':
        record['summary']['conclusions'].append({'text':row['finding'],'checkIds':row['checkIds']})
    return row
