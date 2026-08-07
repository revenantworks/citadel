# Eval Doctrine — What a Trustworthy Suite Looks Like

Load this file on every run. It governs what evalwright generates and what its audits score against. The doctrine extends the pack's `eval-authoring.md` baseline (skillwright); where the two differ, this file governs evalwright runs.

## The coverage map

Before writing a case, derive the map from the target:

- **Entry points** come from the description — every trigger phrase, subcommand, and invocation keyword is a row.
- **Behavior paths** come from the body — restraint paths, overrides ("apply all", quiet modes), degradation modes (a tool absent), multi-turn flows, and any stated law (a firewall, a zero-dep rule) each get a row.
- The map is the contract: one assertion case minimum per row. Merge only cases asserting the same behavior at different turns.
- Map completeness is a match, not a floor. "Assertion count ≥ map rows" cannot catch an **under-derived map** — a dropped row still satisfies a floor once any surplus of cases exists over the shrunken count. Verify the map itself by independently re-deriving it from the target and diffing that re-derivation against the one shipped; the two must match row for row. On the generate side this sets the actual requirement: case count **equals** map row count, not merely meets it: a floor is a construction minimum, never the completeness check.

## Trigger evals

A should/shouldn't table read cold against **name + description only** — the body never routes.

- Balance near 50/50; every set includes **near-misses**: adjacent jobs a lazy description would grab (the boundary sentence's named neighbors first).
- Queries must be substantive — trivially simple asks don't consult skills, so they test nothing.
- Close with an edge note naming the sharpest boundary pair, plus the tuning rule: misses on the yes-set → push triggers; fires on the no-set → tighten boundary language.

## Assertion suites

Assertion-only mechanics — each case is an **Input** plus **Assert**, checkable yes/no by inspecting run output.

- Assertions are literal strings or patterns that must (or must not) appear; numeric comparisons against printed values; named flags for the **target's** correct absence (`<no-draft>`, `<no-post>`, `<no-send>` — evalwright's own output flags share the notation and are enumerated in the SKILL body's non-production states). Multi-turn cases label assertions T1/T2.
- Negative assertions are first-class: "no clarifying question before the deliverable" catches more drift than ten positive checks.
- A must-not-appear assert names its **surface** — where the guarantee has to hold, not everywhere the characters occur. Forbid the flag or phrase in evalwright's own emitted turn, or as an emitted output token; a flag or gate phrase quoted inside prose that states its own absence ("no `<no-build>`: the target was read"), or inside a generated suite's own assert text, is a *mention*, not a violation. An absence check a strict grep breaks on such a mention is under-scoped — write the emission, not the substring. (SKILL Restraint draws this line for evalwright's flags; it binds every literal-absence assert the same way.)
- Size cap: a suite past ~500 lines means the target does too much — flag that, don't trim coverage.
- Generated examples deserve a human pass — models imitate examples precisely, accidental patterns included.

## Count integrity

An intro that says 18 over 22 cases is a real defect (this pack shipped one; the check exists because of it). Audits verify by counting, never by trusting the intro. The rule binds **every** number an audit states about its target, not only the intro/Contents/case-count triple — a scoreline or catalog clause such as "`<no-deploy>` appears 8 times" is itself a countable claim about the target and is grepped before it is printed. A number inside a finding's own justification that was never counted is the same defect, at a smaller scale, as an uncounted intro.

## Provenance and refresh

- Every suite opens with one line: target name · target version · derivation date.
- A refresh diffs the target against that line: regenerate touched cases, add rows for new entry points, retire dead rows by name, re-run count integrity, update the provenance line.
- **"Touches" is not limited to the changed entry's own row.** A rename or behavior change also touches any case filed under a *different* entry whose Input or Assert merely **references** the changed name, flag, or vocabulary — not only the case that is that entry. Verbatim is reserved for cases with no reference, direct or incidental, to what changed; a case that survives a rename still quoting the old vocabulary because its row belongs to some other entry is a stale suite the "leave untouched cases verbatim" rule was never meant to protect.

## Suite composition for packs

When targets are pack siblings, add **cross-boundary pairs**: for each adjacent-job neighbor, one query that must route to the sibling and one that must stay. The set is read as one product line — a fire on a sibling's query is a set defect even when each skill passes alone.

## Audit scoring

The five checks, their anchors, and the P0 line live in the SKILL body's Audit entry and bind whether or not this file is open. Overall = average of the checks scored — five, or **four when boundary pairs is N/A** — one decimal. Scoring self-containment means running the suite the way its reader would: a human with the file, no tooling, no evalwright — if any case stalls waiting for something to be installed, that is the finding.

**Boundary pairs N/A rule.** Boundary pairs scores the trigger-eval set; it needs that set as its artifact. Entry — Audit accepts "an existing suite" singular, and an assertion suite alone is a legitimate audit input (Cases 5 and 6 are exactly this). When no trigger-eval half was supplied, boundary pairs is not a check that came back low: it is a check with nothing to score, and scoring it 1 against an artifact the submitter was never asked for drags the overall average down by a full check for a gap that isn't the suite's. Mark it **N/A** on the scoreline with the reason ("no trigger-eval set supplied"), average the remaining four, and let the catalog note that a full score requires the pair if the auditor wants one.

## Provenance discipline

When the target's version bumps, the suite's provenance line updates **in the same commit**: keep the derivation history, append "re-anchored to vX.Y.Z, YYYY-MM-DD". A suite whose head names an older target version with no dated re-anchor is a finding — the exact staleness class this skill audits others for, and the pack's build gate warns on it. Recording a run: a dated `evals/RESULTS.md` section (date · target version · runner · per-row verdicts · pass rate; irreducible-judgment rows tagged `JUDGE`) — a protocol, never an executor.

## Ecosystem note

skill-creator's eval tooling (evals.json, subagent runs, grading, benchmarks, blind A/B — per the Claude Code skills docs) is the adopted automation lane. A standard-profile target may request an `evals.json` emit alongside the manual pair; standalone targets stay manual by design — no tooling dependency, ever.
