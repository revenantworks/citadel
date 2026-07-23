# revenant-foundation-commsmith

Shapes any message to its channel and audience — one in, the right form out. What separates it from channel-specific writers and send-integrations: **seven channel profiles with hard form contracts** (tone register, length ceiling, structure, subject/title rules), a **neutral professional default** with a specific brand voice applied only when named (voice definitions live in brandsmith), **strategy-labeled variants only when stakes compete**, **dated cadence sets** for releases, **message drift audits** against the channel contracts (report only), and a **pre-publish redaction sweep** on anything public-bound. It never sends — delivery stays with your surface's own tools — and it runs zero scripts, so it behaves identically on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Resolve channel *(+ any named voice)* → Draft → Pre-publish hygiene → Output

## Package contents

```
revenant-foundation-commsmith/
├── SKILL.md                      # entry point — turn shape, entries, load budget
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── channel-profiles.md       # the seven form contracts (event-driven; loaded per draft)
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # should/shouldn't queries
    └── test-cases.md             # assertion suite
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to write, reshape, or audit a message, or by saying `commsmith` (subcommands: `commsmith formats`, `commsmith audit`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Message from intent — resolve channel, draft to the contracts in the neutral default voice (or a named voice if handed in) |
| **reshape** | Existing message → new channel or register; facts frozen |
| **formats** | List the channel profiles and their contracts, no draft |
| **audit** | "commsmith audit" at a message or comms set → six contract areas scored, drift catalog with exact fixes; report only — rewrites run through Reshape on approval |

A specific brand **voice** is applied only when named for the message or handed in as a brandsmith voice-profile export — commsmith consumes that profile, it never defines or stores one.

## Commands & switches

| Invocation | What it does |
|---|---|
| `commsmith` | Bare invocation — capability line, then asks what to shape |
| `commsmith formats` | Compact table of channel profiles |
| `commsmith audit` | Drift report against the channel contracts and any applied voice — P0 for firewall breaches or unredacted secrets; report only |

| In-request switch | Effect |
|---|---|
| "variants" / competing stakes present | 2–3 strategy-labeled drafts instead of one |
| a named voice (+ its brandsmith export) | Applies that voice for this message, subject to the identity firewall |
| "comms plan" / "release comms" | Dated cadence set instead of a single message |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/channel-profiles.md` is **event-driven** — the per-channel registers and length contracts are restamped when a platform's conventions visibly change (ask for a channel-profile update in an ordinary request), never on a clock. Voice is not stored here — those definitions live in brandsmith. Everything else is durable doctrine.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
