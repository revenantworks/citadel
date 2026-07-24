# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | pass |
| 2 | SHOULD | SHOULD | pass |
| 3 | SHOULD | SHOULD | pass |
| 4 | SHOULD | SHOULD | pass |
| 5 | SHOULD (JUDGE) | SHOULD | pass |
| 6 | SHOULD | SHOULD | pass |
| 7 | SHOULD (JUDGE) | SHOULD | pass |
| 8 | SHOULD | SHOULD | pass |
| 9 | SHOULD | SHOULD | pass |
| 10 | SHOULD | SHOULD | pass |
| 11 | SHOULD NOT | SHOULD NOT | pass |
| 12 | SHOULD NOT | SHOULD NOT | pass |
| 13 | SHOULD NOT | SHOULD NOT | pass |
| 14 | SHOULD NOT | SHOULD NOT | pass |
| 15 | SHOULD NOT | SHOULD NOT | pass |
| 16 | SHOULD NOT | SHOULD NOT | pass |
| 17 | SHOULD NOT | SHOULD NOT | pass |
| 18 | SHOULD NOT | SHOULD NOT | pass |
| 19 | SHOULD NOT | SHOULD NOT | pass |
| 20 | SHOULD NOT | SHOULD NOT | pass |

**Pass rate: 20/20.** No failure pattern; the two JUDGE rows (5 — bare "check my suite" with no domain named, 7 — agent-spec audit contested by agentsmith) both resolved correctly only because the description's specific terms "count integrity" and "regression coverage" carried them — those clauses are load-bearing and should not be trimmed.
