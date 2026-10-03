"""Per-requirement job-description audit. Hypothetical inputs only."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

from assessment_fixtures import build

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('requirement_knowledge', PACKAGE/'scripts/knowledge.py')
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)
m = k.assessment_module()


class RequirementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        self.engine = k.engine_module()
        self.record = build(self.engine, m, self.folder, mode='target-role')

    def tearDown(self):
        self.temp.cleanup()

    def verify(self, record):
        return m.verify(self.engine, record, self.folder)

    def rejected(self, record):
        with self.assertRaises(k.RetrievalError):
            self.verify(record)

    def test_requirements_verify_and_render(self):
        self.assertEqual(self.verify(self.record)['validatedRequirements'], 2)
        text = m.report(self.engine, self.record, self.folder)
        section = text[text.index('## 6.'):text.index('## 7.')]
        self.assertIn('| interaction design | Required | Demonstrated |', section)
        self.assertIn('| production deployment ownership | Preferred | Not shown |', section)
        self.assertLess(section.index('Required |'), section.index('Preferred |'))

    def test_target_role_requires_requirement_rows(self):
        for value in ([], None):
            record = copy.deepcopy(self.record)
            record['requirements'] = value
            self.rejected(record)

    def test_requirement_text_must_be_quoted_from_target(self):
        record = copy.deepcopy(self.record)
        record['requirements'][0]['text'] = 'ten years of interaction design'
        self.rejected(record)
        record = copy.deepcopy(self.record)
        record['requirements'][1]['subject'] = []
        self.rejected(record)

    def test_positive_status_requires_asset_evidence(self):
        record = copy.deepcopy(self.record)
        record['requirements'][0]['subject'] = record['requirements'][0]['subject'][:1]
        self.rejected(record)
        for status in ('transferable', 'contradicted'):
            record = copy.deepcopy(self.record)
            record['requirements'][1]['status'] = status
            self.rejected(record)

    def test_invalid_rows_fail_cleanly(self):
        for field, value in (('status', 'met'), ('type', 'essential'), ('explanation', ''), ('id', 'R2'), ('subject', 'x')):
            record = copy.deepcopy(self.record)
            record['requirements'][0][field] = value
            self.rejected(record)
        record = copy.deepcopy(self.record)
        record['requirements'][0]['subject'][1]['quote'] = 'Deployed the service personally'
        self.rejected(record)

    def test_requirements_only_in_target_role_with_target(self):
        general = build(self.engine, m, self.folder)
        general['requirements'] = copy.deepcopy(self.record['requirements'])
        self.rejected(general)
        limited = build(self.engine, m, self.folder, mode='target-role', target=False)
        self.assertEqual(self.verify(limited)['assessmentCompleteness'], 'limited')
        limited['requirements'] = copy.deepcopy(self.record['requirements'])
        self.rejected(limited)


if __name__ == '__main__':
    unittest.main()
