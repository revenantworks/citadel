# revenant-foundation-rigwright

**What separates it from its neighbors:** every other tool in this space generates a config. rigwright decides *which layer the rule belongs in first*, and can score a config you already have without rewriting it. `/init` will write you a CLAUDE.md; it will not tell you that four of your rules are unenforceable as prose and belong in a hook, or that a fifth is paying context rent on every session to say something that mattered twice.

The rig is everything Claude reads before the work starts — standing instructions and files a session opens with, whether you remember they are there or not. rigwright authors that layer and audits it when it has silted up.

## Package

```
revenant-foundation-rigwright/
├── SKILL.md
├── README.md · CHANGELOG.md · SOURCES.md · LICENSE
├── references/
│   ├── surface-notes.md        # volatile, 60-day — per-surface fields, caps, load semantics
│   └── artifact-templates.md   # emit shapes + validation checklists
└── evals/
    ├── trigger-evals.md        # 20 cold routing queries
    └── test-cases.md           # 14 assertion cases
```

## Install

**claude.ai** — Settings → Capabilities → Skills, upload the zip.
**Claude Code** — the foundation plugin carries it; or drop the folder in `~/.claude/skills/`.

## Entry points

| Invocation | Does |
|---|---|
| *(default)* | Builds the config from intent — Project instructions, knowledge-file plan, CLAUDE.md, `.claude` layout, `.mcp.json` |
| `rigwright audit` | Scores an existing config on placement, budget, enforceability, rot, coverage. Reports, never rewrites |
| `rigwright refresh` | Re-verifies `surface-notes.md` against current docs, restamps that file only |
| *(bare placement question)* | "Where should this rule live?" — answered from the layer stack, no build |

## The layer stack

Seven homes for a rule, one question deciding between them: how often is it true, and can the model be trusted to follow it? Profile preferences · Project instructions · Project knowledge files · `CLAUDE.md` · a skill · a hook or permission rule · auto-memory. The stack lives in `SKILL.md` and loads with the body — a rule whose threshold sits in an unloaded file is not a rule.

## Boundaries

Attended config is rigwright's. Anything firing on a schedule or an event with no human reading the result is **agentwright's**, whole — including a desktop scheduled task, which is stored on disk as a `SKILL.md` and is still not a skill. A genuine Agent Skill package is **skillwright's**. Instruction wording, once its home and budget are settled, is **promptwright's**. Trimming an artifact for cost rather than placement is **tokenwright's**. Brand and voice on anything emitted here is **brandwright apply**, on invoke — rigwright emits spec-clean neutral.

## Staying current

`surface-notes.md` carries a 60-day stamp and is the only file that ages. `rigwright refresh` re-verifies it; `skillwright upkeep` sweeps it with the rest of the pack via the `metadata.volatile` block. Rows are marked `[published]` or `[reported]` — reported figures are guidance and are never validated against as hard limits.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
