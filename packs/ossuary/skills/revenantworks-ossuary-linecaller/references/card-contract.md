# Card contract — the exact output format

`longshot/card.py` generates the card; this file exists so the skill layer
never restructures it. The skill may only append sourced context inside the
Drivers bullets (section 5) and fix prose typos.

## Two files, one source of truth

Every run writes **both** `reports/<date>.md` (plain text, the ledger and
skill-parsing source of truth, unchanged format) and `reports/<date>.html`
(same content, rendered — the scoreboard-ticket layout whose design tokens
live in `longshot/style.py`, the single source for card + dashboard;
self-contained/no external requests).
The `.md` is the run lock (idempotency keys off it existing); the `.html`
is generated alongside it whenever the `.md` is written and is what gets
shown to the owner. **Enrichment (Drivers-only edits) must be applied to both
files identically** — same text, same places.

## Header (always)

Date (+ DEGRADED marker and missing-list when applicable) · slate size ·
**today's total risk in dollars and units, against the 6u daily cap** (the
number the owner actually acts on, shown first) · bets recommended ·
bankroll (current, start, peak) · 1u value · P/L to date · ROI · avg CLV
(each of the last three carries an `n=<graded>` caveat below ~30 graded
bets — small-sample P/L reads as noise, not performance) · live record by
bet type · one-line calibration read · odds source. Pause-and-review
banner when drawdown ≥ 20u.

## Game ordering

Games carrying a real bet render **first** (kickoff order preserved within
that group), PASS games after — the card is read to decide what to place,
so the actionable half isn't interleaved with games there's nothing to do
about.

## Per game (numbered 1–5, plus two unnumbered context lines)

Immediately under the game header, when applicable: an italic preseason
week-context line (`Preseason Week N — <the usual starter-usage pattern for
that week>`) and an italic weather line (`Weather at kickoff: 62°F, wind
8mph, clear (open-meteo.com, informational — not a model input)`) — outdoor
venues only, omitted entirely when no forecast is available (never
fabricated). These sit outside the Drivers bullet cap so they can't be
silently truncated.

1. Winner — pick, model win %, market implied %, edge in pp.
2. Track record for this bet type + game phase + confidence bucket — live
   when n ≥ 30, otherwise BACKTEST-labeled (label always visible).
3. Spread — current line and book, model side, cover %, ATS record under the
   same labeling rules.
4. Bet(s) — one bullet per recommended bet, dollar amount first
   (`$X.XX (Nu) on <pick> @ <odds> — tier <T>[, preseason halved]`); the pick
   text is always signed from the picked team's own side (an away underdog
   reads `+N.N`, never the home favorite's `-N.N`). **Or PASS**, rendered as
   a highlighted `PASS — do not bet this game` line with each reason as its
   own bullet underneath (never crammed into one run-on sentence, never
   sharing a slot with a real stake).
5. Drivers — 2–4 bullets: QB/injury status, coach factors incl. preseason
   intent, rest, line movement; data gaps listed as italics.

## Weekly extras

Parlay of the Week only on the first card of the week (Monday): 2–3 legs
from the highest-edge picks, combined odds, true combined probability,
payout on 0.5u, labeled HIGH VARIANCE.

No-game days: a short status card — reconcile results and notable line moves
only. **Never invent a slate.**

## Ledger contract

Every recommended bet lands in `ledger/bets.csv` as `pending` with
`placed=assumed`. The owner corrects `placed`/`placed_stake` when a bet was
skipped or resized (or says so in a coaching note — then the skill edits the
row). PASSes are card-only, never ledger rows.
