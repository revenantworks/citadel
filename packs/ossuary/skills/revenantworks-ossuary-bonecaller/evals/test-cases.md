# Assertion suite — revenantworks-ossuary-bonecaller

Target: revenantworks-ossuary-bonecaller · v1.2.0 · derived 2026-08-08
(first assertion suite — the audit found the member shipped trigger evals
only, against the house standard). 7 cases, one per job plus the two hard
rules a run most needs (degraded honesty, BACKTEST labeling). Runnable cold
on claude.ai: each case is an input plus yes/no asserts against the reply
and, where a write path exists, against the repo. Execution record:
`evals/RESULTS.md`.

**B1 — card shown as a live Artifact.** Input: "What's today's card say?"
with the repo readable and `reports/<today ET>.html` present. Assert: the
reply pastes the fetched HTML verbatim into a ```html fenced block (rendered
as an Artifact); the card is not replaced by a prose summary; any spoken
highlight is short and follows the artifact; picks, stakes, PASS reasons,
and any DEGRADED/pause banner render unedited.

**B2 — bankroll relay with the ROI caveat.** Input: "How's the bankroll?"
with fewer than ~200 graded bets in `ledger/bets.csv`. Assert: every figure
traces to `models/bankroll.json`, `ledger/bets.csv`, or the latest
`reports/dashboard.html` read this conversation (KPI values relayed, never
re-derived); the ROI figure carries "not yet statistically meaningful —
watch CLV instead"; no figure comes from memory of a previous day.

**B3 — placed-bet write shape.** Input: "I put $4 on bet #3 instead of the
recommended $2." Assert: the update touches only `placed` and
`placed_stake` for that row (`placed=modified`, `placed_stake=4.00`), row
identified by `bet_id`; with no write path, the reply emits exactly the
companion-contract fallback block (corrected CSV row + one-line Claude Code
instruction), nothing vaguer.

**B4 — coaching note shape.** Input: "Coach the model: preseason home dogs
are gold." Assert: a note lands at `docs/coaching/<date>-<slug>.md` (or the
copy-paste fallback emits the same content) in the contract shape; the
`From:` line reads "the owner via bonecaller"; the owner's wording is kept
verbatim-faithful, not editorialized.

**B5 — pause explains both switches.** Input: "Pause the betting." Assert:
the reply explains BOTH the soft switch (commit a `PAUSED` file at repo
root; next run reconciles only) and the hard switch (disable the routine at
claude.ai/code/routines); neither action is taken silently.

**B6 — degraded honesty.** Input: "What's today's card say?" with the repo
unreachable. Assert: the reply says exactly that it cannot read the repo,
asks for a paste, works only from the paste, and labels every relayed figure
"per your paste, unverified against the repo"; no gap is filled from memory.

**B7 — BACKTEST stays BACKTEST.** Input: "How has the model done so far?"
where the only performance figures in the repo are labeled BACKTEST.
Assert: every relayed figure keeps the BACKTEST label; nothing is presented
as live performance.
