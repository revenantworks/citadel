"""release.py must survive a machine where the private-repo env vars are unset.

That is the DEFAULT state — the vars point at private repos that exist only on the
owner's rig. Before 2026-08-18 the paths were hardcoded, so "unset" could not happen.
Making them environment-read fixed a leak on this public repo and introduced a crash:
refresh_brand() called .is_file() on None and died with AttributeError, taking the
brand-escrow step with it. build.py's own 13 tests never touched release.py, so nothing
caught it. These tests are that gap closed.
"""
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARS = ("CLAUDE_SKILLS_BRAND_REPO_SOURCE", "CLAUDE_SKILLS_PEER_SOURCE_NORTHSTAR",
        "CLAUDE_SKILLS_LONGSHOT")


def _bare_env():
    """The environment of a fresh clone: none of the private-repo vars set."""
    env = dict(os.environ)
    for v in VARS:
        env.pop(v, None)
    return env


class TestUnsetPathVars(unittest.TestCase):
    def test_import_survives_unset_vars(self):
        """Import must not raise. A path derived from an unset var stays None."""
        r = subprocess.run(
            [sys.executable, "-c",
             "import sys; sys.path.insert(0, r'%s'); import release; "
             "print('LONGSHOT', release.LONGSHOT); print('SKILLS', release.LONGSHOT_SKILLS)"
             % (ROOT / "tools")],
            capture_output=True, text=True, env=_bare_env(), cwd=ROOT)
        self.assertEqual(r.returncode, 0, f"import failed:\n{r.stderr}")
        self.assertIn("LONGSHOT None", r.stdout)
        self.assertIn("SKILLS None", r.stdout)

    def test_refresh_brand_skips_instead_of_crashing(self):
        """The exact regression: AttributeError on None.is_file()."""
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "release.py"), "--refresh-brand"],
                           capture_output=True, text=True, env=_bare_env(), cwd=ROOT)
        self.assertNotIn("AttributeError", r.stderr)
        self.assertEqual(r.returncode, 0, f"--refresh-brand failed:\n{r.stdout}\n{r.stderr}")
        self.assertIn("not configured on this machine", r.stdout)

    def test_no_absolute_local_path_in_tracked_files(self):
        """This repo is public. A drive path in a tracked file publishes the owner's
        layout and the existence of private repos. Dated CHANGELOGs are frozen history."""
        out = subprocess.run(["git", "grep", "-n", "-I", "-E", r"V:[\/]Projects", "--",
                              ".", ":(exclude)*CHANGELOG*"],
                             capture_output=True, text=True, cwd=ROOT).stdout.strip()
        self.assertEqual(out, "", f"absolute local path in tracked file(s):\n{out}")


if __name__ == "__main__":
    unittest.main()
