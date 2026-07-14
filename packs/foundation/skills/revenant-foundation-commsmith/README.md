# revenant-foundation-commsmith

Shapes any message to its channel, audience, and voice — one in, the right form out. What separates it from channel-specific writers and send-integrations: **seven channel profiles with hard form contracts** (tone register, length ceiling, structure, subject/title rules), **saved voices with a professional/persona firewall**, **strategy-labeled variants only when stakes compete**, **dated cadence sets** for releases, **message drift audits** against the channel contracts (report only), and a **pre-publish redaction sweep** on anything public-bound. It never sends — delivery stays with your surface's own tools — and it runs zero scripts, so it behaves identically on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Resolve channel + voice → Draft → Pre-publish hygiene → Output

## Package contents

```
revenant-foundation-commsmith/
├── SKILL.md                      # entry point — turn shape, four entries, load budget
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── channel-profiles.md       # the seven form contracts (loaded per draft)
│   ├── voices.md                 # VOLATILE — saved voices; "commsmith voice" rewrites it
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # excluded from .skill payloads
    ├── trigger-evals.md          # 22 should/shouldn't queries
    └── test-cases.md             # assertion suite
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings.

## Entry points

| Entry | What it does |
|---|---|
| **build** | Message from intent — resolve channel + voice, draft to the contracts |
| **reshape** | Existing message → new channel or register; facts frozen |
| **voice** | Save, apply, or list voices; neutral professional default; identity firewall |
| **formats** | List the channel profiles and their contracts, no draft |
| **audit** | "commsmith audit" at a message or comms set → six contract areas scored, drift catalog with exact fixes; report only — rewrites run through Reshape on approval |

## Commands & switches

| Invocation | What it does |
|---|---|
| `commsmith` | Bare invocation — capability line, then asks what to shape |
| `commsmith voice` | Save/apply/list voice profiles (rewrites `references/voices.md` only) |
| `commsmith formats` | Compact table of channel profiles |
| `commsmith audit` | Drift report against the channel contracts and the applied voice — P0 for firewall breaches or unredacted secrets; report only |

| In-request switch | Effect |
|---|---|
| "variants" / competing stakes present | 2–3 strategy-labeled drafts instead of one |
| a voice name | Applies that saved or handed-in voice for this message |
| "comms plan" / "release comms" | Dated cadence set instead of a single message |

## Staying current and staying yours

One volatile surface: `references/voices.md`, rewritten by "commsmith voice". Channel norms drift slowly; when a platform's conventions visibly change, ask for a channel-profile update in an ordinary request — the profiles are durable guidance, not a stamped baseline.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
