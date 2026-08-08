# Companion contract — exact shapes for write-backs

## Ledger correction (placed / placed_stake)

`ledger/bets.csv` — fixed columns; only ever touch `placed`, `placed_stake`,
and (when the owner gives a verdict on a graded bet) `postmortem`. Identify the
row by `bet_id` when the owner names it, else by (date, game, bet_type) and
confirm the match back to the owner before writing.

- `placed`: `yes` (as recommended) · `no` (skipped) · `modified` (different
  stake — then `placed_stake` = actual dollars) · `assumed` is the default
  the pipeline writes.
- Postmortem tags (graded bets only): right-thesis · right-lucky ·
  wrong-model · wrong-variance · data-gap.

**No write path available:** emit exactly this block and nothing vaguer:

```
Ledger correction for bets.csv — bet #<id> (<date> <game> <bet_type>):
set placed=<value>[, placed_stake=<dollars>]
Tell Claude Code: "mark bet #<id> placed=<value> [stake $<dollars>]"
```

## Coaching note

Path: `docs/coaching/YYYY-MM-DD-<slug>.md`. Shape:

```
# <one-line title>
Date: YYYY-MM-DD · From: the owner via cardcaller

<the note, verbatim-faithful to what the owner said>

Suggested target: <params key / model layer / "general">, if obvious.
```

Notes are instructions to the model — keep the owner's meaning exact; never
soften or editorialize. If a note asks to change a bankroll guardrail,
record it but say plainly that guardrail changes need the owner's explicit
approval in the repo, not just a note.

## Commit etiquette (when a write path exists)

One commit per correction/note, message `cardcaller: <what>` — to
MickMacPW/longshot main only, never any other repo or remote. Never commit
any credential or key. If a GitHub write tool errors, fall back to the
copy-paste block — never retry-loop.
