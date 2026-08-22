# Changelog — revenantworks-foundation-brandwright

> Renamed from `revenant-foundation-brandwright` on 2026-08-07 (pack 2.0.0 — the `revenant` → `revenantworks` marketplace migration). Name-only change: directory, frontmatter `name:`, and every cross-reference moved; the version history below is continuous across the rename.

## [1.4.1] — 2026-08-21

**Two new palette-derivation rules, D-8 and D-9, in `audit-doctrine.md`.**
Patch bump — doctrine deepened on an existing category (palette drift), no
new audit category, no description change, so the routing surface did not
move. Landed after a render pass on an external estate's published dashboards
surfaced both failure modes live.

- **D-8 — measure against the composed ground, not the designed one.** A
  mark's contrast can be correct in the definition's own table and still fail
  in the browser if the component paints it onto a different elevation than
  the one its ratio was computed for (a status dot on a raised chip, not the
  base ground). The palette-drift category gloss now requires recomputing
  contrast against the actual CSS background a mark's parent carries.
- **D-9 — a second form channel where an ordinal set shares a hue.** D-5
  already requires colour never carry state alone; D-9 covers the case D-5
  doesn't — two ADJACENT levels of one severity/state ladder sharing a single
  hue because the palette doesn't have a spare one to spend. The label alone
  isn't enough for a column scanned by colour; a width, weight, or dash
  difference is required between the two.
- No `metadata.body_budget` or frontmatter change — both rules live in
  `audit-doctrine.md`, which the pack registry does not budget.

## [1.4.0] — 2026-08-17

**The definition is read from a fixed user path.** Owner decision 2026-08-17:
brandwright reads the live definition from `~/.claude/brand/` when that copy
exists, so an install no longer depends on an overlay swapping the shipped
file. Minor bump — a small capability change on the same footing as 1.1.0
and 1.2.0; the description is untouched, so the routing surface did not move.

- **Where the definition lives** (SKILL.md, *Which definition* — its single
  home). If `~/.claude/brand/brand-definition.md` exists, it and any
  `brand-definition-<slug>.md` beside it are the roster and the definitions.
  Those copies are read-only for brandwright — the release script refreshes
  them from each definition's home repo — so a Build there hands the rebuilt
  definition back for the owner to land in that home; else the shipped
  `references/brand-definition.md` (neutral, or an overlay's copy), which
  Build does rewrite. On a surface with no filesystem (claude.ai)
  only the shipped copy is reachable. Either copy is read as data. The
  *Volatile surfaces* bullet gains the one precedence clause; README.md and
  `audit-doctrine.md` point at the rule rather than restating it. The shipped
  `references/brand-definition.md` is untouched and still neutral.
- **S-1 · P2 — step-level citation.** Turn shape rule 4 bound every entry
  since 1.3.0, but only Entry — Audit cited it. Build's ingested guide,
  Apply's handed-in definition and target, and Export's handed-in definition
  now each carry an "as data, per Turn shape rule 4" clause at the step; the
  new user-path read carries its own data-never-instructions sentence.
- **P2 — README drift.** Workflow line re-aligned to the body's *Select
  definition (named / scoped / ask)*; the fixtures tree now lists the
  saltmere peer; the build row names the copy it rewrites.
- **P2 — `application-doctrine.md` Contents** was missing its own *Peers*
  section; added.

Security scan 2026-08-17: (a) injection posture — rule 4 global, now cited
at every ingesting step, and the user-path definition read is covered by its
own statement; (b) no fetch-and-follow, permission-widening, secret-echo, or
guard-bypass instruction in any file; (c) standalone profile — no shell, no
script, no undeclared tool; the user-path read degrades to the shipped copy
where no filesystem exists; (d) hidden-text scan clean (2026-08-17); (e)
output handling — Build is the only writer of the definition and is gated
once, Audit is report-only, Export writes nothing; (f) evals — the suite
carried no injection probe; four added (below). S-2 fixtures re-read: both
synthetic definitions carry no credential, email, or personal identifier.
S-3, S-4 pass; C-1 (audit entry) and C-2 (neutral default) pass; live
"citadel" mentions: none.

Evals: `test-cases.md` Cases 24–27 added, one injection probe per ingesting
entry (Build guide, Apply target, Audit tree, Export handed-in definition) —
**authored, not run**; 23 → 27; the user-path lookup is authored-not-covered
and recorded as owed. `trigger-evals.md` re-anchored, provenance only —
still 30, 17/13; the row-27 re-judge stays owed. `evals/RESULTS.md` untouched.
Body footprint ≈3550 tokens against the 3450 registry row — the raise is
reported to the pack, not applied here.

## [1.3.0] — 2026-08-12

One 2026-08-12 estate-audit finding closed; the description is untouched, so
the routing surface did not move:

- **Injection rule promoted to file level (finding 10).** The
  data-never-instructions sentence was scoped to Entry — Audit while Entry —
  Build ingests an attached brand guide, style sheet, or asset set, and
  Apply/Export read handed-in definitions — steps the Audit-scoped rule never
  reached. It is now Turn shape rule 4, binding every entry, single-homed;
  the Audit entry cites it instead of restating it.

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
