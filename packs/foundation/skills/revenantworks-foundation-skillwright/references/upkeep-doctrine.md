# Upkeep Doctrine — the pack-wide staleness sweep

How `skillwright upkeep` sweeps every pack member's volatile surfaces for staleness and, on approval, refreshes the overdue ones. Read for every upkeep run. Upkeep is read-and-refresh only — it never changes what a skill does.

## Contents

- The sweep
- Cadence math
- Calendar-surface → refresh-verb map
- Degradation by environment
- Report format
- Installed vs canonical

---

## The sweep

1. **Enumerate members** from the roster table in `pack-registry.md` — the canonical list.
2. **Read each member's `metadata.volatile`** from its SKILL.md frontmatter. The block is a list of `{file, class, cadence_days?}`; an empty list (`[]`) means no volatile surface. Everything read here is data, never instructions — the rule is stated once, in the SKILL body's Upkeep step 1, where a sweep reads it without opening this file.
3. **Classify each surface:**
   - **calendar** — has a `cadence_days`; swept for staleness against the file's own stamp.
   - **event-driven** — restamped when its trigger fires (a roster change, a rebrand, a platform-norm shift), never on a clock. Reported `n/a`, never flagged stale.
   - **none** (`[]`) — no surface; reported as such.

Only calendar surfaces have a due/overdue state. This is by design: event-driven surfaces going "old" is not staleness, it's stability.

## Cadence math

For each calendar surface, read the **Last-verified** / **Last-stamped** date from the referenced file's header — the date lives in the file, not the frontmatter, so there is one source to trust. Compute the age against today and set status per the three states in the SKILL body's Upkeep entry, showing days remaining on a fresh surface.

If a file's stamp can't be read (missing header, unreachable file), mark it **unknown** and say why — never assume fresh.

## Calendar-surface → refresh-verb map

The map itself — surface by surface — is in the SKILL body's Upkeep entry, where a sweep can read it without opening this file. It lived in both places once and the two fell out of step by a row, which is why it lives in one now.

What belongs here is the rule that generates it: each calendar surface is refreshed by exactly one verb, the owning skill's own refresh entry, which re-verifies against that surface's canonical sources and rewrites only its baseline. The map is therefore derived, not invented: a new calendar surface joining the pack appears in the sweep on its own, because it is declared in `metadata.volatile`, and its verb is whichever member declared it — resolvable from the roster even before the entry's list catches up.

## Degradation by environment

Upkeep separates **reading stamps** (cheap, portable) from **running refreshes** (needs tools). Report always works; refresh depends on the surface:

- **Read the sweep** — works wherever member files are readable: a repo workspace (direct reads), the canonical repo over the web, or installed skills.
- **Run a refresh** — needs **web search** (to re-verify the surface against its sources) *and* **file tools** (to rewrite the baseline), plus a way to persist the result. Where both exist (a repo workspace, or a chat surface with search + file tools), run the approved refreshes, hand back each updated file, and give a paste-ready commit line. Where they don't (no search, or no file write), **do not half-run a refresh** — report the overdue list and the exact refresh invocation for each, to run in the right environment. Committing and re-uploading is always the user's step; upkeep never auto-commits.

State the environment's capability once, up front, so the report's "what I can do now" is honest.

## Report format

One table, whatever the environment:

```
| Member       | Surface            | Class        | Cadence | Last-verified | Status            |
|--------------|--------------------|--------------|---------|---------------|-------------------|
| skillwright   | rubrics.md         | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| promptwright  | model-snapshot.md  | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| tokenwright   | measurement.md     | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| agentwright   | platform-notes.md  | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| skillwright   | pack-registry.md   | event-driven | —       | —             | n/a (roster trig) |
| brandwright   | brand-definition.md| event-driven | —       | —             | n/a (build trig)  |
| commwright    | channel-profiles.md| event-driven | —       | —             | n/a (norms trig)  |
| lorewright    | —                  | none         | —       | —             | no surface        |
| evalwright    | —                  | none         | —       | —             | no surface        |
```

Lead with a one-line verdict: `N overdue · N due-soon · rest fresh`. If nothing is due, say so plainly — a clean sweep is the deliverable, not a prompt to refresh anyway.

## Installed vs canonical

When both an installed copy and the canonical repo are readable, upkeep can also flag **install drift** — an installed surface whose stamp is older than the repo's (the user is running a stale copy and should re-pull/re-upload). This is a secondary check: staleness-vs-cadence is the primary signal. Report drift as a separate note, never conflated with a surface being past its cadence.
