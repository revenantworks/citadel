# revenant-foundation-skillsmith

Builds, audits, brands, and ports Agent Skills — from a one-line intent to a packaged, install-ready skill or multi-skill pack. What separates it from skill scaffolders and creators: every build starts with fresh best-practices research and a **niche verdict** (should this skill exist, and against which incumbents — checked against the live skill registries and plugin directories, not vibes), constructs to a declared **policy profile** rather than one-size rules (standalone by default: self-contained, lean, self-updating — but packs may allow tools, scripts, and sibling skills, all declared), applies a **universal brand system** that cascades the configured identity onto everything it creates, and ships every skill **born testable** — trigger evals and an assertion suite in the box. It runs zero scripts of its own, so it behaves identically on claude.ai, Claude Code, and the API.

**Build workflow:** Intent → Pack & profile → Research → Niche verdict → Design catalog *(one gate)* → Build → Self-audit → Package

Interaction contract: one complete catalog, one approval gate, no drip-feed iteration.

---

## Package contents

```
revenant-foundation-skillsmith/
├── SKILL.md                      # entry point — workflow, four entry points, load budget, turn shape
├── README.md                     # this file
├── LICENSE                       # MIT
├── CHANGELOG.md                  # version history
├── SOURCES.md                    # where the guidance comes from
├── references/                   # runtime — loaded per the SKILL.md load budget
│   ├── rubrics.md                # Rubric A baseline (stamped, refresh target) + policy profiles
│   ├── build-templates.md        # skeletons, naming render, suites & composition, gold standard
│   ├── brand-config.md           # VOLATILE — the user's brand parameters; "skillsmith configure" rewrites it
│   ├── brand-inheritance.md      # durable cascade rules: config → built skills
│   ├── description-crafting.md   # trigger writing, boundary sentences, discoverability test
│   ├── eval-authoring.md         # trigger evals + assertion suites for built skills
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # maintenance / QA assets — excluded from .skill payloads
    ├── test-cases.md             # 28-case assertion-only regression suite
    └── trigger-evals.md          # 26 should/shouldn't-trigger queries
```

---

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your platform's skills directory, or upload the archive in Claude settings. Trigger it by asking to build, audit, score, or package a skill, or by saying `skillsmith` (subcommands: `skillsmith configure`, `skillsmith refresh`, `skillsmith integrate`, `skillsmith pack`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Intent → research → niche verdict → one design catalog + gate → package → self-audit → handback |
| **audit** | Point at any existing skill: dual scoring (best practices + its declared profile), niche verdict, one fix catalog + gate, one consolidated rewrite |
| **configure** | Set the brand and naming for your org — brand token, pack registry with profiles, palette role tokens, voice, license. Rewrites `brand-config.md` only and hands the skill back. Ships neutral until configured |
| **refresh** | Re-verifies the best-practices baseline against canonical sources; regenerates only the stamped section |
| **port** | Point at an existing skill set + a target: identity-scrubbed, renamed, re-verified copy with a PORT-REPORT — source never modified |
| **integrate** | Propagate a new or changed member across its pack: registry row, capstone roster line, `pack.md` restamp ×N, packages rebuilt per policy, repo-sync bundle + upload checklist. Offered as "keep going" after every pack build |
| **pack** | Design and build a whole pack from a domain or role: capability map with adopt-don't-build tiers → one roster gate (trigger-partition table, session plan) → staged builds → set discoverability test → integrate → optional plugin/marketplace prep |

## Commands & switches

Named invocations — everything else routes on natural requests ("build me a skill that…", "audit this SKILL.md"):

| Invocation | What it does |
|---|---|
| `skillsmith` | Bare invocation — capability line, then asks what to build or check |
| `skillsmith configure` | Set or change the brand system (brand token, pack registry, palette roles, voice, license, wordmark). Rewrites `references/brand-config.md` only |
| `skillsmith refresh` | Re-verify the best-practices baseline in `references/rubrics.md`; patch bump + repackage. Run at the 60-day stamp or when the skill format changes |
| `skillsmith port` | Re-issue a skill set for a new owner, brand, or purpose — sanitize sweep + rename + stale-ref refresh + PORT-REPORT; the source set is never modified |
| `skillsmith integrate [member]` | One-operation pack propagation with all-or-notes integrity and a count check; blast radius per the pack's `restamp: eager \| lazy` policy (default lazy) |
| `skillsmith pack [domain]` | Whole-pack design and build: one roster gate, a persisted `<pack>-spec.md` baton, staged multi-session builds above 3 members, plugin prep on request |

| In-request switch | Effect |
|---|---|
| "just build it" / "apply all" | Skips the single approval gate (design catalog or audit findings) |
| "keep going" (at a pack build's continuation offer) | Runs integrate with approval carried over — no second gate |
| `brand: neutral` | Drops brand naming, palette, and wordmark for that build only |
| A profile name ("standard profile", "standalone") | Overrides the pack's declared profile for that build |
| "pack \<name\>" (+ profile for a new pack) | Targets or registers a pack at build time; members ship a stamped `references/pack.md` |
| "plugin target" / "ship as a plugin" (packs) | Additionally packages the pack as a Claude Code plugin repo (plugin.json + `skills/`, optional `.mcp.json`), marketplace-registerable — `.skill` stays the default |

## Staying current and staying yours

Two volatile surfaces, one phrase each: **"skillsmith refresh"** keeps the best-practices baseline honest (60-day staleness rule), and **"skillsmith configure"** re-brands the whole system for a new user or organization — everything it builds afterward inherits the new identity automatically. Per-build `brand: neutral` produces spec-clean unbranded output regardless of configuration.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
