# Eval results — revenantworks-foundation-rigwright

Provenance: results recorded against revenantworks-foundation-rigwright v1.0.0
(wright re-baseline), 2026-07-31. Re-confirmed 2026-08-01: the 1.0.1 bump is
a prose pass (secrets rule cross-referenced to its one home, connector
cleanup) with no rule, gate, count, or entry point moved, so the baseline
below still describes the code under test.


---

## Cold trigger re-run — 2026-07-31, the wright re-baseline listing (20/20)

The rename re-baseline changed every member name and this member's version
designation, so the executed baselines above were carried forward, not valid.
Re-run cold the day of the re-baseline: an independent blind judge held only
the **nine-member wright listing** (names + descriptions as shipped at 1.0.0)
and the numbered query list — no bodies, no Expected column, no repo access —
and named, per query, the single member that fires or none.

**20/20. Zero failures, zero ambiguous.** This is the suite's
**first cold execution** — every prior judgement was authored at build time.
All ten SHOULD rows fired on rigwright's own claims; all ten SHOULD NOT rows
routed to the intended sibling (skillwright ×3, agentwright ×3, promptwright,
tokenwright, brandwright, commwright — one each), so all three birth seams
(agentwright, skillwright, promptwright) held blind, as did the tokenwright
cost-cue split (#18) and the brandwright apply split (#19). Recorded as the
wright-listing baseline.

---

## 2026-08-20 — v1.1.1 — **BLIND COLD TRIGGER RE-JUDGE, 20 / 20** — runner: one blind cold judge (name + description only, all ten members)

Executed inside the dispatch run `2026-08-20-close-outstanding` (unit U4 judged, unit U5 recorded this entry). The judge held only the frontmatter `name` + `description` of **all ten** foundation members — dispatchwright included — and judged every row of `evals/trigger-evals.md` cold against that listing alone. No body, no README, no reference file, no repo access beyond the suite file itself. AMBIGUOUS is scored as a miss, not as a pass.

**Score: 20 / 20. No miss** — every row's cold verdict matched its Expected value, and every should-not row named the sibling the suite names: skillwright (#11, #12), agentwright (#13, #14, #15, #16), promptwright (#17), tokenwright (#18), brandwright (#19), commwright (#20).

The two sharpest rows held but not comfortably, and the judge said so: **#14** ("set up a routine that reviews PRs on merge") and **#15** ("Edit the SKILL.md for my desktop scheduled task") were both returned at medium confidence. #15 is confidently not rigwright either way; which sibling owns it reads closer to a coin flip from the descriptions alone than the other should-not rows do.

**Description length as the judge measured it: 962 characters** — the same figure `tools/build.py`'s regex returns for the shipped line.

**Debt.** This **closes the cold re-judge of all 20 rows owed since v1.0.2**, carried unchanged through the 1.1.0 tokenwright-clause rewrite and the 1.1.1 provenance re-anchor. The tokenwright clause the debt was opened against is the text #18 was judged on, and #18 routed to tokenwright.

**Format caveat, recorded not hidden.** This suite has no literal Expected column — the split is carried by the `## Should fire` / `## Should not fire` headers, and the should-not table also carries a `Routes to` column. There is no way to read a query without seeing which section it sits in, so blindness to the yes/no split was not achievable from this file's layout. The judge disclosed it and re-derived each verdict against the ten descriptions rather than the header. If a future run wants a genuinely blind pass here, the file has to hand out queries without their section.

**Nothing was changed to make a row pass.** No query, no Expected value, no count, no edge note, no `SKILL.md`, no version, and no CHANGELOG was touched by this entry. A miss recorded here is a finding for a human to act on, not a defect for the recorder to paper over.
