# revenantworks-foundation-brandwright

The single home of brand and voice. It builds a full brand definition — identity through
typography, logo usage, motion, and accessibility, plus the voice profile — by interview or
ingestion. It **applies** that definition on request to a built skill, artifact, repo, or
document. It scores repos, skill packs, docs, and artifacts for drift against it, and exports the
pieces siblings consume. Ships neutral — no brand exists until you build one, and outputs default
spec-clean. Consistency is enforced by report, never by silent rewrite. Branding is always a
deliberate invocation, never baked into someone else's build.

**Workflow:** Intake → Select definition *(named / scoped / ask)* → Build / Apply / Audit / Export → Gate → Handback

## Package contents

```
revenantworks-foundation-brandwright/
├── SKILL.md                      # entry point — four entries, load budget, neutral-core law
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── brand-definition.md       # event-driven, stamped — the active identity + voice (ships neutral/empty; a ~/.claude/brand/ copy overrides it)
│   ├── application-doctrine.md    # Entry — Apply: how the brand/voice lands on a target, plus palette inheritance
│   ├── audit-doctrine.md         # build extraction + palette-derivation rules, sweep notes, guide-card fill rules
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── test-cases.md             # assertion-only suite
    ├── trigger-evals.md          # should/shouldn't queries
    └── fixtures/
        ├── brand-definition.md   # SYNTHETIC test brand — fictional, test data only, never a real identity
        └── brand-definition-saltmere.md  # its SYNTHETIC roster peer, same rule
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to define, apply, or audit a brand or voice, or by saying `brandwright` (subcommands: `brandwright build`, `brandwright apply`, `brandwright audit`, `brandwright export`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Ingest-first interview (a handed-in guide is read before anything is asked) → versioned brand + voice definition, gated once |
| **apply** | "brandwright apply" at a built skill, artifact, repo, or document → lands the active identity (name segments, palette on HTML, voice register, wordmark) per the application doctrine; unconfigured elements stay neutral |
| **audit** | "brandwright audit" + a target → seven-category scoreline (the count and order are set in SKILL.md's Entry — Audit; `audit-doctrine.md` glosses them in that order) + drift catalog with exact fixes; report only |
| **export** | Voice profile (commwright consumes it) · structural payload (skillwright) · style one-pager · brand-guide card (self-contained HTML) |

## Commands & switches

| Invocation | What it does |
|---|---|
| `brandwright` | Bare invocation — one-line intro + what it needs |
| `brandwright build` | Define, rebuild, or consolidate a brand + voice; rewrites `references/brand-definition.md` only — a `~/.claude/brand/` copy is read-only, so a Build there is handed back for the owner to land in the definition's home repo |
| `brandwright apply` | Brand a built skill or artifact on invoke — the cascade, run only when asked |
| `brandwright audit` | Drift report against the active definition (or one handed in); fixes land on approval |
| `brandwright export` | Emit a payload a sibling or a human consumes |

| In-request switch | Effect |
|---|---|
| "apply all" | Skips the single gate |
| `neutral` | Produces spec-clean unbranded output regardless of what's stored |
| a per-element exclusion (see `application-doctrine.md`'s Overrides) | Honored without ceremony during Apply |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/brand-definition.md` is **event-driven** — the active identity and voice profile are rewritten only by "brandwright build" (each build bumps the definition version and re-stamps the header), never on a clock. Where the live copy is read from — `~/.claude/brand/brand-definition.md` and its siblings when present, else the shipped file; on claude.ai only the shipped file — is stated once in SKILL.md, *Which definition*. With none stored, every output defaults spec-clean neutral. Everything else is durable doctrine.

## Changelog

See [CHANGELOG.md](CHANGELOG.md). Provenance: foundation skill #6 — first live Forge Run build, 2026-07-13.
