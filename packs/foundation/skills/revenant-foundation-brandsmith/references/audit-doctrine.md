# Audit Doctrine — Build Interview, Drift Categories, Export Shapes, Guide Card

Load on Build and Audit runs (Export shapes at the bottom). The definition itself lives in `brand-definition.md`; this file carries the how.

## Build — ingest-first interview

Read attached guides, style sheets, and assets before asking. The one-batch interview covers only the gaps, in this order: identity map → naming templates per artifact class → palette role tokens (identity accents + functional job-colors) → typography roles (faces, hierarchy, fallback stacks) → voice attributes + register map → taglines/sign-offs with allowed surfaces → wordmark rule + logo usage (clearspace, minimums, misuse) → imagery & iconography direction → motion rules → accessibility floor → application quick-specs → firewall map. Two extraction rules: **roles over values** (a hex without a role can't style an artifact type nobody anticipated) and **templates over examples** (one rendered name is an example; `<brand>-<pack>-<skill>` binds a class). Conflicts between ingested sources are questions, never picks. Every rename or retirement writes a History note — the stale-string hunt depends on it.

## Audit — seven drift categories

Sweep every file or surface in the target; the catalog cites file + line/location per finding.

1. **Naming conformance** — rendered names match the class template; segment order, casing, and separators exact.
2. **Palette drift** — colors in code, styles, and artifacts resolve to role tokens; off-token values are findings even when "close."
3. **Voice / register drift** — prose scored against attributes and the register map for its surface; docs vs. chat vs. titles each judged by their own register.
4. **Tagline / sign-off surfaces** — present only where the definition allows; absence where required is drift too.
5. **Stale identity strings** — old handles, org names, repo paths, and retired taglines from History notes; a rename that left the old string anywhere is the classic miss.
6. **Typography & logo-usage drift** — faces off the type roles for the surface (body copy in a display or pixel face, wrong display face for the brand); wordmark misuse — stretched or off-token-recolored marks, clearspace or minimum-size violations, forbidden effects.
7. **Firewall breaches** — identities co-occurring on a surface the map forbids. Always P0; the fix names which identity stays.

Anchors per category: **7+** on-brand · **4–6** drifts — inconsistencies a reader would notice · **1–3** off-brand or leaking. Overall = average, one decimal. A category with no applicable surface in the target is marked n/a, never padded.

## Severity

**P0** — firewall breach, identity leak, or a live credential/personal identifier surfaced by the sweep (flag loudly, never echo the value). **P1** — a violated convention the definition states (wrong name render, off-token palette, voice breach on a governed surface). **P2** — polish (inconsistent casing the definition doesn't govern, stale-but-harmless strings).

## Export shapes

**Voice profile** (the native shape commsmith consumes):

    name · register · cadence · lexicon-do · lexicon-don't · sign-off · allowed surfaces

**Structural payload (skillsmith consumes it):**

    brand/company token · identity map rows · palette role tokens (role/token/value) · voice line · license default · wordmark rule

**Style one-pager:** identity map, naming templates with one rendered example each, palette table, voice attributes, tagline surfaces — one page, human-readable, no doctrine.

**Brand-guide card (HTML):** one self-contained file, fully offline — no external scripts, fonts, CDNs, network calls, or browser storage. Sections in order: header lockup (skill wordmark + guide title + definition-version chip) · essence · architecture (one card per identity with primary tagline) · palette (core, functional, identity accents — swatches with name + hex, tap/click-to-copy) · typography table (rendered in fallback stacks, noting brand faces install separately) · tag registry · naming quick rules · voice cards with sign-offs · wordmark + logo rules · motion/imagery/application/accessibility digest · firewall · footer echoing the lockup, definition version, and date. Styled from the active definition's own tokens; with none stored, the neutral dark theme. Respect reduced-motion.

Every export names the definition version it was cut from, so consumers can spot staleness at a glance.
