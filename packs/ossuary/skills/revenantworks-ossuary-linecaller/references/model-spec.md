# Model spec — what produces the numbers on the card

*Event-driven surface: re-read after any `model_version` bump in
`models/params.json`. Last stamped: 2026-08-06, model v0.1.0.*

## Layers (regular season / playoffs)

538-spec Elo (K=20, spread = EloDiff/25, logistic win prob) + adjustment
layers, every parameter named in `models/params.json`:

| Layer | Params key | Note |
|---|---|---|
| Team Elo | `elo.*` | seeded from 2021+, ⅓ regression to 1505 each season |
| Home field | `elo.hfa_base_elo` − `elo.hfa_div_discount_elo` | none at neutral sites |
| Rest | `elo.bye_rest_bonus_elo` | +25 Elo off a bye (rest ≥ 13 days) |
| QB | `qb.*` | 538 VALUE from nflverse weekly stats; 3.3 Elo/VALUE pt; low-start upside cap |
| Injuries | `injuries.*` | position-weighted Out/Doubtful/Questionable, capped; declared heuristic |
| Market anchor | `market.market_weight` | blended margin = 65% market + 35% model (nfelo evidence) |
| Margin → prob | `margin_sigma` | fit from backtest residuals, never a literature constant |

Preseason is a separate model (`preseason.*`): team Elo ignored, probability
shrunk toward 50%, driven by coach preseason records (our own ESPN archive),
coach intent ratings, and playing-time intel. **No intel → PASS.**

## Bet rules (do not override in prose)

Moneyline recommended at ≥3pp win-prob edge vs the de-vigged market; ATS at
≥2pp cover edge. Tier A (2u) at ≥5pp / ≥4pp. Stakes come from
`longshot/bankroll.py` GUARDRAILS — 1u = 1.2% of roll, down-now/up-Monday,
preseason ×0.5, parlay 0.5u, ≤5 bets/day, ≤6u/day.

## Labeling rules

- Any figure from `models/backtest.json` carries the **BACKTEST** label until
  30+ graded live bets exist for that bet type + phase. Never present
  backtest as live. Known backtest read (2026-08-06): ML rule +3.2% ROI,
  ATS rule −3.2% ROI — the ATS threshold is teaching priority #1.
- ROI is not judged before ~200 graded bets; CLV and calibration are the
  health metrics until then (verified practice — docs/research.md §3).

## Postmortem tags (one per graded bet)

`right-thesis` (won for the modeled reason) · `right-lucky` (won despite the
thesis failing) · `wrong-model` (lost, thesis was wrong) · `wrong-variance`
(lost, thesis held, ball bounced) · `data-gap` (either way, missing data
drove it). Tag from the box score and the card's recorded drivers — when
unsure between wrong-model and wrong-variance, check whether the closing
line moved toward the pick (variance) or away (model).
