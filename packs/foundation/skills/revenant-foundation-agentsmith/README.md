# revenant-foundation-agentsmith

Designs and audits the system around an autonomous agent — everything but the prompt text. What separates it from guardrail platforms and security harnesses: it's a portable **doctrine skill** — a ten-area checklist (cadence, soft/hard guardrail tiers, kill-switch layers, protected resources, handoff schemas, output contracts, zero-signal rule, failure/retry, injection hygiene, trust tiers) that emits a complete **ops spec** for a new agent or a **scored audit** of an existing one, sized to the agent's blast radius. Runtime enforcement stays with your platform; code-level threat review stays with a security harness — agentsmith is the design layer that decides what those must enforce. It runs zero scripts, so it behaves identically on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Blast radius → Checklist pass → Ops spec / scoreline → Handback

## Package contents

```
revenant-foundation-agentsmith/
├── SKILL.md                      # entry point — two modes, trust tiers, restraint
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── design-checklist.md       # the ten control areas (loaded every run)
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # should/shouldn't queries
    └── test-cases.md             # assertion suite
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to design or audit an agent, bot, or scheduled automation, or by saying `agentsmith` (subcommand: `agentsmith audit`).

## Entry points

| Entry | What it does |
|---|---|
| **design** | New agent from intent → blast radius → ten-area ops spec, one gate |
| **audit** | "agentsmith audit" at an existing agent/spec → 1–10 per area, finding catalog (P0/P1/P2), one gate |

## Commands & switches

| Invocation | What it does |
|---|---|
| `agentsmith` | Bare invocation — capability line, then asks what agent to spec or audit |
| `agentsmith audit` | Points the checklist at an existing agent, prompt, or spec |

| In-request switch | Effect |
|---|---|
| "apply all" / "just spec it" | Skips the single gate |
| naming a checklist area | Scopes the run to that area only (spot-check) |

## Staying current

No volatile surface (`metadata.volatile: []`). The ten-area checklist encodes durable control doctrine, not facts that age on a clock, so there is nothing to refresh and `skillsmith upkeep` skips it. When the pack's audit norms move, audits inherit them through the pack.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
