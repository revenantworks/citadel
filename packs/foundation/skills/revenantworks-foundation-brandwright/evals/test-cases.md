# Test Cases — revenantworks-foundation-brandwright

> **Frozen record — the version numbers below are predecessor-era.** They predate
> the 2026-07-31 re-baseline, so those releases, their tags and the commit SHAs
> cited beside them no longer exist; `foundation-v1.1.0` and `foundation-v1.1.1`
> were later reused by unrelated releases (root `CHANGELOG.md`). Entries are left
> verbatim because they record what was true when written — read them by date,
> not by version.

16 cases covering every entry point and behavior path — build by ingest and by interview, Entry — Apply on a built skill, audit with and without a stored definition (including an already-consistent target), all four exports (including the HTML guide card), the neutral-core and firewall laws, restraint, bare invocation, gating, and the commwright consumer boundary. Provenance: derived from revenantworks-foundation-brandwright v1.0.0, 2026-07-14; Cases 9, 10, and 12 rewritten 2026-07-23 for 1.1.0 (Apply absorbed; export shape renamed). Re-anchored to v1.1.4, 2026-07-24 — Cases 8 and 9 rewritten against the single export contract now stated in Entry — Export, after the first suite execution failed both on a body↔reference contradiction; Case 15 gained the section-order clause at v1.1.5 the same day, once the guide card's section order was confirmed to live only in `audit-doctrine.md`. Case 2 re-anchored to v1.1.6, 2026-07-25 — its "all seven element groups" named a set that existed nowhere (RESULTS suite defect 4a) and now asserts the 14 groups Entry — Build lists, the member's single interview enumeration since the reference's competing 12-group order was deleted. Case 12's T2 register clause re-anchored to v1.1.7, 2026-07-25 — it named README/CHANGELOG prose as the landing surface, a claim `application-doctrine.md` made and the pack's routing seams do not grant; it now asserts what the definition's register map governs, with the message exclusion made explicit. Case 12's per-element-exclusion clause reconfirmed at v1.1.7, 2026-07-25 — its T2 input carried no exclusion, so the "honored without ceremony" clause could never fire (RESULTS defect 4b); the input now names a wordmark exclusion and the assert checks it is withheld, closing the unfirable-clause gap (prior re-anchors: v1.1.2, foundation-v1.1.1 hygiene pass; suite content reviewed at the 2026-07-23 6A refresh). Reconfirmed 2026-07-25 with the fixture definition shipped — Cases 3, 4, 5, 8, 9, 11, 13, 14 and 15 re-anchored off "a definition stored" onto `evals/fixtures/brand-definition.md` (RESULTS defect 4c), and Cases 5 and 15 gained the clauses that check doctrine findings 2 and 3.

Each case: **Input** + **Assert** (mechanical checks on run output). `<no-definition>` = correctly refused to invent identity.

**The fixture.** Nine cases need a definition in play. All nine run against **`evals/fixtures/brand-definition.md`** — a deliberately synthetic, fictional brand ("Quillhaven Instruments", with the "Marrowlight" persona for the firewall cases), invented for this suite and labelled as such at the top of the file. It is **handed in for the run**, the path Entry — Apply, Entry — Audit and Entry — Export all take; `references/brand-definition.md` stays neutral and untouched, because Build is its only writer and no eval run may invent an identity. Anything a case needs — history notes for the stale-string hunt, a firewall map that forbids the persona sign-off on work docs, five naming templates, eleven palette roles, the six voice fields, the three structural fields — is in the fixture, so every executor measures the same thing. Cases 1, 2, 6, 7, 10, 12 and 16 take no fixture by design: they test ingest, interview, the neutral state, or routing.

### Case 1 — build ingests before asking
**Input:** "brandwright build" + an attached guide covering identity, palette, and voice.
**Assert:** interview batch asks only for elements the guide lacks (naming templates, firewall map); no question duplicates ingested content; definition delivered once, gated once, with a Last-built stamp and version.

### Case 2 — build by interview alone
**Input:** "brandwright build — nothing written down yet."
**Assert:** exactly one interview batch carrying all 14 element groups Entry — Build lists, in that order; conflicting answers surfaced as questions (T2), never silently resolved.

### Case 3 — audit a repo against a stored definition
**Input:** "brandwright audit <file tree>" with the fixture definition (`evals/fixtures/brand-definition.md`, v2.0.0) handed in for the run.
**Assert:** seven-category scoreline; catalog rows cite file + location with exact fixes; no file rewritten (`<no-rewrite>`); n/a categories marked, not scored.

### Case 4 — stale-string hunt uses history
**Input:** audit a tree containing strings the fixture's History notes retired — `@quillhvn`, "Quill & Haven Co.", "Made after midnight", and a `qh-` prefixed path — with the fixture handed in.
**Assert:** stale-identity category flags each one, naming the old string verbatim, citing the History note that retired it, and giving that note's replacement (`@quillhaven`, "Quillhaven Instruments", "Instruments for the long watch", `quillhaven-`) as the fix.

### Case 5 — firewall breach is P0
**Input:** audit a work doc carrying the fixture's persona sign-off ("— from the low light"), with the fixture handed in — its firewall map forbids that sign-off on any work surface. The doc is otherwise clean, so the other categories score high.
**Assert:** firewall category ≤3; a P0 row names the breach and states Quillhaven Lab is the identity that stays; and the P0 floor fires as Entry — Audit states it — overall capped at ≤3.0 with an explicit `VERDICT: off-brand` line naming the breach, and the diluted arithmetic mean shown beside it rather than standing as the verdict.

### Case 6 — neutral-core law with no definition
**Input:** "brandwright audit this repo" with `brand-definition.md` empty.
**Assert:** offers hygiene mode or Build; runs no brand judgments; `<no-definition>` — nothing invented.

### Case 7 — hygiene mode audits consistency only
**Input:** accept the hygiene offer from Case 6.
**Assert:** findings limited to internal inconsistency (mixed naming schemes, clashing palettes); no "off-brand" language anywhere.

### Case 8 — export voice profile
**Input:** "brandwright export — voice profile for commwright," with the fixture handed in for the run.
**Assert:** one block with exactly six fields (name → allowed surfaces), lexicon do/don't rendered as one field carrying both lists; values cut from the fixture's voice section without reshaping (name "Long Watch", sign-off "— Quillhaven"); names the definition version it was cut from (2.0.0).

### Case 9 — export structural payload
**Input:** "brandwright export — the structural payload for skillwright," with the fixture handed in for the run.
**Assert:** exactly three fields — brand token (`quillhaven`), naming template (`<brand>-<pack>-<skill>`), license default (MIT); nothing outside the shape (no palette role, wordmark rule, voice line, or identity-map row — styling lands on invoke via Entry — Apply); names the definition version it was cut from.

### Case 10 — bare invocation
**Input:** "brandwright"
**Assert:** one-line intro naming build/apply/audit/export; states whether a definition is stored; nothing else.

### Case 11 — one gate, apply-all skips
**Input:** "brandwright audit <tree> — apply all," with the fixture handed in for the run.
**Assert:** no gate question; scoreline + catalog in one turn.

### Case 12 — message voice routes out; Apply runs here
**Input:** T1 — "make this email on-brand." T2 — "apply the brand to the skill you're building — but leave the wordmark off this one."
**Assert:** T1 routes to commwright with an offer to export the voice profile — brandwright drafts no message; T2 runs Entry — Apply per the application doctrine: name segments confirmed (never silently renamed), palette role tokens land on any HTML, the voice register lands only on the target surfaces the definition's register map governs (never the description field, never a channel-bound message); the named per-element exclusion fires — the wordmark lockup is withheld from the HTML despite it rendering, honored without ceremony (no explanation, no re-ask); unconfigured elements stay neutral.

### Case 13 — restraint: already-consistent target
**Input:** "brandwright audit <tree that conforms to the fixture definition throughout — `quillhaven-` names, `--qh-` palette tokens, Long Watch register, no retired strings, no persona sign-off>", fixture handed in.
**Assert:** category scores land honestly high (≥7); response states the target is on-brand; catalog is empty or Optional-only; no manufactured drift.

### Case 14 — export style one-pager
**Input:** "brandwright export — the style one-pager," with the fixture handed in for the run.
**Assert:** one page, in order: identity map, naming templates each with one rendered example (the fixture's five classes), palette table, voice attributes, tagline surfaces; no doctrine text; names the definition version it was cut from (2.0.0).

### Case 15 — export the brand-guide card
**Input:** "brandwright export — guide card" with the fixture definition handed in for the run.
**Assert:** exactly one self-contained HTML payload (artifact or single code block, never Markdown); the 12 sections `audit-doctrine.md` mandates, in that order, none omitted; no external scripts/fonts/CDNs/storage; header carries the definition-version chip (2.0.0) and the footer echoes it; palette swatches show name + hex, one per fixture role token; styled from the definition's own tokens, with no hex outside them; reduced-motion respected. **Tag registry is populated, not a stub** — it renders the identity map's handles and community terms (`@quillhaven`, `@marrowlight`, "harborhands", `#longwatch`) each with its owning identity and allowed surfaces, per the fill rules' render-source clause; a stub or an omission fails the case.

### Case 16 — guide card with no definition · extended interview coverage
**Input:** T1 — "brandwright export — guide card" with `brand-definition.md` empty. T2 — "brandwright build" with a guide covering only identity + palette.
**Assert:** T1 offers Build or ships the neutral-themed card only, `<no-definition>` — nothing invented; T2's single interview batch asks the ungoverned groups (typography roles, logo usage, motion, functional job-colors, accessibility, application specs) and re-asks nothing the guide covered.
