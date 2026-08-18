# revenantworks-foundation-agentwright

Designs and audits the system around an autonomous agent — everything but the prompt text. It is
a portable **doctrine skill**: a ten-area checklist (cadence, soft/hard guardrail tiers,
kill-switch layers, protected resources, handoff schemas, output contracts, zero-signal rule,
failure/retry, injection hygiene, trust tiers). That checklist produces a complete **ops spec**
for a new agent, or a **scored audit** of an existing one, sized to the agent's blast radius. It
then **renders that spec into the surface that actually runs it**, naming every control the
target cannot enforce — never emitting something that only looks safe. This is what separates it
from guardrail platforms and security harnesses. Runtime enforcement stays with your platform.
Code-level threat review stays with a security harness. agentwright is the design layer that
decides what those must enforce. It runs zero scripts, so it behaves identically on claude.ai,
Claude Code, and the API.

**Workflow:** Intake → Blast radius → Checklist pass *(design or audit)* → Ops spec / scoreline → *(optional)* Emit to target → Handback

## Package contents

```
revenantworks-foundation-agentwright/
├── SKILL.md                      # entry point — five entries, invocation surface, trust tiers, restraint
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── design-checklist.md       # the ten control areas (loaded on every design and audit)
│   ├── security-scan-doctrine.md # the five runtime security classes (loaded on a security-scan; durable, unstamped)
│   ├── platform-notes.md         # calendar-volatile, stamped — what platforms provide to enforce the checklist (loaded when a run names a platform mechanism)
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # should/shouldn't queries
    └── test-cases.md             # assertion suite
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to design or audit an agent, bot, or scheduled automation, or by saying `agentwright` (subcommands: `agentwright emit`, `agentwright audit`, `agentwright security-scan`, `agentwright refresh`).

## Entry points

| Entry | What it does |
|---|---|
| **design** | New agent from intent → blast radius → ten-area ops spec, one gate |
| **emit** | "agentwright emit", or any request to turn a design into the thing that runs → resolves the target surface, renders the spec into its native fields, states the enforcement gap for every control that surface can't hold, and carries the three invariants no scheduler's form asks for (zero-signal line, first actionable fire, missed-run behavior). Hands back paste-ready; never creates, enables, or commits. Arriving with no spec runs design first and emits from it, gated once |
| **audit** | "agentwright audit" at an existing agent/spec → 1–10 per area, finding catalog (P0/P1/P2), one gate |
| **security-scan** | "agentwright security-scan" at an agent, spec, or live config → the five runtime classes (tool-grant scope, untrusted-content flow, guardrails/kill switches, credentials, failure-as-exposure), scored on the same 1–10 scale, same catalog shape, one gate |
| **refresh** | Re-verifies `platform-notes.md` against current platform docs; regenerates only that stamped file |

## Commands & switches

*Mirror only — the invocation surface is stated in `SKILL.md` (Turn shape 4) and binds from there whether or not this file is read. This table is the copy, never the source.*

| Invocation | What it does |
|---|---|
| `agentwright` | Bare invocation — capability line plus a question about what agent to spec or audit, ≤3 sentences, no spec |
| `agentwright emit` | Renders an ops spec — this run's or one handed in — into a target surface's native form, with the enforcement gap stated |
| `agentwright audit` | Points the checklist at an existing agent, prompt, or spec |
| `agentwright security-scan` | Scores the runtime permission surface — what the agent may do when it runs — against the five security classes |
| `agentwright refresh` | Re-verify the platform-notes baseline (enforcement surfaces, schedulers, kill-switch state); patch bump + repackage. Run at the 60-day stamp |

| In-request switch | Effect |
|---|---|
| "apply all" / "just spec it" | Skips the single gate |
| naming a checklist area | Spot-check — that one area in full, none of the other nine |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/platform-notes.md` is **calendar** (60-day) — what current platforms provide to enforce the checklist (permission/hook/sandbox layers, schedulers, kill-switch and injection state) plus the seven emit targets with their triggers, scope control, gate, kill switch and isolation, re-verified by `agentwright refresh`. Non-Anthropic rows carry **per-row stamps**, so a refresh re-stamps only what it actually reached rather than restamping an unchecked row. The ten-area checklist itself is durable control doctrine and never restamped; `skillwright upkeep` sweeps the platform notes with the pack.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
