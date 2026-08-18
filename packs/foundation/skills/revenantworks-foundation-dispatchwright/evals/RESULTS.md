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
