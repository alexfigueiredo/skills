#!/usr/bin/env python3
"""Behavioral checks for retrieval, mode notes, paired figures and a movable skill bundle."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
import find_examples as finder


class ExampleLookupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(finder.INDEX.read_text(encoding="utf-8"))

    def test_problem_queries_find_relevant_rules(self):
        cases = {
            "busy navigation": "de-emphasize-competitors",
            "form labels confusing": "avoid-ambiguous-spacing",
            "crowded dashboard": "rank-content-by-importance",
            "first use empty state": "design-empty-states",
            "hero photo text unreadable": "keep-text-contrast-over-images",
            "chunky icon size": "use-graphics-at-their-intended-size",
            "numbers table alignment": "align-for-reading",
            "action bar buttons crowded next to filters, groups unclear": "avoid-ambiguous-spacing",
            "filter bar wraps toolbar squeezed": "avoid-ambiguous-spacing",
            "too many buttons in the toolbar": "style-actions-by-priority",
            "card inside card with borders": "group-with-space-not-borders",
            "menu popover floats flat": "map-shadows-to-elevation",
            "landing page looks generic like a template": "avoid-template-defaults",
            "logo and hero art dimmed after the refactor": "preserve-brand-material",
            "eyebrow label above every heading": "structure-matches-content",
            "mobile nav items cut off": "keep-navigation-reachable",
            "card layout breaks in a narrow sidebar column": "switch-layout-by-available-width",
            "hero art hidden on mobile": "crop-art-per-viewport",
            "dark mode surfaces blur together": "design-dark-themes-separately",
            "hover focus and loading states missing": "design-every-state",
            "submit button label unclear": "name-actions-by-result",
            "sections fade in on scroll": "animate-to-explain-state",
            "webgl shader background": "reserve-3d-for-visual-subjects",
            "make it prettier": "avoid-template-defaults",
            "every section is loud, nothing stands out": "concentrate-expression",
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                matches = finder.search(self.data["rules"], query, 2)
                self.assertIn(expected, [r["id"] for r in matches])

    def test_visual_evidence_keeps_the_navigation_pair(self):
        rule = finder.search(self.data["rules"], "busy navigation", 1)[0]
        figures = finder.select_figures(rule, "busy navigation")
        self.assertEqual([f["id"] for f in figures], ["de-emphasize-competitors-1", "de-emphasize-competitors-2"])
        self.assertEqual([f["role"] for f in figures], ["before", "after"])

    def test_mode_note_is_added_only_for_the_requested_mode(self):
        rule = next(r for r in self.data["rules"] if r["id"] == "separate-visual-hierarchy-from-document-hierarchy")
        self.assertIn("display headline", finder.result(rule, mode="convert")["mode_note"])
        self.assertIsNone(finder.result(rule, mode="operate")["mode_note"])
        self.assertIsNone(finder.result(rule)["mode_note"])

    def test_rules_without_figures_return_no_figures(self):
        rule = next(r for r in self.data["rules"] if r["id"] == "preserve-brand-material")
        self.assertEqual(finder.result(rule, "brand art")["figures"], [])

    def test_unrelated_or_empty_query_does_not_invent_matches(self):
        for query in ("", "the and of", "quasar spectrograph"):
            with self.subTest(query=query):
                self.assertEqual(finder.search(self.data["rules"], query), [])

    def test_cli_rejects_invalid_inputs(self):
        for args in (("--rule", "missing"), ("nav", "--topic", "missing"), ("nav", "--limit", "0"), ("nav", "--rule", "de-emphasize-competitors"), ("nav", "--mode", "marketing")):
            with self.subTest(args=args):
                process = subprocess.run([sys.executable, "-B", str(Path(finder.__file__)), *args], capture_output=True, text=True)
                self.assertEqual(process.returncode, 2)
                self.assertIn("error:", process.stderr)

    def test_bundle_works_after_move_and_through_symlink(self):
        with tempfile.TemporaryDirectory(prefix="refactoring-ui-test-") as directory:
            base = Path(directory)
            bundle = base / "skills with spaces" / "refactoring-ui"
            shutil.copytree(finder.ROOT, bundle)
            link = base / "installed-skill"
            link.symlink_to(bundle, target_is_directory=True)
            command = [sys.executable, "-B", str(link / "scripts/find_examples.py")]
            process = subprocess.run([*command, "form labels confusing", "--limit", "1", "--json"], cwd=base, capture_output=True, text=True, check=True)
            item = json.loads(process.stdout)["results"][0]
            self.assertEqual(item["id"], "avoid-ambiguous-spacing")
            self.assertEqual([f["id"] for f in item["figures"]], ["avoid-ambiguous-spacing-2", "avoid-ambiguous-spacing-3"])
            for figure in item["figures"]:
                path = Path(figure["path"])
                self.assertTrue(path.is_file())
                self.assertTrue(path.is_relative_to(bundle.resolve()))


if __name__ == "__main__":
    unittest.main()
