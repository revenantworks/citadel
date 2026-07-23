# Pack Registry — structural single source of truth *(event-driven surface)*

> The canonical roster and pack structure `tools/build.py` derives every
> `references/pack.md` from. **Event-driven** — updated on roster or pack
> changes only, not on a calendar (no staleness stamp). Holds only what a
> *build* needs to name and stamp a member. Brand **styling** — palette, voice,
> taglines, wordmark, firewall — does **not** live here; it lives in
> brandsmith's `brand-definition.md` and is applied only when brandsmith is
> invoked. The token below is a **label** (it names skills and stamps
> frontmatter); it applies no styling on its own.

## Build defaults

| Parameter | Value |
|---|---|
| Brand token *(label)* | `revenant` — names skills (`<brand>-<pack>-<skill>`) and stamps `metadata.brand`; a label, not applied styling |
| Naming template | `<brand>-<pack>-<skill>` (64-char guard) |
| License default | MIT |
| Packaging default | Folder-zip, full files including `evals/`, folder at top level, named `<n>-<version>.zip` — `.skill` on request |

## Pack registry

| Pack | Profile | Notes |
|---|---|---|
| `foundation` | standalone | Lean, no tools beyond web search, low overhead; self-updating stamps. Conformance checks (2026-07-13): C-1 drift-audit verb · C-2 neutral default. Integrate policy: restamp: lazy (2026-07-13) |

**foundation members** *(canonical roster — pack manifests are generated from this table)*

| Member | Job | Route there when |
|---|---|---|
| `revenant-foundation-promptsmith` | Builds, scores, and hardens prompts with model-tier routing | The deliverable is a prompt, meta-prompt, or system prompt |
| `revenant-foundation-skillsmith` | Builds, audits, and ports Agent Skills and packs | The deliverable is a skill, SKILL.md, or pack — new, audited, or ported |
| `revenant-foundation-commsmith` | Shapes messages per channel, audience, and applied voice; audits message drift | The deliverable is a message, announcement, comms plan, or message audit |
| `revenant-foundation-agentsmith` | Designs and audits autonomous agent systems — guardrails, trust tiers, kill switches | The deliverable is an agent's operating spec or an audit of one |
| `revenant-foundation-loresmith` | Research-verified verdicts and playbook reference docs with evidence tags | The deliverable is a recommendation or a reference document |
| `revenant-foundation-brandsmith` | Defines brand and voice; applies them on request; audits repos, packs, docs, and artifacts for drift; exports payloads and the HTML brand-guide card | The deliverable is a brand or voice definition, its application, a drift report, or an export |
| `revenant-foundation-evalsmith` | Authors and audits eval suites — build-time generator, zero runtime dependency | The deliverable is a trigger-eval set, assertion suite, or suite audit |
| `revenant-foundation-tokensmith` | Measures, budgets, and slims the token footprint of LLM-facing artifacts | The deliverable is a leaner artifact, a token-efficiency audit, or a budget sheet |

**foundation capstone:** Forge Run — one orchestration prompt driving all eight smiths end-to-end (stored 2026-07-12 · roster updated to eight 2026-07-13 · roster reconfirmed 2026-07-14, pack self-audit, no change · re-run after any member's major version bump). Live runs: brandsmith build, 2026-07-13 · **Forge Run 3, 2026-07-23** — the 1.1.0 rebuild as build proof, all eight doctrines exercised in anger (skillsmith build/integrate conventions, evalsmith diff-scoped suite refresh, tokensmith measurement + C-1 audit, loresmith-grade source verification on four baselines, brandsmith centralization, commsmith-shaped release comms, agentsmith platform research, promptsmith model snapshot + Entry — Model); roster reconfirmed at 1.1.x, no change.

**foundation canonical repo:** `github.com/revenantworks/citadel` — source of truth for member drift audits (registered 2026-07-13). Relocated from the personal account 2026-07-14; the prior copy is a private archive. Nothing else carries the URL: manifests are generated from here, and every other file says "the registered canonical repo."
