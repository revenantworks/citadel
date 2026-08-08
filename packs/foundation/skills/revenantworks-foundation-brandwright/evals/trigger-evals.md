# Trigger Evals — 30 queries (17 should / 13 shouldn't)

> **Frozen record — the version numbers below are predecessor-era.** They predate
> the 2026-07-31 re-baseline, so those releases, their tags and the commit SHAs
> cited beside them no longer exist; `foundation-v1.1.0` and `foundation-v1.1.1`
> were later reused by unrelated releases (root `CHANGELOG.md`). Entries are left
> verbatim because they record what was true when written — read them by date,
> not by version.

Read each cold against name + description only. Provenance: derived from revenantworks-foundation-brandwright v1.0.0, 2026-07-14; refreshed 2026-07-23 for 1.1.0 — #12 flipped to SHOULD (Entry — Apply is brandwright's own now). Re-anchored to v1.1.7, 2026-07-25 — provenance only, nothing was executed here: the 2026-07-24 description-regime slim is already ledgered in `evals/RESULTS.md`, and [1.1.3] through [1.1.7] record no description change since — that work was body, reference, and assertion-case repair (the export shapes, the build interview, the seven audit categories, P0's triggers, the Apply cascade row). No query, expectation, or count touched; still 22, 13/9. **Re-anchored to v1.1.0, 2026-08-07:** reference-doctrine additions plus two load-budget bullets; the `description` is byte-identical to 1.0.2's, so no query, expectation, or count moved — still 22, 13/9 — and no re-run is owed. **Extended at v1.2.1, 2026-08-08:** the 1.2.0 roster/peer-selection mechanism is body-level — the `description` is unchanged since 1.0.2 — but multi-brand phrasings had zero routing coverage; #23–#30 added as four should/shouldn't pairs (count 22 → 30, 17/13). A cold re-run of all 30 was executed the same day; results in `evals/RESULTS.md` (row 27 was reworded after that run — its first form said "repos" where the boundary under test is the skill-set handoff; the entry records it, and the reworded row's single re-judge is owed).

| # | Query | Expected |
|---|---|---|
| 1 | "brandwright build — here's my brand guide PDF" | SHOULD |
| 2 | "help me define a brand for my studio" | SHOULD |
| 3 | "brandwright audit this repo for drift" | SHOULD |
| 4 | "check my skill pack for old handles and off-palette colors" | SHOULD |
| 5 | "is this doc on-brand?" | SHOULD |
| 6 | "export a voice profile for commwright" | SHOULD |
| 7 | "consolidate these three style guides into one" | SHOULD |
| 8 | "our repos use three different naming schemes — standardize the convention" | SHOULD |
| 9 | "did the persona voice leak into any work docs?" | SHOULD — firewall audit |
| 10 | "brandwright" | SHOULD — bare invocation |
| 11 | "make this email sound on-brand" | SHOULD NOT — commwright applies voice to messages |
| 12 | "apply the brand to the skill you're building" | SHOULD — Entry — Apply brands a built skill or artifact on invoke |
| 13 | "design me a logo" | SHOULD NOT — asset production |
| 14 | "rebrand this whole skill set for work" | SHOULD NOT — skillwright port |
| 15 | "write our brand story for the About page" | SHOULD NOT — content production |
| 16 | "which brand of monitor should I buy?" | SHOULD NOT — lorewright |
| 17 | "pick brand colors that convert better" | SHOULD NOT — marketing optimization |
| 18 | "audit this agent's guardrails" | SHOULD NOT — agentwright |
| 19 | "trademark search for my company name" | SHOULD NOT — legal research |
| 20 | "make my slides look nicer" | SHOULD NOT — no brand standard invoked |
| 21 | "give me an HTML brand guide card from my definition" | SHOULD — guide-card export |
| 22 | "add typography and logo usage rules to my brand definition" | SHOULD — build/rebuild covers the extended groups |
| 23 | "define a second brand for my personal work, kept separate from the studio's" | SHOULD — build writes a peer plus its roster row |
| 24 | "apply my personal brand to this HTML card, not the product one" | SHOULD — Entry — Apply with named selection |
| 25 | "this repo mixes two of our brands — audit which one it should carry" | SHOULD — scoped audit; selection precedes the sweep |
| 26 | "export the voice profile for my personal brand, not the house one" | SHOULD — peer-selected export |
| 27 | "rebrand my whole personal skill set under the studio brand" | SHOULD NOT — whole-set rebrand is the handoff: skillwright port propagates |
| 28 | "make this email warmer — it's for my personal list" | SHOULD NOT — commwright; message voice, and tone names no brand |
| 29 | "keep my work and personal GitHub accounts from getting mixed up" | SHOULD NOT — account/config ops, not identity definition |
| 30 | "which of my two brands should the new product launch under?" | SHOULD NOT — a decision, lorewright's verdict; naming two brands doesn't make it define/apply/audit |

**Edge note.** Sharpest pairs: 5 vs 11 — "is this on-brand" (judge against the standard) routes here; "make it on-brand" for a *message* is commwright consuming the exported voice. 11 vs 12 marks the decoupling boundary — voice on a message stays with commwright; branding a built skill or artifact is Entry — Apply, here. Tuning rule: misses on 1–10/12/21–22 → push apply/audit/define triggers; fires on 11 or 13–20 → tighten the consumer boundary in the closing sentence. New pairs' sharpest edges: 24 vs 27 replays the 12-vs-14 split with a peer named — one artifact routes here, the whole set is the port handoff; 23 vs 30 both name two brands, and the verb decides — defining the second routes here, choosing between them is lorewright's verdict. Tuning rule, extended: misses on 23–26 → push the peer-selection define/apply/audit/export triggers; fires on 27–30 → tighten the consumer boundary and the decision carve-out.
