#!/usr/bin/env python3
"""citadel — apply-install-swaps: overlay private config onto neutral members.

Config-carrying members ship *neutral* in the repo by law. Before uploading to
claude.ai, overlay your private files onto the neutral copies and build
install-ready zips. The two swap surfaces (since 1.1.0):

  brandsmith   references/brand-definition.md   (active identity + voice)
  promptsmith  references/prompt-card.md        (install edition of the card)

Usage:
  python3 tools/apply-install-swaps.py <swaps-dir>

<swaps-dir> holds your private copies named exactly `brand-definition.md`
and/or `prompt-card.md` — either or both. For each present swap the script
verifies it differs from the repo's neutral copy (hard-fail otherwise — a
neutral overlay means you pointed it at the wrong file), overlays it onto a
temp copy of the member, and zips to `dist/install/<member>-<ver>+install.zip`.
Members with no swap present are skipped; upload their plain `dist/` zips.
The repo tree is never modified. Stdlib only.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SK = ROOT / "packs" / "foundation" / "skills"
OUT = ROOT / "dist" / "install"

SWAPS = {
    "brand-definition.md": ("revenant-foundation-brandsmith", "references/brand-definition.md"),
    "prompt-card.md": ("revenant-foundation-promptsmith", "references/prompt-card.md"),
}


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
        built += 1

    if built == 0:
        print("✗ nothing built — the swaps dir held neither swap file.")
        return 1
    print(f"\ninstall zips: {built} built · upload these, not the neutral dist/ zips · repo tree untouched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
