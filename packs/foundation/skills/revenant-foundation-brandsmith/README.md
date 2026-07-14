# revenant-foundation-brandsmith

Defines the identity; audits everything against it. Builds a full brand definition — identity through typography, logo usage, motion, and accessibility — by interview or ingestion, scores repos, skill packs, docs, and artifacts for drift against it, and exports the pieces siblings consume. Ships neutral — no brand exists until you build one.

## Commands

| Say | Get |
|---|---|
| "brandsmith build" (± a guide attached) | Ingest-first interview → versioned brand definition, gated once |
| "brandsmith audit" + a target | Seven-category scoreline + drift catalog with exact fixes; report only |
| "brandsmith export" | Voice profile (commsmith shape) · configure payload (skillsmith shape) · style one-pager · brand-guide card (self-contained HTML) |
| "brandsmith" | One-line intro + what it needs |

## The law

Neutral core: doctrine files carry zero identity content. The active definition lives only in `references/brand-definition.md` — the single update surface — and with none stored, outputs default spec-clean and audits run in hygiene mode.

## Package

    revenant-foundation-brandsmith/
    ├── SKILL.md
    ├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
    ├── references/
    │   ├── brand-definition.md       # volatile, stamped — ships neutral/empty
    │   ├── audit-doctrine.md         # interview spec, drift categories, export shapes
    │   └── pack.md                   # foundation roster (advisory)
    └── evals/                        # version-control archive; excluded from .skill payloads
        ├── test-cases.md             # 14-case assertion-only suite
        └── trigger-evals.md          # 20 should/shouldn't queries

## Versioning

Semver; history in CHANGELOG.md. Provenance: foundation skill #6 — Open Decision 1 resolved standalone (renamed from brandkeeper); first live Forge Run build, 2026-07-13.

MIT — see LICENSE.
