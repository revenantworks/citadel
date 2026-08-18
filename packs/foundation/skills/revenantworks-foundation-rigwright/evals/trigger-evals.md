# Trigger Evals — revenantworks-foundation-rigwright

**Provenance:** authored against `revenantworks-foundation-rigwright` v1.0.0, description at 946 characters. Re-anchor this line on any version bump that moves the `description`, and re-judge every row cold — a suite that passes its own rename and fails on the routing underneath it has tested nothing. **Re-anchored to v1.0.0 (wright re-baseline), 2026-07-31:** the member was renamed to the wright motif and its version designation reset to 1.0.0; suite content carried forward unchanged, no case, input, assert, or count moved. Earlier version numbers in this line are predecessor-era designations. **Re-anchored to v1.0.2, 2026-08-05:** the `description` gained "hooks" in the artifact list (952 → 959 chars per `build.py`'s regex; the 946 recorded above is a predecessor-era count). No row, expectation, or count moved. The routing surface changed, so the cold re-judge of every row is **owed, not claimed**; a hook-shaped probe ("write the hook for this rule") now has an advertised landing and is worth adding as a should-row when the re-judge runs. The registry's rigwright ↔ tokenwright seam row (2026-08-05) is carried on tokenwright's side — this description deliberately gained no clause for it. **Re-anchored to v1.1.0, 2026-08-12:** that decision is reversed by finding 9 of the 2026-08-12 estate audit — the boundary now closes from both sides, so the description's closing boundary gains the tokenwright clause (a pure token or cost cut on a config whose layout is already right), with compensating trims holding the length at 962 chars. Body changes in the same release: the handed-in-material injection rule promoted to Turn shape rule 5 (findings 10), and the Refresh entry gained the fetched-page injection rule and search-unavailable fallback (findings 2, 14). The routing surface moved, so the cold re-judge of every row — owed since 1.0.2 — is still owed, now against the tokenwright-clause text; a boundary probe ("slim my CLAUDE.md, the layout is fine") is worth adding as a shouldn't-row when it runs. No row, expectation, or count moved this pass. **Re-anchored to v1.1.1, 2026-08-17:** body and reference changes only (the 2026-08-17 member audit + security scan — `surface-notes.md` refresh, `artifact-templates.md` emit-rule tightening, step-level data-rule pointers, two injection probes in `test-cases.md`); the description is byte-identical to 1.1.0's at 962 chars, so the routing surface these 20 queries judge did not move — no row, expectation, or count touched; still **20, 10/10**, and the cold re-judge owed since 1.0.2 remains owed.

**Method.** Read each query cold against **name + description only** — never the body. Routing is set at the description level; a miss here is a description defect, not a body defect. Judge, then compare to the expected column.

**Counts:** 20 queries — **10 SHOULD** · **10 SHOULD NOT**.

## Should fire

| # | Query | Why |
|---|---|---|
| 1 | "Set up a Claude Project for my client research work" | Named surface, build intent |
| 2 | "Write me a CLAUDE.md for this repo" | Named artifact |
| 3 | "My project instructions are a mess — can you tighten them?" | Fix intent on a named surface |
| 4 | "Should this rule go in my CLAUDE.md or a skill?" | The placement question, verbatim |
| 5 | "What belongs in profile preferences vs project instructions?" | Placement across two named layers |
| 6 | "My CLAUDE.md is 400 lines and Claude ignores half of it" | Bloat symptom on a named artifact |
| 7 | "Score my repo's Claude config" | The audit entry |
| 8 | "rigwright audit" | Quoted invocation keyword |
| 9 | "I need a .mcp.json for this project's servers" | Named artifact in scope |
| 10 | "Plan the knowledge files for a Project about our pricing policy" | Knowledge-file plan, named |

## Should not fire

| # | Query | Routes to | Why it's a near-miss |
|---|---|---|---|
| 11 | "Build me a skill that formats changelogs" | skillwright | Config-shaped verb, skill object |
| 12 | "Audit this SKILL.md against best practices" | skillwright | Shares the `audit` verb |
| 13 | "Make this a weekly Cowork task" | agentwright | Setup-shaped, but unattended |
| 14 | "Set up a routine that reviews PRs on merge" | agentwright | "Set up" is rigwright's verb; the object runs unattended |
| 15 | "Edit the SKILL.md for my desktop scheduled task" | agentwright | **Sharpest pair.** Filename says skill, object is a scheduled task |
| 16 | "What guardrails should my scheduled agent have?" | agentwright | Runtime authority |
| 17 | "Rewrite this system prompt so it stops rambling" | promptwright | Instruction text with no layer question |
| 18 | "Trim the token cost of my CLAUDE.md" | tokenwright | **Sharp pair.** Same artifact, cost motive not placement motive |
| 19 | "Apply our brand palette to the project README" | brandwright | Identity, not configuration |
| 20 | "Draft the announcement telling the team about the new Project" | commwright | Message to a channel |

## Edge notes

**Sharpest boundary pair: #15 against #2.** Both name a `SKILL.md`. The deciding property is the *object*, never the filename: a desktop scheduled task is stored on disk as a `SKILL.md` and is still agentwright's, because a filename describes the format and not the thing. rigwright's description carries this by claiming attended standing configuration and routing "anything that runs unattended" away by name; agentwright's claims scheduled tasks positively. If #15 fires rigwright, the fix is on rigwright's boundary sentence, not on agentwright's.

**Second-sharpest: #18 against #6.** Identical artifact, opposite motive. A cost cue ("trim the token cost", "too expensive") is tokenwright; a placement or effectiveness cue ("Claude ignores half of it", "is this in the right file") is rigwright. A bare "shorten my CLAUDE.md" carries neither cleanly and is a genuine coin-flip — recorded as a known ambiguity rather than papered over, and the honest resolution in a live run is to ask which, once.

**#13 and #14 test the same seam from the setup side.** rigwright owns the verbs *set up*, *configure*, *scaffold*; agentwright owns the objects those verbs are applied to when nobody is watching the result. The verb cannot decide it, which is why both descriptions carry the object test.

**Tuning rule.** Misses on the should-set → the description's triggers need to be pushier, most likely by naming a surface the query used. Fires on the should-not set → tighten the boundary sentence, and check whether the sibling's description makes its own positive claim; a boundary held from one side only is the failure mode this pack has already hit twice.
