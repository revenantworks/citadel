# Changelog — revenant-foundation-rigwright

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
