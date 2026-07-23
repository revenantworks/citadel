# revenant-foundation-brandsmith

The single home of brand and voice. Builds a full brand definition — identity through typography, logo usage, motion, and accessibility, plus the voice profile — by interview or ingestion; **applies** it on request to a built skill, artifact, repo, or document; scores repos, skill packs, docs, and artifacts for drift against it; and exports the pieces siblings consume. Ships neutral — no brand exists until you build one, and outputs default spec-clean. Consistency is enforced by report, never by silent rewrite; branding is always a deliberate invocation, never baked into someone else's build.

**Workflow:** Intake → Resolve definition *(stored / handed-in / neutral)* → Build / Apply / Audit / Export → Gate → Handback

## Package contents

```
revenant-foundation-brandsmith/
├── SKILL.md                      # entry point — four entries, load budget, neutral-core law
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── brand-definition.md       # event-driven, stamped — the active identity + voice (ships neutral/empty)
│   ├── application-doctrine.md    # Entry — Apply: how the brand/voice lands on a built skill or artifact
│   ├── audit-doctrine.md         # interview spec, drift categories, guide-card fill rules
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── test-cases.md             # assertion-only suite
    └── trigger-evals.md          # should/shouldn't queries
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to define, apply, or audit a brand or voice, or by saying `brandsmith` (subcommands: `brandsmith build`, `brandsmith apply`, `brandsmith audit`, `brandsmith export`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Ingest-first interview (a handed-in guide is read before anything is asked) → versioned brand + voice definition, gated once |
| **apply** | "brandsmith apply" at a built skill, artifact, repo, or document → lands the active identity (name segments, palette on HTML, voice register, wordmark) per the application doctrine; unconfigured elements stay neutral |
| **audit** | "brandsmith audit" + a target → seven-category scoreline (naming, palette, typography/logo, voice/register, taglines, stale strings, firewall) + drift catalog with exact fixes; report only |
| **export** | Voice profile (commsmith consumes it) · structural payload (skillsmith) · style one-pager · brand-guide card (self-contained HTML) |

## Commands & switches

| Invocation | What it does |
|---|---|
| `brandsmith` | Bare invocation — one-line intro + what it needs |
| `brandsmith build` | Define, rebuild, or consolidate a brand + voice; rewrites `references/brand-definition.md` only |
| `brandsmith apply` | Brand a built skill or artifact on invoke — the cascade, run only when asked |
| `brandsmith audit` | Drift report against the active definition (or one handed in); fixes land on approval |
| `brandsmith export` | Emit a payload a sibling or a human consumes |

| In-request switch | Effect |
|---|---|
| "apply all" | Skips the single gate |
| `neutral` | Produces spec-clean unbranded output regardless of what's stored |
| a per-element exclusion ("no palette on this one") | Honored without ceremony during Apply |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/brand-definition.md` is **event-driven** — the active identity and voice profile are rewritten only by "brandsmith build" (each build bumps the definition version and re-stamps the header), never on a clock. With none stored, every output defaults spec-clean neutral. Everything else is durable doctrine.

## Changelog

See [CHANGELOG.md](CHANGELOG.md). Provenance: foundation skill #6 — resolved standalone (renamed from brandkeeper); first live Forge Run build, 2026-07-13.
