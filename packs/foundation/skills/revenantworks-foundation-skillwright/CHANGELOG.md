# Changelog — revenantworks-foundation-skillwright

> Renamed from `revenant-foundation-skillwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.1.1] — 2026-08-08

- Eval scenario distance restored (2026-08-08 estate audit, owner judgment):
  the Entry — Pack core case (trigger row 31, assertion case input) now reads
  "a customer-support engineer at a software company" — the previous role was
  a near-description of a firewalled identity's own product; same routing
  shape, no Expect changed.
- `references/pack-registry.md`: ossuary member rename recorded across the
  members, budgets, and seams tables (`cardcaller` → `bonecaller`, ossuary
  2.0.0) with the seam note's frozen narrative preserved.
- Shipped-file changes now bump the member (this entry): the 2.2.3 release
  changed three members' evals without moving their versions, which starves
  the claude.ai lazy-upload rule of its signal — RUNBOOK amended to codify
  the member-bump rule.

## [1.1.0] — 2026-08-07

Two doctrine families added to `references/rubrics.md`, both from defects that
shipped output looking correct.

- **Generator classes G-1 to G-3**, scored where the subject generates one
  artifact from another. G-1: a generator carrying a hardcoded list of its
  source's sections drifts from that source — a hardcoded heading pair dropped a
  renamed section, and a table parser returning only the first table in a block
  dropped every later one, both silently — so derive the list from the source or
  hard-fail on a missing expected section, never skip-and-continue. G-2: a
  `--check` parity mode is part of the generator, not an extra; committed build
  output with no parity gate is indistinguishable from hand-edited output. G-3:
  stale-output detection, so a retired artifact in the target directory cannot
  linger as apparent truth. Each carries its severity floor, and the family is
  N/A on a subject with no generating surface, per *Absent is not the same as
  clean*.
- **Naming-class coverage**, the rule that a naming convention binds every class
  carrying a name — a scheduled task's or routine's display name, its id, and a
  published artifact's title included — that an id carries no day or cadence
  suffix because the cadence lives in the schedule expression, and that the
  classes are enumerated before any of them is scored. The failure it answers:
  a naming audit that measured the machine-readable ids, passed green, and never
  looked at the human-readable display names beside them.

Body wiring cost 33 tokens across two clauses — the `rubrics.md` load-budget
line now names both families, and Entry — Audit step 3 scores them alongside the
registered pack conformance checks. Measured body 7,750 → 7,783 against the
unchanged 7,800 row; the ceiling was not raised, so the next body edit on this
member needs the footprint run first. The `description` is byte-identical and no
entry point, count, or gate moved, so no trigger re-run is owed; the eval
provenance lines are re-anchored with that stated, and no case was added — still
40, with the generator and naming classes authored-not-covered, recorded here
rather than claimed.

## [1.0.6] — 2026-08-05

Lossless trim (AUDIT-2026-08-05 TRIM verdict) at two sites the audit named,
buying headroom back on a body sitting 33 tokens under its 7,800 ceiling.
Build step 6's registry-guard passage is compressed with every asserted
element intact — the absence rule, Integrate-step-1 ownership, the
never-visits-an-unregistered-folder rationale, the drifts-all-N opposite
shortcut with its per-sibling `--check` failure, and the
handback-names-the-roster close (Case 17's five anchors, all standing). The
bare-invocation cap sentence is compressed with the four-sentence cap, the
one-per-job gloss, the complete five-verb map, and the never-a-fifth-sentence
rule all kept (Case 14's anchors). No rule, count, entry point, or mandated
verbatim text moved — the Entry — Build reply itself is untouched. Patch
bump; suite re-anchored, no case moved. This pass also carries the registry's
rigwright ↔ tokenwright seam row and its corrected naming note
(AUDIT-2026-08-05 seam resolution) — registry content, not skillwright
doctrine.

## [1.0.5] — 2026-08-01

`references/release-doctrine.md` — Install parity: the section described
`--parity` as comparing `SKILL.md` frontmatter, which was true and was the
problem. That scope reported **clean** twice over a loaded copy whose
`ledger.md` and `spec.md` lagged a post-tag commit — neither is frontmatter,
so neither was ever compared. The tool now diffs every shipped file and the
section says so, with the general lesson stated once: a detector whose scope
is narrower than what it certifies produces false assurance, which is worse
than no detector because it ends the investigation.

Two limits still stand and are still named — parity skips absent surfaces
(CI-safe, not a CI gate) and knows nothing about claude.ai. No rule, gate,
count, or entry point moved.

## [1.0.4] — 2026-08-01

Prose/register pass over this skill's own files (SKILL.md, README.md,
SOURCES.md, `references/build-templates.md`, `references/rubrics.md`):
dash-chained run-on sentences split into plain sentences, the README's
crammed differentiator sentence converted to a short bulleted list, and one
wording fix in SOURCES.md ("gold-standard" → "reference implementation," to
match the term the same sentence already uses two words later). No rule,
gate, count, or entry point moved — every statement, threshold, and path
reads exactly as before, only the sentences carrying them changed shape. No
eval re-anchor is owed.

## [1.0.3] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.2] — 2026-08-01

`references/release-doctrine.md` cited predecessor-era releases by tag name.
Two of those names — `foundation-v1.1.0` and `foundation-v1.1.1` — were reused
by unrelated releases cut 2026-08-01, so the doctrine read as though its
worked example described them; its header also pointed readers at that history
as "readable in the repo" when the pre-re-baseline tags and commits no longer
exist. Both now cite **dates**, with the collision stated once in the header
and the reuse recorded in the root `CHANGELOG.md`.

No rule, gate, count, or entry point moved — the same guidance, anchored to
something that still resolves. Delivery to an install rides the next pack
bump, per the cache-key rule in 1.0.1.

## [1.0.1] — 2026-08-01

Doc correction in `references/release-doctrine.md` — Install parity. The
section described Claude Code as having **one** installed copy (the
marketplace clone) when it has **two**: the clone an install reads from, and
`~/.claude/plugins/cache/<marketplace>/<pack>/<version>/`, the copy Claude
Code actually loads and that only `claude plugin update` rewrites. Refreshing
the clone does not move the cache, so clone-current and loaded-stale is a
real, silent state — observed at foundation 1.1.0, where a session kept
loading promptwright 1.0.0 while `--parity` reported clean. The section now
names both surfaces, the two-step order, and a third honest limit (parity
knows nothing about claude.ai). It also records the mechanism underneath:
**the pack version is the cache key**, so `claude plugin update` compares
pack versions and a member-only bump is undeliverable — it reports "already
at the latest version" and serves the old body. That is the practical edge of
Two clocks: the member clock says what changed, the pack clock says what
ships. `tools/build.py --parity` was extended to match in the same pass; the
tool and the doctrine move together by design.

No entry point, gate, or count changed — a corrected description of a
mechanism that already behaved this way, so no eval row moves and no run is
owed.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Build pipeline from a one-line intent: pack & profile resolution → fresh
  best-practices research → niche verdict (DEFENSIBLE vs CROWDED/THIN, checked
  against live skill registries and plugin directories) → one-gate design
  catalog → build → self-audit → package. Every build ships spec-clean
  neutral, born testable — trigger evals and an assertion suite in the box.
- Pack design mode: tiered capability map with adopt-don't-build calls, a
  trigger-partition table, one roster gate, and a persisted `<pack>-spec.md`
  baton for staged multi-session builds.
- Audit with dual scoring (Rubric A + the skill's declared policy profile +
  pack conformance), carrying the security pass — four build-time classes
  S-1…S-4 (injection surface, secrets in the artifact, undeclared or ungated
  capability, unsafe generated defaults) — and the register-only prose pass
  with statement-freeze diff discipline.
- Port: identity-scrubbed re-issue of a skill set for a new owner — sanitize
  sweep against a strip-list, rename, stale-ref refresh, PORT-REPORT with the
  old→new map; the source set is never modified.
- Integrate: one-operation pack propagation (registry row, `pack.md` restamp
  ×N, package rebuilds) under all-or-notes integrity and a count check.
- Refresh and upkeep: 60-day re-verification of the best-practices baseline,
  plus the pack-wide staleness sweep reading every member's
  `metadata.volatile` and running the mapped refresh verb per overdue surface.
- Packaging doctrine: `.skill` zip conventions, frontmatter validation, plugin
  and marketplace prep on request; build-time eval generation stands in when
  evalwright is absent.
