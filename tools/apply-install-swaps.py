#!/usr/bin/env python3
"""claude-skills — apply-install-swaps: overlay private config onto neutral members.

Brand-carriage law (owner decision, 2026-07-23): the ONLY brand carrier
anywhere is the locally configured brandwright. Every other member is
brandless in the repo AND in your installs; branded artifacts (prompt cards
included) are produced at need via `brandwright apply`, never stored.

Three swap surfaces, all optional — put in your swaps dir only what you want to
override, and the neutral value ships for the rest:

  brand-definition.md   -> brandwright's references/brand-definition.md
                           (the active identity + voice). Extra definitions in
                           later dirs install as peers.
  LICENSE               -> every member's LICENSE
  brand-token.txt       -> every member's `metadata.brand:` value (one line)

**This is the whole point of the split, and it is not owner-specific.** The repo
ships neutral so anyone can download and use these skills as-is. Anyone who wants
their own identity on their own install builds it here instead: drop a
`brand-definition.md` (and a `LICENSE` and `brand-token.txt` if the default
copyright and token should change too) into a private directory of your own, run
this, and upload the zips it writes. Your branding lives on your disk and in your
install; the repo never carries it. Overriding a previous brand is the same
operation as applying a first one.

Usage:
  python3 tools/apply-install-swaps.py <primary-dir> [<peer-dir> ...]

Each dir holds a private copy named exactly `brand-definition.md`. The first is
the **primary** and overlays `references/brand-definition.md`; every later dir is
a **peer** (brandwright 1.2.0+ holds several definitions) and overlays
`references/brand-definition-<slug>.md`, where the slug is read from that
definition's own `slug:` header line, else derived from its H1. The script
verifies each differs from the repo's neutral copy (hard-fail otherwise — a
neutral overlay means you pointed it at the wrong file), then zips to
`dist/install/<member>-<ver>+install.zip`.

Peers are how a personal or social brand rides along beside a product brand
without either overwriting the other. Selection at runtime reads the primary's
roster, so a peer overlaid here that the roster does not list is inert — the
script warns when it spots that.

Every other member uploads from its plain `dist/` zip. A `prompt-card.md` in a
swaps dir is ignored with a note — that swap retired under the law above. The
repo tree is never modified. Stdlib only.
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
# Overrides that apply to EVERY member, not one. Absent from the swaps dir means
# "keep the neutral value" — never "blank it".
LICENSE_FILE = "LICENSE"
TOKEN_FILE = "brand-token.txt"
RETIRED = {"prompt-card.md": "retired 2026-07-23 — only brandwright carries brand; branded cards come from `brandwright apply` at need"}


def apply_global_overrides(work: Path, swaps_dir: Path) -> list[str]:
    """Overlay the swaps dir's LICENSE and brand token onto one member copy.

    Returns what changed, so the run reports it rather than doing it silently —
    a build that quietly rewrote your copyright would be worse than one that
    refused to.
    """
    notes = []
    lic = swaps_dir / LICENSE_FILE
    if lic.is_file():
        dest = work / "LICENSE"
        if dest.is_file() and dest.read_text(encoding="utf-8") != lic.read_text(encoding="utf-8"):
            dest.write_text(lic.read_text(encoding="utf-8"), encoding="utf-8")
            notes.append("LICENSE")
    tok = swaps_dir / TOKEN_FILE
    if tok.is_file():
        value = tok.read_text(encoding="utf-8").strip().splitlines()[0].strip() if tok.read_text(encoding="utf-8").strip() else ""
        if value:
            skill = work / "SKILL.md"
            src = skill.read_text(encoding="utf-8")
            out, n = re.subn(r"^(\s*brand:\s*)\S+\s*$", lambda m: m.group(1) + value, src, count=1, flags=re.M)
            if n and out != src:
                skill.write_text(out, encoding="utf-8")
                notes.append(f"brand token -> {value}")
    return notes


def member_version(folder: Path) -> str:
    fm = (folder / "SKILL.md").read_text(encoding="utf-8").split("---")[1]
    m = re.search(r'version:\s*"?([\d.]+)"?', fm)
    return m.group(1) if m else "0.0.0"


def slug_of(text: str, fallback: str) -> str:
    """A peer's slug: its own declared one, else derived from its H1."""
    m = re.search(r"^\s*slug:\s*([a-z0-9][a-z0-9-]*)\s*$", text, re.M | re.I)
    if m:
        return m.group(1).lower()
    h = re.search(r"^#\s+(.+)$", text, re.M)
    base = h.group(1) if h else fallback
    base = re.sub(r"(?i)brand definition\s*[—:-]*\s*", "", base).strip()
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-") or fallback


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    dirs = []
    for a in sys.argv[1:]:
        d = Path(a).expanduser().resolve()
        if not d.is_dir():
            print(f"✗ swaps dir not found: {d}")
            return 1
        dirs.append(d)
    swaps_dir = dirs[0]
    peers = dirs[1:]

    built = 0
    written: set[str] = set()
    for fname, why in RETIRED.items():
        if (swaps_dir / fname).is_file():
            print(f"  – ignoring {fname}: {why}")
    has_global = (swaps_dir / LICENSE_FILE).is_file() or (swaps_dir / TOKEN_FILE).is_file()
    for fname, (member, rel) in SWAPS.items():
        src = swaps_dir / fname
        if not src.is_file():
            print(f"  – no {fname} in swaps dir; skipping {member}'s definition swap")
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
            primary_text = src.read_text(encoding="utf-8")
            (work / rel).write_text(primary_text, encoding="utf-8")
            # peers ride along as siblings; the primary's roster is what makes
            # them reachable at runtime, so an unlisted peer is called out.
            for note in apply_global_overrides(work, swaps_dir):
                print(f"    · {note}")
            for pd in peers:
                psrc = pd / fname
                if not psrc.is_file():
                    print(f"  ! {pd.name}: no {fname} — skipped")
                    continue
                ptext = psrc.read_text(encoding="utf-8")
                slug = slug_of(ptext, pd.name)
                (work / rel).parent.joinpath(f"brand-definition-{slug}.md").write_text(ptext, encoding="utf-8")
                listed = slug in primary_text.lower()
                print(f"  + peer '{slug}' overlaid" + ("" if listed else "  ! not in the primary's roster — inert until it is listed"))
            out = OUT / f"{member}-{ver}+install.zip"
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(work.rglob("*")):
                    if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
                        z.write(p, Path(member) / p.relative_to(work))
        print(f"  ▣ dist/install/{out.name}  (private {fname} overlaid)")
        written.add(out.name)
        built += 1

    if has_global:
        swapped = {m for m, _ in SWAPS.values()}
        for folder in sorted(p for p in SK.iterdir() if (p / "SKILL.md").is_file()):
            if folder.name in swapped:
                continue
            ver = member_version(folder)
            with tempfile.TemporaryDirectory() as td:
                work = Path(td) / folder.name
                shutil.copytree(folder, work)
                notes = apply_global_overrides(work, swaps_dir)
                if not notes:
                    continue
                out = OUT / f"{folder.name}-{ver}+install.zip"
                with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                    for p in sorted(work.rglob("*")):
                        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
                            z.write(p, Path(folder.name) / p.relative_to(work))
            print(f"  ▣ dist/install/{out.name}  ({', '.join(notes)})")
            written.add(out.name)
            built += 1

    if built == 0:
        print("✗ nothing built — the swaps dir held no brand-definition.md, LICENSE, or brand-token.txt.")
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
