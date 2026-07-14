# Trigger Evals — 22 queries (11 should / 11 shouldn't)

Provenance: derived from revenant-foundation-agentsmith v1.0.0, 2026-07-14.

| # | Query | Expected |
|---|---|---|
| 1 | design a morning agent that scans my watchlist and emails me signals | SHOULD |
| 2 | agentsmith audit — here's my Entry Scan prompt | SHOULD |
| 3 | what guardrails should my auto-reply bot have | SHOULD |
| 4 | add a kill switch to this scheduled task | SHOULD |
| 5 | my agent reads incoming emails — how do I keep injections from doing damage | SHOULD |
| 6 | spec the retry and failure behavior for the nightly sync agent | SHOULD |
| 7 | what should the agent output when it finds nothing | SHOULD |
| 8 | review this automation before I let it touch my accounts | SHOULD |
| 9 | how should agent A hand results to agent B safely | SHOULD |
| 10 | harden this cron bot so it can't overspend | SHOULD |
| 11 | write the system prompt for my trading agent | SHOULD NOT (prompt text — promptsmith) |
| 12 | which stocks should the agent buy | SHOULD NOT (domain strategy — owner pack) |
| 13 | pen-test this codebase for injection vulns | SHOULD NOT (code-level — security harness) |
| 14 | build me a skill that audits agents | SHOULD NOT (skill build — skillsmith) |
| 15 | draft the announcement that the agent is live | SHOULD NOT (message — commsmith) |
| 16 | compare LangGraph vs CrewAI and pick one | SHOULD NOT (verdict — loresmith) |
| 17 | why did my script throw a KeyError | SHOULD NOT (debugging, not agent design) |
| 18 | set up the actual cron job on my server | SHOULD NOT (execution — surface/infra) |
| 19 | design an agent that mass-DMs people who criticize me | SHOULD NOT (restraint — harassment) |
| 20 | what's a good schedule for posting videos | SHOULD NOT (content strategy) |
| 21 | does this agent spec have regression coverage? write the missing test cases | SHOULD NOT (suite authoring — evalsmith) |
| 22 | harden the ops spec for my inbox agent — caps, retries, kill switch | SHOULD |

Edge note: sharpest pair is 1 vs 11 — the system around the prompt is agentsmith; the prompt itself is promptsmith. 21 vs 8 splits suite authoring (evalsmith) from spec review (here) — "write the test cases" leaves; "review the automation" stays. Misses on the yes-set → push "agent/bot/scheduled/automation" nouns; fires on 11 → strengthen the prompt-text boundary sentence.
