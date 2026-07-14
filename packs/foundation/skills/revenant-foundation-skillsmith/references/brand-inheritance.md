# Brand Inheritance — Durable Cascade Rules

How the active `brand-config.md` lands on every skill skillsmith builds. Configure changes the values; these rules never change for a rebrand.

## Contents

- The cascade
- What never inherits
- Overrides
- Suites

---

## The cascade

| Config element | Where it lands in a built skill |
|---|---|
| Brand + pack | Name segments (`<brand>-<pack>-<skill>`) and frontmatter `metadata.brand` / `metadata.pack` |
| Pack profile | Frontmatter `metadata.profile`; governs the build's dependency rules and audit target |
| Palette role tokens | Any HTML/visual output the built skill produces (cards, pages, reports): background/text/accent CSS variables; also any HTML artifact skillsmith itself emits for the user |
| Voice | The built skill's README and CHANGELOG prose register — never its description field |
| License default | LICENSE file + frontmatter `license` |
| Wordmark rule | Header/footer lockup on the built skill's HTML artifacts |

Unconfigured elements fall back to the Neutral defaults in `brand-config.md` — spec-clean, nothing invented. Partial configuration is normal: apply what exists, skip what doesn't, silently.

## What never inherits

- **The description field.** Descriptions are routing, not branding: trigger words only. A brand term appears there solely when it is itself an invocation keyword the user will say (as "skillsmith" is).
- **Instruction content.** Brand never adds rules, sections, or tokens to a built skill's working instructions — lean beats lockup.
- **Other people's inputs.** A brand guide attached for one build configures nothing; only "skillsmith configure" writes to `brand-config.md`.

## Overrides

Per build: `brand: neutral` produces a fully unbranded, spec-clean package regardless of configuration; `brand: <pack>` selects a different registered pack's identity and profile. Per element: a build may name individual exclusions ("no palette on this one") — honor them without ceremony.

## Suites

All pack siblings inherit identically in one cascade — shared brand/pack segments, shared profile, shared palette — so a suite reads as one product line. Per-skill deviations within a suite are allowed only when deliberate and documented in the pack README.
