# revenant-foundation-loresmith

Research that ends in something usable. What separates it from research-report tools: **verdict mode** ends in one direct recommendation — criteria intake, live primary-source verification, a comparison where every cell wears an evidence tag ([documented] / [vendor-reported] / [estimate] / [unverified]), and the flip condition that would change the pick; **playbook mode** maintains living reference docs — template-first, answer up front, versioned, re-verified on every touch, consolidated instead of duplicated. No reports, no walls of findings, zero scripts — identical on claude.ai, Claude Code, and the API.

**Workflow:** Intake → Criteria / Template → Live verification → Product → Handback

## Package contents

```
revenant-foundation-loresmith/
├── SKILL.md                      # entry point — two modes, doctrines, restraint
├── README.md · LICENSE · CHANGELOG.md · SOURCES.md
├── references/
│   ├── verdict-mode.md           # criteria → verification → one recommendation
│   ├── playbook-mode.md          # template-first living reference docs
│   └── pack.md                   # foundation-pack advisory manifest (stamped)
└── evals/                        # in full folder-zips, excluded from .skill
    ├── trigger-evals.md
    └── test-cases.md
```

## Install

Follows the [Agent Skills](https://agentskills.io/) open standard. Drop the folder into your skills directory or upload the archive in Claude settings.

## Entry points

| Entry | What it does |
|---|---|
| **verdict** | Pick/compare/worth-it → tagged comparison → one recommendation + flip condition |
| **playbook** | Reference doc → template gate → answer-up-front fill → verification pass → versioned file |

## Commands & switches

| Invocation | What it does |
|---|---|
| `loresmith` | Bare invocation — capability line, then asks what to decide or document |
| `loresmith verdict` | Forces verdict mode |
| `loresmith playbook` | Forces playbook mode |

| In-request switch | Effect |
|---|---|
| "just write it" / "apply all" | Skips the template/criteria gate |
| naming an existing doc | Consolidation path — extend and re-version instead of new doc |

## Staying current

Nothing baked to go stale: every run verifies live and dates its checks; playbooks carry their own verified-date stamps and re-verify touched sections on update. If search is unavailable, products ship marked provisional with everything tagged [unverified] — never silently confident.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
