# revenant-foundation-tokensmith

Every token-saver in the ecosystem optimizes the *session* — hooks that track file reads, personas that talk terse, compaction managers, delegation routers. tokensmith works the lane none of them hold: the **artifacts themselves**. Point it at a prompt, a SKILL.md, an agent spec, a CLAUDE.md, a reference doc — it measures the footprint honestly (method named, error band shown), diagnoses waste against a ten-code taxonomy, and rewrites leaner under a preservation contract that keeps every stated behavior intact. Build-time only, zero scripts, zero runtime dependency: what it slims runs anywhere, with tokensmith long gone.

What separates it from the neighbors it was researched against (2026-07-13): session trackers and setup auditors (alexgreensh/token-optimizer, egorfedorov/claude-context-optimizer) are platform-bound and hook-driven — tokensmith is portable text doctrine. Terseness personas (Caveman, rescue-tokens) cut *output* at a legibility cost tokensmith explicitly refuses for instruction artifacts. Context-engineering curricula (muratcankoylan's collection) teach agent architecture — tokensmith is a worker that hands back a measured, slimmer file. The single-artifact SKILL.md optimizers come closest and stop at one file type; tokensmith covers the artifact class, adds score-only audits (pack check C-1), budget sheets for whole sets, and cache-aware structure with the arithmetic shown.

## Package

```
revenant-foundation-tokensmith/
├── SKILL.md                      # lean body: workflow, four entries, turn shape, load budget
├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
├── references/
│   ├── measurement.md            # VOLATILE, stamped — ratios, cache mechanics, platform points
│   ├── waste-taxonomy.md         # durable — W-codes, technique ladder, contract, report formats
│   └── pack.md                   # foundation roster (advisory, generated from skillsmith's registry)
└── evals/                        # trigger-evals.md (20 queries) + test-cases.md (18 cases)
```

## Install

Upload the folder-zip on claude.ai (Settings → Capabilities → skills), or place the folder in your skills directory on Claude Code. Standalone profile: web search only, native file tools for delivery, graceful in-chat fallback where absent.

## Entry points, commands & switches

| Invocation | Does |
|---|---|
| *(default — artifact + intent to shrink)* | **Slim**: measure → ladder pass → gated lossy catalog if needed → re-measure → report + rewritten artifact |
| `tokensmith audit` | **Score-only** (C-1): W-coded findings, recoverable estimate, efficiency score, verdict — nothing rewritten |
| `tokensmith budget` | **Budget sheet** over a set: tier table, ceilings, set-level always-on total, load order, cache plan |
| `tokensmith refresh` | Re-verify `measurement.md`'s baseline against primary sources; restamp; patch bump |
| `tokensmith` *(bare)* | One-line intro + what goes on the scale |
| "just slim it" | Pre-approves **lossless rungs only** — rung 9 (lossy) always gates |
| `brand: <token>` / `brand: neutral` | Per-run report flavor; default is neutral (C-2). Never touches the artifact's instruction content |

## Staying current

`measurement.md` is the volatile surface — ratios, cache rates, platform reference points — stamped and re-verified by `tokensmith refresh` (suggest at >60 days). Doctrine and taxonomy are durable. History in [CHANGELOG.md](CHANGELOG.md); claims-to-sources in [SOURCES.md](SOURCES.md).
