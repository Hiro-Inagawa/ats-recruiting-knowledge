"""Record scaffold and quotation location. Hypothetical inputs only."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from assessment_fixtures import RESUME, PROFILE

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('scaffold_knowledge', PACKAGE/'scripts/knowledge.py')
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)
m = k.assessment_module()
s = k.scaffold_module()


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        self.engine = k.engine_module()
        (self.folder/'resume.txt').write_text(RESUME, encoding='utf-8')
        (self.folder/'profile.txt').write_text(PROFILE, encoding='utf-8')
        self.manifest = self.folder/'inputs.json'
        self.manifest.write_text(json.dumps([
            {'id': 'resume', 'asset': 'resume', 'kind': 'resume-text', 'file': 'resume.txt', 'label': 'Résumé text'},
            {'id': 'profile', 'asset': 'linkedin', 'kind': 'profile-text', 'file': 'profile.txt', 'label': 'Profile text'}]), encoding='utf-8')
        self.output = self.folder/'record.json'

    def tearDown(self):
        self.temp.cleanup()

    def scaffold(self, asset='resume', mode='general'):
        return s.scaffold(self.engine, m, asset, mode, self.manifest, self.output)

    def test_scaffold_lists_every_check_and_fingerprints_inputs(self):
        result = self.scaffold('both', 'general')
        record = json.loads(self.output.read_text(encoding='utf-8'))
        plan = m.criteria(self.engine, 'both', 'general')
        self.assertEqual([x['checkId'] for x in record['coverage']], [x['checkId'] for x in plan['criteria']])
        self.assertEqual(result['checks'], len(plan['criteria']))
        self.assertEqual(record['catalogueSha256'], plan['catalogueSha256'])
        for row in record['inputs']:
            self.assertEqual(row['sha256'], hashlib.sha256((self.folder/row['file']).read_bytes()).hexdigest())
        for row in record['coverage']:
            self.assertEqual(len(row['knowledge']), 1)

    def test_unavailable_inputs_are_prefilled_and_rest_must_be_completed(self):
        result = self.scaffold()
        record = json.loads(self.output.read_text(encoding='utf-8'))
        extraction = next(x for x in record['coverage'] if x['checkId'] == 'resume:resume.extraction')
        self.assertEqual(extraction['result'], 'insufficient-evidence')
        self.assertEqual(extraction['missingInputs'], ['original', 'extraction'])
        self.assertEqual(result['prefilledUnavailable'], ['resume:resume.extraction'])
        with self.assertRaises(k.RetrievalError):
            m.verify(self.engine, record, self.folder)

    def test_completed_scaffold_verifies(self):
        self.scaffold()
        record = json.loads(self.output.read_text(encoding='utf-8'))
        place = s.locate(self.engine, self.folder/'resume.txt', 'Owned interaction design and component governance')
        ref = {'inputId': 'resume', 'file': 'resume.txt', 'sha256': place['sha256'], **place['matches'][0],
               'quote': 'Owned interaction design and component governance'}
        for row in record['coverage']:
            if row['result'] == '':
                row.update(result='meets-criterion', explanation='The supplied text supports this check.', subject=[ref])
        record['summary'] = {'purpose': 'Assess the supplied hypothetical résumé.',
                             'conclusions': [{'text': 'The design contribution is identifiable.', 'checkIds': ['resume:shared.contribution']}],
                             'strengths': []}
        self.assertEqual(m.verify(self.engine, record, self.folder)['assessmentCompleteness'], 'limited')

    def test_scaffold_never_overwrites(self):
        self.scaffold()
        with self.assertRaises(k.RetrievalError):
            self.scaffold()

    def test_invalid_manifest_fails_cleanly(self):
        for bad in ([], [{'id': 'resume'}], [{'id': 'x', 'asset': 'resume', 'kind': 'resume-text', 'file': 'missing.txt', 'label': 'x'}]):
            self.manifest.write_text(json.dumps(bad), encoding='utf-8')
            with self.assertRaises(k.RetrievalError):
                self.scaffold()
            self.assertFalse(self.output.exists())

    def test_locate_counts_newlines_and_spans_lines(self):
        file = self.folder/'extracted.txt'
        file.write_bytes('Name\fPage two heading\r\nFirst bullet\nSecond bullet\n'.encode('utf-8'))
        self.assertEqual(s.locate(self.engine, file, 'Page two heading')['matches'], [{'startLine': 1, 'endLine': 1}])
        self.assertEqual(s.locate(self.engine, file, 'First bullet\nSecond')['matches'], [{'startLine': 2, 'endLine': 3}])
        with self.assertRaises(k.RetrievalError):
            s.locate(self.engine, file, 'Not in the file')

    def test_cli_scaffold_and_locate(self):
        command = [sys.executable, '-B', str(PACKAGE/'scripts/knowledge.py')]
        made = subprocess.run(command + ['scaffold', '--asset', 'resume', '--mode', 'general', '--inputs', str(self.manifest),
                                         '--output', str(self.output), '--json'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(made.returncode, 0, made.stdout)
        found = subprocess.run(command + ['locate', '--file', str(self.folder/'resume.txt'), '--quote', 'Engineers deployed the service.', '--json'],
                               capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(json.loads(found.stdout)['matches'], [{'startLine': 4, 'endLine': 4}])
        again = subprocess.run(command + ['scaffold', '--asset', 'resume', '--inputs', str(self.manifest), '--output', str(self.output)],
                               capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(again.returncode, 2)
        self.assertFalse(json.loads(again.stdout)['ok'])


if __name__ == '__main__':
    unittest.main()
