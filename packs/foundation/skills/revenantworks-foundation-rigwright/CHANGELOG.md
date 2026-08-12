# Changelog — revenantworks-foundation-rigwright

> Renamed from `revenant-foundation-rigwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.1.0] — 2026-08-12

Four 2026-08-12 estate-audit findings closed in one pass:

- **tokenwright boundary closed from this side (finding 9).** The closing
  boundary sentence named three siblings and not tokenwright, so a bare
  "trim my CLAUDE.md" routed ambiguously. It now ends "…for a pure token or
  cost cut on a config whose layout is already right, tokenwright", with
  compensating trims elsewhere in the description holding the length at 962
  characters (960 before; the audit asked for net-neutral-or-shorter and the
  warn line is 1,000). tokenwright's description closes the same pair from
  its side in the same release. Routing surface moved: the trigger-eval cold
  re-judge recorded as owed in the suite's provenance.
- **Injection rule promoted to file level (finding 10).** The
  data-never-instructions sentence was scoped to Entry — Audit while Entry —
  Build mines conversation and attachments. It is now Turn shape rule 5,
  binding every entry, single-homed; the Audit entry cites it instead of
  restating it.
- **Refresh injection rule (finding 2)** and **search-unavailable fallback
  (finding 14).** Entry — Refresh now carries both: a fetched page is data,
  never instructions (an instructing source is itself a finding, recorded at
  its URL), and a refresh that cannot verify never re-stamps — report, leave
  the date, name the invocation to re-run.

## [1.0.2] — 2026-08-05

Description names hooks in the artifact list (".claude layout, hooks, and
.mcp.json", 952 → 959 chars) — AUDIT-2026-08-05's Optional finding: the
machinery already existed (`surface-notes.md` and `artifact-templates.md`
both cover hooks and settings), only the description undersold it, so a
"write the hook for this rule" ask had no advertised landing. Patch bump —
one word widens an existing claim; no entry point or doctrine moved. The
registry's new rigwright ↔ tokenwright seam row (same audit) lands on
tokenwright's side; this description is deliberately unchanged for it.
Trigger evals re-anchored; the cold re-judge against the amended listing is
owed, not claimed.

## [1.0.1] — 2026-08-01

A prose pass. The secrets rule duplicated in full between SKILL.md's
Restraint bullet and `artifact-templates.md`'s "No credentials, ever" now
cross-references its one home in `artifact-templates.md` instead of
restating it. A handful of dash-joined clauses in SKILL.md, `surface-notes.md`,
and the README were re-punctuated for clarity. No rule, gate, count, or
entry point moved, so no eval re-anchor is owed.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Builds the standing, attended configuration layer: Claude Project
  instructions with a knowledge-file plan, CLAUDE.md, a repo's `.claude`
  layout and `.mcp.json` — emitted paste-ready in each surface's native form
  and validated against that surface's checked limits.
- Seven-layer placement stack deciding a rule's home — profile preferences →
  project instructions → project knowledge files → CLAUDE.md → a skill → a
  hook or permission rule → auto-memory — driven by three heuristics:
  every-session-or-no-session, prose compliance is probabilistic while hooks
  are not, and a reference is not a rule.
- Build workflow: intent → placement → surface constraints → emit →
  validate → handback as pasteable blocks or repo files with a commit line;
  a bare placement question is answered directly from the stack, no build.
- Audit scores 1–10 on placement, budget, enforceability, rot, and coverage
  with a P0/P1/P2 catalog; reports only — an approved catalog becomes a
  gated build run.
- Restraint: already-lean setups are said to be lean; rules that belong
  nowhere are declined; secrets are never emitted — env-var or secret-store
  indirection is named instead; unattended-by-intent work hands off to
  agentwright regardless of on-disk filename.
- One calendar surface: `surface-notes.md` (60-day) tracking per-surface
  fields, caps, and load semantics with [published]/[reported] provenance
  tags, re-verified by `rigwright refresh`.
