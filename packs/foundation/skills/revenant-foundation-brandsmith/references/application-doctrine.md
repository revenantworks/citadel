# Application Doctrine — how a brand lands, on invoke

How the active `brand-definition.md` lands on a target when someone runs
**Entry — Apply**. Skills, messages, and artifacts are built *neutral* by their
own smiths; brandsmith applies the identity only when asked. These rules never
change for a rebrand — the definition changes the values, this maps where they go.

## Contents

- The cascade
- What never inherits
- Overrides
- Suites

---

## The cascade

| Definition element | Where it lands in the target |
|---|---|
| Brand token + pack | Name segments (`<brand>-<pack>-<skill>`) and frontmatter `metadata.brand` / `metadata.pack` — for a built skill, usually already stamped structurally at build; Apply confirms, never renames silently |
| Profile | Frontmatter `metadata.profile` (structural; set at build) |
| Palette role tokens | Any HTML/visual output the target produces (cards, pages, reports): background/text/accent CSS variables |
| Voice profile | Prose register of a README, CHANGELOG, or message body — never a skill's `description` field |
| License default | LICENSE file + frontmatter `license` |
| Wordmark rule | Header/footer lockup on the target's HTML artifacts |

Unconfigured elements fall back to neutral — spec-clean, nothing invented.
Partial definitions are normal: apply what exists, skip what doesn't, silently.

## What never inherits

- **The description field.** Descriptions are routing, not branding: trigger
  words only. A brand term appears there solely when it is itself an invocation
  keyword the user will say (as "brandsmith" is).
- **Instruction content.** Brand never adds rules, sections, or tokens to a
  target's working instructions — lean beats lockup.
- **Other people's inputs.** A brand guide attached for one Apply run configures
  nothing; only "brandsmith build" writes the definition.

## Overrides

Per run: `neutral` produces a fully unbranded, spec-clean result regardless of
what's stored. Per element: a run may name individual exclusions ("no palette on
this one") — honor them without ceremony.

## Suites

A pack's members apply identically in one cascade — shared brand/pack segments,
shared profile, shared palette — so a suite reads as one product line. Per-skill
deviations within a suite are allowed only when deliberate and documented in the
pack README.
