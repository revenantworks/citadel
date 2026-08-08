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
bets recommended · bankroll (current, start, peak) · 1u value · P/L to date ·
ROI · avg CLV · live record by bet type · one-line calibration read · odds
source. Pause-and-review banner when drawdown ≥ 20u.

## Per game (numbered 1–5)

1. Winner — pick, model win %, market implied %, edge in pp.
2. Track record for this bet type + game phase + confidence bucket — live
   when n ≥ 30, otherwise BACKTEST-labeled (label always visible).
3. Spread — current line and book, model side, cover %, ATS record under the
   same labeling rules.
4. Stake — units and dollars (preseason halved, tier shown) **or PASS with
   the explicit reason** (edge below threshold, no line, no intel, caps).
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
