# Trigger evals — revenantworks-ossuary-linecaller

Target: revenantworks-ossuary-linecaller · v1.6.0 · derived 2026-08-06;
re-anchored to v1.1.0, 2026-08-06 (HTML card output — no trigger-surface
change, description and rows unaffected); re-anchored to v1.2.0,
2026-08-08 (the description gained the owed seam-closing boundary clause —
existing-card reads and ledger/bankroll questions belong to the claude.ai
companion — so the routing surface changed and the full suite was re-judged
cold the same day: **10/10**, recorded in `evals/RESULTS.md`; row 9's old
JUDGE tag retired by that run). **Re-anchored to v1.3.0, 2026-08-08:** the
boundary clause now names the companion's new name
(`revenantworks-ossuary-bonecaller`) — same exclusion, new token — and the
suite was re-judged cold again with the renamed pair; result in
`evals/RESULTS.md`. **Re-anchored to v1.5.0, 2026-08-12:** body-and-frontmatter
changes only (coaching-note scope bounded, step-7 delivery proof, web-search
and per-surface interpreter declarations in `compatibility`); the description
is byte-identical to 1.4.0's, so the routing surface these rows judge did not
move — no row changed. **Re-anchored to v1.5.1, 2026-08-13:** description
shortened 742 → 495 chars to clear an assumed claude.ai upload ceiling; every
trigger token and both exclusions (bonecaller's card-reads, betting-model
work) carried over verbatim in shorter phrasing, so the suite was re-judged
cold against the new text — 10/10, unchanged, recorded in `evals/RESULTS.md`.
**Re-anchored to v1.5.2, 2026-08-14:** `compatibility`-only change (shortened
to clear the confirmed 500-char upload ceiling on that field, the real cause
this time — verified against the live upload error, not assumed); the
description this suite judges is byte-identical to 1.5.1's, so no row
changed. **Re-anchored to v1.5.3, 2026-08-14 (correction):** description
reverted to its full 742-char pre-trim text — two real upload attempts at
the shortened length never errored on `description`, only on
`compatibility` (1.5.2's own entry), so the assumed 500-char description
ceiling was never real. Byte-identical to the 1.2.0/1.3.0 text already
judged 10/10; re-verified cold rather than assumed unchanged — **10/10**,
recorded in `evals/RESULTS.md`. **Re-anchored to v1.5.4, 2026-08-14:**
`references/card-contract.md` re-synced from the longshot production mirror
(citadel had drifted stale); no `name`, `description`, or `compatibility`
field touched, so the routing surface these rows judge did not move — no row
changed.
**Re-anchored to v1.6.0, 2026-08-15 (audit findings
`ossuary-caller-description-overlap` + `ossuary-trigger-suites-half-spec`):**
the description front-loads the run verbs ("run the daily card", "build
today's card") and CEDES the bare noun phrase "today's bets" to bonecaller,
so the routing surface moved: row 2 FLIPS from FIRE to no-fire — that query
is now a card-read routed to the companion. Ten rows added to reach the
eval-authoring spec's 20 (10 fire / 10 no-fire), four of them
linecaller-vs-bonecaller boundary pairs (2↔11, 15↔16, 17↔18, 19↔20).
Rows 11–20 and the flipped row 2 are **authored-not-run** until a cold
judging pass executes the suite; the 1.5.x 10/10 result attaches to the
retired text, not this one.

Read cold against name +
description only. 20 rows: 10 should-fire / 10 shouldn't-fire.

| # | Query | Expect |
|---|---|---|
| 1 | "Run my daily bet card" | FIRE |
| 2 | "What are today's bets looking like?" | no fire — card-read phrasing; "today's bets" belongs to bonecaller as of v1.6.0 |
| 3 | "linecaller" | FIRE |
| 4 | "It's morning — reconcile yesterday and give me the card for today's NFL slate" | FIRE |
| 5 | "Run the longshot daily pipeline and push the report" | FIRE |
| 6 | "Who's going to win the Cardinals game tonight?" | no fire — general sports chat; no card/pipeline/ledger cue |
| 7 | "Tune the QB layer's decay parameters in the longshot model" | no fire — model-building on the repo's code, not a pipeline run |
| 8 | "Log into FanDuel and place $5 on the Panthers for me" | no fire — sportsbook automation; the description excludes placing bets entirely |
| 9 | "What's my current bankroll in longshot?" | no fire — repo file Q&A, no run requested |
| 10 | "Build me a daily bet-card system for the NBA" | no fire — a build job (skillwright/new project), not a run of this pipeline |
| 11 | "Run the daily card" | FIRE |
| 12 | "Build today's card" | FIRE |
| 13 | "The routine didn't fire this morning — run one pass of the pipeline manually" | FIRE |
| 14 | "Fetch today's lines and injuries and produce the bet card" | FIRE |
| 15 | "Reconcile yesterday's results and regenerate the card" | FIRE |
| 16 | "How did yesterday's bets settle?" | no fire — results question over the existing ledger; bonecaller reads, linecaller runs |
| 17 | "Grade the slate and commit the card" | FIRE |
| 18 | "What's the card say about the Bills game?" | no fire — reading an existing card is bonecaller's literal trigger |
| 19 | "Rerun the card with a fresh odds snapshot" | FIRE |
| 20 | "Mark bet #5 as placed in the ledger" | no fire — the placed column is bonecaller's job (fill logging, not a pipeline run) |

**Edge note.** Sharpest boundaries after v1.6.0: 2↔11 — near-identical
today-flavored phrasings split purely on read-vs-run intent, which is the
seam the description redraw exists to hold; and 15↔16 — "reconcile and
regenerate" is a run, "how did they settle" is a read.

**Tuning rule.** Misses on fire rows → strengthen the description's trigger
phrases; fires on no-fire rows → tighten its exclusion clauses (sports chat,
model work, other repos, bet placement).
