# Application Doctrine — how a brand lands, on invoke

How the active `brand-definition.md` lands on a target when someone runs
**Entry — Apply**. Skills, messages, and artifacts are built *neutral* by their
own wrights; brandwright applies the identity only when asked. These rules never
change for a rebrand — the definition changes the values, this maps where they go.

## Contents

- The cascade
- Overrides
- Suites

---

## The cascade

| Definition element | Where it lands in the target |
|---|---|
| Brand token + pack | Name segments (`<brand>-<pack>-<skill>`) and frontmatter `metadata.brand` / `metadata.pack` — for a built skill, usually already stamped structurally at build; Apply confirms, never renames silently |
| Profile | Frontmatter `metadata.profile` (structural; set at build) |
| Palette role tokens | Any HTML/visual output the target produces (cards, pages, reports): background/text/accent CSS variables |
| Voice profile | Prose register on the target's own surfaces, as the definition's register map governs them — never a skill's `description` field, and never a channel-bound message |
| License default | LICENSE file + frontmatter `license` |
| Wordmark rule | Header/footer lockup on the target's HTML artifacts |

Unconfigured elements fall back to neutral — spec-clean, nothing invented.
Partial definitions are normal: apply what exists, skip what doesn't, silently.

**Register lands where the definition governs, not wherever prose lives.** Apply
sets register only on surfaces the register map names — landing a *defined*
voice, the ask Entry — Apply's "put the house voice on this README" example
describes. Two limits on that row, neither of them this table's to relax. A
channel-bound message is never an Apply target: applying a voice to the message
in hand is commwright's, via the exported profile. And prose-style work *as
such* — humanizing or restyling how a repo file is written, with no definition
in play — is skillwright's under Entry — Audit's prose pass, per the
`skillwright ↔ commwright` seam row; a cascade row is not where that gets decided,
so a run that turns out to be asking for it says so and routes there.

**Sibling artifacts are apply targets.** Every other wright builds neutral; their outputs come here to be branded, and brandwright is the *only* place brand is applied. Canonical targets: a promptwright **prompt card** (its neutral "Prompt Card" header takes the wordmark lockup and the palette), a tokenwright **report / budget sheet** (its neutral HTML takes the palette), and any skill's HTML artifact. None of them apply brand themselves — Apply is the single door.

## Overrides

Per run: `neutral` produces a fully unbranded, spec-clean result regardless of
what's stored. Per element: a run may name individual exclusions ("no palette on
this one") — honor them without ceremony.

## Suites

A pack's members apply identically in one cascade — shared brand/pack segments,
shared profile, shared palette — so a suite reads as one product line. Per-skill
deviations within a suite are allowed only when deliberate and documented in the
pack README.
