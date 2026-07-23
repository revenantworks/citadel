# Upkeep Doctrine — the pack-wide staleness sweep

How `skillsmith upkeep` sweeps every pack member's volatile surfaces for staleness and, on approval, refreshes the overdue ones. Read for every upkeep run. Upkeep is read-and-refresh only — it never changes what a skill does.

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
2. **Read each member's `metadata.volatile`** from its SKILL.md frontmatter. The block is a list of `{file, class, cadence_days?}`; an empty list (`[]`) means no volatile surface.
3. **Classify each surface:**
   - **calendar** — has a `cadence_days`; swept for staleness against the file's own stamp.
   - **event-driven** — restamped when its trigger fires (a roster change, a rebrand, a platform-norm shift), never on a clock. Reported `n/a`, never flagged stale.
   - **none** (`[]`) — no surface; reported as such.

Only calendar surfaces have a due/overdue state. This is by design: event-driven surfaces going "old" is not staleness, it's stability.

## Cadence math

For each calendar surface, read the **Last-verified** / **Last-stamped** date from the referenced file's header (the date lives in the file, not the frontmatter — the single source). Then, against today:

- **OVERDUE** — `age ≥ cadence_days`.
- **due-soon** — `cadence_days − 7 ≤ age < cadence_days` (inside the last week of the window).
- **fresh** — `age < cadence_days − 7`. Show days remaining.

If a file's stamp can't be read (missing header, unreachable file), mark it **unknown** and say why — never assume fresh.

## Calendar-surface → refresh-verb map

Each calendar surface is refreshed by exactly one verb — the owning skill's own refresh entry, which re-verifies against that surface's canonical sources and rewrites only its baseline:

| Surface | Owning member | Refresh verb |
|---|---|---|
| `references/rubrics.md` | skillsmith | `skillsmith refresh` |
| `references/model-snapshot.md` | promptsmith | `promptsmith refresh` |
| `references/measurement.md` | tokensmith | `tokensmith refresh` |

This map is derived, not hardcoded elsewhere: any member declaring a calendar surface is refreshed by that member's refresh entry. If a new calendar surface joins the pack, it appears in the sweep automatically (it's in `metadata.volatile`) and refreshes through its own member's verb.

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
| skillsmith   | rubrics.md         | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| promptsmith  | model-snapshot.md  | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| tokensmith   | measurement.md     | calendar     | 60d     | 2026-07-23    | fresh (Nd left)   |
| skillsmith   | pack-registry.md   | event-driven | —       | —             | n/a (roster trig) |
| brandsmith   | brand-definition.md| event-driven | —       | —             | n/a (build trig)  |
| commsmith    | channel-profiles.md| event-driven | —       | —             | n/a (norms trig)  |
| agentsmith   | —                  | none         | —       | —             | no surface        |
| loresmith    | —                  | none         | —       | —             | no surface        |
| evalsmith    | —                  | none         | —       | —             | no surface        |
```

Lead with a one-line verdict: `N overdue · N due-soon · rest fresh`. If nothing is due, say so plainly — a clean sweep is the deliverable, not a prompt to refresh anyway.

## Installed vs canonical

When both an installed copy and the canonical repo are readable, upkeep can also flag **install drift** — an installed surface whose stamp is older than the repo's (the user is running a stale copy and should re-pull/re-upload). This is a secondary check: staleness-vs-cadence is the primary signal. Report drift as a separate note, never conflated with a surface being past its cadence.
