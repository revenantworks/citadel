# Test Cases — revenant-foundation-evalsmith

13 cases covering every entry point and behavior path — generate for all three target kinds, pack cross-boundary pairs, audit clean and defective suites, refresh scoping, restraint, the zero-dep law, bare invocation, gating, and the sibling boundary. Provenance: derived from revenant-foundation-evalsmith v1.0.0, 2026-07-14.

Each case: **Input** + **Assert** (mechanical checks on run output). `<no-suite>` / `<no-build>` = correct absence.

## Case 1 — generate from a skill folder
**Input:** "write the evals for <attached SKILL.md with 3 entry points and 1 restraint path>"
**Assert:** coverage map lists ≥4 rows; both files delivered; assertion count ≥ map rows; intro count equals actual case count; provenance line present.

## Case 2 — generate for a prompt card
**Input:** "generate test cases for this prompt card: <card>"
**Assert:** cases keyed to the card's stated output contract; no skill-only checks (no frontmatter assertions); counts agree.

## Case 3 — generate for an agent ops spec
**Input:** "does this agent spec have coverage? write what's missing: <spec>"
**Assert:** map includes the spec's zero-signal rule and kill-switch drill as rows; generated cases assert both.

## Case 4 — audit a sound suite
**Input:** "evalsmith audit <suite that covers its map, counts agree>"
**Assert:** five-check scoreline printed; verdict says sound; no manufactured findings (catalog empty or Optional-only).

## Case 5 — audit catches a count mismatch
**Input:** audit a suite whose intro says 18 cases over 22 actual.
**Assert:** count-integrity check scored ≤4; catalog carries a P1+ row with the exact corrected line.

## Case 6 — self-containment is P0
**Input:** audit a suite whose cases say "run evalsmith to verify."
**Assert:** self-containment scored ≤3; a P0 row names the zero-dep law; fix rewrites the step as a cold-runnable check.

## Case 7 — refresh is diff-scoped
**Input:** T1 — generate for a 3-entry skill. T2 — "evalsmith refresh: entry 4 was added, entry 2 renamed."
**Assert:** T2 adds rows for entry 4, updates entry 2's cases by name, leaves untouched cases verbatim, retires nothing silently, updates counts + provenance.

## Case 8 — restraint on subjective targets
**Input:** "write evals for my art-direction skill"
**Assert:** trigger evals delivered; assertion suite skipped with a stated reason; `<no-suite>`.

## Case 9 — target absent
**Input:** "write the full suite for my scheduling skill" (nothing attached, not in context)
**Assert:** asks for the target; no invented cases; `<no-build>`.

## Case 10 — bare invocation
**Input:** "evalsmith"
**Assert:** one-line intro naming generate/audit/refresh; asks for a target; nothing else.

## Case 11 — one gate, apply-all skips
**Input:** "write evals for <target> — apply all, just hand me the files"
**Assert:** no gate question appears; complete pair delivered in one turn.

## Case 12 — sibling boundary holds
**Input:** "build me a skill and make sure it has good evals"
**Assert:** routes the build to skillsmith by name; offers the suite once the build exists; `<no-build>` on generating standalone.

## Case 13 — pack targets get cross-boundary pairs
**Input:** "write the trigger evals for these two sibling skills in my pack: <A drafts release notes, B posts them>"
**Assert:** each sibling's set includes at least one query that must route to the other and one that must stay; the edge note names the cross-pair; the output states that a fire on a sibling's query is a set defect, not a per-skill pass.
