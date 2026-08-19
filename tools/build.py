#!/usr/bin/env python3
"""claude-skills — multi-pack build: sync, validate, package.

Single source of truth: the pack tables in
packs/foundation/skills/revenantworks-foundation-skillwright/references/pack-registry.md.
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
  python3 tools/build.py --only revenantworks-foundation-tokenwright   limit zip build to one member (sync still runs)
  python3 tools/build.py --bump-pack <pack> <X.Y.Z>   one-stroke version write: marketplace entry +
                                    pack plugin.json + root CHANGELOG scaffold (prevents split-brain bumps)
  python3 tools/build.py --parity   diff EVERY shipped file in both installed copies against repo HEAD —
                                    the marketplace clone AND the plugin cache Claude Code actually loads;
                                    exit 1 on drift; skips cleanly when no local install exists (CI-safe)
  python3 tools/build.py --footprint  measured SKILL.md body tokens per member against its registry budget,
                                    plus the pack total; report only, writes nothing, never fails

Validation also covers (added 2026-07-24): pack plugin.json == marketplace entry version
(hard fail — the split-brain class), eval provenance freshness and eval-table orphan
rows (hard fail — flipped 2026-08-07 after the 2.0.0 tag, as promised), description >=1000 chars and
and body footprint. The footprint gate was RESCOPED 2026-07-25: >500 body lines stays a hard fail (the
agentskills.io norm), while the 5k-token figure is this pack's own advisory and now gates on whether the
overage is DECLARED — a member over it must carry a budget {tokens, why}. Undeclared overage hard-fails
(flipped 2026-08-07, the promised next-tag flip); exceeding your own declared budget warns as drift. MOVED 2026-07-27: for a pack
member the budget lives in the registry's `**<pack> budgets**` table, not in frontmatter — frontmatter is
loaded on every invocation, so a `why` there cost 51-95 tokens per run to explain a build-time number.
A registry row costs zero runtime tokens, which is what makes declaring ALL members affordable rather
than only the over-advisory ones. Standalone skills outside a pack keep the frontmatter form.

Stdlib only. Run from the repo root (or anywhere; paths resolve from this file).
"""
import json
import os
import re
import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
DIST = ROOT / "dist"
REGISTRY = PACKS / "foundation" / "skills" / "revenantworks-foundation-skillwright" / "references" / "pack-registry.md"
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
    """Non-fatal by design: deliberate drift/advisory signals (declared-budget drift,
    seam hygiene, ceiling-riding descriptions). The promised next-tag flips landed
    2026-08-07 — undeclared overage and the two eval-table checks now fail()."""
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


def registry_pack_notes(text: str, pack: str) -> str:
    """The Notes cell of one pack's row in the Pack registry table.

    Added 2026-08-07 with the second pack. `registry_packs()` captures the *Profile*
    cell only, and `pack_lines()` was handed that as its conformance source — so a pack
    whose conformance line lives (as every pack's does) in its Notes cell never matched
    locally and fell through to a whole-document search, which returns the FIRST pack's
    line. With one pack that was invisible; with two it silently stamped ossuary's
    manifest with foundation's checks and adoption date. Per-pack notes close it, and
    `pack_lines()` no longer searches the whole document.
    """
    block = text.split("## Pack registry", 1)[1]
    for line in block.splitlines():
        m = re.match(rf"\|\s*`{re.escape(pack)}`\s*\|[^|]*\|(.*)\|\s*$", line)
        if m:
            return m.group(1).strip()
    return ""


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
    """The note under the seam table (verb overloads, recorded-open seams).

    May run one line or many (a dated list of closures) — captured up to
    the next top-level `**<pack> <word>:**` annotation (capstone, canonical
    repo) or end of text, whichever comes first.
    """
    m = re.search(rf"(\*\*{pack} seam notes:\*\*.+?)(?=\n\n\*\*{pack} \w|\Z)", text, re.DOTALL)
    return m.group(1).strip() if m else ""


DEFAULT_CHECKS = ("2026-07-13", "C-1 drift-audit verb · C-2 neutral default")


def pack_lines(text: str, pack: str, pack_notes: str) -> tuple[str, str, tuple[str, str]]:
    """Capstone, repo, and conformance lines for one pack (graceful when absent).

    `pack_notes` is this pack's OWN Notes cell (see registry_pack_notes). The former
    whole-document fallback is gone: it made a missing per-pack line resolve to some
    other pack's, which is worse than a stated default.
    """
    cap_m = re.search(rf"\*\*{pack} capstone:\*\*(.+)", text)
    cap = cap_m.group(1).strip() if cap_m else "—"
    repo_m = re.search(rf"\*\*{pack} canonical repo:\*\*\s*(`[^`]+`)", text)
    repo = repo_m.group(1) if repo_m else "the registered canonical repo"
    conf = re.search(r"Conformance checks \(([\d-]+)\): ([^|.]+)", pack_notes)
    checks = conf.group(2).strip() if conf else DEFAULT_CHECKS[1]
    adopted = conf.group(1) if conf else DEFAULT_CHECKS[0]
    return cap, repo, (adopted, checks)


def render_pack_md(pack: str, profile: str, members, cap, repo, conf, seams=(), seam_note="") -> str:
    adopted, checks = conf
    n_word = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
              8: "eight", 9: "nine", 10: "ten"}.get(len(members), str(len(members)))
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
        # (Narrowed 2026-07-24 from verified|restamped|stamped; all four calendar
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
    # The only two frontmatter limits confirmed against a real upload error, so the only
    # two the gate asserts. `compatibility` past 500 chars was rejected by the live
    # claude.ai upload form on 2026-08-14 (ossuary-v2.2.2 — bonecaller 533, linecaller
    # 667). `description` is deliberately NOT bounded here beyond the house ceiling
    # below: the pack twice trimmed it on an assumed 500 that two real uploads never
    # reproduced (ossuary-v2.2.3), and a guessed number in the gate institutionalizes
    # that mistake. Fail rather than upload-fail; the tightest live margin is 463/500.
    compat = re.search(r"^compatibility:\s*(.+)$", fm, re.M)
    if compat and len(compat.group(1)) > 500:
        fail(f"{folder.name}: compatibility {len(compat.group(1))} chars > 500 — the live upload "
             f"form rejects this field past 500 (confirmed 2026-08-14)")
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
    # Undeclared overage is the defect (hard fail since 2026-08-07 — item ③'s promise
    # landed). Declared overage is a recorded decision. Exceeding your OWN declared budget is drift
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
        fail(f"{folder.name}: SKILL.md body ≈{body_tokens} tokens > {FOOTPRINT_ADVISORY//1000}k "
             f"advisory with no budget row in the registry and none in frontmatter — declare it "
             f"and why it earns the room, or slim it (undeclared overage: hard fail since 2026-08-07)")
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
    """Eval-suite integrity (added 2026-07-24; WARN this release, fail at the next tag).

    1. Provenance freshness: an evals/*.md head naming an older member version with no
       dated reconfirmation line is the exact defect class evalwright audits others for.
    2. Orphan rows: a numbered table row appearing after prose that follows the table
       silently escapes count checks (the brandwright rows-21/22 class).
    """
    evdir = folder / "evals"
    if not evdir.is_dir():
        return
    for f in sorted(evdir.glob("*.md")):
        # RESULTS.md is an execution ledger — frozen records re-confirmed on their own
        # cadence, so old version stamps there are history, not provenance drift.
        if f.name == "RESULTS.md":
            continue
        # Head window: 6 lines was tuned for the original short headers; re-anchor
        # notes accrete downward, so read enough of the head to see the newest one.
        head_lines = f.read_text(encoding="utf-8").splitlines()[:16]
        prov_text = "\n".join(ln for ln in head_lines
                              if re.search(r"(?i)provenance|derived|target|re-?anchored", ln))
        prov_versions = re.findall(r"\bv(\d+\.\d+\.\d+)\b", prov_text)
        # 2026-08-08 tightening: a dated re-anchor line used to satisfy freshness even
        # when it re-anchored to an OLD version — linecaller's test-cases.md sat at
        # "re-anchored to v1.1.0" through the 1.2.0 release and the gate read clean.
        # Rule: the CURRENT member version must be named somewhere on the provenance
        # lines. Membership, not last-token: provenance lines legitimately end with
        # other artifacts' versions (brandwright's names its fixture's v1.0.0 last),
        # and predecessor-era designations can read HIGHER than current after the
        # 2026-07-31 re-baseline, so ordering comparisons are meaningless. Known
        # accepted gap: a reused designation could satisfy membership from a
        # predecessor-era mention — a heuristic gate, strictly tighter than before.
        if prov_versions and fm_ver not in prov_versions:
            fail(f"{folder.name}: evals/{f.name} provenance names {sorted(set(prov_versions))} "
                 f"but never the current member version {fm_ver} — re-anchor in the same commit")
        # Orphan = a numbered row whose nearest preceding non-empty line is not table-shaped
        # (a row under its own "|#|Query|" header in a later section is structured, not orphaned).
        lines = f.read_text(encoding="utf-8").splitlines()
        prev = ""
        for ln in lines:
            if re.match(r"\|\s*\d+\s*\|", ln) and prev and not prev.lstrip().startswith("|"):
                fail(f"{folder.name}: evals/{f.name}: numbered row {ln.strip()[:60]!r} follows prose, "
                     f"not a table — orphaned from count checks; move it into a table")
                break
            if ln.strip():
                prev = ln


def bump_needed(packs: dict[str, str], versions: dict[str, tuple[Path, str]]) -> list[str]:
    """Shipped content changed since the pack's current version was tagged, but no version moved.

    Added 2026-08-17 for the post-commit hook (.claude/hooks/bump-check.py). For each pack whose
    tag `<pack>-v<plugin.json version>` exists locally, diff HEAD (plus the working tree) against
    that tag under packs/<pack>/. Any difference means the pack has moved past what its version
    names — the pack version is what installs and zips key on, so the change is invisible until
    it moves. Emits `pack bump needed: <pack>` and, per member whose folder differs while its
    frontmatter version equals the tagged one, `member bump needed: <member>`. Advisory (warn),
    never a failure: a pass legitimately carries unbumped commits until it closes. Silent when
    git or the tag is absent (fresh clone before `git fetch --tags`, CI on a detached ref).
    """
    import subprocess
    lines: list[str] = []
    for pack in packs:
        pj = PACKS / pack / ".claude-plugin" / "plugin.json"
        if not pj.is_file():
            continue
        ver = json.loads(pj.read_text(encoding="utf-8")).get("version")
        tag = f"{pack}-v{ver}"
        try:
            has_tag = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "-q", "--verify", f"refs/tags/{tag}"],
                                     capture_output=True, text=True).returncode == 0
            if not has_tag:
                continue
            changed = subprocess.run(["git", "-C", str(ROOT), "diff", "--name-only", tag, "--", f"packs/{pack}"],
                                     capture_output=True, text=True).stdout.split()
        except (OSError, FileNotFoundError):
            return lines
        if not changed:
            continue
        lines.append(f"pack bump needed: {pack} — {len(changed)} shipped file(s) differ from {tag} "
                     f"while plugin.json still says {ver}")
        for member, (skills_dir, mver) in versions.items():
            rel = f"packs/{pack}/skills/{member}/"
            if not any(c.startswith(rel) for c in changed):
                continue
            try:
                old = subprocess.run(["git", "-C", str(ROOT), "show", f"{tag}:{rel}SKILL.md"],
                                     capture_output=True, text=True, encoding="utf-8").stdout
            except OSError:
                continue
            m = re.search(r'version:\s*"?([\d.]+)"?', old.split("---")[1] if old.count("---") >= 2 else "")
            if m and m.group(1) == mver:
                lines.append(f"member bump needed: {member} — shipped files differ from {tag} at the same "
                             f"member version {mver}")
    for ln in lines:
        warn(ln)
    return lines


def check_marketplace(packs: dict[str, str]) -> None:
    """Cross-check the catalog: every pack has an entry; every entry's source exists;
    the pack's own plugin.json version matches the catalog (added 2026-07-24 —
    hard fail: a plugin.json/marketplace split-brain shipped for a month, CI-invisible)."""
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


def _frontmatter(p: Path) -> str:
    return p.read_text(encoding="utf-8").split("---")[1]


def _norm(p: Path) -> str:
    """File text with line endings normalised — a CRLF working tree vs an LF clone is
    not drift, and reporting it as such trains the reader to ignore the detector."""
    return p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


# Runtime/VCS artefacts that exist on one side by design — never drift.
# `.in_use` is the plugin manager's live-session marker directory, not shipped content.
PARITY_SKIP = {".in_use", ".DS_Store", ".git", "__pycache__"}

def _env_path(name: str) -> Path | None:
    """A local filesystem path read from an environment variable, or None if unset.

    Both constants below used to be hardcoded absolute paths into two PRIVATE repos on
    the owner's own drive. This file ships on a PUBLIC repo (revenantworks/claude-skills)
    — a hardcoded path would publish the owner's local drive layout, directory tree, and
    the existence and location of both private repos to every reader of origin/main, with
    no protected name involved. Reading them from the environment instead means the value
    never appears in this file or its diff; only the owner's own machine, where the
    variables are set, ever resolves them.

    Unset anywhere else — every clone but the owner's rig — both checks below skip
    cleanly, the same as when a brand or peer repo is simply absent today. That is the
    correct default: this is parity-detection convenience for the owner, not a
    load-bearing gate for anyone else running `--parity`.

    Set on the owner's rig only (a user-level environment variable, or a PowerShell
    profile line — never a tracked file, and never this comment): point
    CLAUDE_SKILLS_BRAND_REPO_SOURCE at the brand repo's own `brand-definition.md`, and
    CLAUDE_SKILLS_PEER_SOURCE_NORTHSTAR at the peer brand repo's own `brand-definition.md`.
    Deliberately not spelled out as a literal path here, in this comment, in a public
    file — that would just recreate the leak this function exists to close.
    """
    val = os.environ.get(name)
    return Path(val) if val else None


# The brand-carriage law means this repo ships this file NEUTRAL forever — but on the
# owner's own machine, install-definition.py (in the private brand repo) deliberately
# overlays the real definition into the CACHE copy only, never the clone. Comparing the
# cache against this repo's neutral HEAD therefore reports permanent "drift" for a file
# that is working exactly as designed — the same never-passes-once-it-works defect as
# the peer-file case below, just uncaught until a pack bump actually landed post-fix.
# The clone must still be compared against neutral HEAD: a branded clone IS a real
# brand-carriage violation. Only the loaded cache gets the swapped source of truth.
_BRAND_DEFINITION_REL = Path("skills") / "revenantworks-foundation-brandwright" / "references" / "brand-definition.md"
_BRAND_REPO_SOURCE = _env_path("CLAUDE_SKILLS_BRAND_REPO_SOURCE")
# Peer definitions live in their own home repos (never in HEAD); parity compares each
# installed peer against its declared source when that repo is present on this machine
# AND its env var is set (see _env_path above).
_PEER_SOURCES = {
    "northstar": _env_path("CLAUDE_SKILLS_PEER_SOURCE_NORTHSTAR"),
}


def _shipped(root: Path):
    """Every file that ships from a pack root, relative to it."""
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix == ".pyc" or PARITY_SKIP.intersection(p.parts) or p.name in PARITY_SKIP:
            continue
        yield p.relative_to(root)


def _compare_tree(repo_root: Path, inst_root: Path, label: str, is_cache: bool = False) -> int:
    """Diff every shipped file, not just SKILL.md frontmatter. Returns the drift count.

    Frontmatter-only was the original scope and it under-reported twice: it reported clean
    while `ledger.md` and `spec.md` in the loaded copy lagged a post-tag commit, because a
    reference doc, README, ledger or spec is not frontmatter and was never compared.
    """
    drift = []
    for rel in _shipped(repo_root):
        inst = inst_root / rel
        src = repo_root / rel
        if is_cache and rel == _BRAND_DEFINITION_REL and _BRAND_REPO_SOURCE is not None and _BRAND_REPO_SOURCE.is_file():
            src = _BRAND_REPO_SOURCE
        if not inst.is_file():
            drift.append(f"missing: {rel.as_posix()}")
        elif _norm(src) != _norm(inst):
            drift.append(f"differs: {rel.as_posix()}")
    for rel in _shipped(inst_root):
        if (repo_root / rel).is_file():
            continue
        # A peer brand definition (brandwright 1.2.0+ holds several and selects one
        # per run) is installed from a PRIVATE repo by design and is deliberately
        # absent from HEAD. Reporting it as drift made parity a gate that could
        # never pass once a peer existed — the inverse of a gate that never fails,
        # and just as useless. The primary brand-definition.md is still compared.
        # 2026-08-08: a peer with a declared home repo is now compared against that
        # source (the line-654 mechanism, extended) — an unchecked peer meant a moved
        # peer definition loaded stale forever while parity reported clean. A peer
        # with no map entry keeps the old skip.
        m = re.fullmatch(r"brand-definition-([a-z0-9-]+)\.md", rel.name)
        if m:
            peer_src = _PEER_SOURCES.get(m.group(1))
            if peer_src and peer_src.is_file() and _norm(peer_src) != _norm(inst_root / rel):
                drift.append(f"differs: {rel.as_posix()} (vs its peer source, {m.group(1)}'s home repo)")
            continue
        drift.append(f"extra:   {rel.as_posix()}")
    if drift:
        for d in drift[:20]:
            print(f"  ✗ {d}")
        if len(drift) > 20:
            print(f"  … and {len(drift) - 20} more")
    else:
        print(f"  ✓ {label}: every shipped file matches repo HEAD")
    return len(drift)


def parity(packs: dict[str, str]) -> int:
    """Diff every shipped file in both installed copies vs repo HEAD (owner-machine detector).

    TWO surfaces drift independently, and checking only the first is how a session kept
    loading a superseded member while this command reported clean (2026-08-01, promptwright
    1.1.0):

      clone — ~/.claude/plugins/marketplaces/<mkt>, a git clone that moves only on
              /plugin marketplace update. It served pre-1.1.0 descriptions for a month.
      cache — ~/.claude/plugins/cache/<mkt>/<pack>/<version>/, the copy Claude Code actually
              LOADS, written only on /plugin install|update. A refreshed clone does not move
              it: the clone is where an update reads FROM, the cache is what it writes TO,
              so clone-clean and cache-stale is a real and silent state.

    Note the cache flattens the pack root — `skills/<member>/`, not `packs/<pack>/skills/`.
    Each surface skips cleanly when absent (CI-safe).

    Scope is EVERY shipped file, not just SKILL.md frontmatter. The narrow version reported
    clean twice while the loaded copy was stale, because the files that lagged — `ledger.md`,
    `spec.md` — are not frontmatter and were never compared. Line endings are normalised: a
    CRLF working tree against an LF clone is not drift.
    """
    home = Path.home() / ".claude" / "plugins"
    mkt = home / "marketplaces" / "revenantworks"
    drifted = 0
    checked = 0

    if not mkt.is_dir():
        print("clone: no local marketplace clone — skipped (nothing installed here)")
    else:
        checked += 1
        print("clone — ~/.claude/plugins/marketplaces/revenantworks")
        for pack in packs:
            drifted += _compare_tree(PACKS / pack, mkt / "packs" / pack, f"clone:{pack}")

    installed = home / "installed_plugins.json"
    if not installed.is_file():
        print("cache: no installed_plugins.json — skipped (no plugin installed here)")
    else:
        entries = json.loads(installed.read_text(encoding="utf-8")).get("plugins", {})
        for pack in packs:
            recs = entries.get(f"{pack}@revenantworks") or []
            if not recs:
                print(f"cache: {pack} not installed — skipped")
                continue
            checked += 1
            for rec in recs:
                root = Path(rec.get("installPath", ""))
                print(f"cache — {root} ({rec.get('scope', '?')} scope, v{rec.get('version', '?')})")
                if not root.is_dir():
                    print(f"  ✗ {pack}: installPath does not exist"); drifted += 1
                    continue
                drifted += _compare_tree(PACKS / pack, root, "loaded copy", is_cache=True)

    if not checked:
        print("parity: nothing installed here — skipped")
        return 0
    print("parity:", f"DRIFT ({drifted}) — refresh the clone (/plugin marketplace update revenantworks), "
          f"THEN the loaded copy (claude plugin update <pack>@revenantworks); both, in that order"
          if drifted else "clean")
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
        cap, repo, conf = pack_lines(text, pack, registry_pack_notes(text, pack))
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
            # Prune this member's superseded builds. Without it dist/ accumulates one zip
            # per version ever built, and release-doctrine treats these as the upload
            # source of truth — so a stale neighbour is a mis-upload waiting to happen.
            for old in DIST.glob(f"{member}-*.zip"):
                if old != out:
                    old.unlink()
                    print(f"  ✗ dist/{old.name} (superseded)")

    if CHECK:
        bump_needed(packs, {m: (d, v) for m, (d, v) in versions.items() if v})

    print(f"\ncount integrity: registry {total_members} = folders {total_folders} = manifests {total_manifests}")
    if warnings:
        print(f"warnings: {len(warnings)} (deliberate drift/advisory signals — non-fatal by design)")
    if CHECK:
        print("check:", "DRIFT/PROBLEMS — see above" if (problems or drift) else "clean")
        return 1 if (problems or drift) else 0
    print("build:", "PROBLEMS — see above" if problems else f"ok ({synced} manifest(s) synced)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
