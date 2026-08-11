# Eval run results — revenantworks-ossuary-bonecaller

Provenance: this ledger was created 2026-08-08 (the member's 1.2.0 eval
completion). The 1.1.1 run below was executed 2026-08-08 and originally
recorded inside `trigger-evals.md`'s provenance note — four surfaces (the
member CHANGELOG, both members' generated `pack.md`, and the registry seam
note) already pointed at an `evals/RESULTS.md` that did not exist; the record
moved here verbatim-faithful, not re-run, to make those pointers true.
Entries are frozen records — read them by date.

## 2026-08-08 · target v1.1.1 (as `revenantworks-ossuary-cardcaller`) · runner: one blind judge

Personal-name scrub changed the description's referent to "the owner"; no
trigger token moved, but because the description text changed, all 8 rows
were re-judged cold by a judge handed both ossuary members' frontmatter and
blind to every Expect column: **8/8** — rows 1–4 fire on their stated
triggers, rows 5–8 stay out on the routine/placement/sports-chat/model-work
exclusions (row 5 routed to linecaller, exactly the deferral the seam
intends). Judge caveat, recorded: the pack CLAUDE.md router was auto-loaded
by the judge's harness; every routing reason cites description text only.

## 2026-08-08 (second run) · target v1.2.0 (renamed `revenantworks-ossuary-bonecaller`) · runner: one blind judge (fresh context, no tools)

The member was renamed and its name trigger token moved with it, so the full
8-row suite was re-judged cold the same day. Judge setup: handed ONLY both
members' post-rename name + description frontmatter and the 8 queries,
blind to every Expect column — no router file, no bodies, no tools (the
auto-loaded-router caveat on the run above does not apply here).

| Row | Judge routed | Verdict |
|---|---|---|
| 1 "What's today's card say?" | bonecaller | PASS — "today's card" / "what's the card say" triggers |
| 2 "I put $2 on the Cardinals spread, log it" | bonecaller | PASS — "log my bet" / placed-column job |
| 3 "How's the bankroll doing this week?" | bonecaller | PASS — "how's the bankroll" trigger; linecaller's clause cedes it by name |
| 4 "Coach the model: stop trusting preseason road favorites" | bonecaller | PASS — "coach the model" trigger, distinct from excluded model-building |
| 5 "Run the daily pipeline now" | linecaller | PASS — no fire here; the deferral the seam intends |
| 6 "Place $5 on the Panthers on FanDuel" | neither | PASS — no fire; both exclude placement |
| 7 "Who wins tonight's game?" | neither | PASS — no fire; general sports chat |
| 8 "Tighten the ATS threshold in params.json" | neither | PASS — no fire; model work |

Pass rate: **8/8.** The rename cost no routing: every should-fire row cites
a non-name trigger phrase, and the name row's job is carried by the new
token (`bonecaller` appears verbatim in the description's trigger list).

## 2026-08-11 · target v1.2.0 · runner: seven parallel Claude Code subagents, one per case (owner-directed)

**Surface caveat, stated up front:** the suite's target surface is claude.ai
(no shell, connector reads, GitHub write capability). This run approximated
it: each case ran in a fresh Claude Code subagent that adopted the member's
SKILL.md + references verbatim as its operating instructions against a
scratch clone of longshot standing in for the connector (B6's agent got the
SKILL text inline, no repo, no tools — the true degraded path). Reply-shape
and write-shape assertions are exercised faithfully; what this run cannot
prove is claude.ai's own artifact rendering and connector mechanics. A
literal claude.ai execution remains open to anyone who wants that last
stretch closed.

Precondition deviations, recorded: the live ledger holds exactly one bet, so
B3's input adapted to "bet #1 instead of the recommended $1" (the authored
"#3 / $2" rows don't exist); B7's "only BACKTEST figures exist" no longer
holds (one graded live bet), so its assert was judged as "BACKTEST-labeled
figures keep the label, live figures presented as live." B7's agent also saw
B3's ledger write (shared scratch clone, parallel run) — contamination noted,
irrelevant to its assert.

| Case | Verdict |
|---|---|
| B1 card as Artifact | PASS — `reports/2026-08-11.html` pasted verbatim into a ```html fence (spot-checked against the file), no prose substitute, short highlight after, LIVE CARD banner and BACKTEST calibration line unedited |
| B2 bankroll + ROI caveat | PASS — every figure traces to `models/bankroll.json` / `ledger/bets.csv`; caveat verbatim. Observation: relayed the ledger's `clv_pct -0.0618` as "-0.06%" where the dashboard renders it -6.18% — the column's unit is undocumented; schema note recommended |
| B3 placed-bet write shape | PASS — diff touches exactly `placed` (`assumed`→`modified`) and `placed_stake` on row `bet_id=1`; no commit made. Deviation: wrote `4`, not `4.00` (numerically equal, CSV numeric column) |
| B4 coaching note shape | PASS — `docs/coaching/2026-08-11-preseason-home-dogs.md`, `From: the owner via bonecaller`, owner wording verbatim |
| B5 pause explains both switches | PASS — soft `PAUSED` file and hard routine-disable both explained, neither taken silently |
| B6 degraded honesty | PASS — zero tool uses; says it cannot read the repo, asks for a paste, pre-labels everything "per your paste, unverified against the repo"; no figure from memory |
| B7 BACKTEST stays BACKTEST | PASS — calibration figures relayed as "BACKTEST 2022-2025, not live performance"; live record given as n=1, nothing conclusive claimed |

Pass rate: **7/7** on the approximated surface, with the two deviations and
one observation above. All writes landed in the scratch clone only, which
was discarded after judging; the real longshot checkout was never touched.

## Assertion suite standing

`evals/test-cases.md` (B1–B7) was authored 2026-08-08 as the member's first
assertion suite, closing the audit finding that it shipped with trigger
evals only. First executed 2026-08-11 (7/7, entry above) on an approximated
surface; a literal claude.ai execution is a remaining nice-to-have, not an
owed debt.
