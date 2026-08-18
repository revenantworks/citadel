# Unit brief template

Copy this into every dispatched unit's own prompt. It carries the durability contract verbatim
(SKILL.md §5) so a unit that never saw this doctrine still behaves the way the doctrine requires.
Fill the bracketed fields; do not paraphrase the contract itself.

---

**Unit:** `[unit_id]` — [one-line task]

**You own this repo for this run.** [Name the repo and worktree/branch, or state "no other unit
touches this repo in this window."] No other unit writes here while you run.

**Class:** [mechanical / structured / judgment] · **Model:** [from the tier table] ·
**Effort:** [from the tier table] — assigned by promptwright's target table, not chosen by you.

**Expected artifacts:** [what "done" looks like — a file, a commit, a specific report shape]

**Stop condition:** [what tells you the unit is finished, stated before you start]

---

### DURABILITY CONTRACT — follow this exactly

- Commit and push as ONE atomic call: `git add -A && git commit -m "..." && git push origin main`
  (or your assigned branch). Never separate the commit from the push.
- Do that after each finished piece of work, not at the end. If you die mid-run, everything
  finished is already on the remote.
- Push BEFORE writing your report. The report is the cheapest thing to lose.
- Before your first write, run `git pull --ff-only` and `git log --oneline -3`.
- Update your ledger row at `[ledger path]` at three points: when you start (already written for
  you), right after your first commit (add the sha), and right after your first push (confirm the
  sha reached `origin`). A row you cannot update yourself, update by reporting the sha back to the
  dispatcher.
- If a step needs a large fetched document (a spec, a long page, an API dump), write it once to
  `[shared fetch cache path]` and read it from there if you need it again — do not re-fetch, and
  do not assume you are the only unit that needs it.
- If you must escalate — a failed check, a failed test, a contract violation, a verifier's
  refutation, never a hunch — raise effort within your current tier first (SKILL.md §7). One
  escalation only. Stop and ask the owner before any top-tier escalation, any irreversible action
  this brief did not already name, or running past 2x your estimated budget.

### On resume (if you are picking this unit back up)

1. First action, always: `git log --oneline origin/main -5` and read this unit's ledger row.
2. If the row already shows a `remote_sha`, that work is done — do not redo it. Start from what
   the row says is still outstanding.
3. Never restart from scratch because a report looks incomplete; check origin first.

---

Your report at the end should be reconcilable, not just credible: name the exact commit sha(s)
you pushed, so the dispatcher (or `dispatchwright audit`) can verify them against
`git rev-parse origin/main` rather than take your word for it.
