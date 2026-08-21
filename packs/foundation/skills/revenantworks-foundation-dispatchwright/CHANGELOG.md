# Changelog — revenantworks-foundation-dispatchwright

## [1.2.0] — 2026-08-21

Earned the standalone profile back by removing what disqualified it, not by
relabelling. 1.1.0 flipped this member to `standard` because it shipped
executable code and read as hard-depending on `git` and the surface's
Task/Agent/Workflow tools. Both findings were correct. This release removes the
first and corrects the second, and the profile follows as a result.

- **The two forcing hooks left the package.** `dispatch_gate.py`,
  `dispatch_ledger_guard.py` and `dispatch_patterns.txt` moved out of
  `references/hooks/` and into the `claude-skills` repo's own `.claude/hooks/`,
  beside the brand firewall and the pack-bump check. They are rig
  infrastructure keyed to `~/.claude/dispatch-mode.json`, not skill payload,
  and a marketplace installer of this pack has no business receiving
  auto-installed `PreToolUse` hooks. The files moved with `git mv`, so history
  follows them; no line of either script changed, and both `--selftest` runs
  pass byte-identical from the new location. The live hooks a session actually
  executes still live under `~/.claude/hooks/` and are untouched by this move.
- **This member now ships no executable code.** That was the one hard bar the
  standalone profile sets, and it is the change that clears it. `references/`
  holds three Markdown files and nothing else.
- **`git` and subagent tools restated as optional, with the degradation
  named.** Neither was ever required to finish a plan; the old wording implied
  they were. Without `git`, a run still plans, tiers, dispatches and records —
  a row it cannot check against origin is reported unverified rather than done,
  which is section 8's existing rule, not a new one. Without subagent or Task
  tools, a run ends at the tiered plan and the ledger, handed back for a human
  or a later session to launch. This follows skillwright's own precedent: an
  optional dependency with stated degradation does not break standalone, a hard
  one does.
- **`profile: standalone` restored as a consequence.** The declaration is true
  because the package changed, not because the label did. Load budget was
  already inside the standalone ceiling — a plan opens one reference, a
  dispatch two, an audit one — and dropping the hooks costs a run no load,
  since executables were never read into context.
- **Stale claim removed.** SKILL.md and README both pointed a reader at "that
  folder's own README" for the hook install block. No such README has ever
  existed in `references/hooks/`; the sentence is gone rather than repointed.
- No behavior change anywhere else. The workflow, the wave caps, the durability
  contract, the ledger schema, the anti-patterns and the three seams are
  unchanged, and the description did not move.

## [1.1.0] — 2026-08-20

Pack-wide skillwright audit findings, P1-1 and P1-2. Both were self-inflicted
gaps between what this member claimed and what it enforced.

- **P1-1 — the declared profile was wrong.** Frontmatter said
  `profile: standalone`, but the package ships two executable Python hook
  scripts and hard-depends on `git` and the surface's Task/Agent/Workflow
  tools; the standalone profile bars shipped executable code outright, and
  this member does not behave identically on chat/API (where it degrades to
  plan-and-tier) as standalone requires. Now `profile: standard`, with the
  dependency paragraph naming the hooks and stating that the skill runs
  identically without them, just without the automatic forcing behavior.
- **P1-2 (S-3) — the wave caps were prose nobody enforced.** SKILL.md §6
  states a 6-unit concurrency cap and a one-writer-per-repo rule; the
  `PreToolUse` guard only ever proved *a* tiered row existed, so a run could
  fan out past either cap with a plausible ledger and nothing would stop it.
  `dispatch_ledger_guard.py` gains `open_unit_count()` and `repo_collision()`,
  both reading the ledger as it stands and blocking (exit 2) when it already
  shows a cap violated. A row counts as open from `dispatched` until it
  reaches a terminal status; an unlabeled status counts as open, since an
  unlabeled row is what a cap exists to catch. Four new exit-code selftest
  cases, 17 total, all passing.

## [1.0.1] — 2026-08-18

Fail-open audit of the two shipped hooks (D1-D4). A sibling session repaired four fail-open
defects in the LIVE hooks at `~/.claude/hooks/`; this release brings the version-controlled
copies under `references/hooks/` into line with them — the shipped copies had drifted to the
broken originals, which is exactly the gap this member's own package exists to prevent.

- **D1 — no session id was a total no-op.** `flag_is_live` returned `False` (allow) whenever the
  PreToolUse payload carried no session id, so any Task/Agent/Workflow call without one passed
  the guard outright. `flag_state()` now returns one of absent / stale / other-session /
  uncorrelated / live, and an uncorrelatable session id on either side enforces the ledger check
  rather than skipping it.
- **D2 — exit 1 on any exception, not 2.** Claude Code blocks a PreToolUse call only on exit code
  2; only `json.load` was wrapped, so a fault anywhere else failed open. The whole hook body is
  now wrapped; every path returns 0 or 2, never 1.
- **D3 — a stale ledger disarmed the guard forever.** `find_ledger` took the newest ledger by
  mtime with no age limit, so one old populated ledger passed every dispatch in that directory
  for good. A ledger now counts only inside the same staleness window that keeps the flag live,
  or by naming the current session outright.
- **D4 — junk cells counted as tiered.** The populated-row check rejected only `""`, `-`, and the
  em dash, so a row of `TBD` / `?` / `x` read as a real model/effort/surface. Each cell is now
  validated per field against a placeholder list and an effort vocabulary.
- Both files carry a `--selftest` exercising all four defects at the real exit-code level
  (verified: `python dispatch_gate.py --selftest` and `python dispatch_ledger_guard.py
  --selftest`, both OK against the copies now shipped here).
- No behavior change to anything else in this member — SKILL.md, the anti-patterns, the ledger
  schema, and the three seams are unchanged.
- The pack registry's seam table (`pack-registry.md`, shipped inside skillwright — see that
  member's own CHANGELOG for its version) now carries the three rows this member's README named
  as owed at 1.0.0: dispatchwright ↔ promptwright, ↔ rigwright, ↔ agentwright, each declared as
  an uncontested, one-sided edge. README's "What did not land" section updated to match.

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
