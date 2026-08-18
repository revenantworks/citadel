# Changelog — revenantworks-foundation-evalwright

> Renamed from `revenant-foundation-evalwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.1.1] — 2026-08-17

Frozen member; one real defect from the 2026-08-17 estate audit + security
scan closed, nothing else touched. Body, description, and `eval-doctrine.md`
are byte-identical to 1.1.0's, so the routing surface did not move.

- **S-1 · P1 (eval half) — no injection probe for any ingesting entry.**
  Turn shape rule 4 binds Generate, Audit, and Refresh — every entry reads
  handed-in material — but the suite carried no case that seeds a directive
  inside a target, a suite under audit, or a refresh diff and asserts it is
  reported, not obeyed. The 1.1.0 re-anchor line even named "any case
  asserting Generate's injection handling" as owed a re-run; none existed.
  `evals/test-cases.md` **Case 14** adds it as one law exercised at all
  three entries (T1 generate target, T2 audited suite, T3 refresh diff),
  **authored, not run**. Count 13 → 14; the intro count line and both eval
  provenance heads re-anchored to 1.1.1; the trigger suite is unchanged at
  20 (10/10) and no RESULTS.md row was added.
- Security scan 2026-08-17: (a) injection posture — the statement is
  file-level (Turn shape rule 4) and binds every entry, Generate citing it;
  (b) no fetch-and-follow, permission widening, secret echo, or guard bypass
  in SKILL.md or the doctrine; (c) no tools, scripts, MCPs, or siblings
  assumed — siblings named with the handoff direction stated, `pack.md`
  advisory; (d) hidden-text scan clean (2026-08-17, parent-run); (e) writes
  only the target's `evals/` pair, gated once, never auto-committed; (f) the
  injection probe now exists (this entry). Frontmatter carries only `name`,
  `description`, `license`, `metadata` — upload-safe. Scoreline after the
  fix: Rubric A 9.3 / standalone pass / C-1 pass · C-2 N/A; body ≈1947
  tokens against the 2200 row. Recorded, not changed (frozen): the standalone
  profile asks for stated degradation where file tools are absent and the
  body implies rather than states it (P2); dimension 11's stated-reason
  path is a pack-level call for every file-writing member.

## [1.1.0] — 2026-08-12

One 2026-08-12 estate-audit finding closed; the description is untouched, so
the routing surface did not move:

- **Injection rule promoted to file level (finding 10).** The
  data-never-instructions sentence was scoped to Entry — Generate's target
  while Entry — Audit reads an existing suite with no equivalent statement.
  It is now Turn shape rule 4, binding every entry, single-homed; the
  Generate entry cites it instead of restating it.

## [1.0.2] — 2026-08-01

A prose pass. Two SKILL.md rules that duplicated `eval-doctrine.md` in full —
the count-drift check and the provenance-line requirement — now name the
failure mode briefly and cross-reference the doctrine file instead of
restating it. A handful of dash-joined clauses in SKILL.md and
`eval-doctrine.md` were re-punctuated for clarity. No rule, gate, count, or
entry point moved, so no eval re-anchor is owed.

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Derives a coverage map from the target — a skill or SKILL.md, a prompt
  card, or an agent spec: entry points from the description, behavior paths
  (restraint, overrides, degradation, multi-turn) from the body.
- Generates two artifacts: the should/shouldn't trigger-eval table with
  near-misses, edge note, and tuning rule, and the assertion suite with
  negative assertions first-class.
- Count integrity: stated case counts must exactly match the actual case
  count and the re-derived coverage-map row count.
- Zero-runtime-dependency law: every generated suite runs cold by hand — no
  tooling, no harness — and the skill's own audits check that first.
- Audit scores 1–10 across five checks — coverage, boundary pairs, assertion
  mechanics, count integrity, self-containment — with a stated N/A rule when
  no trigger set is supplied; refresh is diff-scoped, regenerating only
  touched cases and re-verifying counts.
- Six-state restraint table with explicit flags; no volatile surfaces —
  refresh is event-driven by target change, so pack upkeep sweeps correctly
  skip it.
