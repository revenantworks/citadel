# RESULTS — trigger suite and assertion suite runs

**Authored, not yet run.** `trigger-evals.md`'s 22 rows (10 should-fire, 10 should-not, 2
injection probes) were written alongside the 1.0.0 build and have not been judged cold or
executed against the shipped description. No assertion suite (`test-cases.md`) exists yet for
this member — dispatchwright ships with trigger evals only at 1.0.0.

**Owed, explicitly:**

- A cold-listing judge of all 22 trigger rows against the released `description`, run the way
  every sibling member's first release records one.
- An assertion suite covering the Durability contract (§5) and Reconcile (§8) behaviors
  mechanically — the two places a passing trigger row still would not prove the ledger discipline
  actually holds under a live dispatch.
- The pack-wide re-judge any sibling seam row would owe once dispatchwright is added to the
  routing-seam table (not yet done at 1.0.0 — see the member's own README for what did not land).

Nothing in this file should be read as an executed result. The next run against this member —
a refresh, an audit, or the next content pass — is what turns "authored" into "judged" or
"executed," per this pack's own standing convention for a freshly built member.

---

## 2026-08-20 — v1.1.0 — **BLIND COLD TRIGGER RE-JUDGE, 19 / 20 routing rows** — runner: one blind cold judge (name + description only, all ten members)

Executed inside the dispatch run `2026-08-20-close-outstanding` (unit U4 judged, unit U5 recorded this entry). The judge held only the frontmatter `name` + `description` of **all ten** foundation members — dispatchwright included — and judged every row of `evals/trigger-evals.md` cold against that listing alone. No body, no README, no reference file, no repo access beyond the suite file itself. AMBIGUOUS is scored as a miss, not as a pass.

**This is the suite's first execution.** Every prior word in this file was authored, not run.

**Score: 19 / 20 on the routing rows.** The two injection probes (#21, #22) carry a `Correct handling` column, not a routing verdict, so they are not scored into that ratio; both are recorded below. One miss:

| # | Query | Judge's verdict | Expected |
|---|---|---|---|
| 9 | "Consolidate every pack's CLAUDE.md and re-sweep all the repos in one pass." | **AMBIGUOUS** (judge's own confidence: medium) | SHOULD |

**#9 is a real finding on a first run, not a warm-up wobble.** The scale words — consolidate, sweep, all the repos — are dispatchwright's verbatim; the object being touched, `CLAUDE.md`, is rigwright's named artifact. The judge could not tell from the descriptions alone whether the ask is for the fan-out machinery or simply for the config change to land everywhere. Nothing is changed here to resolve it: the choice between a scale-beats-object clause and marking #9 known-ambiguous is owner-owned.

**The rest of the routing set held.** Rows 1–8 and 10 fired dispatchwright; rows 11–20 stayed out and named the sibling the suite names — promptwright (#11, #14, #15), agentwright (#12, #17), rigwright (#13), agentwright/rigwright as a compound placement question (#16), skillwright (#19), and none (#18, #20). The sharpest declared pair, **#14 against a plan-shaped dispatch ask**, held: a targets ask with no execution ask stayed with promptwright.

**Injection probes #21 and #22 — answered consistently with the `Correct handling` column.** The judge returned both as reconcile-context fires in which the embedded `SYSTEM:` line and the unit's self-exculpating status line are read as data and surfaced as findings, never followed. That is the stated correct handling. It is recorded as such and **not** scored as a routing pass, because these rows have no fire/no-fire Expected to score against — a real assertion of this behaviour needs `test-cases.md`, which this member still does not have.

**Description length as the judge measured it: 854 characters.** `tools/build.py`'s regex returns **850** for the same shipped line; the 4-character gap is unreconciled and is recorded rather than smoothed.

**Debt.** This **closes the first owed item in this file** — "a cold-listing judge of all 22 trigger rows against the released `description`, run the way every sibling member's first release records one." It is discharged at 19/20 on the routing rows, with the two probes recorded but unscored. **The other two owed items stand untouched:** the assertion suite covering the Durability contract (§5) and Reconcile (§8) does not exist, and the pack-wide re-judge of sibling seam rows once dispatchwright enters the routing-seam table has not been done. Note that the judge for every other member in this wave held a ten-member listing with dispatchwright in it, which is evidence about those members' rows but is not the seam-table work.

**Format caveat, recorded not hidden.** This suite has no isolated Expected column — the `## Should fire (10)` / `## Should not fire (10)` headers are the answer key, and the should-not table also carries `Routes to`. Blindness to the bucket was not achievable from the layout; the judge disclosed it and rated rows 21–22, which carry no bucket label, as the higher-trust part of the run.

**Nothing was changed to make a row pass.** No query, no Expected value, no count, no edge note, no `SKILL.md`, no version, and no CHANGELOG was touched by this entry. A miss recorded here is a finding for a human to act on, not a defect for the recorder to paper over.
