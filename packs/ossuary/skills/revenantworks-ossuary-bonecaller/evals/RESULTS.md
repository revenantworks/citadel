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

## Assertion suite standing

`evals/test-cases.md` (B1–B7) was **authored 2026-08-08 and has not been
executed** — the cases assert claude.ai reply and repo-write behavior, so a
cold execution needs a live claude.ai session against the longshot repo
(write path and degraded path both). Recorded as owed, not claimed; this is
the member's first assertion suite, closing the audit finding that it
shipped with trigger evals only.
