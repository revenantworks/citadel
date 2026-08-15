# Foundation Pack — router & conventions

The always-on companion to the **foundation** pack's nine wrights. Each skill routes on its own description when invoked; this file is the standing context that makes them work *together*, so the right wright gets reached for without being named, and the pack's conventions hold across a session.

**Using it:** APPEND into your project root's `CLAUDE.md` (or into `~/.claude/CLAUDE.md` to cover every project) so Claude Code loads it automatically — both packs' routers can coexist in one file, and a copy would overwrite whichever router landed first. It also loads on its own when you work under `packs/foundation/` in the citadel repo. It is not a skill: nothing here is invoked; it is context.

## Reaching for the right wright

| The task | Wright | Say |
|---|---|---|
| Build, audit, port, or pack a skill, or a register pass on a skill's or pack's own files | **skillwright** | "build / audit a skill", "humanize / tighten this README", `skillwright` |
| Write, fix, or score a prompt | **promptwright** | "write / improve a prompt", `promptwright` |
| Which model or tier to run a task on — or a per-subtask target table for a whole plan | **promptwright** | `promptwright model`, "tier my plan" |
| Shape a message to a channel | **commwright** | "rewrite this for &lt;channel&gt;", `commwright` |
| Design or audit an autonomous agent | **agentwright** | "guardrails / kill switch for my agent", `agentwright` |
| Turn an agent spec into the thing that actually runs it | **agentwright** | "make this a weekly Cowork task", "set this up as a routine", `agentwright emit` |
| Security-scan what an agent may do at runtime | **agentwright** | "is my agent's tool grant too wide", `agentwright security-scan` |
| Set up or trim a Claude Project, `CLAUDE.md`, or a repo's Claude config | **rigwright** | "write my Project instructions", "trim my CLAUDE.md", `rigwright` |
| Which layer a standing rule belongs in, or score a setup for bloat | **rigwright** | "should this be a rule, a skill, or a hook", `rigwright audit` |
| Security-scan a skill package as built | **skillwright** | "audit this skill for secrets / injection surface", `skillwright audit` |
| A researched verdict or a reference doc | **lorewright** | "which X should I pick", "playbook for Y" |
| Define, apply, or audit a brand or voice | **brandwright** | `brandwright build / apply / audit` |
| Author or audit an eval suite | **evalwright** | "write trigger evals for &lt;target&gt;" |
| Slim, budget, or audit token footprint | **tokenwright** | "slim this / what does it cost" |

Each works alone. Initial routing is at the description level: this table is the proactive cue, not a dependency; an uninstalled wright is named, never a blocker.

## How they compose

- **skillwright builds neutral → brandwright brands it.** A built skill carries only its structural identity; palette, voice, and wordmark are applied by `brandwright apply`. brandwright is the single door for *all* brand output. No other wright styles its own.
- **Rebranding a whole skill set is a two-step handoff, not one owner.** brandwright defines or updates the identity — names, palette, wordmark, voice; skillwright `port` then propagates that identity across the pack's files. A request naming both a brand and a whole skill set reaches brandwright first for the definition, then skillwright to apply it. Neither claims the other's half, which is what keeps the two boundary sentences from pointing in a circle.
- **skillwright → evalwright for suites.** When evalwright is installed it authors a built skill's `evals/`; skillwright's own generator is the stated fallback.
- **promptwright owns model data.** For the tier + model to run a task on, `promptwright model`; every other wright reasons in tier names (frontier / flagship / balanced / fast) and defers here for the current specifics. A plan's target table is **living**: a subtask created mid-session gets a row through the same tier logic *before* dispatch — tiered first, dispatched second — so emergent subtasks adhere to the same per-task targets as the plan they join.
- **skillwright upkeep sweeps freshness.** `skillwright upkeep` reads every member's `metadata.volatile` and flags calendar surfaces past their 60-day window, refreshing the approved ones through each owner's refresh verb.
- **Prose on repo files is skillwright's; prose in a message is commwright's.** A README, CLAUDE.md, SOURCES, or reference doc is an artifact skillwright generates, audits and ports, so a register pass over one is its job. Anything bound for a channel — an email, a Slack post, a release announcement — is commwright's, and the same content pasted into a release body is a message again.
- **lorewright decides; the others build.** A sourced "which should I pick" is lorewright's verdict, distinct from promptwright's model pick and skillwright's niche verdict.
- **Security splits on the object, not the vocabulary.** Two members carry a security capability and the word *injection* sits in both descriptions, so the object decides and nothing else. A **running agent** — its tool grants, credentials, blast radius, what an injected instruction could make it do — is agentwright's `security-scan`. A **skill package as built** — injection surface in its own instructions, secrets in the artifact, undeclared or ungated capability, unsafe defaults in what it generates — is skillwright's, run as a named pass inside every `audit` rather than as its own verb. Code-level threat coverage is neither; that is a security harness's, and both descriptions say so. Each ships self-contained: neither loads a file in the other's directory, so either works with the other uninstalled.
- **The rig is attended; the agent is not.** Standing configuration a human reads in session — Project instructions, a knowledge-file plan, `CLAUDE.md`, a `.claude` layout, `.mcp.json` — is **rigwright**'s. Anything firing on a schedule or an event with nobody reading the result — a Cowork task, a routine, a desktop scheduled task, and the cadence, blast radius and kill switch around it — is **agentwright**'s, and `agentwright emit` renders the spec into the surface that runs it. The test is **who reads the output, never the filename**: a desktop scheduled task stored on disk as a `SKILL.md` is still agentwright's, because a filename names a format and not an object. "Set up" appears on both sides and decides nothing.
- **Always-on config is rigwright's; on-demand packages are skillwright's.** The split is whether the artifact is charged on every turn or only when it is relevant: the same every-session/some-sessions test rigwright's own layer stack applies internally, so the seam and the doctrine cannot drift apart. A `SKILL.md` under `.claude/skills/` is skillwright's even though rigwright emits the tree around it.
- **rigwright places; promptwright words.** Which layer a rule belongs in, and what budget binds it there, is rigwright's; the wording of the instruction block once its home is settled is promptwright's. A named surface carrying a layer question is rigwright; a block in hand with a quality cue is promptwright. Watched edge: a Project instruction block sits close to a system prompt, and it is rigwright's named-surface claim that beats promptwright's generic one.

## Conventions

- **Neutral by default.** Every wright outputs spec-clean; brand is an opt-in `brandwright apply` layer, never baked in.
- **One catalog, one gate.** Decisions are presented complete, once; "just do it" / "apply all" skips the gate. No drip-feed.
- **Audits report; they don't rewrite.** A finding catalog lands fixes only on approval.
- **Declared dependencies.** Any tool or sibling a skill needs is named, with its absence behavior stated — the pack degrades gracefully, never fails silently.
- **Volatile surfaces are stamped and swept.** Calendar baselines carry a date and a 60-day cadence; `skillwright upkeep` is the pack-wide check.
