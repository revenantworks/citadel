# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.2 — runner: claude (listing-based routing simulation, single pass)

Judged cold against the current frontmatter descriptions of all eight foundation members; verdict formed per row before reading the Expected column. Note: suite expectations were derived against 1.1.0-era descriptions; members are now at 1.1.1–1.1.2.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | PASS |
| 2 | SHOULD | SHOULD | PASS |
| 3 | SHOULD | SHOULD | PASS |
| 4 | SHOULD | SHOULD | PASS |
| 5 | SHOULD | SHOULD | PASS |
| 6 | SHOULD | SHOULD | PASS |
| 7 | SHOULD | SHOULD | PASS |
| 8 | SHOULD | SHOULD | PASS — JUDGE (no brand keyword; naming-across-repos ownership carries it) |
| 9 | SHOULD | SHOULD | PASS — JUDGE (multi-doc voice-leak audit vs commsmith's per-message drift check) |
| 10 | SHOULD | SHOULD | PASS |
| 11 | SHOULD NOT | SHOULD NOT | PASS — JUDGE (\"on-brand\" pulls, but the object is a message; both closers route it to commsmith) |
| 12 | SHOULD | SHOULD | PASS — JUDGE (Entry — Apply; skillsmith's closer defers apply to brandsmith) |
| 13 | SHOULD NOT | SHOULD NOT | PASS |
| 14 | SHOULD | SHOULD NOT | FAIL — JUDGE (brand verb on a skill set now reads as brandsmith apply; see below) |
| 15 | SHOULD NOT | SHOULD NOT | PASS |
| 16 | SHOULD NOT | SHOULD NOT | PASS |
| 17 | SHOULD NOT | SHOULD NOT | PASS — JUDGE (\"convert better\" marks it an evidence-driven pick, loresmith, not identity definition) |
| 18 | SHOULD NOT | SHOULD NOT | PASS |
| 19 | SHOULD NOT | SHOULD NOT | PASS |
| 20 | SHOULD NOT | SHOULD NOT | PASS |
| 21 | SHOULD | SHOULD | PASS |
| 22 | SHOULD | SHOULD | PASS |

**Pass rate: 21/22.** Single failure is a boundary-erosion pattern, not a trigger miss: #14 fires because skillsmith v1.1.2 dropped \"rebranding\" from its port trigger while brandsmith gained Apply plus the \"skillsmith builds neutral for brandsmith to brand on invoke\" closer — per the suite's own tuning rule, tighten brandsmith's consumer boundary (name skillsmith port for skill-set re-issue) or restore \"rebranding\" to skillsmith's port trigger.
