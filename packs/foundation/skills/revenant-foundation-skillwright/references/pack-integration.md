# Pack Integration — Durable

> Loaded for every Entry — Integrate run and for the keep-going continuation after a pack-member build. The registry in `pack-registry.md` is the single canonical roster; everything here reads from it and writes downstream of it.

## Why this entry exists

Adding or changing a pack member used to end at the member's package, leaving the propagation manual: registry row, capstone roster line, a `pack.md` restamp in every sibling, rebuilt archives, per-surface uploads. Each touch is trivial; the set is error-prone and undocumented drift is the failure mode. Integrate makes the set one operation with an integrity contract.

## Touch-point table

| Touch | Where | Rule |
|---|---|---|
| Registry row | `pack-registry.md` → pack members table | One row per member; add/amend first — everything else derives from it |
| Capstone roster line | `pack-registry.md` capstone entry (and the stored capstone card, when reachable) | Member add updates the roster line **only**; a capstone re-run triggers on a member's next major version bump or on request — never on an add |
| Roster manifest | `references/pack.md` in **every** member | Generated once from the registry — roster plus the routing-seam table when the registry declares seams — fresh Last-stamped date, then written byte-identical to all N |
| Packages | Per Packaging | Blast radius set by the pack's `restamp` policy (below) |
| Uploads | Per surface | Checklist split *due now / rides next release* — see Surface modes |

## Restamp policy — `restamp: eager | lazy`

Declared per pack in the registry Notes (default **lazy** when absent). The policy exists because installed-surface uploads are manual and per-account: claude.ai custom skills upload one zip at a time under Customize → Skills, and the API Skills endpoint serves API surfaces, not claude.ai accounts. Roster manifests are advisory (absence-graceful by pack law), so a stale roster in a not-yet-rebuilt sibling breaks nothing.

- **lazy** — rebuild and list for upload only members whose content actually changed: the new/changed member, plus the registry-carrying member when the registry changed. Every other sibling picks up the fresh `pack.md` automatically on its own next release (the repo copy is already restamped; only the installed snapshot lags). The report names the deferred members explicitly.
- **eager** — rebuild all N and list all N for upload. Choose when roster accuracy on every installed surface matters more than upload count (e.g., just before a port or an org-wide provision).

Either way the **repo** copies are always fully restamped — policy governs packages and uploads, never source truth.

## Surface modes

**Chat (no repo access):** deliver (1) rebuilt member archives per the pack's packaging default, (2) one **repo-sync bundle** — a zip of only the changed files at repo-relative paths (`skills/<member>/references/pack.md`, `skills/<registry-member>/references/pack-registry.md`, …) so it unzips over the repo root — (3) a paste-ready commit line, (4) the upload checklist. The bundle is additive-only: it never deletes repo files.

**Repo workspace (Claude Code or equivalent):** edit in place. When the repo carries a pack build script (`tools/build.py` by convention), run it — it re-derives `pack.md` from the registry, syncs and validates the members **the registry names**, and rebuilds `dist/` — instead of packaging natively. `--check` mode is the CI drift guard: it fails when any member's `pack.md` disagrees with the registry. Its reach ends where the registry does: a folder no registry row names is not visited at all, so nothing inside an unregistered member is checked until Integrate step 1 adds its row.

## Commit line template

`pack(<pack>): integrate <member> <version> — registry row, roster ×<N>, <k> package(s) rebuilt [<policy>]`

## Count integrity

Entry — Integrate step 5 owns the check, the three roster numbers, and the abort. What this file adds is the wire format — report them inline (`8 = 8 = 8`) — and why the abort is not negotiable: a partial restamp is worse than a documented manual list, because it looks finished. Write nothing further once the numbers disagree; the integration-notes are the deliverable from that point on.

## Failure and fallback

No file tools on the surface → integration-notes only (every touch named, paste-ready content included). Registry unreadable or pack unregistered → stop; register the pack first (registry row + marketplace entry + build run per the RUNBOOK — the old Configure entry that owned this was retired at 1.1.0). Sibling folders absent in chat (nothing uploaded to integrate against) → deliver the regenerated `pack.md`, the registry diff, and notes; never fabricate sibling packages from memory.
