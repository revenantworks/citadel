# Trigger Evals — 20 queries (10 should / 10 shouldn't)

Provenance: derived from revenantworks-foundation-lorewright v1.0.0, 2026-07-14. Re-anchored to v1.1.1, 2026-07-24 (foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh). Re-anchored to v1.1.5, 2026-07-25 — provenance only, nothing was executed here: the 2026-07-24 description-regime re-run is already ledgered in `evals/RESULTS.md`, and [1.1.2] through [1.1.5] record no description change since — that work was the anti-patterns dedup and the three `[documented]` gloss repair rounds in the body and `references/verdict-mode.md`. No query, expectation, or count touched; still 20, 10/10. **Re-anchored to v1.0.0 (wright re-baseline), 2026-07-31:** the member was renamed to the wright motif and its version designation reset to 1.0.0; suite content carried forward unchanged, no case, input, assert, or count moved. Earlier version numbers in this line are predecessor-era designations. **Re-anchored to v1.1.0, 2026-08-01 (evalwright refresh):** the release added the Selection/Decision class split and supporting output-contract rules. Routing is unchanged — no entry point, boundary sentence, or description clause moved — so no query, expectation, or count was touched here; still 20, 10/10. The behavior change is covered by Cases 24-39 of the assertion suite. **Re-anchored to v1.1.2, 2026-08-08 — provenance only, nothing executed here:** 1.1.1 was a §4a wording fix whose changelog records this suite's provenance re-read (no entry point or boundary moved), and 1.1.2 was a token slim with the frontmatter `description` explicitly untouched; the anchor line just never moved with them, which the 2026-08-08 build-gate tightening now catches. No query, expectation, or count touched; still 20, 10/10. **Re-anchored to v1.1.3, 2026-08-12 — provenance only:** a Contents block was added to `references/verdict-mode.md` (2026-08-12 estate audit, finding 13 — navigability only, no rule moved); the description is byte-identical, so the routing surface did not move; still 20, 10/10. **Re-anchored to v1.1.4, 2026-08-14 — provenance only, nothing executed here:** this clause's own predecessor was inserted third in this paragraph instead of appended, so the chain terminated at the 2026-08-08 v1.1.2 anchor while the member sat at 1.1.3 — a reader taking the terminal anchor, which is how every other member's block reads, got the wrong version. Position corrected, wording untouched, order now chronological; the sibling `test-cases.md` already carried the same edit terminal and is the shape matched. No query, expectation, or count touched; still 20, 10/10.

| # | Query | Expected |
|---|---|---|
| 1 | which budget 3D printer should I buy under $400 — compare and pick one | SHOULD |
| 2 | is the premium USB4 switch worth it over the cheaper one | SHOULD |
| 3 | lorewright verdict — Unity vs Godot for my project | SHOULD |
| 4 | build me a playbook for setting up a new monitor with this GPU | SHOULD |
| 5 | make a reference doc for our release checklist, answer up front | SHOULD |
| 6 | verify this guide against current docs and update it | SHOULD |
| 7 | I have three overlapping setup docs — consolidate them | SHOULD |
| 8 | go/no-go on switching a scheduled agent to a new data source | SHOULD |
| 9 | compare these two hosting plans with actual evidence, not vibes | SHOULD |
| 10 | which of these skills registries should I list on first | SHOULD |
| 11 | write me a 30-page research report on the AI agent market | SHOULD NOT (report — research tool) |
| 12 | write a system prompt that does comparisons | SHOULD NOT (prompt — promptwright) |
| 13 | build a skill that writes playbooks | SHOULD NOT (skill build — skillwright) |
| 14 | announce the decision to the team on Slack | SHOULD NOT (message — commwright) |
| 15 | document this Python module's API | SHOULD NOT (code docs — engineering tooling) |
| 16 | what's the capital of Peru | SHOULD NOT (trivial lookup — no product) |
| 17 | summarize this PDF | SHOULD NOT (summary, not verdict/playbook) |
| 18 | design the guardrails for my research agent | SHOULD NOT (agent system — agentwright) |
| 19 | just give me all the specs of every GPU this year | SHOULD NOT (data dump — no decision/doc) |
| 20 | brainstorm names for my channel | SHOULD NOT (ideation, not verified knowledge) |

Edge note: sharpest pair is 9 vs 11 — evidence ending in a pick is lorewright; breadth ending in a report is a research tool. Misses on 1–10 → push "compare/pick/worth it/playbook" verbs; fires on 11 → tighten the not-reports boundary sentence.
