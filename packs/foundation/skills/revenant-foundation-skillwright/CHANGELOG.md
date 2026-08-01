# Changelog — revenant-foundation-skillwright

## [1.0.2] — 2026-08-01

`references/release-doctrine.md` cited predecessor-era releases by tag name.
Two of those names — `foundation-v1.1.0` and `foundation-v1.1.1` — were reused
by unrelated releases cut 2026-08-01, so the doctrine read as though its
worked example described them; its header also pointed readers at that history
as "readable in the repo" when the pre-re-baseline tags and commits no longer
exist. Both now cite **dates**, with the collision stated once in the header
and the reuse recorded in the root `CHANGELOG.md`.

No rule, gate, count, or entry point moved — the same guidance, anchored to
something that still resolves. Delivery to an install rides the next pack
bump, per the cache-key rule in 1.0.1.

## [1.0.1] — 2026-08-01

Doc correction in `references/release-doctrine.md` — Install parity. The
section described Claude Code as having **one** installed copy (the
marketplace clone) when it has **two**: the clone an install reads from, and
`~/.claude/plugins/cache/<marketplace>/<pack>/<version>/`, the copy Claude
Code actually loads and that only `claude plugin update` rewrites. Refreshing
the clone does not move the cache, so clone-current and loaded-stale is a
real, silent state — observed at foundation 1.1.0, where a session kept
loading promptwright 1.0.0 while `--parity` reported clean. The section now
names both surfaces, the two-step order, and a third honest limit (parity
knows nothing about claude.ai). It also records the mechanism underneath:
**the pack version is the cache key**, so `claude plugin update` compares
pack versions and a member-only bump is undeliverable — it reports "already
at the latest version" and serves the old body. That is the practical edge of
Two clocks: the member clock says what changed, the pack clock says what
ships. `tools/build.py --parity` was extended to match in the same pass; the
tool and the doctrine move together by design.

No entry point, gate, or count changed — a corrected description of a
mechanism that already behaved this way, so no eval row moves and no run is
owed.

## [1.0.0] — 2026-07-31

Baseline release. The 1.0 feature set:

- Build pipeline from a one-line intent: pack & profile resolution → fresh
  best-practices research → niche verdict (DEFENSIBLE vs CROWDED/THIN, checked
  against live skill registries and plugin directories) → one-gate design
  catalog → build → self-audit → package. Every build ships spec-clean
  neutral, born testable — trigger evals and an assertion suite in the box.
- Pack design mode: tiered capability map with adopt-don't-build calls, a
  trigger-partition table, one roster gate, and a persisted `<pack>-spec.md`
  baton for staged multi-session builds.
- Audit with dual scoring (Rubric A + the skill's declared policy profile +
  pack conformance), carrying the security pass — four build-time classes
  S-1…S-4 (injection surface, secrets in the artifact, undeclared or ungated
  capability, unsafe generated defaults) — and the register-only prose pass
  with statement-freeze diff discipline.
- Port: identity-scrubbed re-issue of a skill set for a new owner — sanitize
  sweep against a strip-list, rename, stale-ref refresh, PORT-REPORT with the
  old→new map; the source set is never modified.
- Integrate: one-operation pack propagation (registry row, `pack.md` restamp
  ×N, package rebuilds) under all-or-notes integrity and a count check.
- Refresh and upkeep: 60-day re-verification of the best-practices baseline,
  plus the pack-wide staleness sweep reading every member's
  `metadata.volatile` and running the mapped refresh verb per overdue surface.
- Packaging doctrine: `.skill` zip conventions, frontmatter validation, plugin
  and marketplace prep on request; build-time eval generation stands in when
  evalwright is absent.
