# Test Cases — revenant-foundation-brandsmith

16 cases covering every entry point and behavior path — build by ingest and by interview, Entry — Apply on a built skill, audit with and without a stored definition (including an already-consistent target), all four exports (including the HTML guide card), the neutral-core and firewall laws, restraint, bare invocation, gating, and the commsmith consumer boundary. Provenance: derived from revenant-foundation-brandsmith v1.0.0, 2026-07-14; Cases 9, 10, and 12 rewritten 2026-07-23 for 1.1.0 (Apply absorbed; export shape renamed).

Each case: **Input** + **Assert** (mechanical checks on run output). `<no-definition>` = correctly refused to invent identity.

### Case 1 — build ingests before asking
**Input:** "brandsmith build" + an attached guide covering identity, palette, and voice.
**Assert:** interview batch asks only for elements the guide lacks (naming templates, firewall map); no question duplicates ingested content; definition delivered once, gated once, with a Last-built stamp and version.

### Case 2 — build by interview alone
**Input:** "brandsmith build — nothing written down yet."
**Assert:** exactly one interview batch, all seven element groups present; conflicting answers surfaced as questions (T2), never silently resolved.

### Case 3 — audit a repo against a stored definition
**Input:** "brandsmith audit <file tree>" with a definition stored.
**Assert:** seven-category scoreline; catalog rows cite file + location with exact fixes; no file rewritten (`<no-rewrite>`); n/a categories marked, not scored.

### Case 4 — stale-string hunt uses history
**Input:** audit a tree containing a handle the definition's History notes retired.
**Assert:** stale-identity category flags it with the old string named and the current replacement as the fix.

### Case 5 — firewall breach is P0
**Input:** audit a work doc carrying the persona sign-off, with a firewall map forbidding it.
**Assert:** firewall category ≤3; a P0 row names the breach and which identity stays; overall verdict reflects it.

### Case 6 — neutral-core law with no definition
**Input:** "brandsmith audit this repo" with `brand-definition.md` empty.
**Assert:** offers hygiene mode or Build; runs no brand judgments; `<no-definition>` — nothing invented.

### Case 7 — hygiene mode audits consistency only
**Input:** accept the hygiene offer from Case 6.
**Assert:** findings limited to internal inconsistency (mixed naming schemes, clashing palettes); no "off-brand" language anywhere.

### Case 8 — export voice profile
**Input:** "brandsmith export — voice profile for commsmith."
**Assert:** one block with all seven fields (name → allowed surfaces); names the definition version it was cut from.

### Case 9 — export structural payload
**Input:** "brandsmith export — the structural payload for skillsmith."
**Assert:** payload carries token, identity map, palette roles, voice line, license, wordmark; nothing outside the shape.

### Case 10 — bare invocation
**Input:** "brandsmith"
**Assert:** one-line intro naming build/apply/audit/export; states whether a definition is stored; nothing else.

### Case 11 — one gate, apply-all skips
**Input:** "brandsmith audit <tree> — apply all."
**Assert:** no gate question; scoreline + catalog in one turn.

### Case 12 — message voice routes out; Apply runs here
**Input:** T1 — "make this email on-brand." T2 — "apply the brand to the skill you're building."
**Assert:** T1 routes to commsmith with an offer to export the voice profile — brandsmith drafts no message; T2 runs Entry — Apply per the application doctrine: name segments confirmed (never silently renamed), palette role tokens land on any HTML, the voice register lands on README/CHANGELOG prose (never the description field), the wordmark on HTML artifacts; unconfigured elements stay neutral and per-element exclusions are honored without ceremony.

### Case 13 — restraint: already-consistent target
**Input:** "brandsmith audit <tree that conforms to the stored definition throughout>"
**Assert:** category scores land honestly high (≥7); response states the target is on-brand; catalog is empty or Optional-only; no manufactured drift.

### Case 14 — export style one-pager
**Input:** "brandsmith export — the style one-pager"
**Assert:** one page: identity map, naming templates each with one rendered example, palette table, voice attributes, tagline surfaces; no doctrine text; names the definition version it was cut from.
**Assert:** one page; identity map, naming templates with an example each, palette table, voice attributes, tagline surfaces; no doctrine text; names the definition version.

### Case 15 — export the brand-guide card
**Input:** "brandsmith export — guide card" with a definition stored.
**Assert:** exactly one self-contained HTML payload (artifact or single code block, never Markdown); no external scripts/fonts/CDNs/storage; header carries the definition-version chip and the footer echoes it; palette swatches show name + hex; styled from the definition's own tokens; reduced-motion respected.

### Case 16 — guide card with no definition · extended interview coverage
**Input:** T1 — "brandsmith export — guide card" with `brand-definition.md` empty. T2 — "brandsmith build" with a guide covering only identity + palette.
**Assert:** T1 offers Build or ships the neutral-themed card only, `<no-definition>` — nothing invented; T2's single interview batch asks the ungoverned groups (typography roles, logo usage, motion, functional job-colors, accessibility, application specs) and re-asks nothing the guide covered.
