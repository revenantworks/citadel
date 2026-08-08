# Trigger evals — revenantworks-ossuary-bonecaller

Target: revenantworks-ossuary-bonecaller · v1.2.0 · derived 2026-08-06;
re-anchored to v1.1.0, 2026-08-06 (card now shown as a live Artifact — no
trigger-surface change, description and rows unaffected); re-anchored to
v1.1.1, 2026-08-08 (personal-name scrub — the description's referent became
"the owner"; no trigger token moved). **Re-anchored to v1.2.0, 2026-08-08:**
member renamed `revenantworks-ossuary-cardcaller` → `revenantworks-ossuary-bonecaller`,
so the name trigger token in the description moved with it; no other row or
exclusion changed. Execution records (the 1.1.1 cold re-judge and the
post-rename re-judge) live in `evals/RESULTS.md`. Read cold
against name + description. 8 rows: 4 should-fire / 4 shouldn't.

| # | Query | Expect |
|---|---|---|
| 1 | "What's today's card say?" | FIRE |
| 2 | "I put $2 on the Cardinals spread, log it" | FIRE |
| 3 | "How's the bankroll doing this week?" | FIRE |
| 4 | "Coach the model: stop trusting preseason road favorites" | FIRE |
| 5 | "Run the daily pipeline now" | no fire — the cloud routine owns runs; skill points there |
| 6 | "Place $5 on the Panthers on FanDuel" | no fire — never places bets |
| 7 | "Who wins tonight's game?" | no fire — general sports chat |
| 8 | "Tighten the ATS threshold in params.json" | no fire — model change, repo/Claude Code work |

**Edge note.** Sharpest pair: #2 vs #6 — both name a bet and money; #2
records a bet the owner already placed (fires), #6 asks the skill to
place one (never fires).

**Tuning rule.** Misses on 1–4 → strengthen trigger phrases; fires on 5–8 →
tighten the routine/placement/model-work exclusions.
