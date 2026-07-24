# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Method: each of the 25 queries in `evals/trigger-evals.md` read cold against the current frontmatter descriptions of all eight foundation members; verdict formed before comparing to the expected column. Rows requiring irreducible judgment tagged JUDGE.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | ✅ trigger | ✅ yes | ✅ |
| 2 | ✅ trigger | ✅ yes | ✅ |
| 3 | ✅ trigger | ✅ yes | ✅ |
| 4 | ✅ trigger | ✅ yes | ✅ |
| 5 | ✅ trigger | ✅ yes | ✅ |
| 6 | ✅ trigger | ✅ yes | ✅ |
| 7 | ✅ trigger | ✅ yes | ✅ |
| 8 | ✅ trigger | ✅ yes | ✅ |
| 9 | ✅ trigger | ✅ yes | ✅ |
| 10 | ✅ trigger | ✅ yes | ✅ |
| 11 | ❌ no | ❌ no | ✅ |
| 12 | ❌ no | ❌ no | ✅ |
| 13 | ❌ no | ❌ no | ✅ |
| 14 | ❌ no | ❌ no | ✅ |
| 15 | ❌ no | ❌ no | ✅ |
| 16 | ❌ no | ❌ no | ✅ JUDGE |
| 17 | ❌ no | ❌ no | ✅ |
| 18 | ❌ no | ❌ no | ✅ |
| 19 | ❌ no (commsmith) | ❌ no | ✅ |
| 20 | ❌ no | ❌ no | ✅ |
| 21 | ❌ no (skillsmith) | ❌ no | ✅ |
| 22 | ❌ no (skillsmith) | ❌ no | ✅ |
| 23 | ❌ no (evalsmith) | ❌ no | ✅ JUDGE |
| 24 | ✅ trigger | ✅ yes | ✅ JUDGE |
| 25 | ✅ trigger | ✅ yes | ✅ JUDGE |

**Pass rate: 25/25.** No failures; nearest miss is #25, which passes only on loose semantic matching — the description's model clauses remain prompt-bound ("which model or tier *a prompt* should run on") while #25 is a promptless task pick, so the 1.1.0 Entry — Model feature is not yet reflected in the trigger language (promptsmith still wins the listing because no other member's description mentions model selection; loresmith's "which X should I pick" is generic).
