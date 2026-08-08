# Trigger evals — revenantworks-ossuary-linecaller

Target: revenantworks-ossuary-linecaller · v1.1.0 · derived 2026-08-06;
re-anchored to v1.1.0, 2026-08-06 (HTML card output — no trigger-surface
change, description and rows unaffected). Read cold against name +
description only. 10 rows: 5 should-fire / 5 shouldn't-fire.

| # | Query | Expect |
|---|---|---|
| 1 | "Run my daily bet card" | FIRE |
| 2 | "What are today's bets looking like?" | FIRE |
| 3 | "linecaller" | FIRE |
| 4 | "It's morning — reconcile yesterday and give me the card for today's NFL slate" | FIRE |
| 5 | "Run the longshot daily pipeline and push the report" | FIRE |
| 6 | "Who's going to win the Cardinals game tonight?" | no fire — general sports chat; no card/pipeline/ledger cue |
| 7 | "Tune the QB layer's decay parameters in the longshot model" | no fire — model-building on the repo's code, not a pipeline run |
| 8 | "Log into FanDuel and place $5 on the Panthers for me" | no fire — sportsbook automation; the description excludes placing bets entirely |
| 9 | "What's my current bankroll in longshot?" | no fire — repo file Q&A, no run requested |
| 10 | "Build me a daily bet-card system for the NBA" | no fire — a build job (skillwright/new project), not a run of this pipeline |

**Edge note.** Sharpest boundary: #2 vs #6 — both are today-flavored NFL
questions; #2 carries the description's "today's bets" pipeline cue, #6 is a
prediction question with no card/run/ledger language and must stay out.

**Tuning rule.** Misses on rows 1–5 → strengthen the description's trigger
phrases; fires on rows 6–10 → tighten its exclusion clauses (sports chat,
model work, other repos, bet placement).
