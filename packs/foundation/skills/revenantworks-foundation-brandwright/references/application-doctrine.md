# Application Doctrine — how a brand lands, on invoke

How the active `brand-definition.md` lands on a target when someone runs
**Entry — Apply**. Skills, messages, and artifacts are built *neutral* by their
own wrights; brandwright applies the identity only when asked. These rules never
change for a rebrand — the definition changes the values, this maps where they go.

## Contents

- The cascade
- Palette inheritance — structure, light, and marks
- Overrides
- Suites
- Peers — applying one brand where another lives

---

## The cascade

| Definition element | Where it lands in the target |
|---|---|
| Brand token + pack | Name segments (`<brand>-<pack>-<skill>`) and frontmatter `metadata.brand` / `metadata.pack` — for a built skill, usually already stamped structurally at build; Apply confirms, never renames silently |
| Profile | Frontmatter `metadata.profile` (structural; set at build) |
| Palette role tokens | Any HTML/visual output the target produces (cards, pages, reports): background/text/accent CSS variables, plus the surface/border stack and the lit/glow pair where the definition carries them — which of those a given target inherits is Palette inheritance below |
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

## Palette inheritance — structure, light, and marks

Three rules deciding which palette values reach a target once the definition holds
more than one identity or more than one mode. Where the values come from is
`audit-doctrine.md`'s Build — palette derivation; this is where they land.

**Structure is shared; light is not.** The neutral surface and border stack may be
one system-wide set — at those chromas its hue is barely perceptible, so sharing it
costs no identity — and Apply lands it on every target in the system. Visible colour
is the opposite: an accent, and the lit and glow values derived from it, belong to
**one identity and one mode**. A sub-brand's surface derives its own light from its
own accent and never inherits the parent's, inside one pack, one repo, or one page.

**A multi-mode brand needs a complete light set per mode, and modes never mix on one
surface.** Where the definition holds a primary and an alternate accent, Apply
resolves the mode first and lands that mode's whole set together; taking one value
from each mode is the defect this rule exists to prevent. The definition states the
**switch condition** — which surfaces or contexts select the alternate — and Apply
follows it. A mode carrying values but no stated switch condition is an incomplete
definition, raised at the gate rather than guessed at.

**The mark tier — a parent accent may cross as attribution, never as light.** A
parent brand's accent is allowed on a child's surface where it is doing *attribution*
work: a lineage line, a co-branded lockup, a link home. It is never that surface's
identity, never its lit or glow, and never its content emphasis. Scope the
no-crossing rule that way — **light versus mark** — rather than forbidding the colour
outright, or every honest lockup becomes a finding. The firewall map still governs
which identities may co-occur at all; the mark tier only bounds what a permitted
co-occurrence may use the colour *for*.

## Overrides

Per run: `neutral` produces a fully unbranded, spec-clean result regardless of
what's stored. Per element: a run may name individual exclusions ("no palette on
this one") — honor them without ceremony.

## Suites

A pack's members apply identically in one cascade — shared brand/pack segments,
shared profile, shared palette — so a suite reads as one product line. Per-skill
deviations within a suite are allowed only when deliberate and documented in the
pack README.

## Peers — applying one brand where another lives

An install may carry several definitions. They are peers, not a hierarchy, and the
cascade runs for exactly one of them per invocation.

- **Selection precedes application.** Resolve which definition applies (SKILL.md,
  *Which definition*) before mapping a single element. Applying the wrong brand is
  not a drift finding to fix later — it is a mislabelled artifact.
- **Never blend.** One output carries one brand's identity. A palette from one and a
  voice from another is not a hybrid, it is two brands failing at once.
- **Scope wins over convenience.** A target inside a peer's declared scope takes that
  peer even when the request arrived while another was in hand. Say which one you
  used in the handback.
- **Attribution is the one shared surface.** A peer's mark may appear on this brand's
  surface only where *this* brand's definition declares it — lineage lines, a
  co-branded lockup, a link home. It carries no other job there: never that surface's
  light, never its content emphasis, never a matched set beside its accent.
- **A per-run exclusion never crosses brands.** "Skip the palette" narrows one
  application; it does not authorise reaching into a peer for the part you skipped.
