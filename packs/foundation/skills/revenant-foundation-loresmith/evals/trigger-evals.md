# Trigger Evals — 20 queries (10 should / 10 shouldn't)

Provenance: derived from revenant-foundation-loresmith v1.0.0, 2026-07-14. Re-anchored to v1.1.1, 2026-07-24 (foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh).

| # | Query | Expected |
|---|---|---|
| 1 | which budget 3D printer should I buy under $400 — compare and pick one | SHOULD |
| 2 | is the premium USB4 switch worth it over the cheaper one | SHOULD |
| 3 | loresmith verdict — Unity vs Godot for my project | SHOULD |
| 4 | build me a playbook for setting up a new monitor with this GPU | SHOULD |
| 5 | make a reference doc for our release checklist, answer up front | SHOULD |
| 6 | verify this guide against current docs and update it | SHOULD |
| 7 | I have three overlapping setup docs — consolidate them | SHOULD |
| 8 | go/no-go on switching a scheduled agent to a new data source | SHOULD |
| 9 | compare these two hosting plans with actual evidence, not vibes | SHOULD |
| 10 | which of these skills registries should I list on first | SHOULD |
| 11 | write me a 30-page research report on the AI agent market | SHOULD NOT (report — research tool) |
| 12 | write a system prompt that does comparisons | SHOULD NOT (prompt — promptsmith) |
| 13 | build a skill that writes playbooks | SHOULD NOT (skill build — skillsmith) |
| 14 | announce the decision to the team on Slack | SHOULD NOT (message — commsmith) |
| 15 | document this Python module's API | SHOULD NOT (code docs — engineering tooling) |
| 16 | what's the capital of Peru | SHOULD NOT (trivial lookup — no product) |
| 17 | summarize this PDF | SHOULD NOT (summary, not verdict/playbook) |
| 18 | design the guardrails for my research agent | SHOULD NOT (agent system — agentsmith) |
| 19 | just give me all the specs of every GPU this year | SHOULD NOT (data dump — no decision/doc) |
| 20 | brainstorm names for my channel | SHOULD NOT (ideation, not verified knowledge) |

Edge note: sharpest pair is 9 vs 11 — evidence ending in a pick is loresmith; breadth ending in a report is a research tool. Misses on 1–10 → push "compare/pick/worth it/playbook" verbs; fires on 11 → tighten the not-reports boundary sentence.
