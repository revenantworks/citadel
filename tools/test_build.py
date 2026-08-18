#!/usr/bin/env python3
"""Unit tests for build.py's registry parsers — the single point every manifest
derives from. Guards the regex-table bug class that has bitten twice: the
budgets table matching the roster regex (16 = 16 = 16 on an eight-member pack)
and the parser edits that shipped unexercised ("unit blindness").

Run: python3 -m unittest discover -s tools -p "test_*.py"
Stdlib only, no fixtures on disk — the synthetic registry below is the fixture.
"""
import unittest

import build

SYNTH = """# Pack Registry

## Build defaults

| Parameter | Value |
|---|---|
| Brand token *(label)* | `revenantworks` |

## Pack registry

| Pack | Profile | Notes |
|---|---|---|
| `demo` | standalone | Test pack. Conformance checks (2026-01-02): D-1 first · D-2 second. Integrate policy: restamp: lazy |
| `other` | standalone | Second pack, no conformance line of its own |

**demo members**

| Member | Job | Route there when |
|---|---|---|
| `revenantworks-demo-alpha` | Does alpha | The deliverable is alpha |
| `revenantworks-demo-beta` | Does beta | The deliverable is beta |

**demo budgets**

| Member | Tokens | Why it earns the room |
|---|---|---|
| `revenantworks-demo-alpha` | 3000 | reasons |
| `revenantworks-demo-beta` | 2000 | reasons |

**demo seams**

| Seam | Left owns | Right owns | Router keys on | Cold-listing signal |
|---|---|---|---|---|
| alpha ↔ beta | the alpha half | the beta half | the object | both descriptions |

**demo capstone:** none.

**demo canonical repo:** `github.com/example/demo`
"""


class RegistryParsers(unittest.TestCase):
    def test_registry_packs(self):
        # Documented quirk: the parser scans everything after "## Pack registry",
        # so backticked member/budget rows are collected too — harmless because
        # downstream treats an empty members table as "not a pack". The contract
        # under test: the real pack row parses with its profile intact.
        packs = build.registry_packs(SYNTH)
        self.assertEqual(packs["demo"], "standalone")

    def test_pack_members_stops_before_budgets(self):
        # The budgets table's rows also match `| `name` | x | y |` — the roster
        # parser must stop at the budgets marker or every member counts twice.
        members = build.pack_members(SYNTH, "demo")
        self.assertEqual([m[0] for m in members],
                         ["revenantworks-demo-alpha", "revenantworks-demo-beta"])

    def test_pack_budgets(self):
        budgets = build.pack_budgets(SYNTH, "demo")
        self.assertEqual(budgets["revenantworks-demo-alpha"][0], 3000)
        self.assertEqual(budgets["revenantworks-demo-beta"][0], 2000)

    def test_pack_seams(self):
        seams = build.pack_seams(SYNTH, "demo")
        self.assertEqual(len(seams), 1)
        self.assertEqual(seams[0][:2], ("alpha", "beta"))
        self.assertEqual(seams[0][5], "both descriptions")

    def test_unknown_pack_is_empty(self):
        self.assertEqual(build.pack_members(SYNTH, "nope"), [])

    def test_registry_pack_notes_is_per_pack(self):
        # The Notes cell, not the Profile cell — pack_lines reads conformance from here.
        self.assertIn("Conformance checks (2026-01-02)", build.registry_pack_notes(SYNTH, "demo"))
        self.assertNotIn("Conformance", build.registry_pack_notes(SYNTH, "other"))
        self.assertEqual(build.registry_pack_notes(SYNTH, "nope"), "")

    def test_pack_lines_does_not_borrow_another_packs_conformance(self):
        # The bug the second pack exposed (2026-08-07): pack_lines was handed the
        # Profile cell, never matched, and fell through to a whole-document search
        # that returns the FIRST pack's conformance line — so pack #2's manifest was
        # stamped with pack #1's checks. A pack with no line of its own must get the
        # stated default, never a neighbour's.
        _, _, (adopted, checks) = build.pack_lines(SYNTH, "demo", build.registry_pack_notes(SYNTH, "demo"))
        self.assertEqual((adopted, checks), ("2026-01-02", "D-1 first · D-2 second"))
        _, _, other = build.pack_lines(SYNTH, "other", build.registry_pack_notes(SYNTH, "other"))
        self.assertEqual(other, build.DEFAULT_CHECKS)


class LiveRegistry(unittest.TestCase):
    """The real registry, parsed with the real parsers — count integrity at
    the unit level, independent of --check's aggregate run."""

    @classmethod
    def setUpClass(cls):
        cls.text = build.registry_text()

    def test_foundation_registered(self):
        self.assertIn("foundation", build.registry_packs(self.text))

    def test_roster_budgets_agree(self):
        members = {m[0] for m in build.pack_members(self.text, "foundation")}
        budgets = set(build.pack_budgets(self.text, "foundation"))
        self.assertEqual(members, budgets)
        self.assertEqual(len(members), 10)

    def test_seams_reference_roster_members(self):
        members = {m[0].split("-")[-1] for m in build.pack_members(self.text, "foundation")}
        for seam in build.pack_seams(self.text, "foundation"):
            self.assertIn(seam[0], members, seam[:2])
            self.assertIn(seam[1], members, seam[:2])

    def test_ossuary_registered(self):
        self.assertIn("ossuary", build.registry_packs(self.text))

    def test_ossuary_roster_budgets_agree(self):
        members = {m[0] for m in build.pack_members(self.text, "ossuary")}
        budgets = set(build.pack_budgets(self.text, "ossuary"))
        self.assertEqual(members, budgets)
        self.assertEqual(len(members), 2)

    def test_each_pack_has_its_own_conformance_line(self):
        # Guards the borrowed-conformance bug on the LIVE registry, not just the fixture:
        # two packs must not resolve to the same (adopted, checks) pair by accident.
        seen = {}
        for pack in ("foundation", "ossuary"):
            notes = build.registry_pack_notes(self.text, pack)
            self.assertIn("Conformance checks (", notes, pack)
            seen[pack] = build.pack_lines(self.text, pack, notes)[2]
        self.assertNotEqual(seen["foundation"], seen["ossuary"])


if __name__ == "__main__":
    unittest.main()
