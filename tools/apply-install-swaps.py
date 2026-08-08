#!/usr/bin/env python3
"""citadel — apply-install-swaps: overlay private config onto neutral members.

Brand-carriage law (owner decision, 2026-07-23): the ONLY brand carrier
anywhere is the locally configured brandwright. Every other member is
brandless in the repo AND in your installs; branded artifacts (prompt cards
included) are produced at need via `brandwright apply`, never stored.

One swap surface:

  brandwright   references/brand-definition.md   (active identity + voice)

Usage:
  python3 tools/apply-install-swaps.py <swaps-dir>

<swaps-dir> holds your private copy named exactly `brand-definition.md`. The
script verifies it differs from the repo's neutral copy (hard-fail otherwise —
a neutral overlay means you pointed it at the wrong file), overlays it onto a
temp copy of brandwright, and zips to `dist/install/<member>-<ver>+install.zip`.
Every other member uploads from its plain `dist/` zip. A `prompt-card.md` in
the swaps dir is ignored with a note — that swap retired under the law above.
The repo tree is never modified. Stdlib only.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

# Same guard build.py carries: this script prints box glyphs, and a Windows console
# defaulting to cp1252 raises UnicodeEncodeError on the success line — AFTER the zip
# is written, so the run looks failed while the artifact is fine. Worse failure mode
# than a plain crash: the operator re-runs, or ships nothing.
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
SK = ROOT / "packs" / "foundation" / "skills"
OUT = ROOT / "dist" / "install"

SWAPS = {
    "brand-definition.md": ("revenantworks-foundation-brandwright", "references/brand-definition.md"),
}
RETIRED = {"prompt-card.md": "retired 2026-07-23 — only brandwright carries brand; branded cards come from `brandwright apply` at need"}


def member_version(folder: Path) -> str:
    fm = (folder / "SKILL.md").read_text(encoding="utf-8").split("---")[1]
    m = re.search(r'version:\s*"?([\d.]+)"?', fm)
    return m.group(1) if m else "0.0.0"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    swaps_dir = Path(sys.argv[1]).expanduser().resolve()
    if not swaps_dir.is_dir():
        print(f"✗ swaps dir not found: {swaps_dir}")
        return 1

    built = 0
    written: set[str] = set()
    for fname, why in RETIRED.items():
        if (swaps_dir / fname).is_file():
            print(f"  – ignoring {fname}: {why}")
    for fname, (member, rel) in SWAPS.items():
        src = swaps_dir / fname
        if not src.is_file():
            print(f"  – no {fname} in swaps dir; skipping {member} (upload its plain dist/ zip)")
            continue
        folder = SK / member
        neutral = folder / rel
        if src.read_text(encoding="utf-8").strip() == neutral.read_text(encoding="utf-8").strip():
            print(f"✗ {fname} is identical to the repo's neutral copy — that's the wrong file.")
            print("  Point the script at your PRIVATE copy; the repo stays neutral by law.")
            return 1
        ver = member_version(folder)
        OUT.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / member
            shutil.copytree(folder, work)
            (work / rel).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            out = OUT / f"{member}-{ver}+install.zip"
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(work.rglob("*")):
                    if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
                        z.write(p, Path(member) / p.relative_to(work))
        print(f"  ▣ dist/install/{out.name}  (private {fname} overlaid)")
        written.add(out.name)
        built += 1

    if built == 0:
        print("✗ nothing built — the swaps dir held no brand-definition.md.")
        return 1

    # skillwright rubric G-3, stale-output detection: a member bump leaves the
    # previous version's zip sitting in dist/install, and an operator uploading
    # "the brandwright zip" can grab the older one. Caught for real on 2026-08-07,
    # when a 1.0.2 zip carrying a definition nine versions stale outlived the
    # 1.1.0 build beside it. Silence from the generator is what endorsed it.
    stale = sorted(p for p in OUT.glob("*+install.zip") if p.name not in written)
    for p in stale:
        p.unlink()
        print(f"  ✗ dist/install/{p.name} (superseded — removed)")

    print(f"\ninstall zips: {built} built · upload these, not the neutral dist/ zips · repo tree untouched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
