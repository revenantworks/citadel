# RESULTS — trigger suite runs

## 2026-07-24 — v1.1.2 — runner: claude (listing-based routing simulation, single pass)

Each query judged cold against the current frontmatter descriptions of all eight foundation members; verdict formed before reading the expected column.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | yes | yes | ✅ |
| 2 | yes | yes | ✅ |
| 3 | yes | yes | ✅ |
| 4 | yes | yes | ✅ |
| 5 | yes | yes | ✅ |
| 6 | yes | yes | ✅ JUDGE — loresmith's "is Y worth it" overlaps, but skillsmith names the skill-niche question verbatim |
| 7 | yes | yes | ✅ |
| 8 | no | no | ✅ — brand application now absent from skillsmith's description; brandsmith's "apply" clause takes it |
| 9 | yes | yes | ✅ |
| 10 | yes | yes | ✅ |
| 11 | no | no | ✅ |
| 12 | no | no | ✅ |
| 13 | no | no | ✅ JUDGE — "skills" keyword pulls, but no trigger verb (explain isn't create/build/audit/package) |
| 14 | no | no | ✅ JUDGE — "install-ready" vocabulary sits in the description, but install isn't a listed trigger verb |
| 15 | no | no | ✅ |
| 16 | no | no | ✅ |
| 17 | no | no | ✅ |
| 18 | no | no | ✅ |
| 19 | no | no | ✅ |
| 20 | no | no | ✅ |
| 21 | yes | yes | ✅ |
| 22 | yes | yes | ✅ JUDGE — "strip the branding" could pull brandsmith, but its verbs are define/apply/audit; sanitizing a skill set is skillsmith port |
| 23 | yes | yes | ✅ |
| 24 | no | no | ✅ |
| 25 | no | no | ✅ — evalsmith's trigger matches near-verbatim; skillsmith's "ships trigger evals" is build-scoped |
| 26 | yes | yes | ✅ |
| 27 | yes | yes | ✅ |
| 28 | yes | yes | ✅ |
| 29 | no | no | ✅ |
| 30 | no | no | ✅ JUDGE — the phrase appears in the description but is context-gated ("after a pack build"); cold, it's ordinary conversation |
| 31 | yes | yes | ✅ |
| 32 | yes | yes | ✅ |
| 33 | no | no | ✅ JUDGE — heavy "skills"/"pack" keyword overlap, but a roster lookup matches no trigger verb |
| 34 | no | no | ✅ JUDGE — "build me a pack" pulls, but the object is prompts; the promptsmith deferral clause flips it |

**Pass rate: 34/34.** No failures — every JUDGE row resolved on trigger-verb match over keyword pull, and the 1.1.0 brand decoupling holds at #8, which now routes cleanly to brandsmith on the current descriptions.
