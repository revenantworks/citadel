# Brand Config — Volatile *(single update surface)*

> **Last configured: 2026-07-14.** This is the **only** file "skillsmith configure" rewrites — durable rules live in `brand-inheritance.md` and never change for a rebrand. Everything below adjusts skillsmith to its current user or organization; a fresh install without configuration behaves per the Neutral defaults at the bottom. Configured from brandsmith's export (brand-definition **v1.2.2**): **Revenant** is the parent house brand; the `revenant` token names its skills — token unchanged, hierarchy inverted from the prior persona-parent configuration.

## Active configuration

| Parameter | Value |
|---|---|
| Brand / company token | `revenant` — the **Revenant** house brand ("always comes back"; assistant nickname "Rev"). Skills are house products |
| Identity map | GitHub org `revenantworks` (to create — separate Revenant identity; repo relocating there) · tags RVNT / REV |
| Voice | House voice — calm, exact, inevitable; short declaratives, no exclamation marks, no hype. Docs plain technical; release notes dry + max one flavor line; social minimal, lowercase fine |
| Tagline | "Always comes back." (alts: "Nothing stays dead here." · "Down is temporary.") — HTML-artifact and README flavor only; never in descriptions or instruction content |
| Sign-off | Releases: "Back online." · social: "— RVNT" — house surfaces; persona sign-offs live in brandsmith's definition (the firewall governs use) |
| License default | MIT |
| Packaging default | Folder-zip, full files including `evals/`, folder at top level, named `<name>-<version>.zip` — `.skill` on request (uploader compatibility; registered 2026-07-13, previously a standing oral rule) |
| Wordmark rule | Terminal lockup: lowercase monospace `revenant▍` — block cursor in threshold-blue on voidblack (blinking where motion is allowed) — in HTML-artifact headers with a small footer echo; optional tagline in the footer |

## Pack registry

| Pack | Profile | Notes |
|---|---|---|
| `foundation` | standalone | Lean, no tools beyond web search, low overhead; self-updating stamps. Conformance checks (2026-07-13): C-1 drift-audit verb · C-2 neutral default. Integrate policy: restamp: lazy (2026-07-13) |

**foundation members** *(canonical roster — pack manifests are generated from this table)*

| Member | Job | Route there when |
|---|---|---|
| `revenant-foundation-promptsmith` | Builds, scores, and hardens prompts with model-tier routing | The deliverable is a prompt, meta-prompt, or system prompt |
| `revenant-foundation-skillsmith` | Builds, audits, brands, and ports Agent Skills and packs | The deliverable is a skill, SKILL.md, or pack — new, audited, or ported |
| `revenant-foundation-commsmith` | Shapes messages per channel, audience, and saved voice; audits message drift | The deliverable is a message, announcement, comms plan, or message audit |
| `revenant-foundation-agentsmith` | Designs and audits autonomous agent systems — guardrails, trust tiers, kill switches | The deliverable is an agent's operating spec or an audit of one |
| `revenant-foundation-loresmith` | Research-verified verdicts and playbook reference docs with evidence tags | The deliverable is a recommendation or a reference document |
| `revenant-foundation-brandsmith` | Builds the brand definition (identity through typography, motion, accessibility); audits repos, packs, docs, and artifacts for drift across seven categories; exports voice/config payloads and the HTML brand-guide card | The deliverable is a brand definition, a drift report, or an export for a sibling |
| `revenant-foundation-evalsmith` | Authors and audits eval suites — build-time generator, zero runtime dependency | The deliverable is a trigger-eval set, assertion suite, or suite audit |
| `revenant-foundation-tokensmith` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | The deliverable is a leaner artifact, a token-efficiency audit, or a budget sheet |

**foundation capstone:** Forge Run — one orchestration prompt driving all eight smiths end-to-end (stored 2026-07-12 · roster updated to eight 2026-07-13 · roster reconfirmed 2026-07-14, pack self-audit, no change; re-run after any member's major version bump). First live run: brandsmith, 2026-07-13.

**foundation canonical repo:** `github.com/revenantworks/citadel` — source of truth for member drift audits (registered 2026-07-13). **Subject to relocation** — planned move to the `revenantworks` org (decided 2026-07-14; personal-account copy goes private as archive); on the move, update this row and restamp the pack manifests. Nothing else carries the URL: manifests are generated from here, and every other file says "the registered canonical repo."

New packs and members are added here by "skillsmith configure" or at build time (name + profile per pack; one row per member; custom profiles list their policies inline).

## Palette — role tokens

Roles, not just hex: roles let the system style artifact types not anticipated.

| Role | Token | Value |
|---|---|---|
| background | voidblack | `#0A0A0B` |
| text | bone-white | `#EDEDED` |
| secondary-text | ash-grey | `#8A8F98` |
| accent *(house)* | threshold-blue | `#00E5FF` |
| functional — hype *(one-off)* | glitch-magenta | `#FF2D78` |
| functional — error *(one-off)* | phantom-green | `#39FF14` |
| functional — live/warning *(one-off)* | ember-orange | `#FF6A00` |

Contrast rule: black dominates and threshold-blue is the house's single identity accent — the contrast **is** the brand. Ash grey carries secondary UI text; functional tokens signal states (hype / error / live), never identity, and never sit evenly distributed. Sub-brand accents live in brandsmith's brand definition and never style house/dev surfaces.

## Neutral defaults *(unconfigured behavior)*

No brand or pack segments — plain descriptive skill names, gerund form preferred. No palette applied — HTML outputs use a clean neutral dark theme. Voice: plain professional. License: MIT. Wordmark: none. Every neutral default is also reachable per build via the `brand: neutral` override, regardless of configuration.
