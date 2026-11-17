"""Static regression checks: does not evaluate any actual agent/model response."""
import importlib.util
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import files, SOURCE, ROOT as BUILD_ROOT
from score import score


class PackageTests(unittest.TestCase):
    def test_all_adapters_match_canonical(self):
        self.assertEqual(BUILD_ROOT, ROOT)
        for path, expected in files(SOURCE.read_text(encoding='utf-8').rstrip() + '\n').items():
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), f'Missing {path}')
                self.assertEqual(path.read_text(encoding='utf-8'), expected)

    def test_skill_frontmatter(self):
        for path in ROOT.glob('**/SKILL.md'):
            with self.subTest(path=path):
                content = path.read_text(encoding='utf-8')
                self.assertTrue(content.startswith('---\n'))
                name = re.search(r'^name: (.+)$', content, re.MULTILINE)
                desc = re.search(r'^description: (.+)$', content, re.MULTILINE)
                self.assertIsNotNone(name)
                self.assertIsNotNone(desc)
                self.assertEqual(name.group(1), path.parent.name)
                self.assertLessEqual(len(desc.group(1)), 1024)
                self.assertNotIn('tools:', content.split('---', 2)[1])

    def test_scoring_example(self):
        self.assertEqual(score([2, 2, None, 1, 1]), (8, 'Provisional', 4))
        self.assertEqual(score([2, 2, 2, 2, 2]), (10, 'Evidence-based', 5))
        self.assertEqual(score([0, 0, 0, 0, 0]), (1, 'Evidence-based', 5))
        self.assertEqual(score([2, None, None, None, 0]), (None, 'Not scored — insufficient evidence', 2))
        with self.assertRaises(ValueError):
            score([2, 3, 1, 1, 1])

    def test_core_behavior_contract(self):
        core = SOURCE.read_text(encoding='utf-8')
        for phrase in ['Create mode', 'Review mode', 'Observed', 'Inferred',
                       'Needs testing', 'WCAG 2.2 AA', 'Not scored',
                       'one, both', 'two meaningfully different approaches',
                       'Do not automatically claim', 'ux-companion/prototypes/']:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), core.lower())

    def test_preserved_original_matches_upload(self):
        # Expect the original Kiro YAML header and first-response rule to remain archived.
        original = (ROOT / 'legacy/ux-companion-kiro-original.md').read_text(encoding='utf-8')
        self.assertTrue(original.startswith('---\nname: ux-companion'))
        self.assertIn('## First Response — Introduce and Ask Which Mode', original)


if __name__ == '__main__':
    unittest.main()
