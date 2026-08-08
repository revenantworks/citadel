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
