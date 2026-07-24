# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Judged against the current frontmatter descriptions of all eight foundation members, each query read cold (name + description only), verdict formed before consulting the Expected column. Rows requiring irreducible judgment are tagged JUDGE.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD — "which X should I buy, compare and pick one" is loresmith's verbatim verdict trigger | SHOULD | pass |
| 2 | SHOULD — "is Y worth it" is a verbatim loresmith trigger phrase | SHOULD | pass |
| 3 | SHOULD — explicit "loresmith verdict" invocation | SHOULD | pass |
| 4 | SHOULD — "playbook" is loresmith playbook mode by name | SHOULD | pass |
| 5 | SHOULD — "reference doc… answer up front" matches playbook mode verbatim | SHOULD | pass |
| 6 | SHOULD — "existing doc needs a verification pass" is a listed trigger | SHOULD | pass |
| 7 | SHOULD — "overlapping docs need consolidating" is a listed trigger | SHOULD | pass |
| 8 | SHOULD (JUDGE) — "go/no-go" is loresmith's verbatim decision verb; agentsmith's "scheduled agent" + untrusted-data-source language pulls hard, but the ask is a decision, not a design/audit of the agent system | SHOULD | pass |
| 9 | SHOULD — compare-with-evidence ending in a pick is verdict mode | SHOULD | pass |
| 10 | SHOULD (JUDGE) — "which… should I list on first" is a which-should-I-pick recommendation; skillsmith's "skill"/"registry" vocabulary is a lexical distractor only (its registry is pack-internal propagation, not a listing choice) | SHOULD | pass |
| 11 | SHOULD NOT — 30-page breadth report; loresmith's closing boundary sentence explicitly cedes reports to a research tool | SHOULD NOT (report — research tool) | pass |
| 12 | SHOULD NOT — "write a system prompt" is promptsmith verbatim; loresmith disclaims prompts | SHOULD NOT (prompt — promptsmith) | pass |
| 13 | SHOULD NOT — deliverable is a skill; skillsmith owns builds, loresmith disclaims skills ("playbooks" is subject matter only) | SHOULD NOT (skill build — skillsmith) | pass |
| 14 | SHOULD NOT — Slack message shaping is commsmith; loresmith disclaims channel messages | SHOULD NOT (message — commsmith) | pass |
| 15 | SHOULD NOT (JUDGE) — "API docs" reads adjacent to "reference doc", but loresmith frames everything as research with live-source verification; documenting local code is direct engineering work, no member fires | SHOULD NOT (code docs — engineering tooling) | pass |
| 16 | SHOULD NOT — trivial lookup, no knowledge product requested | SHOULD NOT (trivial lookup — no product) | pass |
| 17 | SHOULD NOT — summarization appears in no member's trigger set; neither verdict nor playbook | SHOULD NOT (summary, not verdict/playbook) | pass |
| 18 | SHOULD NOT — "guardrails… agent" is agentsmith verbatim; "research" is subject matter only | SHOULD NOT (agent system — agentsmith) | pass |
| 19 | SHOULD NOT (JUDGE) — a raw spec dump asks for neither a pick nor a maintained doc; resolved by "produces decisions and reference docs, not reports", but "specs of every GPU" sits close to comparison territory | SHOULD NOT (data dump — no decision/doc) | pass |
| 20 | SHOULD NOT — open ideation with no verification component; nearest member is brandsmith (naming), not loresmith | SHOULD NOT (ideation, not verified knowledge) | pass |

**Pass rate: 20/20.** No failures. Closest calls: row 8, where agentsmith's "scheduled agent" and untrusted-content language competes with loresmith's verbatim "go/no-go" and only the decision-shaped verb settles it; and row 10, where skillsmith's lexical overlap ("skill", "registry") could distract a weaker router from the which-should-I-pick shape — both held, but they are the rows to watch on any future description edit to loresmith, agentsmith, or skillsmith.
