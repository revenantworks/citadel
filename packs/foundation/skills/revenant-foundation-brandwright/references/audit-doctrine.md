# Audit Doctrine — Build Extraction Rules, Sweep Notes, Guide Card

Load on Build and Audit runs, and on the guide-card export for its fill rules at the bottom. The definition itself lives in `brand-definition.md`. Three of the four export shapes — voice profile, structural payload, style one-pager — are stated in full in the SKILL body's Entry — Export and bind whether or not this file is open; this file restates none of them. The fourth, the brand-guide card, carries its mandatory section order and fill rules here at the bottom and nowhere else — that is why a card export loads this file. This file carries the how.

## Build — the two extraction rules

The interview groups and the order they are asked in are stated in the SKILL body's Entry — Build and bind whether or not this file is open; this file names none of them, adds none, and reorders none. What is this file's own: two rules that shape how any answer is recorded. **Roles over values** — a hex without a role can't style an artifact type nobody anticipated. **Templates over examples** — one rendered name is an example; `<brand>-<pack>-<skill>` binds a class.

## Audit — per-category sweep notes

The categories, their count, and their order are stated in the SKILL body's Entry — Audit and bind whether or not this file is open. What follows are glosses **keyed to that list, in its order** — one note per category, each opening with the body's own name for it verbatim, adding no category, reordering none, and never an independent sequence to count against. Sweep every file or surface in the target; the catalog cites file + line/location per finding.

- **naming-template conformance** — rendered names match the class template; segment order, casing, and separators exact.
- **palette drift** — colors in code, styles, and artifacts resolve to role tokens; off-token values are findings even when "close."
- **typography & logo-usage drift** — faces off the type roles for the surface (body copy in a display or pixel face, wrong display face for the brand); wordmark misuse — stretched or off-token-recolored marks, clearspace or minimum-size violations, forbidden effects.
- **voice and register drift** — prose scored against attributes and the register map for its surface; docs vs. chat vs. titles each judged by their own register.
- **tagline/sign-off surface violations** — present only where the definition allows; absence where required is drift too.
- **stale identity strings** — old handles, org names, repo paths, and retired taglines from History notes; a rename that left the old string anywhere is the classic miss.
- **firewall breaches** — identities co-occurring on a surface the map forbids; the fix names which identity stays.

Scored on the SKILL body's anchors, one score per category; a mid-band score means an inconsistency a reader would notice. Overall = average of the scored categories, one decimal — **except when a P0 is open**, where Entry — Audit's P0 floor overrides this arithmetic; that override is stated there and binds whether or not this file is open, and this file does not restate it. A category with no applicable surface in the target is marked n/a, never padded — n/a categories are excluded from the average, not scored zero.

## Severity — the two bands below P0

P0's triggers are stated in Entry — Audit and bind whether or not this file is open; this file states neither them nor a fourth. **P1** — a violated convention the definition states (wrong name render, off-token palette, voice breach on a governed surface). **P2** — polish (inconsistent casing the definition doesn't govern, stale-but-harmless strings).

## Brand-guide card — fill rules

The one export that opens this file: Entry — Export states the card's envelope, this section states what goes inside it. One self-contained HTML file, fully offline — no external scripts, fonts, CDNs, network calls, or browser storage. **Exactly 12 sections, in this order:** header lockup (skill wordmark + guide title + definition-version chip) · essence · architecture (one card per identity with primary tagline) · palette (core, functional, identity accents — swatches with name + hex, tap/click-to-copy) · typography table (rendered in fallback stacks, noting brand faces install separately) · tag registry · naming quick rules · voice cards with sign-offs · wordmark + logo rules · motion/imagery/application/accessibility digest · firewall · footer echoing the lockup, definition version, and date. Styled from the active definition's own tokens; with none stored, the neutral dark theme. Respect reduced-motion.

**Every section renders from a definition section — the card collects nothing of its own.** Each of the twelve draws on the definition group of the same name; the two that do not map by name are stated here. **Tag registry** renders from the **identity map** — its handles/orgs and community terms rows, each listed with the identity that owns it and the surfaces it is allowed on, taglines and sign-offs included by their allowed-surface rule. It is a *view* of already-collected fields, not a group of its own: Entry — Build's fourteen groups collect no tags, and adding a fifteenth is not the fix. **Architecture** renders from the identity map's parent brand and sub-brands, one card each, carrying that identity's primary tagline. Where a source field is empty the section renders an explicit "none registered" row and is never omitted, never a stub, and never invented — the section count is fixed at twelve whatever the definition holds.
