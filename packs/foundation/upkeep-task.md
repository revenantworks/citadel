# Foundation Upkeep — Cowork Scheduled Task

The pack's four **calendar** surfaces age on a 60-day cadence. Cowork's native
schedules are hourly / daily / weekly / weekdays — no arbitrary-day cadence —
so the task runs **weekly** as a cheap stamp check and only acts when a surface
is actually due (the zero-signal rule: a fresh pack costs one quiet line).

**Setup:** Cowork → Scheduled tasks → New → schedule **Weekly, Monday** →
paste the prompt below. With all four stamps at 2026-07-23 and a 60-day
cadence, the first *actionable* run lands **Monday 2026-09-21** — exactly on
the due date; every Monday before that exits on the zero-signal line.

**Kill switch:** pause or delete the task in Cowork. Nothing runs between
fires; nothing is ever committed by the task.

---

## Task prompt (paste into Cowork)

```
You are the upkeep runner for the revenantworks/citadel foundation pack.

Each run, do exactly this:

1. READ the four calendar stamps from the canonical repo (raw.githubusercontent.com,
   revenantworks/citadel, branch main, path packs/foundation/skills/<member>/references/<file>):
   - revenant-foundation-skillsmith  / rubrics.md          — "Last verified: YYYY-MM-DD"
   - revenant-foundation-promptsmith / model-snapshot.md   — "Last verified: YYYY-MM-DD"
   - revenant-foundation-tokensmith  / measurement.md      — "Last verified: YYYY-MM-DD"
   - revenant-foundation-agentsmith  / platform-notes.md   — "Last verified: YYYY-MM-DD"
   Cadence for all four: 60 days.

2. COMPUTE each surface's age against today.
   - All four < 53 days old → reply with ONE line — "Foundation upkeep: all
     fresh · oldest <member> at <N>d · next due <date>" — and STOP. No tables,
     no summaries, no suggestions.
   - Any 53–59 days → the one-liner plus a "due within a week: <list>" note. STOP.
   - Any ≥ 60 days → step 3.

3. FOR EACH overdue surface, run its owner's refresh (fresh web research
   against the sources listed inside that file; regenerate ONLY that file with
   a new Last-verified stamp; note real drift found vs. confirmed-unchanged):
   - rubrics.md → skillsmith refresh · model-snapshot.md → promptsmith refresh
   - measurement.md → tokensmith refresh · platform-notes.md → agentsmith refresh
   Deliver: the upkeep table (member · surface · age · status), each
   regenerated file, a one-line drift summary per surface, and a paste-ready
   commit line, e.g.:
     git add -A && git commit -m "chore(foundation): upkeep — <surfaces> re-verified + restamped <date>" && git push
   Remind me that installed claude.ai copies need re-upload after the push
   (RUNBOOK: the one swap surface is brandsmith's brand-definition.md; all
   other members upload plain).

HARD RULES: never commit, push, or write to the repo yourself — files and
commands only. If web search is unavailable, report the due list with each
surface marked provisional/unverified and stop — never restamp without
re-verifying. If a stamp can't be read, say which and mark it unknown, never
assume fresh.
```

---

*Maintained as part of the pack (Forge Run 3, Phase 7C — cadence set to 60
days by owner decision, replacing the earlier 61-day draft). If a fifth
calendar surface ever joins `metadata.volatile`, add its row to step 1 and its
verb to step 3 — or re-derive the whole prompt from `upkeep-doctrine.md`.*
