# Changelog — revenant-foundation-promptwright

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Seven-phase build pipeline — Intake → Analyze & score → Pick structure →
  Clarify → Build → Re-score & self-check → Output — with a five-dimension
  1–10 scoring rubric (clarity, specificity, context, completeness,
  structure) delivered as a before→after delta.
- Framework menu with named-origin doctrine: CO-STAR, RISEN, TIDD-EC, BAB,
  RTF/APE, chain-of-thought, and agent/system shapes; a user-named framework
  always wins and is never silently substituted.
- Fast path: a fixed five-condition gate collapsing Phases 1–6 into one trace
  line for small RTF/APE-shape prompts, with published exit conditions.
- Hostile read: a bad-faith-literal pass over every binding line — four
  failure shapes, each with a named repair — plus collision and
  instruction-boundary cross-checks; the knowledge-vacuum check flags factual
  tasks lacking reference material before scoring.
- Model-tier routing (S/A/B/C: frontier / flagship / balanced / fast) feeding
  a mandatory Model line on every delivered prompt, and the standalone
  `promptwright model` entry for live-task tier picks without a build.
- Output contract: TL;DR, Model line, Score, Structure, an optional
  self-contained HTML prompt card, and the fixed four-option "Keep going"
  close.
- One calendar surface: `model-snapshot.md` (60-day), re-verified by
  `promptwright refresh`, with tier-name fallback when the stamp is stale.
