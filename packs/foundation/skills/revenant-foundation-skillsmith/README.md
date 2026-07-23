# revenant-foundation-skillsmith

Builds, audits, and ports Agent Skills — from a one-line intent to a packaged, install-ready skill or multi-skill pack. What separates it from skill scaffolders and creators: every build starts with fresh best-practices research and a **niche verdict** (should this skill exist, and against which incumbents — checked against the live skill registries and plugin directories, not vibes), constructs to a declared **policy profile** rather than one-size rules (standalone by default: self-contained, lean, self-updating — but packs may allow tools, scripts, and sibling skills, all declared), and ships every skill **born testable** — trigger evals and an assertion suite in the box. It builds **spec-clean neutral** — brand and voice are applied only by invoking brandsmith. It runs zero scripts of its own, so it behaves identically on claude.ai, Claude Code, and the API.

**Build workflow:** Intent → Pack & profile → Research → Niche verdict → Design catalog *(one gate)* → Build → Self-audit → Package

Interaction contract: one complete catalog, one approval gate, no drip-feed iteration.

## Package contents

```
revenant-foundation-skillsmith/
├── SKILL.md                      # entry point — workflow, entry points, load budget, turn shape
├── README.md                     # this file
├── LICENSE                       # MIT
├── CHANGELOG.md                  # version history
├── SOURCES.md                    # where the guidance comes from
├── references/                   # runtime — loaded per the SKILL.md load budget
│   ├── rubrics.md                # Rubric A baseline (calendar-volatile, refresh target) + policy profiles
│   ├── build-templates.md        # skeletons, naming render, suites & composition, gold standard
│   ├── pack-registry.md          # structural registry (event-driven) — roster, naming template, profiles; build.py derives manifests here
│   ├── description-crafting.md   # trigger writing, boundary sentences, discoverability test
│   ├── pack-design.md            # whole-pack design: capability map, roster catalog, session staging
│   ├── pack-integration.md       # integrate doctrine: registry → roster → manifests → release
│   ├── upkeep-doctrine.md        # upkeep sweep: cadence math, refresh-verb map, degradation by environment
│   ├── eval-authoring.md         # trigger evals + assertion suites for built skills
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # maintenance / QA assets — in full folder-zips, excluded from .skill
    ├── test-cases.md             # assertion-only regression suite
    └── trigger-evals.md          # should/shouldn't-trigger queries
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your platform's skills directory, or upload the archive in Claude settings. Trigger it by asking to build, audit, score, or package a skill, or by saying `skillsmith` (subcommands: `skillsmith refresh`, `skillsmith integrate`, `skillsmith pack`, `skillsmith port`, `skillsmith upkeep`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Intent → research → niche verdict → one design catalog + gate → package → self-audit → handback |
| **audit** | Point at any existing skill: dual scoring (best practices + its declared profile), niche verdict, one fix catalog + gate, one consolidated rewrite |
| **refresh** | Re-verifies the best-practices baseline against canonical sources; regenerates only the stamped section |
| **upkeep** | Pack-wide staleness sweep: reads every member's `metadata.volatile`, reports each calendar surface's status vs cadence (report-only default), runs the mapped refresh verb per overdue surface on approval — degrading by environment |
| **port** | Point at an existing skill set + a target: identity-scrubbed, renamed, re-verified copy with a PORT-REPORT — source never modified |
| **integrate** | Propagate a new or changed member across its pack: registry row, capstone roster line, `pack.md` restamp ×N, packages rebuilt per policy, repo-sync bundle + upload checklist. Offered as "keep going" after every pack build |
| **pack** | Design and build a whole pack from a domain or role: capability map with adopt-don't-build tiers → one roster gate (trigger-partition table, session plan) → staged builds → set discoverability test → integrate → optional plugin/marketplace prep |

To define, apply, or audit a **brand or voice**, that's brandsmith — skillsmith builds neutral and leaves branding to a deliberate brandsmith invocation.

## Commands & switches

Named invocations — everything else routes on natural requests ("build me a skill that…", "audit this SKILL.md"):

| Invocation | What it does |
|---|---|
| `skillsmith` | Bare invocation — capability line, then asks what to build or check |
| `skillsmith refresh` | Re-verify the best-practices baseline in `references/rubrics.md`; patch bump + repackage. Run at the 60-day stamp or when the skill format changes |
| `skillsmith upkeep` | Sweep the whole pack for stale calendar surfaces (reads each member's `metadata.volatile`); report due/overdue, refresh the approved ones per their owning skill's verb, degrade by environment |
| `skillsmith port` | Re-issue a skill set for a new owner or purpose — sanitize sweep + rename + stale-ref refresh + PORT-REPORT; the source set is never modified |
| `skillsmith integrate [member]` | One-operation pack propagation with all-or-notes integrity and a count check; blast radius per the pack's `restamp: eager \| lazy` policy (default lazy) |
| `skillsmith pack [domain]` | Whole-pack design and build: one roster gate, a persisted `<pack>-spec.md` baton, staged multi-session builds above 3 members, plugin prep on request |

| In-request switch | Effect |
|---|---|
| "just build it" / "apply all" | Skips the single approval gate (design catalog or audit findings) |
| "keep going" (at a pack build's continuation offer) | Runs integrate with approval carried over — no second gate |
| A profile name ("standard profile", "standalone") | Overrides the pack's declared profile for that build |
| "pack \<name\>" (+ profile for a new pack) | Targets or registers a pack at build time; members ship a stamped `references/pack.md` |
| "plugin target" / "ship as a plugin" (packs) | Additionally packages the pack as a Claude Code plugin repo (plugin.json + `skills/`, optional `.mcp.json`), marketplace-registerable — `.skill` stays the default |

## Staying current

Two volatile surfaces, declared in `metadata.volatile`. `references/rubrics.md` is **calendar** (60-day) — **"skillsmith refresh"** re-verifies the best-practices baseline against its canonical sources, patch-bumps, and repackages. `references/pack-registry.md` is **event-driven** — restamped only when pack membership or structure changes (via `skillsmith integrate`), never on a clock. Everything else is durable doctrine.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
