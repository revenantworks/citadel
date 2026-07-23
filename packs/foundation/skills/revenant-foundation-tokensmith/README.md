# revenant-foundation-tokensmith

Every token-saver in the ecosystem optimizes the *session* — hooks that track file reads, personas that talk terse, compaction managers, delegation routers. tokensmith works the lane none of them hold: the **artifacts themselves**. Point it at a prompt, a SKILL.md, an agent spec, a CLAUDE.md, a reference doc — it measures the footprint honestly (method named, error band shown), diagnoses waste against a ten-code taxonomy, and rewrites leaner under a preservation contract that keeps every stated behavior intact. Build-time only, zero scripts, zero runtime dependency: what it slims runs anywhere, with tokensmith long gone.

What separates it from the neighbors it was researched against (2026-07-13): session trackers and setup auditors are platform-bound and hook-driven — tokensmith is portable text doctrine. Terseness personas cut *output* at a legibility cost tokensmith explicitly refuses for instruction artifacts. Context-engineering curricula teach agent architecture — tokensmith is a worker that hands back a measured, slimmer file. The single-artifact SKILL.md optimizers come closest and stop at one file type; tokensmith covers the artifact class, adds score-only audits (pack check C-1), budget sheets for whole sets, and cache-aware structure with the arithmetic shown.

**Workflow:** Intake → Measure → Diagnose (waste taxonomy) → Slim / Audit / Budget → Re-measure → Handback

## Package contents

```
revenant-foundation-tokensmith/
├── SKILL.md                      # lean body: workflow, four entries, turn shape, load budget
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── measurement.md            # calendar-volatile, stamped — ratios, cache mechanics, platform points
│   ├── waste-taxonomy.md         # durable — W-codes, technique ladder, contract, report formats
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md          # should/shouldn't queries
    └── test-cases.md             # assertion suite
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Upload the folder-zip on claude.ai (Settings → Capabilities → Skills), or place the folder in your skills directory on Claude Code. Trigger it by asking to slim, score, or budget an artifact, or by saying `tokensmith` (subcommands: `tokensmith audit`, `tokensmith budget`, `tokensmith refresh`). Standalone profile: web search for Refresh, native file tools for delivery, graceful in-chat fallback where absent.

## Entry points

| Entry | What it does |
|---|---|
| **slim** *(default)* | artifact + intent to shrink → measure → ladder pass → gated lossy catalog if needed → re-measure → report + rewritten artifact |
| **audit** *(score-only, C-1)* | W-coded findings, recoverable estimate, efficiency score, verdict — nothing rewritten |
| **budget** | budget sheet over a set: tier table, ceilings, set-level always-on total, load order, cache plan |
| **refresh** | re-verify `measurement.md`'s baseline against primary sources; restamp; patch bump |

## Commands & switches

| Invocation | What it does |
|---|---|
| `tokensmith` | Bare invocation — one-line intro + what goes on the scale |
| `tokensmith audit` | Score-only efficiency audit (C-1) — nothing rewritten |
| `tokensmith budget` | Budget sheet over an artifact set |
| `tokensmith refresh` | Re-verify and restamp the measurement baseline |

| In-request switch | Effect |
|---|---|
| "just slim it" | Pre-approves **lossless rungs only** — rung 9 (lossy) always gates |
| `brand: <token>` / `brand: neutral` | Per-run report flavor; default is neutral (C-2), never touching the artifact's instruction content |

## Staying current

One volatile surface, declared in `metadata.volatile`: `references/measurement.md` is **calendar** (60-day) — the estimation ratios, cache rates, and platform reference points are re-verified against primary sources by `tokensmith refresh` (suggest at >60 days). Doctrine and taxonomy are durable.

## Changelog

See [CHANGELOG.md](CHANGELOG.md). Claims-to-sources in [SOURCES.md](SOURCES.md).
