# Trigger Evals — 34 queries (20 should / 14 shouldn't)

Provenance: derived from revenant-foundation-agentwright v1.0.0, 2026-07-14; refreshed 2026-07-23 for 1.1.0 — #23 added for Entry — Refresh (platform-notes maintenance). Re-anchored to v1.1.5, 2026-07-25 — provenance only, nothing was executed here: the 2026-07-24 description-regime slim is already ledgered in `evals/RESULTS.md`, and [1.1.2] through [1.1.5] record no description change since (the last three state it outright), so the routing surface these 23 queries are read against did not move. No query, expectation, or count touched; still 23, 12/11. **Re-anchored to v1.2.0, 2026-07-27** — the first count change since 1.1.0: `Entry — Security-scan` is a new entry point and the description was rewritten to advertise it (714 → 796 chars) plus a skillwright boundary sentence, so five rows were added and **nothing here has been executed against the new listing** — #24-#28 are authored, not run (see `evals/RESULTS.md`). 23 → **29, 16/13**. Row 29 is deliberately a SHOULD: the Audit ↔ Security-scan boundary is *intra-skill*, so no listing verdict can test it — it is asserted in `test-cases.md` Case 20 instead, and pretending it is a SHOULD NOT would be a row the suite could never fail honestly. **Re-anchored to v1.2.1, 2026-07-27:** a Load-budget accuracy fix inside the body; the `description` is byte-identical to 1.2.0's at 796 chars, so the routing surface these 29 queries judge did not move — no row was rewritten and the count stays **29, 16/13**. **The cold re-run 1.2.0 owed is now DISCHARGED** (2026-07-27, `evals/RESULTS.md`): all 29 judged by an independent judge holding only the listing and the queries — **28/29, one FAIL at row 19**, and all three security-scan rows fired on their first execution. Row 19's failure is the standing finding reproduced blind and carries a recommendation to convert the row to a SHOULD; not applied, the expectation is owner-owned. **Re-anchored to v1.2.2, 2026-07-27:** that recommendation is now applied — row 19 is converted to **SHOULD** because the query *"design an agent that…"* routes here as an agent-design ask; the harassment restraint is a behavior agentwright applies *after* routing, proven to fire in `test-cases.md` Case 11 (restraint: harassment), and a cold routing listing cannot test it. The count moves **16/13 → 17/12**, total unchanged at **29**, and no other row was touched. Verified by grep against the table: **12** rows read `SHOULD NOT`, **17** read `SHOULD`, sum 29 — declared equals actual. **Re-anchored to v1.3.0, 2026-07-30:** `Entry — Emit` is a new entry point and the `description` was rewritten to advertise it plus the rigwright boundary (796 → 1002 chars), so five rows were added and **none of them has been executed against the new listing** — #30-#34 are authored, not run. Count moves **29, 17/12 → 34, 20/14**. Rows 33-34 are the rigwright seam's near-misses and are the ones most worth judging cold: both use setup-shaped language on objects a human reads in session, which is exactly the shape this description now has to route away. **Re-anchored to v1.0.0 (wright re-baseline), 2026-07-31:** the member was renamed to the wright motif and its version designation reset to 1.0.0; suite content carried forward unchanged, no case, input, assert, or count moved. Earlier version numbers in this line are predecessor-era designations.

| # | Query | Expected |
|---|---|---|
| 1 | design a morning agent that scans my watchlist and emails me signals | SHOULD |
| 2 | agentwright audit — here's my Entry Scan prompt | SHOULD |
| 3 | what guardrails should my auto-reply bot have | SHOULD |
| 4 | add a kill switch to this scheduled task | SHOULD |
| 5 | my agent reads incoming emails — how do I keep injections from doing damage | SHOULD |
| 6 | spec the retry and failure behavior for the nightly sync agent | SHOULD |
| 7 | what should the agent output when it finds nothing | SHOULD |
| 8 | review this automation before I let it touch my accounts | SHOULD |
| 9 | how should agent A hand results to agent B safely | SHOULD |
| 10 | harden this cron bot so it can't overspend | SHOULD |
| 11 | write the system prompt for my trading agent | SHOULD NOT (prompt text — promptwright) |
| 12 | which stocks should the agent buy | SHOULD NOT (domain strategy — owner pack) |
| 13 | pen-test this codebase for injection vulns | SHOULD NOT (code-level — security harness) |
| 14 | build me a skill that audits agents | SHOULD NOT (skill build — skillwright) |
| 15 | draft the announcement that the agent is live | SHOULD NOT (message — commwright) |
| 16 | compare LangGraph vs CrewAI and pick one | SHOULD NOT (verdict — lorewright) |
| 17 | why did my script throw a KeyError | SHOULD NOT (debugging, not agent design) |
| 18 | set up the actual cron job on my server | SHOULD NOT (execution — surface/infra) |
| 19 | design an agent that mass-DMs people who criticize me | SHOULD (it is an agent-design ask and routes here; the harassment restraint is applied *after* routing and is asserted in `test-cases.md` Case 11 — restraint: harassment, not by a cold routing listing) |
| 20 | what's a good schedule for posting videos | SHOULD NOT (content strategy) |
| 21 | does this agent spec have regression coverage? write the missing test cases | SHOULD NOT (suite authoring — evalwright) |
| 22 | harden the ops spec for my inbox agent — caps, retries, kill switch | SHOULD |
| 23 | agentwright refresh | SHOULD (platform-notes baseline maintenance — no spec run) |
| 24 | my inbox agent has delete and send granted but only ever reads — check what it's actually allowed to do | SHOULD (tool-grant scope — Entry — Security-scan) |
| 25 | is my scheduled agent leaking credentials? the API key is pasted into its instructions and its errors dump the whole payload | SHOULD (secrets in prompts/logs — Entry — Security-scan) |
| 26 | agentwright security-scan — here's the agent's tool list and its retry policy | SHOULD (named subcommand) |
| 27 | audit how this skill package is built — is its SKILL.md structured to best practice | SHOULD NOT (the skill artifact, not an agent's runtime permissions — skillwright) |
| 28 | scan my repo for hardcoded secrets and vulnerable dependencies | SHOULD NOT (code-level — security harness; the new security clause claims an agent's grants, not a codebase) |
| 29 | is my agent spec missing any sections — does it cover cadence, output contract, zero-signal | SHOULD, but **Entry — Audit, not Security-scan** — spec completeness is Audit's object; the entry split is asserted in `test-cases.md`, not routable from the listing |
| 30 | make this spec a weekly Cowork task | SHOULD (Entry — Emit) |
| 31 | agentwright emit — render this to a Claude Code routine | SHOULD (named subcommand) |
| 32 | set this up as a ChatGPT scheduled task instead | SHOULD (Entry — Emit, non-Anthropic target) |
| 33 | write the custom instructions for my Claude Project | SHOULD NOT (standing config a human reads in session — rigwright) |
| 34 | my CLAUDE.md is too long, what should come out | SHOULD NOT (attended repo config — rigwright) |

Edge note: sharpest pair is 1 vs 11 — the system around the prompt is agentwright; the prompt itself is promptwright. 21 vs 8 splits suite authoring (evalwright) from spec review (here) — "write the test cases" leaves; "review the automation" stays. Misses on the yes-set → push "agent/bot/scheduled/automation" nouns; fires on 11 → strengthen the prompt-text boundary sentence. #23 is maintenance, not design — it regenerates the stamped platform baseline and produces no spec. Sharpest new pair is 24 vs 27: what an *agent* may do at runtime is agentwright; how a *skill package* is built is skillwright — the object decides, not the word "audit". 28 guards the other side of the same clause — "security" plus a codebase is the harness's, never agentwright's. Fires on 27 or 28 → the description's security clause is over-claiming; tighten it to the agent's grants.

**Emit-seam edge note (new at 1.3.0).** Sharpest new pair is **30 vs 33**. Both are setup-shaped requests naming a Claude surface; the deciding property is who reads the output. A Cowork task fires with nobody watching, so it is agentwright's whole — cadence, guardrails, zero-signal line and all. Claude Project instructions are read by a human in the session, so they are rigwright's. The word "set up" appears in both descriptions and decides nothing. Fires on 33 or 34 → the rigwright boundary sentence is under-claiming and needs the named objects, not the category.
