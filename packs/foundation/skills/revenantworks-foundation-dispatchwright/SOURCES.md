# Sources

This skill's doctrine is drawn from two places, both internal to this estate rather than
external documentation, so this file maps content to origin instead of to a published standard.

| Source | Applies to | Key guidance |
|---|---|---|
| `V:\Projects\github\MickMacPW\workshop\handbook\lessons-2026-08-17-rebuild.md` — the owner's own record of one large multi-agent rebuild session | `SKILL.md` §5 (Durability contract), §6 (Wave execution), §7 (Escalation), §9 (Anti-patterns); `references/anti-patterns.md` | Every numbered lesson in that page names a concrete failure from a real run — one tier for all work, push-at-the-end losing an agent's commit, two writers colliding on one repo, a read-only pass that wrote anyway, a tool result overflowing context, and self-reports that did not match reality. dispatchwright's rules are the enforcement this skill exists to be; the page itself states "every rule here is enforced somewhere — a skill, a hook, or a template — and the enforcement is named beside it." This member and its two hooks are that enforcement for the fan-out lesson. |
| `revenantworks-foundation-promptwright/SKILL.md` — Tier routing (Phase 5) and Entry — Model, plan grain | `SKILL.md` §4 (Tier) | The four capability tiers (frontier / flagship / balanced / fast), the effort-before-tier ladder, and the living-table contract for a subtask added mid-run are promptwright's and held here by reference only, never restated or re-derived. |
| `revenantworks-foundation-rigwright/SKILL.md` — the layer-placement stack | `SKILL.md` §1 (Scope and seams) | The call on which layer (CLAUDE.md, a hook, a permission rule) makes dispatchwright's trigger fire is rigwright's, quoted rather than re-argued. |
| `revenantworks-foundation-agentwright/SKILL.md` and `packs/foundation/CLAUDE.md` — the rigwright/agentwright attended-vs-unattended boundary | `SKILL.md` §1 (Scope and seams) | The line separating a same-session fan-out (in scope here) from anything unattended (agentwright's, whole) is quoted verbatim from the pack's own router file. |

**Unsourced by design.** The specific numeric caps in §6 (six concurrent units, two nesting
levels, a twelve-unit split threshold) and the specific durability mechanics in §5 (the atomic
commit+push call, the three-checkpoint ledger row) are doctrine authored for this skill from the
2026-08-17 rebuild's lessons, not drawn from a published orchestration standard. Declared here so
the gap is visible rather than implied, matching this pack's own convention for unsourced
material (see `revenantworks-foundation-promptwright/SOURCES.md`).
