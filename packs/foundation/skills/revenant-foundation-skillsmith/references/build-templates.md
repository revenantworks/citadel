# Build Templates — Skeletons, Naming, Suites

Read on every build. Skeletons are starting points, not quotas — include only what the built skill's job needs.

## Contents

- Naming render rules
- Frontmatter skeleton
- Package layout skeleton
- Plugin target — optional, packs
- File stubs (README · CHANGELOG · SOURCES)
- Suites & composition
- Gold standard
- Pack-time checklist

---

## Naming render rules

Template: **`<brand>-<pack>-<skill>`** — three segments from `pack-registry.md` (brand) + the pack registry (pack) + the build (skill). Render lowercase, hyphens only, no leading/trailing/consecutive hyphens. **64-char guard:** if the rendered name exceeds 64 chars, warn and propose a shorter skill segment or pack token before proceeding — never silently truncate. Unbranded (neutral) builds drop brand and pack and use a plain descriptive skill name, gerund form preferred (e.g. `auditing-contracts`). The folder name always equals the rendered `name` exactly.

## Frontmatter skeleton

```yaml
---
name: <rendered-name>
description: <what + when, third person, ≤1024 chars — see description-crafting.md>
license: <from pack-registry, default MIT>
metadata:
  version: "1.0.0"
  profile: <standalone | standard | custom:<pack-policy>>
  pack: <pack name, omit when neutral>
  brand: <brand token, omit when neutral>
# standard/custom profiles with dependencies also declare:
# compatibility: <tools, packages, per-surface notes, sibling skills + absence behavior>
---
```

## Package layout skeleton

```
<rendered-name>/
├── SKILL.md            # lean body: workflow, entry points, load budget, turn shape
├── README.md           # humans: what it is, differentiators, install, staying current
├── CHANGELOG.md        # born at 1.0.0, features-and-differentiators entry
├── SOURCES.md          # where the guidance comes from; verification pointers
├── LICENSE
├── references/         # runtime, loaded per a declared load budget; TOC on long files
│   └── <domain>.md     # volatile facts isolated in stamped single-update-surface files
├── scripts/            # standard/custom profiles only — each states run-vs-read
└── evals/              # trigger-evals.md + test-cases.md; excluded from .skill payloads
```

Small skills legitimately collapse to `SKILL.md` + LICENSE (+ evals). Add layers only when the body would otherwise pass ~300 lines or mix mutually exclusive contexts.

## Plugin target — optional, packs

`.skill` is the default delivery for every build. On request, a pack can *additionally* ship as a Claude Code plugin repo — marketplace-registerable, one slash namespace per pack. Format verified against the plugin docs (code.claude.com/docs/en/plugins), 2026-07-12:

```
<pack>/                          # plugin repo root — manifest name = slash namespace
├── .claude-plugin/
│   └── plugin.json              # {"name","description","version","author"} — ONLY this file lives here
├── skills/                      # every other component sits at repo root, never inside .claude-plugin/
│   ├── <rendered-name>/         # each pack member unchanged: SKILL.md (+ references/) — model-invoked
│   └── <workflow>/              # explicit workflow: SKILL.md with disable-model-invocation: true,
│                                #   invoked as /<pack>:<workflow>; $ARGUMENTS supported
└── .mcp.json                    # optional — bundled MCP servers (standard/custom profiles only, declared)
```

- **Two kinds of entries, one directory.** Auto-loaded domain knowledge is a normal skill; an explicit slash-command workflow is a skill with `disable-model-invocation: true`. That flag is the current format's "command" — the legacy flat-file `commands/` layout still loads, but the docs point new plugins at `skills/`. A pack's capstone orchestration prompt maps to a workflow entry (e.g. `/foundation:forge-run`).
- **Version:** set `version` in plugin.json explicitly, matching the pack release — omitted, every git commit counts as a new version.
- **Distribution:** any git repo installs directly; a self-hosted marketplace adds `.claude-plugin/marketplace.json`; community-directory listing goes through clau.de/plugin-directory-submission — run `claude plugin validate` before submitting.
- **The target wraps, never rewrites.** Member skills keep their own frontmatter, profiles, and evals; the `.skill` and full-zip artifacts still ship alongside the plugin repo.

## File stubs

**README** — opening paragraph leads with what separates it from neighbors, then: package tree, install, entry points, commands & switches (when the skill defines named invocations or in-request switches — one table, one row each; never a separate commands file), how it stays current, changelog link. **CHANGELOG** — Keep a Changelog + SemVer header; single `[1.0.0] — <date>` entry listing features and differentiators; "Released under the <license>." close. **SOURCES** — one table per guidance area mapping claims to primary sources, with a verified-as-of stamp and re-check pointers.

## Suites & composition

A pack may ship several skills designed to work together. Rules for every suite build:

- **Declared siblings.** Each skill lists the pack siblings it references in `compatibility`/`metadata` and names them in its description or docs.
- **Absence behavior, stated.** For every sibling: degrade gracefully (skill still completes its core job alone) or hard-require (skill says it needs the sibling installed and stops cleanly). Silent coupling is a P0 audit finding.
- **Shared identity.** Siblings share brand + pack segments and the pack's profile unless a per-skill override is deliberate and documented.
- **Partitioned triggers.** Sibling descriptions must pass the discoverability test *as a set* — ten realistic pack-relevant requests route to the right sibling. Write the boundary sentences explicitly.
- **One delivery.** A suite packages as one archive containing each skill folder at root, plus a pack README naming the members and their contracts.

## Gold standard

The current `revenant-foundation-promptsmith` release is the reference implementation for standalone-profile builds: lean SKILL.md with a declared load budget, turn-shape rules including the tool-list test, volatile facts behind a stamped snapshot with a refresh phrase, `references/` + `evals/` split, assertion-only test suite, changelog born at 1.0.0. Pattern outputs on it; don't copy its domain content.

## Pack-time checklist

- Folder name == frontmatter name; name ≤64, lowercase-hyphen
- Description ≤1024, third person, what + when; discoverability test passes
- SKILL.md ≤500 lines; long references carry TOCs; links one level deep
- Profile declared; every dependency declared; absence behavior stated where relevant
- Volatile facts stamped; no rot outside stamped files; no Windows paths
- evals/ present (or absence justified); brand cascade applied or `brand: neutral` honored
- Named commands and in-request switches surfaced in the README table when any exist
- CHANGELOG at 1.0.0; LICENSE present; zip archives everything, .skill excludes evals/
- Plugin target (only when requested): plugin.json parses and its name is the pack namespace; components at repo root; workflows carry `disable-model-invocation: true`; `.skill` + zip still emitted
