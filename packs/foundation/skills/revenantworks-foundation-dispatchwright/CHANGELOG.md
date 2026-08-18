# Changelog — revenantworks-foundation-dispatchwright

## [1.0.0] — 2026-08-18

Baseline release. The tenth foundation member, built to close the gap the 2026-08-17 estate
rebuild's lessons page named directly: a session-scale fan-out with no standing doctrine for
tiering, durability, or reconciling against reality rather than an agent's own report.

- **Shape check first.** Every plan is tested against the cheaper alternatives — the main
  conversation, a single subagent, a skill — before any unit, tier, or ledger row exists.
- **Decompose, then tier through promptwright.** Explicit unit boundaries and stop conditions,
  one writer per repo; the finished unit list is handed to promptwright's Entry — Model plan
  grain and its target table is copied verbatim. dispatchwright never invents a tier.
- **The durability contract.** Atomic commit+push, pushed after every finished piece of work and
  before any report, a ledger row at dispatch/commit/push, and `git log --oneline origin/main -5`
  plus the ledger read as resume's first action.
- **Wave execution caps.** Six concurrent units, two nesting levels, a named split above twelve
  units, staggered launch, `isolation: "worktree"` for every writer, and a usage-window check
  before a top-tier wave.
- **Escalation on signal only.** Effort raised before tier, one escalation per unit, a reviewer
  that changes model family rather than resampling, and an owner ask before any top-tier
  escalation, irreversible action, or 2x budget overrun.
- **Reconcile against origin, not report.** Every ledger row checked against
  `git rev-parse origin/main`; unclaimed commits, unpushed worktrees, duplicated work, and actual
  vs. estimated spend reported per run.
- **Thirteen named anti-patterns** (`references/anti-patterns.md`), several with the 2026-08-17
  rebuild's own instance recorded beside the reason.
- Two forcing hooks shipped as version-controlled copies under `references/hooks/`
  (`dispatch_gate.py`, `dispatch_ledger_guard.py`); the installed copies a session actually runs
  live under `~/.claude/hooks/` — see that folder's own README for the settings.json block.
- Trigger evals only at this release: 10 should-fire, 10 should-not (including the promptwright,
  agentwright, and rigwright boundary pairs), and 2 injection probes. Authored, not yet run
  (`evals/RESULTS.md`). No assertion suite yet, and no routing-seam row in the pack registry —
  both named as owed in this member's own README.
