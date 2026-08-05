# Trigger Evals — revenant-foundation-tokenwright

> **Frozen record — the version numbers below are predecessor-era.** They predate
> the 2026-07-31 re-baseline, so those releases, their tags and the commit SHAs
> cited beside them no longer exist; `foundation-v1.1.0` and `foundation-v1.1.1`
> were later reused by unrelated releases (root `CHANGELOG.md`). Entries are left
> verbatim because they record what was true when written — read them by date,
> not by version.

> **Provenance:** target `revenant-foundation-tokenwright` v1.0.0 · suite derived 2026-07-13 (evalwright doctrine; runnable cold, no tooling). Twenty queries — ten should fire the description, ten shouldn't. Read each cold against **name + description only** and compare to the expected column. Re-anchored to v1.1.1, 2026-07-24; **re-anchored to v1.1.6, 2026-07-25** — 1.1.2 through 1.1.6 left this head five patches stale, and `build.py` stayed silent because its check accepts any dated re-anchor line by shape without checking the version it names. Those bumps changed the description-cap doctrine and the Refresh sync rule, not the `description` field, so no row here changed and **no re-run is claimed or owed** (foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh). **Extended and re-anchored to v1.1.0, 2026-08-05** (post-re-baseline designation): the `description` gained the rigwright boundary clause (802 → 894 chars), closing the rigwright ↔ tokenwright seam AUDIT-2026-08-05 opened, so the routing surface moved for the first time since the re-baseline. Y11/N11 added as the new seam's boundary pair — a cost cue with behavior held constant fires; a placement/setup cue on the same file routes to rigwright. Twenty → **22, 11/11**. No prior row was rewritten; the cold re-judge of all 22 against the amended listing is **owed, not claimed** — no row here has been executed against the new text.

## Should trigger (11)

| # | Query | Expected |
|---|---|---|
| Y1 | "Slim this system prompt — it's 6k tokens and I need it under 3k." | Fire (Slim, budgeted) |
| Y2 | "Why does my CLAUDE.md cost so many tokens every session?" | Fire (cost question on an instruction file) |
| Y3 | "tokenwright audit my pack's skill descriptions." | Fire (Audit, keyword) |
| Y4 | "This agent spec has to fit an 8k context budget with room left for tool output — make it fit." | Fire (Slim, budget/context fit) |
| Y5 | "Set token budgets for the seven instruction files in this project." | Fire (Budget) |
| Y6 | "My skill's always-on surface is eating context at session start — trim what loads every turn." | Fire (Slim, always-on role) |
| Y7 | "Compress this reference doc without losing any of the rules in it." | Fire (Slim, preservation) |
| Y8 | "tokenwright refresh." | Fire (Refresh, keyword) |
| Y9 | "Estimate what this prompt costs per call and whether caching it would pay off." | Fire (measurement + cache accounting) |
| Y10 | "Get this SKILL.md under 300 lines without changing what it does." | Fire (Slim, behavior-preserving) |
| Y11 | "My CLAUDE.md costs too much per session — slim it, but keep every rule exactly as it is." | Fire (cost cue, behavior held constant; the rigwright seam's near-miss twin is N11) |

## Should NOT trigger (11)

| # | Query | Expected | Routes to |
|---|---|---|---|
| N1 | "Make this prompt more persuasive and improve its examples." | No fire | promptwright (near-miss — quality, not cost) |
| N2 | "Audit my skill against current best practices." | No fire | skillwright (near-miss — conformance, not footprint) |
| N3 | "Shorten this email to a client to three sentences." | No fire | commwright (near-miss — audience-facing length) |
| N4 | "My session keeps compacting mid-task — manage my live context." | No fire | runtime/platform tools (near-miss — session, not artifact) |
| N5 | "Write the assertion suite for my slimmed skill." | No fire | evalwright (near-miss) |
| N6 | "Which model tier should this prompt run on?" | No fire | promptwright |
| N7 | "Build me a skill that makes responses terse." | No fire | skillwright (near-miss — a build ask; terse output is a runtime style) |
| N8 | "What's a token and how does tokenization work?" | No fire | plain explanation |
| N9 | "Summarize this article for me." | No fire | ordinary summarization |
| N10 | "Cut our cloud spend on this AWS bill." | No fire | not an LLM text artifact |
| N11 | "Trim my CLAUDE.md — half these rules probably belong in hooks or a skill anyway." | No fire | rigwright (near-miss — placement/setup cue on the same object Y11 keeps) |

## Edge notes

**Sharpest boundary pair:** N1 vs Y1 — "make this prompt *better*" is promptwright; "make this prompt *cheaper / fit a budget*" is tokenwright. Second sharpest: N2 vs Y3 — "audit my skill" (best practices) is skillwright; "audit my skill's *token footprint*" is tokenwright.

**Tuning rule:** misses on the yes-set → make the description's triggers pushier (add the cost/fit/footprint vocabulary users actually type); fires on the no-set → tighten the boundary sentence naming promptwright, skillwright, commwright, and rigwright. Third sharpest pair: Y11 vs N11 — one object, two motives; the stated motive decides, per the registry's rigwright ↔ tokenwright row.
