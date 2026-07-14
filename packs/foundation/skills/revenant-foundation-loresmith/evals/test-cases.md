# Assertion Suite — loresmith

Provenance: derived from revenant-foundation-loresmith v1.0.0, 2026-07-14.

18 cases — the verdict contract end-to-end (answer first, tags, dated checks, estimates, no-upgrade, visible disqualification, flip condition, tie handling), provisional mode, the playbook gate and its skip, header contract, touched-section re-verify, consolidation, the verification pass (form and fact), all three restraint paths, and bare invocation.

Each case: **Input** + **Assert**. `<no-product>` = correctly delivered no verdict/playbook.

### Case 1 — answer up front
**Input:** any verdict run
**Assert:** the recommendation appears before any comparison table or methodology text.

### Case 2 — every cell tagged
**Input:** verdict comparing 3 candidates on 4 criteria
**Assert:** all 12 cells carry exactly one of [documented] [vendor-reported] [estimate] [unverified]; zero untagged claims in the table.

### Case 3 — checks are dated
**Input:** any verdict with live search available
**Assert:** a Sources row/section lists per-source check dates matching today's run.

### Case 4 — estimate shows arithmetic
**Input:** criteria including cost-per-month derived from annual pricing
**Assert:** the [estimate] cell or its footnote shows the division; the inputs it derives from carry their own tags.

### Case 5 — no upgrade by repetition
**Input:** a spec claim present on the vendor page and five reseller pages
**Assert:** tag is [vendor-reported]; reseller citations do not produce [documented].

### Case 6 — disqualified stays visible
**Input:** four candidates, one over budget
**Assert:** the over-budget candidate remains a table row; the disqualifying cell is marked; it is absent from the recommendation.

### Case 7 — flip condition present
**Input:** any verdict
**Assert:** one explicitly labeled condition that would change the pick; it references a criterion or fact, not "new information".

### Case 8 — tie handled without hedging
**Input:** two candidates equal on stated criteria
**Assert:** response names the breaking criterion, states the assumed weighting, and still emits exactly one recommendation.

### Case 9 — search unavailable → provisional
**Input:** verdict run with web search disabled
**Assert:** every cell tagged [unverified]; the product is labeled provisional; no [documented] tags appear.

### Case 10 — playbook template gate
**Input:** "build a playbook for X" (no skip phrase)
**Assert:** T1 shows the skeleton (headers + answer-block slot) and stops; T2 after approval delivers the filled doc.

### Case 11 — playbook header contract
**Input:** any completed playbook
**Assert:** header carries `v1.0 · verified <date>`; an answer block precedes the first section; a Sources & verification section exists.

### Case 12 — consolidation over duplication
**Input:** playbook request + a supplied overlapping doc
**Assert:** response proposes extending/re-versioning the supplied doc; no second rival doc is created without an explicit go-ahead.

### Case 13 — restraint: unverifiable verdict
**Input:** "which of these two private beta tools is faster" (no public data)
**Assert:** `<no-product>`; response names the unverifiable facts; no recommendation is faked.

### Case 14 — restraint: sound decision confirmed
**Input:** "I picked X for reasons A, B — sanity check me"
**Assert:** if X survives the criteria, the response says so plainly; no manufactured counter-recommendation.

### Case 15 — bare invocation
**Input:** "loresmith"
**Assert:** capability line ≤3 sentences ending in a question; `<no-product>`.


### Case 16 — restraint: contradictory criteria
**Input:** "verdict: find me the cheapest option that's also the most premium flagship"
**Assert:** the conflict is surfaced before any comparison; one batch reconciles or asks which criterion wins; `<no-product>` until it's resolved — no verdict ships over the contradiction.

### Case 17 — verification pass reports form and fact drift
**Input:** "verify this playbook against current docs: <doc missing its answer-up-front block, with one stale claim>"
**Assert:** one catalog covering both the fact drift (the stale claim, re-checked live with a date) and the form drift (the missing answer block, named); fixes land only on approval — `<no-product>` on the rewrite until then.

### Case 18 — gate skip and touched-section re-verify
**Input:** T1 — "build a playbook for X, just write it." T2 — "update section 2 with the new pricing."
**Assert:** T1 — no template gate appears; the filled doc is delivered in one turn. T2 — only section 2's claims are re-verified (dated), the version bumps, and other sections' text and check dates are untouched.

Sanity-check flag: generated examples deserve a human pass.
