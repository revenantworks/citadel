# revenant-foundation-commwright

Shapes any message to its channel and audience — one in, the right form out. What separates it from channel-specific writers and send-integrations: **seven channel profiles with hard form contracts** (tone register, length ceiling, structure, subject/title rules), a **humanized default register** on every draft (no em/en dashes, no emoji, no AI tells), a **neutral professional default** with a specific brand voice applied only when named (voice definitions live in brandwright), **strategy-labeled variants only when stakes compete**, **dated cadence sets** for releases, **message drift audits** against the channel contracts (report only), and a **pre-publish redaction sweep** on anything public-bound. It never sends (delivery stays with your surface's own tools), and it runs zero scripts, so it behaves identically on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Resolve channel *(+ any named voice)* → Draft *(humanized, always)* → Pre-publish hygiene → Output

Humanize is the register commwright writes in, not a mode you switch on: every draft already obeys it, silently. Em dashes and en dashes are out in any role (hyphens inside compound words stay), emoji are zero by default on every channel including Slack and Discord, and the usual machine tells (preamble, recap close, trailing help offer, hedge stacking, agentless passives, the lexicon smells) are absent before you see the draft. You can ask for emoji on a specific message and it complies; that override covers that message only and is never sticky. Channel contracts still win: a length ceiling or a profile's required structure outranks the register. Humanize is a register, never a voice — it defines and saves nothing.

## Package contents

```
revenant-foundation-commwright/
├── SKILL.md                      # entry point — turn shape, hard rules H1-H9, entries, load budget
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── channel-profiles.md       # the seven form contracts (event-driven; loaded per draft)
│   ├── humanize.md               # the deep tell catalog, lexicon, worked repairs (not a per-draft load)
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # should/shouldn't queries
    ├── test-cases.md             # assertion suite
    ├── RESULTS.md                # dated trigger-eval run log
    └── fixtures/                 # three cold-run inputs: the neutral voice-profile
                                  #   stand-in (6/7/19) and the Case 4 / Case 26 sources
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings. Trigger it by asking to write, reshape, humanize, or audit a message, or by saying `commwright` (subcommands: `commwright formats`, `commwright audit`, `commwright humanize`).

## Entry points

| Entry | What it does |
|---|---|
| **build** | Message from intent — resolve channel, draft to the contracts in the neutral default voice (or a named voice if handed in) |
| **reshape** | Existing message → new channel or register; facts frozen |
| **humanize** | "strip the AI tells" on text you hand in — removes the tells the hard rules and the catalog name and nothing else; facts frozen as in Reshape, the writer's own quirks kept except their em dashes and emoji, which H1 and H2 remove and the report line names; closing report line of what came out and what was kept on purpose |
| **formats** | List the channel profiles and their contracts, no draft |
| **audit** | "commwright audit" at a message or comms set → six contract areas scored plus AI-tell density, drift catalog with exact fixes; report only — rewrites run through Reshape on approval |

Humanize is the default on everything Build and Reshape produce; the explicit entry exists for text that arrives from somewhere else. A specific brand **voice** is applied only when named for the message or handed in as a brandwright voice-profile export — commwright consumes that profile, it never defines or stores one. Humanize is not a voice and never becomes one: asking to define or save a way of writing routes to brandwright.

## Commands & switches

| Invocation | What it does |
|---|---|
| `commwright` | Bare invocation — capability line, then asks what to shape |
| `commwright formats` | Compact table of channel profiles |
| `commwright audit` | Drift report against the channel contracts and any applied voice, AI-tell density included — P0 for firewall breaches or unredacted secrets; report only |
| `commwright humanize` | Strips the AI tells out of text you hand in, facts frozen; also fires on "humanize this" / "strip the AI tells" |

| In-request switch | Effect |
|---|---|
| "variants" / competing stakes present | 2–3 strategy-labeled drafts instead of one |
| a named voice (+ its brandwright export) | Applies that voice for this message, subject to the identity firewall |
| "comms plan" / "release comms" | Dated cadence set instead of a single message |
| asking for emoji on a message | Emoji allowed on that message only, exactly what was asked for — per-message, never sticky, never inferred |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/channel-profiles.md` is **event-driven** — the per-channel registers and length contracts are restamped when a platform's conventions visibly change (ask for a channel-profile update in an ordinary request), never on a clock. Voice is not stored here — those definitions live in brandwright. Everything else is durable doctrine, `humanize.md` included.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
