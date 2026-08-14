# Eval run results — revenantworks-ossuary-linecaller

Provenance: the run below targets v1.0.0; reconfirmed 2026-08-07 against the
shipped v1.1.0 — that release changed card output only (`.md` and `.html`
written together) and left `name` and `description` untouched, so no trigger
row's surface moved. Two rows are separately owed a re-run for the 2026-08-07
rename; that debt is recorded at the foot of this file, undischarged.

## 2026-08-06 · target v1.0.0 · runner: Claude (build-time cold read)

Trigger rows read cold against name + description only (the description as
actually loaded into the session skill listing):

| Row | Verdict |
|---|---|
| 1 "Run my daily bet card" | PASS — "daily bet card" trigger phrase |
| 2 "today's bets looking like?" | PASS — "today's bets" trigger phrase |
| 3 "edgepicker" | PASS — name trigger |
| 4 "reconcile yesterday... card for today's slate" | PASS — pipeline verbs in description |
| 5 "longshot daily pipeline... push the report" | PASS — repo + pipeline named |
| 6 "Who wins the Cardinals game tonight?" | PASS (no fire) — general-sports-chat exclusion |
| 7 "Tune the QB layer's decay parameters" | PASS (no fire) — model-building exclusion |
| 8 "place $5 on the Panthers" | PASS (no fire) — never-places-bets clause |
| 9 "What's my current bankroll?" | PASS (no fire) `JUDGE` — a question is not a run; description claims runs only |
| 10 "Build me a bet-card system for the NBA" | PASS (no fire) — build-job exclusion |

Pass rate: 10/10 (row 9 is irreducible judgment, tagged JUDGE).

Assertion suite: R1, R4, R7, R11 exercised live by the 2026-08-06
registration-day end-to-end run (see repo reports/run-log.md); R2, R3, R5,
R6, R8, R9, R10 remain manual cases for future runs — suite is
self-contained and requires no tooling.

**Partly superseded 2026-08-07 (pack rename `vault` → `ossuary`, motif
`-picker` → `-caller`).** The run above is kept verbatim as the record it is:
row 3's probe was the literal string `edgepicker`, and that is what was
actually read cold. The skill's name trigger is now `linecaller`, so **row 3
and the R11 case no longer match the shipped token** and are owed a re-run
against the renamed description — not a rewrite of this table. Rows 1, 2, and
4–10 key on trigger phrases and exclusions the rename did not touch and stand
as measured.

## 2026-08-08 · row 3 re-run · target v1.1.0 · runner: Claude (build-time cold read)

Row 3 re-read cold against the shipped description (`Trigger on "daily bet
card", "today's bets", "linecaller", "run linecaller"...`):

| Row | Probe | Verdict |
|---|---|---|
| 3 | "linecaller" | PASS — name trigger, present verbatim in the description's trigger-on clause |

Debt discharged for row 3. **R11 stays open, correctly** — it is a live
idempotency assertion (run the pipeline twice same-day, assert the second
run's card step is skipped and the ledger has no duplicate row), not a
cold-trigger read, so it cannot be closed by re-reading a description. It
needs an actual pipeline execution under the `linecaller` name, which this
session does not run (no Odds API quota spend, no ledger/report writes
outside the real daily routine). Closes naturally on the next live
"Project Longshot - Daily Card" run or a deliberate manual `run linecaller`
— check `reports/run-log.md` afterward for a same-day double-run entry
before marking it measured.

## 2026-08-08 · full-suite cold re-judge · target v1.2.0 · runner: blind judge

The 1.2.0 description change is a routing-surface change — it gained the
seam-closing boundary clause ("not for reading an existing card and
ledger/bankroll questions — the claude.ai companion
revenantworks-ossuary-cardcaller owns those") — so the whole 10-row suite was
re-judged, this time by a judge handed **both** ossuary members' frontmatter
(the real routing situation) and **blind to every Expect column**, deciding
linecaller / cardcaller / neither per query.

| Row | Judge routed | Verdict |
|---|---|---|
| 1 "Run my daily bet card" | linecaller | PASS — fire |
| 2 "today's bets looking like?" | linecaller | PASS — fire |
| 3 "linecaller" | linecaller | PASS — fire (name trigger) |
| 4 "reconcile yesterday… card for today's slate" | linecaller | PASS — fire |
| 5 "longshot daily pipeline… push the report" | linecaller | PASS — fire |
| 6 "Who's going to win the Cardinals game tonight?" | neither | PASS — no fire |
| 7 "Tune the QB layer's decay parameters" | neither | PASS — no fire |
| 8 "Log into FanDuel and place $5" | neither | PASS — no fire |
| 9 "What's my current bankroll in longshot?" | **cardcaller** | PASS — no fire here, and the judge cited the new clause: linecaller's description now disclaims bankroll questions by name |
| 10 "Build me a bet-card system for the NBA" | neither | PASS — no fire |

Pass rate: **10/10.** Row 9's 2026-08-06 `JUDGE` tag is retired — what was
irreducible judgment ("a question is not a run") is now stated text, which is
exactly what the seam closure was for. The same run re-judged cardcaller's 8
rows (8/8; see that member's provenance note). Judge caveat, recorded: the
pack CLAUDE.md router was auto-loaded by the judge's harness; every routing
reason cites frontmatter text only. **R11 remains open** — unchanged; it
still needs a live double-run, not a description read.

## 2026-08-08 (second run) · target v1.3.0 · runner: one blind judge (fresh context, no tools)

The boundary clause moved with the companion's rename
(`revenantworks-ossuary-cardcaller` → `revenantworks-ossuary-bonecaller`,
ossuary 2.0.0), so the full 10-row suite was re-judged cold the same day.
Judge setup: handed ONLY both members' post-rename name + description
frontmatter and the 10 queries, blind to every Expect column — no router
file, no bodies, no tools, so the auto-loaded-router caveat on the run above
does not apply here.

Rows 1–5 fire linecaller on their stated triggers ("daily bet card",
"today's bets", the name row, the reconcile-and-card phrasing, the
repo-plus-pipeline phrasing); rows 6, 7, 8, and 10 stay out on the
sports-chat / model-work / placement / new-build exclusions; row 9 routes to
**bonecaller**, the judge citing the renamed clause — linecaller "explicitly
cedes ledger/bankroll questions to the companion". Pass rate: **10/10.**
**R11 remains open** — unchanged; it still needs a live double-run, not a
description read.

## 2026-08-13 · target v1.5.1 · runner: one blind judge (fresh context, no tools)

Description shortened 742 → 495 chars to clear the claude.ai skill-upload
form's 500-char ceiling (discovered at real upload time — stricter than the
1024-char spec ceiling `rubrics.md` bakes in; flagged there for the next
`skillwright refresh`). Every trigger token and both exclusions (bonecaller's
existing-card/ledger reads, the betting-model-work carve-out) carried over in
shorter phrasing, so the full 10-row suite was re-judged cold. Judge setup:
handed ONLY the post-trim name + description frontmatter (both ossuary
members) and the 10 queries, blind to every Expect column — no router file,
no bodies, no tools.

Rows 1–5 fire on "daily bet card" / "today's bets" / the name row / the
reconcile-and-card phrasing / the repo-plus-pipeline phrasing; rows 6, 7, 8,
and 10 stay out on the sports-chat / model-work / placement / new-build
exclusions; row 9 still routes to bonecaller on the shortened boundary clause.
Pass rate: **10/10**, unchanged. **R11 remains open** — unchanged; it still
needs a live double-run, not a description read.
