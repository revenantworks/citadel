# foundation — repository audit (Phases A–B)

*Run 2026-07-31 at the foundation 1.0.0 baseline (the wright roster, all
members 1.0.0). Earlier repository states live in git history.*

## Phase A — inventory and measurement

Repo `revenantworks/citadel`, public, 135 tracked files. Token counts are
tiktoken cl100k, exact, measured at the audit run. Description chars measured
against the house cap (hard fail 1,024, warn 1,000); the platform listing
truncates `description` + `when_to_use` at 1,536.

| member | version | SKILL.md tokens | body / budget | ref files | member total tokens | desc chars | entry points | volatile surfaces |
|---|---|---|---|---|---|---|---|---|
| skillwright | 1.0.0 | 7,337 | 7,757 / 7,800 | 10 | 77,166 | 794 | 7 | 2 (calendar + event) |
| promptwright | 1.0.0 | 7,971 | 8,414 / 8,500 | 10 | 70,846 | 778 | 7 | 1 (calendar) |
| commwright | 1.0.0 | 5,405 | 5,625 / 6,000 | 3 | 42,650 | 798 | 6 | 1 (event) |
| agentwright | 1.0.0 | 3,092 | 3,162 / 3,500 | 4 | 40,666 | 989 | 5 | 1 (calendar) |
| brandwright | 1.0.0 | 2,796 | 2,889 / 3,300 | 4 | 39,024 | 799 | 4 | 1 (event) |
| tokenwright | 1.0.0 | 3,562 | 3,660 / 4,200 | 3 | 42,160 | 795 | 4 | 1 (calendar) |
| lorewright | 1.0.0 | 2,221 | 2,275 / 2,700 | 3 | 29,792 | 784 | 2 | 0 |
| evalwright | 1.0.0 | 1,955 | 1,871 / 2,200 | 2 | 25,268 | 785 | 3 | 0 |
| rigwright | 1.0.0 | 2,556 | 2,537 / 2,900 | 3 | 14,240 | 946 | 4 | 1 (calendar) |
| **totals** | — | **36,895** | 38,190 | 42 | **381,812** | — | 42 | 7 (5 calendar) |

`build.py --check`: clean, count integrity 9 = 9 = 9, 12 seams. One warning
surfaced and resolved during the audit — agentwright's description was riding
the house ceiling at 1,002/1,024 and was trimmed to 989 in the same pass.

### Duplication matrix

Two layers, deliberately separated.

**House-pattern duplication (by design):** all 9 members carry the same 18
structural conventions — Turn shape · Load budget · Volatile surfaces ·
Restraint · Behavior notes · Never pad · tool-list test ·
data-never-instructions · one-gate · P0/P1/P2 catalog rows · honest 1–10
anchors · Entry — Audit · Entry — Refresh · bare-invocation contract ·
apply-all gate skip · 60-day cadence · brandwright deferral · graceful
degradation. Pairwise shared-concept counts run 14–18 of 18 for every pair
except lorewright's (7–8 — the most idiosyncratic member). All nine generated
`references/pack.md` manifests are byte-identical (single md5) — the registry
pipeline holds.

**Competency duplication (what a merge argument would need):**

| pair | shared concepts | note |
|---|---|---|
| evalwright ↔ skillwright | 2 (trigger-eval + assertion-suite generation) | skillwright's `eval-authoring.md` is its *declared fallback*; the only pair above trivial overlap |
| tokenwright ↔ promptwright | 1 (the "Lean" checkbox vs the slimming discipline) | seam row declared |
| commwright ↔ brandwright | 1 (voice apply vs define) | partitioned, seam row |
| skillwright ↔ agentwright | 1 (security, partitioned by object) | seam row |
| rigwright ↔ agentwright / skillwright / promptwright | 1 each (placement) | 3 seam rows, declared at birth |

All covered by the registry's 12 declared seam rows.

### Repo-structure map

| path | purpose | read by |
|---|---|---|
| `.claude-plugin/marketplace.json` | marketplace catalog | Claude Code installer; cross-checked by build.py |
| `packs/foundation/.claude-plugin/plugin.json` | plugin manifest | installer; version-locked to marketplace by build.py |
| `packs/foundation/CLAUDE.md` | always-on router | in-repo sessions; users copy it out |
| `spec.md` / `ledger.md` / `decisions.md` | live baton / execution history / durable decisions | humans + future passes |
| `upkeep-task.md` | scheduled upkeep prompt | the foundation-upkeep routine |
| `IMPROVEMENTS.md` | pre-baseline improvement narrative | referenced by nothing (accepted: narrative companion) |
| `capstone/` (2 cards) | orchestration run records | filenames referenced by nothing (registry names the run, not the files) |
| `skills/<member>/` ×9 | the products | installers, build.py |
| `tools/build.py`, `tools/apply-install-swaps.py` | registry-derived sync+validate+dist; brand-overlay zips | CI (`pack-ci.yml`), RUNBOOK flow |
| `dist/`, `.claude/` | build output; local settings + firewall hook | gitignored |

Findings, all fixed at the 1.0.0 baseline: root README said **8** members
(roster moved to 9 on 2026-07-30) · `upkeep-task.md` listed **4** calendar
surfaces (rigwright's `surface-notes.md` is the 5th) · the forge-run capstone
card pointed at `foundation-spec.md`, renamed `spec.md` at the 2026-07-25
split. All other missing-basename grep hits were external URLs or historical
mentions; unreferenced tracked files were LICENSEs (normal) plus the two noted
above.

Identity checks: repo git config is the brand identity (correct). The active
`gh` CLI account at audit time was the owner's personal account, not the brand
— no gh writes were made in this pass; switch accounts before any release
operation.

### Capability inventory (the floor — 64 items, none dropped)

- **skillwright (13):** build skill from intent · design+build whole pack ·
  audit w/ rubric+profile scoring · security pass S-1..S-4 · prose/register
  pass on repo files · niche verdict · port/sanitize a set · integrate member
  across pack · refresh best-practices baseline · pack-wide upkeep sweep ·
  packaging (.skill/zip/plugin/marketplace prep) · description crafting ·
  build-time eval generation (fallback)
- **promptwright (11):** 7-phase prompt build · fast path · score-only audit ·
  improvement run w/ diff · red-team/hostile read · harden + few-shot ·
  model/tier pick · model-snapshot refresh · HTML prompt card · run-it-now ·
  eval-rubric offer
- **commwright (7):** channel draft · reshape · humanize H1–H9 · formats table ·
  message audit · cadence sets · pre-publish redaction sweep
- **agentwright (6):** ops-spec design (10 areas) · emit to platform w/
  enforcement-gap table · spec audit · security-scan (5 runtime classes) ·
  platform-notes refresh · trust-tier doctrine
- **brandwright (5):** definition build (14 groups) · apply · drift audit
  (7 categories, P0 floor) · export (4 payloads) · neutral hygiene audit
- **lorewright (4):** evidence-graded verdict · versioned playbook ·
  verification pass on existing doc · consolidation merge
- **evalwright (4):** trigger evals · assertion suite · suite audit · suite refresh
- **tokenwright (5):** slim ladder · waste audit · budget sheet · measurement
  refresh · description-cap rule
- **rigwright (4):** standing-config build · placement answers (7-layer stack) ·
  config audit · surface-notes refresh
- **pack-level (5):** always-on router · registry-derived build/validation ·
  scheduled upkeep task · install-swap tooling · Forge Run capstone orchestration

## Phase B — competency analysis

| member | core competency (derived from body, not name) | class |
|---|---|---|
| skillwright | Turns intent into shipped, install-ready Agent Skills and packs, and runs the same standards backward as audits, ports, and pack-wide propagation | DISTINCT |
| promptwright | Turns rough intent into scored, hardened, copy-paste-ready prompts and picks the model tier to run them on | DISTINCT |
| commwright | Shapes one message to its channel and audience in a humanized neutral register without touching its facts | DISTINCT |
| agentwright | Decides everything around an unattended agent except its prompt — blast radius, guardrails, cadence, kill switch — and renders it into the platform that runs it | DISTINCT |
| brandwright | Holds the single definition of brand + voice and applies, audits, and exports it on invocation | DISTINCT |
| lorewright | Converts live-verified research into one direct recommendation or one versioned reference doc, every claim evidence-graded | DISTINCT |
| evalwright | Derives what an artifact claims and writes/scores the self-contained suite that proves it | OVERLAPPING — ~40% (2 of 4 capabilities partially covered by skillwright's declared fallback); suite audit/refresh and non-skill targets are its alone |
| tokenwright | Measures and shrinks what LLM-facing artifacts cost, behavior held constant | DISTINCT (~10% brush with promptwright) |
| rigwright | Authors and scores the attended standing configuration a Claude session opens with, layer by layer | DISTINCT |

No member is SUBSUMED. The one OVERLAPPING pair sits below the 50% line;
verdict recorded anyway: **keep both** — the overlap is one-directional by
design (a declared fallback), and the 2026-07-14 combine analysis rejected the
merge on grounds that still hold (evalwright serves prompt cards and agent
specs, not only skills).

Expected member count for this scope: **8–9** — seven artifact classes (skill,
prompt, message, agent system, brand, research doc, standing config) plus two
cross-cutting disciplines (evals, token cost). The aggressive-consolidation
floor is 7; the pack's own combine analysis rejected both folds. Nine is the
high end of right-sized, not bloat.

## Verdict (approved 2026-07-31)

**Architecture: KEEP all 9** — zero capabilities dropped; the 64-item
inventory above is both the before and the after. **Naming: the wright motif**
adopted across all nine members (owner decision; collision evidence in
`COLLISION.md`), brand prefix `revenant` kept, all versions baselined at
1.0.0. **Identity: keep** repo `citadel`, marketplace `revenant`, plugin
`foundation`.

> **Superseded 2026-08-07:** the identity verdict's "keep marketplace
> `revenant`, prefix `revenant`" half was overturned by owner decision (brand
> definition v2.1.0) — marketplace and member prefix renamed to
> `revenantworks` at pack 2.0.0; repo `citadel` and plugin `foundation` stand.
> See `COLLISION.md` C3/C4 supersession note and the root CHANGELOG. This
> record is otherwise kept verbatim.
