# Changelog — revenantworks-foundation-brandwright

> Renamed from `revenant-foundation-brandwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.2.1] — 2026-08-07

**The neutral definition can now hold what the doctrine expects.** 1.1.0 added
palette-derivation rules (D-1 to D-7) but left the neutral storage shape at four
rows — background / text / accent / functional — so a fresh build had nowhere to put
a surface ladder, a quiet/lit border pair, or per-mode light. The rules were
unlandable on a new brand and the gap read as compliance.

- `references/brand-definition.md` gains storage for the neutral ladder (with the
  derivation hue recorded), accent base/ink pairs with their ratios, per-brand
  per-mode `border-lit`/`glow`, shared accents with their default readings, and the
  CIEDE2000 separation floor. Each block names the rule it exists for.
- Storage shape only — still zero identity content, still spec-clean neutral.

## [1.2.0] — 2026-08-07

**Several definitions, one selected per run.** brandwright could hold exactly one
active definition, which made a personal or social brand impossible to keep beside a
product brand without overwriting it. It now carries a roster: `brand-definition.md`
holds the table of every brand the install knows, and peers live in
`brand-definition-<slug>.md` siblings that open only when selected.

- **Selection is a named workflow step**, resolved before any other work: named in
  the request, else scoped by the target, else **asked** in one line. Topic and tone
  never decide it — a personal-voice request aimed at a product surface is the case
  that must be asked about rather than inferred.
- **Cross-brand law**: never apply one definition to a surface another owns, never
  blend two in one output; they share a surface only where the owning definition
  declares an attribution mark for the peer.
- **Build writes peers.** A build for a brand the roster does not hold creates its
  sibling file and adds the roster row in the same pass.
- Scope and coexistence are asked inside the existing firewall-map group rather than
  as a fifteenth — the count of 14 is load-bearing and references may not renumber it.
- `application-doctrine.md` gains a *Peers* section for the application-side rules.

## [1.1.0] — 2026-08-07

Palette doctrine, additive. Until now the palette guidance was a role-token
rule and a drift sweep note: a definition could name a background, a text
colour and an accent and be judged complete, while the surface stack, the
borders, the derived light and the separation between accents were governed by
nothing. Nine live definition revisions in one day each fixed a defect that
doctrine should have caught before it shipped, so the fixes are recorded as
rules rather than as values.

- `audit-doctrine.md` gains **Build — palette derivation**, seven rules stated
  as numbers to measure: neutrals computed in OKLCH at the brand's own accent
  hue rather than hand-picked (D-1) · a ~1.13:1 visibility floor per elevation
  step (D-2) · the border token split into quiet and lit, the lit one clearing
  3:1 on its own surface (D-3) · lit and glow derived from the accent's *own*
  lightness with a floor as the `max`'s second term, and the general rule that a
  rule tuned on one hue is re-tested on every hue before it becomes doctrine
  (D-4) · colour never carrying state alone, per WCAG 1.4.1 (D-5) · a shared
  accent set proved by a ΔE00 coverage matrix, optimised jointly rather than
  member-by-member, with semantic overrides recorded (D-6) · CIEDE2000 as the
  separation metric with a regional floor where the wheel is crowded (D-7).
- The **palette drift** sweep note now puts the neutrals in scope and requires
  the ratios be recomputed and reported, and the palette scored against the
  definition's own accessibility floor as well as its role tokens. The audit
  that missed the 76°-off stack scored the accents and measured nothing else.
- `application-doctrine.md` gains **Palette inheritance — structure, light, and
  marks**: structure may be shared system-wide while light belongs to one
  identity and one mode; a multi-mode brand needs a complete set per mode with a
  stated switch condition and modes never mix on one surface; and a parent
  accent may cross onto a child's surface as *attribution* but never as that
  surface's light — the no-crossing rule is scoped light-versus-mark rather than
  as a ban on the colour. The cascade's palette row points here.

No entry point, count, gate, or ordered list moved, and the `description` is
byte-identical, so no trigger re-run is owed; the eval provenance lines are
re-anchored with that stated. Zero identity content added — the neutral-core law
holds, and every rule is stated as a derivation or a threshold, never a value.

## [1.0.2] — 2026-08-01

A prose/register pass. The per-element-exclusion example ("no palette on
this one"), previously restated near-verbatim in SKILL.md, README.md, and
`application-doctrine.md`, is now single-homed in `application-doctrine.md`'s
Overrides section, with SKILL.md and README.md pointing there instead of
repeating it. A hard-to-parse clause in `audit-doctrine.md` was reworded for
clarity, and a triple-stacked em dash in `brand-definition.md` was recast.
No rule, gate, count, or entry point moved, so no eval re-anchor is owed.

## [1.0.1] — 2026-08-01

Frozen-record marker added to the `evals/` files that cite predecessor-era
version numbers. Those designations predate the 2026-07-31 re-baseline, and
two of the tag names were later reused by unrelated releases, so a reader
could take a historical entry for a current one. The rows, verdicts, dates
and counts are untouched — only a header marker was added, so nothing about
what was executed or when has moved.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Build: an ingest-first interview across all 14 definition groups in fixed
  order — identity map, naming templates, role-token palette, six-field
  voice profile with register map, taglines and sign-offs, wordmark rule,
  typography roles, logo usage, imagery, motion, functional job-color
  tokens, accessibility floor, application quick-specs, and the firewall map
  of identities that never co-occur — written to the single volatile
  `brand-definition.md`, which ships neutral: no brand exists until one is
  built or handed in.
- Apply: the cascade that lands the active identity (name segments, palette
  as CSS variables, voice register, wordmark, license) on a sibling's
  neutral output per `application-doctrine.md`, never touching a skill's
  description field; per-element exclusions honored without ceremony.
- Audit: seven drift categories in fixed order with the P0 floor — any
  firewall breach, identity leak, or exposed credential caps the overall
  score at 3.0 with an explicit off-brand verdict, mean shown alongside so
  dilution cannot hide the breach. Report only; fixes land on approval.
- Export: four payloads — the six-field voice profile commwright consumes,
  the skillwright structural payload, a human style one-pager, and a fully
  offline 12-section HTML brand-guide card.
- A `neutral` switch forcing spec-clean output regardless of the stored
  definition, and a stated boundary: brandwright defines identity;
  skillwright port propagates it across a pack.
