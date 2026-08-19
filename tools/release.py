#!/usr/bin/env python3
"""claude-skills — release: the whole close-of-pass loop in one command.

    python tools/release.py foundation=2.5.0 [ossuary=2.4.0] [-m "message"] [--no-push]
                            [--swaps DIR ...] [--export-dir DIR]
    python tools/release.py --refresh-brand      # only step 9 (the ~/.claude/brand copies)
    python tools/release.py --mirror-only        # only step 8 (the longshot ossuary mirror)
    python tools/release.py --dry-run foundation=2.5.0   # print the plan, write nothing

Steps, in order (each stops the run on failure, nothing after it runs):
  1. bump-pack       build.py --bump-pack <pack> <ver> for each pack named — marketplace
                     entry + plugin.json + root CHANGELOG scaffold in one stroke; idempotent
  2. changelog gate  the root CHANGELOG entry for each new tag must be written — a
                     "(fill in)" scaffold under the new heading stops the run here
  3. build           python tools/build.py — regenerates every references/pack.md, builds dist/
  4. check           python tools/build.py --check must be clean
  5. tests           python -m unittest discover -s tools -p "test_*.py"
  6. commit          git add -A; git commit -m <message>
  7. tag + push      git tag <pack>-v<ver> per pack; git push origin HEAD --follow-tags
                     (--no-push leaves the tags local; CI attaches the member zips on tag)
  8. mirror          copy packs/ossuary/skills/* over the longshot repo's skills/ mirror,
                     diff -r must be empty, then commit + push THERE under that repo's own
                     identity: "skills: re-sync ossuary mirrors from claude-skills ossuary-vX.Y.Z"
                     (runs when the mirror differs; skipped when it is already clean)
  9. brand copies    refresh ~/.claude/brand/brand-definition.md and brand-definition-northstar.md
                     from the two brand repos (build.py names them; copies, not symlinks —
                     a file symlink needs admin on Windows) — the path brandwright reads first
 10. upload list     members whose zip changed since the previous tag, and the exact claude.ai
                     upload list — REQUIRED: bonecaller (claude.ai is its only surface) and
                     brandwright's branded install variant (dist/install/*+install.zip, built by
                     apply-install-swaps.py when --swaps dirs are given); everything else optional
 11. export          with --export-dir, copy every member zip (+ install zips) there with a
                     README.txt carrying the upload list

The rig loads every foundation member and bonecaller by user-scope junction into this
working tree, and linecaller from the longshot mirror — so a release changes nothing on the
rig beyond the mirror; `claude plugin update` is not part of this loop (2026-08-17).
Stdlib only. Run from anywhere; paths resolve from this file.
"""
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  — ROOT, PACKS, DIST, MARKETPLACE, _BRAND_REPO_SOURCE, _PEER_SOURCES

ROOT = build.ROOT
PY = sys.executable
# Read from the environment for the same reason build.py does: this file ships on a
# PUBLIC repo, and a hardcoded path publishes the owner's drive layout and the
# existence of a private repo to every reader. Unset simply means "not this machine".
LONGSHOT = build._env_path("CLAUDE_SKILLS_LONGSHOT")
LONGSHOT_SKILLS = (LONGSHOT / "skills") if LONGSHOT else None
LONGSHOT_IDENTITY = "MickMacPW"
BRAND_HOME = Path.home() / ".claude" / "brand"
BRAND_COPIES = {  # destination name -> source (the two brand repos, per build.py's parity map)
    "brand-definition.md": build._BRAND_REPO_SOURCE,
    "brand-definition-northstar.md": build._PEER_SOURCES["northstar"],
}
REQUIRED_ON_CLAUDE_AI = {
    "revenantworks-ossuary-bonecaller": "claude.ai is its only runtime surface",
    "revenantworks-foundation-brandwright": "the branded install variant is the only brand carrier "
                                            "(dist/install/*+install.zip via apply-install-swaps.py)",
}


def sh(*args: str, cwd: Path = ROOT, check: bool = True, quiet: bool = False) -> subprocess.CompletedProcess:
    r = subprocess.run(list(args), cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if not quiet and r.stdout.strip():
        print(r.stdout.rstrip())
    if check and r.returncode != 0:
        print(r.stderr.rstrip() or r.stdout.rstrip())
        raise SystemExit(f"✗ {' '.join(args)} failed (exit {r.returncode})")
    return r


def step(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def pack_version(pack: str) -> str:
    return json.loads((build.PACKS / pack / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]


def member_versions_at(ref: str | None) -> dict[str, str]:
    """{member: version} at a git ref (None = working tree)."""
    out = {}
    for pack_dir in sorted(build.PACKS.iterdir()):
        for folder in sorted((pack_dir / "skills").iterdir()) if (pack_dir / "skills").is_dir() else []:
            rel = folder.relative_to(ROOT).as_posix() + "/SKILL.md"
            if ref is None:
                text = (ROOT / rel).read_text(encoding="utf-8") if (ROOT / rel).is_file() else ""
            else:
                text = sh("git", "show", f"{ref}:{rel}", check=False, quiet=True).stdout
            m = re.search(r'version:\s*"?([\d.]+)"?', text.split("---")[1]) if text.count("---") >= 2 else None
            if m:
                out[folder.name] = m.group(1)
    return out


def previous_tag(pack: str, exclude: str) -> str | None:
    tags = sh("git", "tag", "-l", f"{pack}-v*", "--sort=-v:refname", check=False, quiet=True).stdout.split()
    tags = [t for t in tags if t != exclude]
    return tags[0] if tags else None


# ---------------------------------------------------------------- steps 8, 9 (also standalone)

def sync_mirror(tag_label: str | None, push: bool = True) -> bool:
    """Copy packs/ossuary/skills/* over longshot/skills/*; commit + push there when it moved."""
    src = build.PACKS / "ossuary" / "skills"
    if LONGSHOT_SKILLS is None or not LONGSHOT_SKILLS.is_dir():
        where = LONGSHOT_SKILLS if LONGSHOT_SKILLS else "CLAUDE_SKILLS_LONGSHOT unset"
        print(f"  mirror: {where} — not on this machine, skipped")
        return False
    changed = False
    for member in sorted(p for p in src.iterdir() if p.is_dir()):
        dst = LONGSHOT_SKILLS / member.name
        before = _tree_bytes(dst) if dst.exists() else None
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(member, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        if before != _tree_bytes(dst):
            changed = True
            print(f"  ✎ mirror {member.name} re-synced")
        else:
            print(f"  = mirror {member.name} already identical")
    # the whole test: a recursive byte compare must be empty (the same test as
    # `diff -r`, done in-process because `diff` is not on PATH outside Git Bash)
    for member in sorted(p for p in src.iterdir() if p.is_dir()):
        a, b = _tree_bytes(member), _tree_bytes(LONGSHOT_SKILLS / member.name)
        if a != b:
            for k in sorted(set(a) ^ set(b)):
                print(f"    only on one side: {k}")
            for k in sorted(set(a) & set(b)):
                if a[k] != b[k]:
                    print(f"    differs: {k}")
            raise SystemExit(f"✗ mirror {member.name} still differs after copy")
    print("  ✓ recursive compare clean for both members (diff -r equivalent)")
    if not changed:
        return False
    ident = sh("git", "config", "user.name", cwd=LONGSHOT, check=False, quiet=True).stdout.strip()
    if ident != LONGSHOT_IDENTITY:
        raise SystemExit(f"✗ longshot repo identity is {ident!r}, expected {LONGSHOT_IDENTITY!r} — not committing there")
    label = tag_label or f"ossuary-v{pack_version('ossuary')}"
    sh("git", "add", "skills", cwd=LONGSHOT, quiet=True)
    if sh("git", "diff", "--cached", "--quiet", cwd=LONGSHOT, check=False, quiet=True).returncode == 0:
        print("  mirror: nothing staged in longshot (already committed) — no commit")
        return False
    sh("git", "commit", "-q", "-m", f"skills: re-sync ossuary mirrors from claude-skills {label}", cwd=LONGSHOT, quiet=True)
    print(f"  ✓ longshot commit: skills: re-sync ossuary mirrors from claude-skills {label}")
    if push:
        sh("git", "push", "-q", "origin", "HEAD", cwd=LONGSHOT, quiet=True)
        print("  ✓ longshot pushed")
    return True


def _tree_bytes(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts}


def refresh_brand() -> None:
    """Copy the two live definitions to ~/.claude/brand — the fixed path brandwright reads first."""
    BRAND_HOME.mkdir(parents=True, exist_ok=True)
    for name, src in BRAND_COPIES.items():
        dst = BRAND_HOME / name
        # src is None when its env var is unset — the default on any machine but the
        # owner's. That is not an error, it is "the source repo is not here"; the same
        # outcome as a path that exists but points at nothing. Without this guard the
        # whole step died with AttributeError on a bare checkout.
        if src is None:
            print(f"  ! {name}: source not configured on this machine — left as is")
            continue
        if not src.is_file():
            print(f"  ! {name}: source {src} not on this machine — left as is")
            continue
        new = src.read_bytes()
        if dst.is_file() and dst.read_bytes() == new:
            print(f"  = {dst} current")
        else:
            dst.write_bytes(new)
            print(f"  ✎ {dst} refreshed from {src}")


# ---------------------------------------------------------------- the loop

def main() -> int:
    argv = sys.argv[1:]
    if "--refresh-brand" in argv:
        refresh_brand(); return 0
    if "--mirror-only" in argv:
        sync_mirror(None, push="--no-push" not in argv); return 0
    dry = "--dry-run" in argv
    push = "--no-push" not in argv
    msg = None
    swaps: list[str] = []
    export_dir: Path | None = None
    bumps: dict[str, str] = {}
    it = iter(argv)
    for a in it:
        if a in ("-m", "--message"):
            msg = next(it)
        elif a == "--swaps":
            swaps.append(next(it))
        elif a == "--export-dir":
            export_dir = Path(next(it))
        elif a.startswith("--"):
            continue
        elif "=" in a:
            pack, ver = a.split("=", 1)
            if not re.fullmatch(r"\d+\.\d+\.\d+", ver):
                raise SystemExit(f"✗ {a}: version must be X.Y.Z")
            bumps[pack] = ver
        else:
            raise SystemExit(f"✗ unrecognized argument {a!r}")
    if not bumps:
        raise SystemExit("✗ name at least one pack=X.Y.Z (or --refresh-brand / --mirror-only)")

    prev_tags = {p: previous_tag(p, f"{p}-v{v}") for p, v in bumps.items()}
    if dry:
        print("dry run — plan:")
        for p, v in bumps.items():
            print(f"  {p}: {pack_version(p)} → {v}  (previous tag {prev_tags[p]})  tag {p}-v{v}")
        print(f"  push: {push} · swaps: {swaps or '—'} · export: {export_dir or '—'}")
        return 0

    step(1, "bump-pack")
    for p, v in bumps.items():
        if pack_version(p) == v:
            print(f"  = {p} already at {v}")
        else:
            sh(PY, str(ROOT / "tools" / "build.py"), "--bump-pack", p, v)

    step(2, "changelog gate")
    clog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    for p, v in bumps.items():
        head = f"## [{p}-v{v}]"
        i = clog.find(head)
        if i < 0:
            raise SystemExit(f"✗ CHANGELOG.md has no heading {head}")
        section = clog[i:].split("\n## ", 2)[1] if clog[i:].count("\n## ") else clog[i:]
        if "(fill in)" in section:
            raise SystemExit(f"✗ CHANGELOG.md: write the entry under {head} (the scaffold still says '(fill in)'), "
                             f"then re-run — bump-pack is idempotent")
    print("  ✓ every new heading has an entry")

    step(3, "build")
    sh(PY, str(ROOT / "tools" / "build.py"))
    if swaps:
        sh(PY, str(ROOT / "tools" / "apply-install-swaps.py"), *swaps)

    step(4, "check")
    sh(PY, str(ROOT / "tools" / "build.py"), "--check")

    step(5, "tests")
    sh(PY, "-m", "unittest", "discover", "-s", "tools", "-p", "test_*.py")

    step(6, "commit")
    tags = [f"{p}-v{v}" for p, v in bumps.items()]
    message = msg or f"release: {' + '.join(tags)}"
    sh("git", "add", "-A", quiet=True)
    if sh("git", "diff", "--cached", "--quiet", check=False, quiet=True).returncode == 0:
        print("  = nothing to commit (already committed)")
    else:
        sh("git", "commit", "-q", "-m", message, quiet=True)
        print(f"  ✓ committed: {message}")

    step(7, "tag + push")
    for t in tags:
        if sh("git", "rev-parse", "-q", "--verify", f"refs/tags/{t}", check=False, quiet=True).returncode == 0:
            print(f"  = tag {t} exists")
        else:
            sh("git", "tag", t, quiet=True); print(f"  ✓ tagged {t}")
    if push:
        sh("git", "push", "-q", "origin", "HEAD", "--follow-tags", quiet=True)
        sh("git", "push", "-q", "origin", "--tags", quiet=True)
        print("  ✓ pushed branch + tags — CI attaches the member zips to each Release")
    else:
        print("  --no-push: tags stay local")

    step(8, "longshot mirror")
    sync_mirror(f"ossuary-v{pack_version('ossuary')}", push=push)

    step(9, "~/.claude/brand copies")
    refresh_brand()

    step(10, "zips changed + claude.ai upload list")
    now = member_versions_at(None)
    changed: dict[str, tuple[str, str]] = {}
    for p in bumps:
        prev = prev_tags[p]
        before = member_versions_at(prev) if prev else {}
        for member, ver in now.items():
            if member.startswith(f"revenantworks-{p}-") and before.get(member) != ver:
                changed[member] = (before.get(member, "—"), ver)
    if not changed:
        print("  no member zip changed since the previous tags")
    for member, (b, a) in sorted(changed.items()):
        zip_path = build.DIST / f"{member}-{a}.zip"
        inst = sorted((build.DIST / "install").glob(f"{member}-{a}+install.zip")) if (build.DIST / "install").is_dir() else []
        req = REQUIRED_ON_CLAUDE_AI.get(member)
        flag = "REQUIRED" if req else "optional"
        print(f"  {flag:<8} {member}  {b} → {a}   {inst[0] if inst else zip_path}" + (f"   ({req})" if req else ""))
    print("  claude.ai: Settings → Capabilities → Skills → delete the old copy → Create skill → upload the zip")

    if export_dir:
        step(11, f"export → {export_dir}")
        export_dir.mkdir(parents=True, exist_ok=True)
        copied = []
        for z in sorted(build.DIST.glob("*.zip")) + (sorted((build.DIST / "install").glob("*.zip")) if (build.DIST / "install").is_dir() else []):
            shutil.copy2(z, export_dir / z.name); copied.append(z.name)
        lines = [f"claude-skills member zips — built {date.today().isoformat()} · tags: {', '.join(tags)}", "",
                 "Re-upload on claude.ai (Settings → Capabilities → Skills → delete old → Create skill → upload):", ""]
        for member, (b, a) in sorted(changed.items()):
            req = REQUIRED_ON_CLAUDE_AI.get(member)
            inst = [c for c in copied if c.startswith(f"{member}-{a}+install")]
            lines.append(f"  [{'REQUIRED' if req else 'optional'}] {inst[0] if inst else f'{member}-{a}.zip'}"
                         + (f"  — {req}" if req else ""))
        lines += ["", "Every SKILL.md inside these zips carries only the six frontmatter keys claude.ai accepts",
                  "(name, description, license, compatibility, metadata, allowed-tools).", "",
                  "All zips in this folder:"] + [f"  {c}" for c in copied]
        (export_dir / "README.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"  ✓ {len(copied)} zip(s) + README.txt")

    print("\nrelease: done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
