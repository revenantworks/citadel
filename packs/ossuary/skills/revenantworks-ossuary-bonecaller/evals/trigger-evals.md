# Trigger evals — revenantworks-ossuary-bonecaller

Target: revenantworks-ossuary-bonecaller · v1.4.0 · derived 2026-08-06;
re-anchored to v1.1.0, 2026-08-06 (card now shown as a live Artifact — no
trigger-surface change, description and rows unaffected); re-anchored to
v1.1.1, 2026-08-08 (personal-name scrub — the description's referent became
"the owner"; no trigger token moved). **Re-anchored to v1.2.0, 2026-08-08:**
member renamed `revenantworks-ossuary-cardcaller` → `revenantworks-ossuary-bonecaller`,
so the name trigger token in the description moved with it; no other row or
exclusion changed. Execution records (the 1.1.1 cold re-judge and the
post-rename re-judge) live in `evals/RESULTS.md`. **Re-anchored to v1.3.0,
2026-08-12:** body-and-frontmatter changes only (ROI threshold re-homed to a
pointer, connector tools fully qualified in `compatibility`, hard rule 3
extended to the render path); the description is byte-identical to 1.2.0's,
so the routing surface these rows judge did not move — no row changed. **Re-anchored
to v1.3.1, 2026-08-13:** description shortened 791 → 496 chars to clear an
assumed claude.ai upload ceiling; every trigger token and both exclusions
carried over verbatim in shorter phrasing, so the suite was re-judged cold
against the new text — 8/8, unchanged, recorded in `evals/RESULTS.md`.
**Re-anchored to v1.3.2, 2026-08-14:** `compatibility`-only change (shortened
to clear the confirmed 500-char upload ceiling on that field, the real cause
this time — verified against the live upload error, not assumed); the
description this suite judges is byte-identical to 1.3.1's, so no row
changed. **Re-anchored to v1.3.3, 2026-08-14 (correction):** description
reverted to its full 791-char pre-trim text — two real upload attempts at
the shortened length never errored on `description`, only on
`compatibility` (1.3.2's own entry), so the assumed 500-char description
ceiling was never real. Byte-identical to the 1.2.0/1.3.0 text already
judged 8/8; re-verified cold rather than assumed unchanged — **8/8**,
recorded in `evals/RESULTS.md`. **Re-anchored to v1.3.4,
2026-08-14:** the description now names the Pause/resume job and its trigger
phrase (2026-08-14 estate audit) — the body has implemented that job since
1.0.0 and `test-cases.md` has asserted it at B5, but no routing text
advertised it, and on this member's declared surface the description is the
only routing text there is (the pack router ships as a Claude Code
`CLAUDE.md`, which claude.ai does not load). Description 791 → 890 chars;
row 9 added for the pause query and **authored, not run** — the routing
surface moved, so a cold re-judge of all 9 is **owed, not claimed**. 8 rows,
4/4 → **9 rows, 5/4**. **Extended to v1.4.0, 2026-08-15 (audit finding
`ossuary-trigger-suites-half-spec`):** eleven rows added to reach the
eval-authoring spec's 20 (10 fire / 10 no-fire), four of them
linecaller-vs-bonecaller boundary pairs (10↔linecaller-11, 12↔13, 14↔15,
19↔20); v1.4.0 also gains "today's bets" as this member's token, ceded by
linecaller's 1.6.0 description redraw. Rows 10–20 are **authored, not
run** — a cold re-judge of the full 20 is owed. Read cold
against name + description. 20 rows: 10 should-fire / 10 shouldn't.

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
| 9 | "Pause the betting" | FIRE — explains both switches, takes neither |
| 10 | "What are today's bets looking like?" | FIRE — card-read phrasing; this token is bonecaller's as of the 1.6.0/1.4.0 seam redraw |
| 11 | "Show me the Monday dashboard numbers" | FIRE |
| 12 | "How did yesterday's bets settle?" | FIRE |
| 13 | "Reconcile yesterday's results and regenerate the card" | no fire — a pipeline run; linecaller/the routine own regeneration |
| 14 | "Mark bet #5 as placed in the ledger" | FIRE |
| 15 | "Grade the slate and commit the card" | no fire — grading + committing is the pipeline, not fill logging |
| 16 | "I skipped the JAX bet today" | FIRE |
| 17 | "Explain why the card passed on the Eagles game" | FIRE |
| 18 | "Build me a bet-card system for the NBA" | no fire — a build job, neither caller's work |
| 19 | "What's my CLV been this month?" | FIRE |
| 20 | "Fetch fresh odds and rebuild today's card" | no fire — fetch/rebuild is a run; this member never runs the pipeline |

**Edge note.** Sharpest pairs: #2 vs #6 — both name a bet and money; #2
records a bet the owner already placed (fires), #6 asks the skill to
place one (never fires). After the seam redraw: #10 vs #13/#20 — same
today's-card subject, split purely on read-vs-run intent.

**Tuning rule.** Misses on 1–4 → strengthen trigger phrases; fires on 5–8 →
tighten the routine/placement/model-work exclusions.
