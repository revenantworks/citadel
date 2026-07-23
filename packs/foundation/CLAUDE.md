# Foundation Pack — router & conventions

The always-on companion to the **foundation** pack's eight smiths. Each skill routes on its own description when invoked; this file is the standing context that makes them work *together* — so the right smith gets reached for without being named, and the pack's conventions hold across a session.

**Using it:** copy into your project root as `CLAUDE.md` (or into `~/.claude/CLAUDE.md` to cover every project) so Claude Code loads it automatically. It also loads on its own when you work under `packs/foundation/` in the citadel repo. It is not a skill — nothing here is invoked; it is context.

## Reaching for the right smith

| The task | Smith | Say |
|---|---|---|
| Build, audit, port, or pack a skill | **skillsmith** | "build / audit a skill", `skillsmith` |
| Write, fix, or score a prompt | **promptsmith** | "write / improve a prompt", `promptsmith` |
| Which model or tier to run a task on | **promptsmith** | `promptsmith model` |
| Shape a message to a channel | **commsmith** | "rewrite this for &lt;channel&gt;", `commsmith` |
| Design or audit an autonomous agent | **agentsmith** | "guardrails / kill switch for my agent", `agentsmith` |
| A researched verdict or a reference doc | **loresmith** | "which X should I pick", "playbook for Y" |
| Define, apply, or audit a brand or voice | **brandsmith** | `brandsmith build / apply / audit` |
| Author or audit an eval suite | **evalsmith** | "write trigger evals for &lt;target&gt;" |
| Slim, budget, or audit token footprint | **tokensmith** | "slim this / what does it cost" |

Each works alone. Initial routing is at the description level — this table is the proactive cue, not a dependency; an uninstalled smith is named, never a blocker.

## How they compose

- **skillsmith builds neutral → brandsmith brands it.** A built skill carries only its structural identity; palette, voice, and wordmark are applied by `brandsmith apply`. brandsmith is the single door for *all* brand output — no other smith styles its own.
- **skillsmith → evalsmith for suites.** When evalsmith is installed it authors a built skill's `evals/`; skillsmith's own generator is the stated fallback.
- **promptsmith owns model data.** For the tier + model to run a task on, `promptsmith model`; every other smith reasons in tier names (frontier / flagship / balanced / fast) and defers here for the current specifics.
- **skillsmith upkeep sweeps freshness.** `skillsmith upkeep` reads every member's `metadata.volatile` and flags calendar surfaces past their 60-day window, refreshing the approved ones through each owner's refresh verb.
- **loresmith decides; the others build.** A sourced "which should I pick" is loresmith's verdict — distinct from promptsmith's model pick and skillsmith's niche verdict.

## Conventions

- **Neutral by default.** Every smith outputs spec-clean; brand is an opt-in `brandsmith apply` layer, never baked in.
- **One catalog, one gate.** Decisions are presented complete, once; "just do it" / "apply all" skips the gate. No drip-feed.
- **Audits report; they don't rewrite.** A finding catalog lands fixes only on approval.
- **Declared dependencies.** Any tool or sibling a skill needs is named, with its absence behavior stated — the pack degrades gracefully, never fails silently.
- **Volatile surfaces are stamped and swept.** Calendar baselines carry a date and a 60-day cadence; `skillsmith upkeep` is the pack-wide check.
