# Changelog — revenant-foundation-promptwright

## [1.1.1] — 2026-08-01

Prose/register pass over this skill's own files (SKILL.md, README.md,
`references/hostile-interpreter.md`): dash-chained run-on sentences split
into plain sentences, the README's crammed differentiator sentence converted
to a short bulleted list, and the hostile-read catalog's four failure-shape
entries trimmed to keep only the added instances, pointing back to SKILL.md
Phase 6 for the definition instead of re-stating it.

Also fixed: `references/model-snapshot.md`'s tier-map footnotes skipped ²
entirely (¹, then ³, then ⁴, with no ² anywhere in the file) — a table-
formatting defect, not a claim change. Renumbered sequentially (¹ ² ³) since
no source in the pack recorded what a footnote 2 would have claimed; the
facts each footnote carries are unchanged, only their markers moved.

No rule, gate, count, or entry point moved. No eval re-anchor is owed.

## [1.1.0] — 2026-08-01

Entry — Model gains **plan grain**: handed a task list or project plan with a
targets ask, steps 1–3 run per subtask and delivery becomes one target table —
`subtask · tier + model · effort/depth · run inline or as a subagent · one-line
why` — in place of the single-recommendation line. Two contracts ride with
every table: the **living table** (a subtask created mid-session gets a row
through the same steps *before* dispatch, so emergent work adheres to the same
tier logic as the plan it joins) and the **standing rule** (one paste-ready
rule line emitted beneath the table so the contract survives the session;
layer placement stays rigwright's, named not made). Decomposition stays the
caller's — promptwright targets the subtasks it is handed and never re-plans
the project.

- `description` gains the plan clause ("a prompt, a live task, or each subtask
  of a plan"), the mid-session binding, and the target-table mention in the
  `promptwright model` parenthetical.
- **Body budget raised 8500 → 8800** in skillwright's registry: the plan-grain
  delivery shape and both contracts are decision rules, body-resident like the
  rest of Entry — Model — the content reason this raise owes per the
  registry's own budget notes.
- Trigger rows #31–#34 (two should, two shouldn't — the rigwright standing-
  config boundary and the no-targets decomposition boundary) and assertion
  Case 37 (target table + living table + standing rule, two turns) added;
  both suites re-anchored. All 34 trigger rows judged cold against the new
  description this pass; Case 37 is authored, not executed — see
  `evals/RESULTS.md`.

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
