#!/usr/bin/env python3
"""Behavioral checks for retrieval, paired evidence and a movable skill bundle."""

import copy
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
            "busy navigation": "emphasize-by-de-emphasizing",
            "form labels confusing": "avoid-ambiguous-spacing",
            "crowded dashboard": "not-all-elements-are-equal",
            "first use empty state": "dont-overlook-empty-states",
            "hero photo text unreadable": "text-needs-consistent-contrast",
            "chunky icon size": "everything-has-an-intended-size",
            "numbers table alignment": "align-with-readability-in-mind",
            "action bar buttons crowded next to filters, groups unclear": "avoid-ambiguous-spacing",
            "filter bar wraps toolbar squeezed": "avoid-ambiguous-spacing",
            "too many buttons in the toolbar": "semantics-are-secondary",
            "card inside card with borders": "use-fewer-borders",
            "menu popover floats flat": "use-shadows-to-convey-elevation",
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                matches = finder.search(self.data["rules"], query, 2)
                self.assertIn(expected, [r["id"] for r in matches])

    def test_visual_evidence_keeps_the_navigation_pair(self):
        rule = finder.search(self.data["rules"], "busy navigation", 1)[0]
        figures = finder.select_figures(rule, "busy navigation")
        self.assertEqual([f["id"] for f in figures], ["fig-046-041", "fig-046-042"])
        self.assertEqual([f["role"] for f in figures], ["before", "after"])

    def test_unrelated_or_empty_query_does_not_invent_matches(self):
        for query in ("", "the and of", "quasar spectrograph"):
            with self.subTest(query=query):
                self.assertEqual(finder.search(self.data["rules"], query), [])

    def test_bundled_corpus_integrity(self):
        self.assertEqual(finder.validate(self.data), {"rules": 50, "figures": 283, "topics": 9})

    def test_integrity_check_detects_broken_evidence(self):
        mutations = [
            ("missing file", lambda d: d["rules"][0]["figures"][0].update(path="references/figures/missing.webp")),
            ("changed image", lambda d: d["rules"][0]["figures"][0].update(sha256="0" * 64)),
            ("broken anchor", lambda d: d["rules"][0].update(reference="references/starting-from-scratch.md#missing")),
            ("missing counterpart", lambda d: d["rules"][1]["figures"][-1].update(role="example")),
            ("incomplete curated pair", lambda d: d["rules"][1].update(featured_figures=["fig-013-005"])),
        ]
        for label, mutate in mutations:
            with self.subTest(label=label):
                data = copy.deepcopy(self.data)
                mutate(data)
                with self.assertRaises(ValueError):
                    finder.validate(data)

    def test_cli_rejects_invalid_inputs(self):
        for args in (("--rule", "missing"), ("nav", "--topic", "missing"), ("nav", "--limit", "0"), ("nav", "--rule", "emphasize-by-de-emphasizing")):
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
            checked = subprocess.run([*command, "--check"], cwd=base, capture_output=True, text=True)
            self.assertEqual(checked.returncode, 0, checked.stderr)
            process = subprocess.run([*command, "form labels confusing", "--limit", "1", "--json"], cwd=base, capture_output=True, text=True, check=True)
            item = json.loads(process.stdout)["results"][0]
            self.assertEqual(item["id"], "avoid-ambiguous-spacing")
            self.assertEqual([f["id"] for f in item["figures"]], ["fig-097-096", "fig-097-097"])
            for figure in item["figures"]:
                path = Path(figure["path"])
                self.assertTrue(path.is_file())
                self.assertTrue(path.is_relative_to(bundle.resolve()))


if __name__ == "__main__":
    unittest.main()
