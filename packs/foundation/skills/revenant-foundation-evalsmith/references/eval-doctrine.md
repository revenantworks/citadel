# Eval Doctrine — What a Trustworthy Suite Looks Like

Load this file on every run. It governs what evalsmith generates and what its audits score against. The doctrine extends the pack's `eval-authoring.md` baseline (skillsmith); where the two differ, this file governs evalsmith runs.

## The coverage map

Before writing a case, derive the map from the target:

- **Entry points** come from the description — every trigger phrase, subcommand, and invocation keyword is a row.
- **Behavior paths** come from the body — restraint paths, overrides ("apply all", quiet modes), degradation modes (a tool absent), multi-turn flows, and any stated law (a firewall, a zero-dep rule) each get a row.
- The map is the contract: one assertion case minimum per row. Merge only cases asserting the same behavior at different turns.

## Trigger evals

A should/shouldn't table read cold against **name + description only** — the body never routes.

- Balance near 50/50; every set includes **near-misses**: adjacent jobs a lazy description would grab (the boundary sentence's named neighbors first).
- Queries must be substantive — trivially simple asks don't consult skills, so they test nothing.
- Close with an edge note naming the sharpest boundary pair, plus the tuning rule: misses on the yes-set → push triggers; fires on the no-set → tighten boundary language.

## Assertion suites

Assertion-only mechanics — each case is an **Input** plus **Assert**, checkable yes/no by inspecting run output.

- Assertions are literal strings or patterns that must (or must not) appear; numeric comparisons against printed values; named flags for correct absence (`<no-build>`, `<no-draft>`, `<no-suite>`). Multi-turn cases label assertions T1/T2.
- Negative assertions are first-class: "no clarifying question before the deliverable" catches more drift than ten positive checks.
- Size cap: a suite past ~500 lines means the target does too much — flag that, don't trim coverage.
- Generated examples deserve a human pass — models imitate examples precisely, accidental patterns included.

## Count integrity

Stated numbers are assertions about the file itself. The intro count, any Contents grouping, and the actual case count must agree — after every generate, refresh, append, or merge. An intro that says 18 over 22 cases is a real defect (this pack shipped one; the check exists because of it). Audits verify by counting, never by trusting the intro.

## Provenance and refresh

- Every suite opens with one line: target name · target version · derivation date.
- A refresh diffs the target against that line: regenerate touched cases, add rows for new entry points, retire dead rows by name, re-run count integrity, update the provenance line.

## Suite composition for packs

When targets are pack siblings, add **cross-boundary pairs**: for each adjacent-job neighbor, one query that must route to the sibling and one that must stay. The set is read as one product line — a fire on a sibling's query is a set defect even when each skill passes alone.

## Audit scoring

Five checks, 1–10 each, standard anchors (7+ trustworthy · 4–6 tests something, misses paths · 1–3 decorative): coverage vs. the derived map · boundary pairs present · assertion mechanics · count integrity · self-containment (the zero-runtime-dependency law — no step requires evalsmith, a script, or a harness; a human with the file can run it cold). Overall = average, one decimal. P0 = can't run cold, or a coverage hole on a restraint path.

## Ecosystem note

skill-creator's eval tooling (evals.json, subagent runs, grading, benchmarks, blind A/B — per the Claude Code skills docs) is the adopted automation lane. A standard-profile target may request an `evals.json` emit alongside the manual pair; standalone targets stay manual by design — no tooling dependency, ever.
