# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Method: each of the 23 queries in `evals/trigger-evals.md` judged cold against the current frontmatter descriptions of all eight foundation members (agentsmith 1.1.1, brandsmith 1.1.2, commsmith 1.1.1, evalsmith 1.1.1, loresmith 1.1.1, promptsmith 1.1.1, skillsmith 1.1.2, tokensmith 1.1.1); verdict formed per row before reading the Expected column.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | ✓ |
| 2 | SHOULD — JUDGE (explicit "agentsmith audit" outranks the prompt-shaped payload) | SHOULD | ✓ |
| 3 | SHOULD | SHOULD | ✓ |
| 4 | SHOULD | SHOULD | ✓ |
| 5 | SHOULD | SHOULD | ✓ |
| 6 | SHOULD | SHOULD | ✓ |
| 7 | SHOULD | SHOULD | ✓ |
| 8 | SHOULD | SHOULD | ✓ |
| 9 | SHOULD | SHOULD | ✓ |
| 10 | SHOULD | SHOULD | ✓ |
| 11 | SHOULD NOT (promptsmith — "system prompt for an agent or bot" is its listed trigger; agentsmith's closer cedes prompt text) | SHOULD NOT | ✓ |
| 12 | SHOULD NOT (domain strategy — no design/spec/harden ask despite the "agent" noun) | SHOULD NOT | ✓ |
| 13 | SHOULD NOT (code-level — agentsmith's closer sends it to a security harness) | SHOULD NOT | ✓ |
| 14 | SHOULD NOT (skillsmith — deliverable is a skill) | SHOULD NOT | ✓ |
| 15 | SHOULD NOT (commsmith — drafting an announcement) | SHOULD NOT | ✓ |
| 16 | SHOULD NOT (loresmith — "compare A vs B and recommend one") | SHOULD NOT | ✓ |
| 17 | SHOULD NOT (code debugging — no member fires) | SHOULD NOT | ✓ |
| 18 | SHOULD NOT — JUDGE ("cron job" noun is agentsmith territory, but "set up the actual… on my server" is execution, not design/spec/harden/review/audit) | SHOULD NOT | ✓ |
| 19 | SHOULD NOT — JUDGE (restraint override; see note below) | SHOULD NOT | ✓ |
| 20 | SHOULD NOT (content strategy — "schedule" with no agent/bot/automation noun) | SHOULD NOT | ✓ |
| 21 | SHOULD NOT — JUDGE (evalsmith — "regression coverage… for an agent spec" + "write the test cases" is near-verbatim its trigger; the "does this spec have…" half could pull an audit reading) | SHOULD NOT | ✓ |
| 22 | SHOULD | SHOULD | ✓ |
| 23 | SHOULD (explicit name + listed "refresh" subcommand) | SHOULD | ✓ |

**Pass rate: 23/23.** No failures; one finding worth recording — #19 passes on assistant-level restraint, not on the listing: its yes-verbs ("design an agent" that acts on its own) match agentsmith's description verbatim, so description text alone would route it in, and the row is only as safe as the runner's values.
