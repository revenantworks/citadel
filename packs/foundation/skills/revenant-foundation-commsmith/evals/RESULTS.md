# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Judged cold against the current frontmatter descriptions of all eight foundation members (name + description only; verdict formed before comparing to the expected column).

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | PASS |
| 2 | SHOULD | SHOULD | PASS |
| 3 | SHOULD | SHOULD | PASS |
| 4 | SHOULD | SHOULD | PASS |
| 5 | SHOULD | SHOULD | PASS |
| 6 | SHOULD | SHOULD | PASS |
| 7 | SHOULD | SHOULD NOT | **FAIL** (JUDGE) |
| 8 | SHOULD | SHOULD | PASS |
| 9 | SHOULD | SHOULD | PASS |
| 10 | SHOULD | SHOULD | PASS |
| 11 | SHOULD NOT | SHOULD NOT | PASS |
| 12 | SHOULD NOT | SHOULD NOT | PASS |
| 13 | SHOULD NOT | SHOULD NOT | PASS |
| 14 | SHOULD NOT | SHOULD NOT | PASS |
| 15 | SHOULD NOT | SHOULD NOT | PASS |
| 16 | SHOULD NOT | SHOULD NOT | PASS |
| 17 | SHOULD NOT | SHOULD NOT | PASS |
| 18 | SHOULD NOT | SHOULD NOT | PASS |
| 19 | SHOULD NOT | SHOULD NOT | PASS (JUDGE) |
| 20 | SHOULD NOT | SHOULD NOT | PASS |
| 21 | SHOULD | SHOULD | PASS |
| 22 | SHOULD NOT | SHOULD NOT | PASS |
| 23 | SHOULD | SHOULD | PASS (JUDGE) |

**Pass rate: 22/23.** Single failure is the 1.1.0 decoupling boundary in the name-invocation direction: row 7's bare \"commsmith\" mention fires the 'when they say \"commsmith\"' trigger clause in a cold listing read, overriding the \"to define or save a voice, brandsmith\" hand-off — the description needs a carve-out on the name trigger (or the row must accept load-then-redirect); the content-only twin (row 23) holds cleanly.

JUDGE notes: #7 — name-mention trigger vs. explicit voice hand-off, irreducible conflict, judged by strongest-signal rule. #19 — passes on assistant-level restraint (harassment declined before routing), not on any boundary present in the description text. #23 — \"brand... apply\" wording pulls toward brandsmith, but both descriptions cross-reference message-voice application to commsmith and the target is a message.
