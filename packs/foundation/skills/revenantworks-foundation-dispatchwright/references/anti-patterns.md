# Anti-patterns

Thirteen ways a fan-out loses work or wastes it, each with the one-line reason it matters and,
where the 2026-08-17 estate rebuild produced a real instance, that instance. SKILL.md §9 points
here; this file is the lookup, not a standing load.

1. **Dispatch without a ledger row.** A unit launched before its row exists has no record to
   reconcile against — if it dies silently, nothing shows it was ever running.

2. **Separate commit and push.** A commit with no matching push is invisible on the remote; the
   2026-08-17 rebuild lost one agent's work this exact way — it died on a usage limit at the
   words "Final verification and push," committed but unpushed, and looked lost until the next
   session checked the tree by hand.

3. **Treating a report as proof.** An agent's own account of what it did is not evidence of what
   landed. The same rebuild's adversarial verification against the filesystem, git, and the live
   routine API found 3 refuted and 5 partial claims out of 98 self-reported ones — including a
   disaster-recovery document still pointing at a repo path that no longer existed.

4. **Restarting instead of resuming.** Re-running a unit from scratch after a stall throws away
   whatever it already pushed and risks redoing (or conflicting with) real, landed work — the
   whole reason Resume's first action is reading origin before anything else.

5. **One agent marking another complete.** A dispatcher or sibling unit that certifies another
   unit's work without checking origin is trusting a report by proxy — the same failure as #3,
   one layer removed.

6. **Concurrent writers without a worktree.** Two units writing one repo in the same window
   collide. The 2026-08-17 rebuild hit this directly: two agents both wrote to the `workshop`
   repo in the same window, one had to rebase, and a third agent's own sub-agents died mid-run and
   it silently redid their work by hand rather than surfacing the collision.

7. **A whole wave inside one minute.** Launching every unit in a wave at once removes the stagger
   that keeps two units from racing for the same file before either has committed anything.

8. **Two units fetching the same large document.** Every unit that independently fetches a big
   spec or listing pays its cost twice and doubles the chance of blowing a context window — the
   rebuild's own listing call returned up to 393 KB per page and overflowed the token limit on
   nearly every repo, more than once, because nothing cached the result for reuse.

9. **Escalating on a hunch.** A tier jump with no failed check, failed test, contract violation,
   or verifier's refutation behind it is a guess wearing the shape of a decision — the rebuild's
   root cause for running everything at one tier was exactly this: nothing forced a unit to earn
   its tier with a signal.

10. **A planning turn run at high effort.** High reasoning effort on a planning or orchestrator
    subtask reliably over-thinks and scope-creeps the plan itself, past what was actually asked —
    promptwright's own role-based override exists because of this failure mode.

11. **Fanning out work that shares context.** Splitting iterative work — where each step needs
    what the last one built — into separate units throws that shared context away between them;
    it belongs in the main conversation (SKILL.md §2), not a wave.

12. **No stop condition.** A unit with no stated definition of "done" cannot be checked against
    one; it either runs past what was needed or gets marked complete by guesswork.

13. **Launching top-tier work on a nearly spent window.** Starting a frontier-tier wave against a
    rolling usage window that is nearly exhausted is how a unit dies mid-write with nothing
    pushed yet. The 2026-08-17 rebuild's own run — about 20 background agents and 4 workflows, all
    at the top tier and high effort, across 9 repos — cost five separate usage-limit stops and two
    agents that died mid-write.
