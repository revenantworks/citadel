#!/usr/bin/env python3
"""citadel — multi-pack build: sync, validate, package.

Single source of truth: the pack tables in
packs/foundation/skills/revenant-foundation-skillwright/references/pack-registry.md.
Every pack under packs/ is derived from its `**<pack> members**` table there —
no second manifest to drift. The marketplace catalog is cross-checked, not derived.

Validation covers frontmatter identity/description/body limits, CHANGELOG-version
agreement, and the `metadata.volatile` block (U-7): legal classes, and for
calendar-class surfaces a sane cadence, an existing file, and a dated header stamp.

The routing-seam table rides the same registry pipeline as the roster (1.2.0 item ①):
authored once under `**<pack> seams**`, generated into every member's pack.md, and
boundary-pair checked — both members in the roster, no self-pairs, no empty ownership
or signal cell, no pair declared twice with conflicting ownership, and the table present
and complete in all N manifests.

Usage:
  python3 tools/build.py            sync pack.md -> all members in all packs, validate, build dist/ zips
  python3 tools/build.py --check    CI mode: validate + report drift, write nothing, exit 1 on any problem
  python3 tools/build.py --only revenant-foundation-tokenwright   limit zip build to one member (sync still runs)
  python3 tools/build.py --bump-pack <pack> <X.Y.Z>   one-stroke version write: marketplace entry +
                                    pack plugin.json + root CHANGELOG scaffold (prevents split-brain bumps)
  python3 tools/build.py --parity   diff installed marketplace-clone SKILL.md descriptions against repo HEAD;
                                    exit 1 on drift; skips cleanly when no local install exists (CI-safe)
  python3 tools/build.py --footprint  measured SKILL.md body tokens per member against its registry budget,
                                    plus the pack total; report only, writes nothing, never fails

Validation also covers (added at foundation-v1.1.1): pack plugin.json == marketplace entry version
(hard fail — the 1.0.0/1.1.0 split-brain class), eval provenance freshness and eval-table orphan
rows (WARN this release; flip to fail at the next tagged release), description >=1000 chars and
and body footprint. The footprint gate was RESCOPED 2026-07-25: >500 body lines stays a hard fail (the
agentskills.io norm), while the 5k-token figure is this pack's own advisory and now gates on whether the
overage is DECLARED — a member over it must carry a budget {tokens, why}. Undeclared overage warns now and
fails at the next tag; exceeding your own declared budget warns as drift. MOVED 2026-07-27: for a pack
member the budget lives in the registry's `**<pack> budgets**` table, not in frontmatter — frontmatter is
loaded on every invocation, so a `why` there cost 51-95 tokens per run to explain a build-time number.
A registry row costs zero runtime tokens, which is what makes declaring ALL members affordable rather
than only the over-advisory ones. Standalone skills outside a pack keep the frontmatter form.

Stdlib only. Run from the repo root (or anywhere; paths resolve from this file).
"""
import json
import re
import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
DIST = ROOT / "dist"
REGISTRY = PACKS / "foundation" / "skills" / "revenant-foundation-skillwright" / "references" / "pack-registry.md"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

CHECK = "--check" in sys.argv
ONLY = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
PARITY = "--parity" in sys.argv
BUMP = None
if "--bump-pack" in sys.argv:
    i = sys.argv.index("--bump-pack")
    BUMP = (sys.argv[i + 1], sys.argv[i + 2])  # (pack, version)
FOOTPRINT = "--footprint" in sys.argv
problems: list[str] = []
warnings: list[str] = []
FOOTPRINTS: dict[str, tuple[int, int | None]] = {}  # member -> (measured, budget)


def fail(msg: str) -> None:
    problems.append(msg)
    print(f"  ✗ {msg}")


def warn(msg: str) -> None:
    """Non-fatal this release; flip to fail() at the next tagged release (see docstring)."""
    warnings.append(msg)
    print(f"  ⚠ {msg}")


def registry_text() -> str:
    return REGISTRY.read_text(encoding="utf-8")


def registry_packs(text: str) -> dict[str, str]:
    """Pack name -> profile, from the Pack registry table."""
    packs = {}
    block = text.split("## Pack registry", 1)[1]
    for line in block.splitlines():
        m = re.match(r"\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|", line)
        if m and m.group(1) != "Pack":
            packs[m.group(1)] = m.group(2)
    return packs


def pack_members(text: str, pack: str) -> list[tuple[str, str, str]]:
    """(member, job, route) rows from the pack's canonical members table."""
    marker = f"**{pack} members**"
    if marker not in text:
        return []
    block = text.split(marker, 1)[1]
    # Order matters: these are checked in document order, first hit wins. The budgets table
    # (added 2026-07-27) sits between members and seams and its rows are ALSO `member | x | y`,
    # so it matches the roster regex below verbatim — without stopping here first, every budget
    # row was counted as a second roster entry and count integrity read 16 = 16 = 16 for an
    # eight-member pack. The seams table is naturally disjoint (no backticked first cell); this
    # one is not, so the stop is what keeps them apart.
    for stop in (f"**{pack} budgets**", f"**{pack} seams**", f"**{pack} capstone:**", "\n## ", "\n**"):
        if stop in block:
            block = block.split(stop, 1)[0]
            break
    rows = []
    for line in block.splitlines():
        m = re.match(r"\|\s*`([^`]+)`\s*\|([^|]+)\|([^|]+)\|", line)
        if m:
            rows.append((m.group(1).strip(), m.group(2).strip(), m.group(3).strip()))
    return rows


def pack_budgets(text: str, pack: str) -> dict[str, tuple[int, str]]:
    """{member: (tokens, why)} from the pack's body-footprint table.

    Moved here from each member's `metadata.body_budget` on 2026-07-27. The gate is
    unchanged — a body over the advisory must be DECLARED and JUSTIFIED — but frontmatter
    is loaded on every invocation, so a `why` there cost 51-95 tokens per member per run to
    explain a number no runtime reader acts on. A registry row costs zero runtime tokens,
    which is what makes declaring all N members affordable rather than only the over-limit
    ones. Standalone skills outside a pack keep the frontmatter form: they have no registry.
    """
    marker = f"**{pack} budgets**"
    if marker not in text:
        return {}
    block = text.split(marker, 1)[1]
    for stop in (f"**{pack} seams**", "\n## "):
        if stop in block:
            block = block.split(stop, 1)[0]
            break
    out = {}
    for line in block.splitlines():
        m = re.match(r"\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|([^|]+)\|", line)
        if m:
            out[m.group(1).strip()] = (int(m.group(2)), m.group(3).strip())
    return out


def pack_seams(text: str, pack: str) -> list[tuple[str, str, str, str, str, str]]:
    """(left, right, left-owns, right-owns, signal, cold-listing) rows from the pack's seam table.

    The Seam cell is `left ↔ right` in short wright names and carries no backticks — that
    keeps this table disjoint from the roster and pack-registry parsers above, which both
    key on a backticked first cell.
    """
    marker = f"**{pack} seams**"
    if marker not in text:
        return []
    block = text.split(marker, 1)[1]
    for stop in ("\n## ", "\n**"):
        if stop in block:
            block = block.split(stop, 1)[0]
            break
    rows = []
    for line in block.splitlines():
        m = re.match(r"\|\s*([\w.-]+)\s*↔\s*([\w.-]+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if m:
            rows.append(tuple(g.strip() for g in m.groups()))
    return rows


def pack_seam_note(text: str, pack: str) -> str:
    """The one-line note under the seam table (verb overloads, recorded-open seams)."""
    m = re.search(rf"(\*\*{pack} seam notes:\*\*.+)", text)
    return m.group(1).strip() if m else ""


def pack_lines(text: str, pack: str, profile_notes: str) -> tuple[str, str, tuple[str, str]]:
    """Capstone, repo, and conformance lines for one pack (graceful when absent)."""
    cap_m = re.search(rf"\*\*{pack} capstone:\*\*(.+)", text)
    cap = cap_m.group(1).strip() if cap_m else "—"
    repo_m = re.search(rf"\*\*{pack} canonical repo:\*\*\s*(`[^`]+`)", text)
    repo = repo_m.group(1) if repo_m else "the registered canonical repo"
    conf = re.search(r"Conformance checks \(([\d-]+)\): ([^|.]+)", profile_notes) or \
           re.search(r"Conformance checks \(([\d-]+)\): ([^|.]+)", text)
    checks = conf.group(2).strip() if conf else "C-1 drift-audit verb · C-2 neutral default"
    adopted = conf.group(1) if conf else "2026-07-13"
    return cap, repo, (adopted, checks)


def render_pack_md(pack: str, profile: str, members, cap, repo, conf, seams=(), seam_note="") -> str:
    adopted, checks = conf
    n_word = {7: "seven", 8: "eight", 9: "nine", 10: "ten"}.get(len(members), str(len(members)))
    rows = "\n".join(f"| `{m}` | {j} | {r} |" for m, j, r in members)
    seam_block = ""
    if seams:
        seam_rows = "\n".join(f"| {l} ↔ {r} | {lo} | {ro} | {sig} | {cold} |" for l, r, lo, ro, sig, cold in seams)
        seam_block = (
            "\n**Routing seams** — one row per boundary pair: what each side owns, and the signal that "
            "decides. Same advisory standing as the roster; a row reading *none — table only* is a seam "
            "the cold listing cannot decide, recorded here rather than claimed.\n\n"
            "| Seam | Left owns | Right owns | Router keys on | Cold-listing signal |\n"
            "|---|---|---|---|---|\n"
            f"{seam_rows}\n"
            + (f"\n{seam_note}\n" if seam_note else "")
        )
    return f"""# Pack — {pack} *({profile} profile)*

> Advisory only — consulted on boundary doubt; initial routing stays at the name + description level. **Last stamped: {date.today().isoformat()}** ({n_word}-member roster + canonical repo; generated from the registry in skillwright's `pack-registry.md`).

| Member | Job | Route there when |
|---|---|---|
{rows}
{seam_block}
**Pack conformance checks** (adopted {adopted}, scored on every member audit): **{checks.replace(' · ', '** · **')}**.

**Canonical repo:** {repo} — pack source of truth for drift audits (registered in skillwright's `pack-registry.md`; subject to relocation — the registry row is authoritative).

**Capstone:** {cap}

**Absence rule:** recommend an uninstalled sibling by name — never fail the task over it.
"""


SEAM_SIGNALS = ("both descriptions", "one description", "none — table only")


def validate_seams(pack: str, members: list[str], seams) -> None:
    """Boundary-pair check (1.2.0 item ①): every declared seam is structurally sound.

    Fails on a seam naming a member the pack does not have, a row pairing a member with
    itself, an empty ownership or signal cell, an unknown cold-listing value, and the same
    pair declared twice with conflicting ownership — one home per pair, as for every other
    surface the registry owns. Warns on a redundant duplicate row, a member no row mentions,
    and on `none — table only`: the recorded marker for a seam whose signal no description
    carries, which the cold listing therefore cannot route. That warn is instrumentation,
    not a defect to silence — the seam stays visible until a description claims it.
    """
    if not seams:
        if len(members) > 1:
            warn(f"[{pack}]: no routing-seam table (**{pack} seams**) for {len(members)} members — "
                 f"every boundary pair is unrecorded")
        return

    def resolve(short: str) -> str | None:
        hits = [m for m in members if m == short or m.endswith(f"-{short}")]
        if len(hits) != 1:
            fail(f"[{pack}] seam member {short!r}: {'no match' if not hits else 'ambiguous'} "
                 f"in the pack roster")
            return None
        return hits[0]

    seen: dict[frozenset, tuple[dict[str, str], str]] = {}
    covered: set[str] = set()
    for left, right, lo, ro, sig, cold in seams:
        a, b = resolve(left), resolve(right)
        label = f"{left} ↔ {right}"
        if not a or not b:
            continue
        if a == b:
            fail(f"[{pack}] seam {label}: one member on both sides — not a boundary pair")
            continue
        covered |= {a, b}
        for cell, what in ((lo, "left-ownership"), (ro, "right-ownership"), (sig, "router-signal")):
            if not cell.strip("* "):
                fail(f"[{pack}] seam {label}: empty {what} cell — a seam missing it decides nothing")
        norm = cold.strip("* ").lower()
        if norm not in SEAM_SIGNALS:
            fail(f"[{pack}] seam {label}: cold-listing signal {cold!r} not one of {SEAM_SIGNALS}")
        elif norm == "none — table only":
            warn(f"[{pack}] seam {label}: cold-listing signal 'none — table only' — no description "
                 f"carries the signal, so the listing cannot route this pair; recorded open, not closed")
        pair, owns = frozenset((a, b)), {a: lo, b: ro}
        if pair in seen:
            prior_owns, prior_label = seen[pair]
            if prior_owns != owns:
                fail(f"[{pack}] seam {label}: pair already declared as {prior_label} with different "
                     f"ownership — one home per pair")
            else:
                warn(f"[{pack}] seam {label}: duplicate of {prior_label} — redundant row")
        else:
            seen[pair] = (owns, label)
    for m in members:
        if m not in covered:
            warn(f"[{pack}] {m}: named in no routing seam — every edge uncontested, or unrecorded?")


def validate_seam_manifest(folder: Path, n_seams: int) -> None:
    """Item ①'s single-home half: the seam table is authored once in the registry and
    generated into every member, so every member's pack.md must carry all of it."""
    if not n_seams:
        return
    target = folder / "references" / "pack.md"
    if not target.is_file():
        fail(f"{folder.name}: no references/pack.md to carry the routing-seam table")
        return
    text = target.read_text(encoding="utf-8")
    if "**Routing seams**" not in text:
        fail(f"{folder.name}: references/pack.md carries no routing-seam table (regenerate from the registry)")
        return
    rows = sum(1 for ln in text.splitlines() if re.match(r"\|\s*[\w.-]+\s*↔\s*[\w.-]+\s*\|", ln))
    if rows != n_seams:
        fail(f"{folder.name}: references/pack.md carries {rows} seam row(s), registry declares {n_seams}")


def validate_volatile(folder: Path, fm: str) -> None:
    """U-7: validate the metadata.volatile block (stdlib parse, no yaml needed).

    Rules: block must exist (uniform layer); entries need file + class
    (calendar | event-driven); the referenced file must exist. Calendar
    entries additionally need a sane cadence_days (7-365) and a dated
    header stamp (Last verified/restamped/stamped: YYYY-MM-DD) in the
    file's first lines; event-driven entries must not carry cadence_days.
    """
    m = re.search(r"^\s*volatile:\s*\[\s*\]\s*$", fm, re.M)
    block_m = re.search(r"^(\s*)volatile:\s*$((?:\n\1\s+.*)+)", fm, re.M)
    if not m and not block_m:
        fail(f"{folder.name}: metadata.volatile missing (uniform layer requires it — [] for none)")
        return
    if m:  # volatile: []
        return
    entries, cur = [], None
    for line in block_m.group(2).splitlines():
        if not line.strip():
            continue
        item = re.match(r"\s*-\s+file:\s*(\S+)", line)
        kv = re.match(r"\s+(class|cadence_days):\s*(\S+)", line)
        if item:
            cur = {"file": item.group(1)}
            entries.append(cur)
        elif kv and cur is not None:
            cur[kv.group(1)] = kv.group(2)
        else:
            fail(f"{folder.name}: metadata.volatile has an unparseable line: {line.strip()!r}")
    if not entries:
        fail(f"{folder.name}: metadata.volatile block declares no entries (use [] for none)")
    for e in entries:
        ref, cls = e.get("file", "?"), e.get("class")
        if cls not in ("calendar", "event-driven"):
            fail(f"{folder.name}: volatile {ref}: class {cls!r} not calendar|event-driven")
            continue
        target = folder / ref
        if not target.is_file():
            fail(f"{folder.name}: volatile {ref}: declared file does not exist")
            continue
        if cls == "event-driven":
            if "cadence_days" in e:
                fail(f"{folder.name}: volatile {ref}: event-driven must not carry cadence_days")
            continue
        # calendar
        cad = e.get("cadence_days")
        if not (cad and cad.isdigit() and 7 <= int(cad) <= 365):
            fail(f"{folder.name}: volatile {ref}: calendar cadence_days {cad!r} not a sane integer (7-365)")
        # Stamp may sit at the file head (model-snapshot, measurement, platform-notes)
        # or at the head of the file's volatile *section* (rubrics.md ~line 18) —
        # 40 lines covers both; the strict "Last …:" form avoids prose dates.
        head = "\n".join(target.read_text(encoding="utf-8").splitlines()[:40])
        # One grammar only: "Last verified:" — matches the Cowork upkeep task's grep exactly.
        # (Narrowed at foundation-v1.1.1 from verified|restamped|stamped; all four calendar
        # files already used the strict form, so this was a zero-content-change tightening.)
        stamp = re.search(r"Last verified:\s*(\d{4}-\d{2}-\d{2})", head)
        if not stamp:
            fail(f"{folder.name}: volatile {ref}: calendar file has no dated header stamp")
        else:
            try:
                d = date.fromisoformat(stamp.group(1))
                if d > date.today():
                    fail(f"{folder.name}: volatile {ref}: stamp {stamp.group(1)} is in the future")
            except ValueError:
                fail(f"{folder.name}: volatile {ref}: stamp {stamp.group(1)!r} is not a valid date")


FOOTPRINT_ADVISORY = 5000  # house advisory, not a spec limit; see validate_skill


def validate_skill(folder: Path, budget: tuple[int, str] | None = None) -> str | None:
    """Return the member's version, recording problems as we go."""
    sk = folder / "SKILL.md"
    if not sk.exists():
        fail(f"{folder.name}: no SKILL.md")
        return None
    text = sk.read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 3:
        fail(f"{folder.name}: no frontmatter block")
        return None
    fm = parts[1]
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    ver = re.search(r'version:\s*"?([\d.]+)"?', fm)
    if not name or name.group(1) != folder.name:
        fail(f"{folder.name}: frontmatter name != folder name")
    if name and len(name.group(1)) > 64:
        fail(f"{folder.name}: name > 64 chars")
    if not desc:
        fail(f"{folder.name}: no description")
    elif len(desc.group(1)) > 1024:  # characters, not bytes — multibyte punctuation overreads byte counters
        fail(f"{folder.name}: description {len(desc.group(1))} chars > 1024 (house ceiling, not the platform cap)")
    elif len(desc.group(1)) >= 1000:
        warn(f"{folder.name}: description {len(desc.group(1))}/1024 chars — ceiling-riding, zero edit headroom "
             f"(8 maxed descriptions ≈ the entire default 2k-token listing budget; slim at the 1.2.0 pass)")
    # Platform truth is a different unit from the house ceiling above: Claude Code truncates the
    # CONCATENATION of description + when_to_use at 1,536 chars per listing entry (configurable via
    # skillListingMaxDescChars). Checking description alone is blind to the unit that actually
    # truncates — a member could pass the 1024 house rule and still be cut by the platform once a
    # when_to_use is added. No member declares when_to_use today, so this is a latent guard.
    if desc:
        wtu = re.search(r"^when_to_use:\s*(.+)$", fm, re.M)
        combined = len(desc.group(1)) + (len(wtu.group(1)) if wtu else 0)
        if combined > 1536:
            fail(f"{folder.name}: description+when_to_use {combined} chars > 1536 — the platform truncates "
                 f"the combined listing entry (skillListingMaxDescChars)")
        elif combined > 1382:  # 90% of the platform cap
            warn(f"{folder.name}: description+when_to_use {combined}/1536 chars — near the platform "
                 f"truncation cap for the combined listing entry")
    if ": " in (desc.group(1) if desc else "") and not desc.group(1).startswith(('"', "'")):
        try:
            import yaml  # optional; naive check above is the fallback signal
            yaml.safe_load(fm)
        except ModuleNotFoundError:
            pass
        except Exception:
            fail(f"{folder.name}: frontmatter fails YAML parse (unquoted ': ' in description?)")
    body_lines = parts[2].count("\n")
    if body_lines > 500:
        fail(f"{folder.name}: SKILL.md body {body_lines} lines > 500")
    # Footprint. The ≤500-line rule above is the ecosystem norm (agentskills.io, via rubrics.md)
    # and stays a hard fail. The token figure below is this pack's OWN advisory, not a spec limit:
    # tokens are the truer cost (a dense 265-line body can outweigh a sparse 500-line one), but the
    # 5k number was arbitrary and fired on members the spec passes.
    #
    # Rescoped 2026-07-25: the gate is no longer "how big" but "is the size DECLARED and JUSTIFIED".
    # A member over the advisory must carry, under metadata:
    #     body_budget:
    #       tokens: <int>   # the ceiling this member is allowed, its own drift check
    #       why: <text>     # why it earns the room
    # Undeclared overage is the defect (warn now, fail at the next tag — item ③'s promise lands
    # here). Declared overage is a recorded decision. Exceeding your OWN declared budget is drift
    # and warns regardless. This applies the pack's existing declared-dependencies doctrine to cost.
    body_tokens = len("---".join(parts[2:])) // 4  # chars/4 prose estimate, ±15%
    FOOTPRINTS[folder.name] = (body_tokens, budget[0] if budget else None)
    # Registry row is the home for a pack member (see pack_budgets). Frontmatter remains
    # valid for a standalone skill with no registry, and is an error for a member: two
    # homes for one number is the duplicate-statement defect this pack keeps closing.
    bb = re.search(r"^\s{2}body_budget:\s*$", fm, re.M)
    if bb and budget:
        fail(f"{folder.name}: body_budget declared in BOTH frontmatter and the registry — "
             f"the registry is the home for a pack member; drop the frontmatter block")
    if bb and not budget:
        bb_tokens = re.search(r"^\s{4}tokens:\s*(\d+)\s*$", fm, re.M)
        bb_why = re.search(r"^\s{4}why:\s*(\S.*)$", fm, re.M)
        if not (bb_tokens and bb_why):
            fail(f"{folder.name}: metadata.body_budget needs both 'tokens:' and 'why:'")
        elif body_tokens > int(bb_tokens.group(1)):
            warn(f"{folder.name}: SKILL.md body ≈{body_tokens} tokens over its OWN declared "
                 f"budget of {bb_tokens.group(1)} — drift; slim it or raise it deliberately")
    elif budget:
        if body_tokens > budget[0]:
            warn(f"{folder.name}: SKILL.md body ≈{body_tokens} tokens over its registry budget "
                 f"of {budget[0]} — drift; slim it or raise the row deliberately")
    elif body_tokens > FOOTPRINT_ADVISORY:
        warn(f"{folder.name}: SKILL.md body ≈{body_tokens} tokens > {FOOTPRINT_ADVISORY//1000}k "
             f"advisory with no budget row in the registry and none in frontmatter — declare it "
             f"and why it earns the room, or slim it (undeclared overage fails at the next tag)")
    validate_volatile(folder, fm)
    validate_evals(folder, re.search(r'version:\s*"?([\d.]+)"?', fm).group(1) if re.search(r'version:\s*"?([\d.]+)"?', fm) else "0.0.0")
    fm_ver = ver.group(1) if ver else "0.0.0"
    changelog = folder / "CHANGELOG.md"
    if changelog.exists():
        head = re.search(r"^##\s*\[([\d.]+)\]", changelog.read_text(encoding="utf-8"), re.M)
        if head and head.group(1) != fm_ver:
            fail(f"{folder.name}: CHANGELOG head [{head.group(1)}] != frontmatter version {fm_ver}")
        elif not head:
            fail(f"{folder.name}: CHANGELOG.md has no version heading")
    else:
        fail(f"{folder.name}: no CHANGELOG.md")
    return fm_ver


def validate_evals(folder: Path, fm_ver: str) -> None:
    """Eval-suite integrity (added foundation-v1.1.1; WARN this release, fail at the next tag).

    1. Provenance freshness: an evals/*.md head naming an older member version with no
       dated reconfirmation line is the exact defect class evalwright audits others for.
    2. Orphan rows: a numbered table row appearing after prose that follows the table
       silently escapes count checks (the brandwright rows-21/22 class).
    """
    evdir = folder / "evals"
    if not evdir.is_dir():
        return
    for f in sorted(evdir.glob("*.md")):
        head = "\n".join(f.read_text(encoding="utf-8").splitlines()[:6])
        prov = re.search(r"(?:[Pp]rovenance|derived|target)[^\n]*?v(\d+\.\d+\.\d+)", head)
        if prov and prov.group(1) != fm_ver:
            if not re.search(r"(?i)re-?(?:anchored|confirmed|verified|freshed|stamped)[^\n]*\d{4}-\d{2}-\d{2}", head):
                warn(f"{folder.name}: evals/{f.name} provenance names v{prov.group(1)} but member is "
                     f"{fm_ver} and no dated reconfirmation line found — restamp or reconfirm")
        # Orphan = a numbered row whose nearest preceding non-empty line is not table-shaped
        # (a row under its own "|#|Query|" header in a later section is structured, not orphaned).
        lines = f.read_text(encoding="utf-8").splitlines()
        prev = ""
        for ln in lines:
            if re.match(r"\|\s*\d+\s*\|", ln) and prev and not prev.lstrip().startswith("|"):
                warn(f"{folder.name}: evals/{f.name}: numbered row {ln.strip()[:60]!r} follows prose, "
                     f"not a table — orphaned from count checks; move it into a table")
                break
            if ln.strip():
                prev = ln


def check_marketplace(packs: dict[str, str]) -> None:
    """Cross-check the catalog: every pack has an entry; every entry's source exists;
    the pack's own plugin.json version matches the catalog (added foundation-v1.1.1 —
    hard fail: the 1.0.0-vs-1.1.0 split-brain shipped for a month, CI-invisible)."""
    if not MARKETPLACE.exists():
        fail("missing .claude-plugin/marketplace.json")
        return
    cat = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entries = {p["name"]: p for p in cat.get("plugins", [])}
    for pack in packs:
        if pack not in entries:
            fail(f"marketplace.json: no plugin entry for pack '{pack}'")
        else:
            src = ROOT / entries[pack].get("source", "").lstrip("./")
            if not src.is_dir():
                fail(f"marketplace.json: '{pack}' source {entries[pack].get('source')} not found")
            else:
                pj = src / ".claude-plugin" / "plugin.json"
                cat_ver = entries[pack].get("version")
                if not pj.is_file():
                    fail(f"'{pack}': missing {pj.relative_to(ROOT)}")
                else:
                    pj_ver = json.loads(pj.read_text(encoding="utf-8")).get("version")
                    if pj_ver != cat_ver:
                        fail(f"'{pack}': plugin.json version {pj_ver!r} != marketplace entry {cat_ver!r} "
                             f"(use --bump-pack to write both in one stroke)")
    for name, entry in entries.items():
        if name not in packs:
            fail(f"marketplace.json: plugin '{name}' has no pack table in the registry")


def bump_pack(pack: str, ver: str) -> int:
    """One-stroke version write: marketplace entry + pack plugin.json + root CHANGELOG scaffold."""
    if not re.fullmatch(r"\d+\.\d+\.\d+", ver):
        print(f"✗ {ver!r} is not X.Y.Z"); return 1
    cat = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entry = next((p for p in cat.get("plugins", []) if p["name"] == pack), None)
    if entry is None:
        print(f"✗ no marketplace entry for pack {pack!r}"); return 1
    old = entry.get("version")
    entry["version"] = ver
    MARKETPLACE.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    pj_path = ROOT / entry.get("source", "").lstrip("./") / ".claude-plugin" / "plugin.json"
    pj = json.loads(pj_path.read_text(encoding="utf-8"))
    pj["version"] = ver
    pj_path.write_text(json.dumps(pj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    clog = ROOT / "CHANGELOG.md"
    if clog.exists():
        text = clog.read_text(encoding="utf-8")
        heading = f"## [{pack}-v{ver}] - {date.today().isoformat()}"
        if heading not in text:
            lines = text.splitlines()
            for i, ln in enumerate(lines):
                if ln.startswith("## "):
                    lines[i:i] = [heading, "", "- (fill in)", ""]
                    break
            else:
                lines += ["", heading, "", "- (fill in)", ""]
            clog.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✓ {pack}: {old} → {ver} (marketplace.json + plugin.json + CHANGELOG scaffold)")
    return 0


def parity(packs: dict[str, str]) -> int:
    """Diff installed marketplace-clone SKILL.md frontmatter vs repo HEAD (owner-machine detector).

    The live drift mechanism: ~/.claude/plugins/marketplaces/<mkt> is a git clone that only
    moves on /plugin marketplace update — it served pre-1.1.0 descriptions for a month.
    Skips cleanly when no clone exists (CI-safe).
    """
    mkt = Path.home() / ".claude" / "plugins" / "marketplaces" / "revenant"
    if not mkt.is_dir():
        print("parity: no local marketplace clone — skipped (nothing installed here)")
        return 0
    drifted = 0
    for pack in packs:
        for repo_sk in sorted((PACKS / pack / "skills").glob("*/SKILL.md")):
            member = repo_sk.parent.name
            inst_sk = mkt / "packs" / pack / "skills" / member / "SKILL.md"
            if not inst_sk.is_file():
                print(f"  ✗ {member}: not present in installed clone"); drifted += 1
                continue
            fm = lambda p: p.read_text(encoding="utf-8").split("---")[1]
            if fm(repo_sk) != fm(inst_sk):
                print(f"  ✗ {member}: installed frontmatter drifts from repo HEAD"); drifted += 1
            else:
                print(f"  ✓ {member}")
    print("parity:", f"DRIFT ({drifted}) — run /plugin marketplace update revenant (or git pull the clone)" if drifted else "clean")
    return 1 if drifted else 0


def main() -> int:
    text = registry_text()
    packs = registry_packs(text)
    packs = {p: prof for p, prof in packs.items() if (PACKS / p).is_dir() or pack_members(text, p)}
    if BUMP:
        return bump_pack(*BUMP)
    if PARITY:
        return parity(packs)
    check_marketplace(packs)

    total_members = total_folders = total_manifests = 0
    versions: dict[str, tuple[Path, str]] = {}
    synced = drift = 0

    for pack, profile_notes in packs.items():
        profile = profile_notes.split(" ")[0] if profile_notes else "standalone"
        members = pack_members(text, pack)
        seams = pack_seams(text, pack)
        budgets = pack_budgets(text, pack)
        cap, repo, conf = pack_lines(text, pack, profile_notes)
        print(f"registry[{pack}]: {len(members)} members · {len(seams)} seams")
        validate_seams(pack, [m for m, _, _ in members], seams)
        pack_md = render_pack_md(pack, profile, members, cap, repo, conf, seams, pack_seam_note(text, pack))
        skills_dir = PACKS / pack / "skills"
        folders = [skills_dir / m for m, _, _ in members]
        missing = [f.name for f in folders if not f.is_dir()]
        for nm in missing:
            fail(f"[{pack}] member in registry but not in packs/{pack}/skills/: {nm}")
        total_members += len(members)
        total_folders += len(members) - len(missing)
        for folder in folders:
            if not folder.is_dir():
                continue
            target = folder / "references" / "pack.md"
            current = target.read_text(encoding="utf-8") if target.exists() else ""
            strip = lambda s: re.sub(r"Last stamped: [\d-]+", "Last stamped: X", s)
            if strip(current) != strip(pack_md):
                drift += 1
                if CHECK:
                    fail(f"{folder.name}: references/pack.md drifts from the registry")
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(pack_md, encoding="utf-8")
                    synced += 1
                    print(f"  ✎ synced {folder.name}/references/pack.md")
            validate_seam_manifest(folder, len(seams))
            total_manifests += 1
            versions[folder.name] = (skills_dir, validate_skill(folder, budgets.get(folder.name)))

    if FOOTPRINT:
        print()
        print("footprint — measured SKILL.md body vs registry budget (chars/4, ±15%)")
        print()
        tot = 0
        for member in sorted(FOOTPRINTS):
            measured, budget = FOOTPRINTS[member]
            tot += measured
            short = member.split("-")[-1]
            if budget is None:
                print(f"  {short:<12} {measured:>6}       —  (no budget row)")
            else:
                head = budget - measured
                flag = "  ← OVER" if head < 0 else ("  ← thin" if head < 200 else "")
                print(f"  {short:<12} {measured:>6}  /{budget:>6}   {head:>+6} headroom{flag}")
        print()
        print(f"  {'TOTAL':<12} {tot:>6} tokens across {len(FOOTPRINTS)} members — the whole-pack"
              f" figure, not a per-session cost: members load one at a time.")

    if not CHECK and not FOOTPRINT and not problems:
        DIST.mkdir(exist_ok=True)
        for member, (skills_dir, ver) in versions.items():
            if ONLY and member != ONLY:
                continue
            folder = skills_dir / member
            out = DIST / f"{member}-{ver}.zip"
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                for p in sorted(folder.rglob("*")):
                    if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
                        z.write(p, p.relative_to(skills_dir))
            print(f"  ▣ dist/{out.name}")

    print(f"\ncount integrity: registry {total_members} = folders {total_folders} = manifests {total_manifests}")
    if warnings:
        print(f"warnings: {len(warnings)} (non-fatal this release; flip to fail at the next tag)")
    if CHECK:
        print("check:", "DRIFT/PROBLEMS — see above" if (problems or drift) else "clean")
        return 1 if (problems or drift) else 0
    print("build:", "PROBLEMS — see above" if problems else f"ok ({synced} manifest(s) synced)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
