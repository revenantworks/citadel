# Brand Definition — Volatile *(single update surface)*

> **Last built: — (never; ships neutral).** This is the **only** file "brandwright build" rewrites — doctrine lives in `audit-doctrine.md` and never changes for a rebrand. With no definition below, every brandwright output defaults to the Neutral baseline, and audits run in hygiene mode only (internal consistency, no brand judgments).

## Roster

Every definition this install carries. One row per brand; the primary is this file,
peers are `brand-definition-<slug>.md` beside it. Selection reads this table, so a
brand absent here is a brand brandwright will not find.

| Slug | File | Scope — surfaces it owns | Coexists with | Boundary |
|---|---|---|---|---|
| — | — | — | — | — |

*Empty. A build adds the row for the brand it writes.* **Scope** is what makes
selection possible without asking every time; **Boundary** states whether a peer's
attribution mark may appear on this brand's surfaces, and nothing more.

## Active definition

*None. Run "brandwright build" (ingest a guide, or take the one-batch interview Entry — Build enumerates) to populate the sections below. These sections are the storage shape, not that interview list, and the mapping is deliberately not one-to-one: Essence and the History notes are written from the answers, never asked as groups. Each build bumps the definition version and re-stamps this header.*

### Essence *(empty)*
### Identity map *(empty)*

| Element | Value |
|---|---|
| Parent brand | — |
| Sub-brands | — |
| Handles / orgs | — |
| Community terms | — |
| Brand owner / exceptions | — |

### Naming conventions *(empty)*

Templates per artifact class (repos, skills, packs, files, titles) go here — e.g. `<brand>-<pack>-<skill>` — with the classes they bind.

### Palette — role tokens *(empty)*

Storage shape only; a build fills it. The rows below exist because
`audit-doctrine.md`'s *Build — palette derivation* rules have nowhere to land
without them — a definition missing the surface ladder or the border pair cannot
be audited against D-2 or D-3, and the gap reads as compliance.

**Neutrals — computed, not picked.** Generate the ladder in OKLCH at this brand's
own accent hue with even lightness steps (D-1), and record the hue so an audit can
re-derive it. Each step clears ~1.13:1 against the one below (D-2).

| Role | Token | Value | on background | step above |
|---|---|---|---|---|
| background | — | — | — | — |
| surface | — | — | — | — |
| surface raised | — | — | — | — |
| border *(quiet — structure)* | — | — | — | — |
| muted text | — | — | — | — |
| text | — | — | — | — |

*Hue all neutrals were derived at: — . Add further elevations only when a real
surface needs one.*

**Accents — one row per accent, both values.** `base` for the dark ground, `ink`
for the light one, each with its measured ratio (D-4).

| Token | Owner *(house or sub-brand)* | `base` | on dark | `ink` | on light |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**Light — per brand, per mode.** `border-lit` is the load-bearing edge and clears
3:1 on its own surface (D-3); `glow` is bloom, never a fill. Both derive from the
accent's **own** lightness, never a borrowed one (D-5). A brand with a primary and
an alternate accent carries a complete set per mode, and modes never mix on one
surface.

| Brand | Mode | Derived from | `border-lit` | vs surface | `glow` | vs background |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

**Shared accents / functional job-colors — status, never identity.** State each
one's default reading, and remember colour never carries state alone (D-6). Where
a set exists so that one always works whatever accent leads a surface, prove it
with a ΔE00 coverage matrix rather than asserting it (D-7).

| Token | Value | Character | Default reading when it carries state |
|---|---|---|---|
| — | — | — | — |

*Separation floor (CIEDE2000, tightest pair among the tokens above): — . Any new
accent must beat it.*

### Typography roles *(empty)*

Faces per brand role, hierarchy, open-license fallback stacks.

### Voice profile + register map *(empty)*

The single home of voice: the six fields Entry — Export names (name → allowed surfaces, in that order), plus which surfaces get which register. commwright consumes this profile (via export) to apply a voice to one message; Entry — Apply consumes it to set prose register on the surfaces this register map governs, never on a message. With none defined, everything downstream defaults to neutral professional.
### Taglines / sign-offs *(empty)*

Each with its allowed surfaces.

### Wordmark rule + logo usage *(empty)*

Clearspace, minimum sizes, misuse list.

### Imagery & iconography *(empty)*
### Motion *(empty)*
### Applications — quick specs *(empty)*
### Accessibility *(empty)*
### Firewall map *(empty)*

Identity pairs that never share a surface, and the surfaces in question.

### History notes *(empty)*

Renames and retirements land here — old handles, org names, and taglines the audit hunts as stale strings.

## Neutral baseline *(behavior with no definition)*

Plain descriptive naming, gerund form preferred · no palette — clean neutral dark for HTML outputs · voice: plain professional · no taglines, sign-offs, or wordmark · firewall: n/a. Every neutral default is also reachable per run via an explicit "neutral" override, regardless of what's stored.
