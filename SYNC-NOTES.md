# Repo sync — 2026-07-14 (public brand v1.3.1 + README docs)

Unzip over the repo root, then commit + push.

| File | Change |
|---|---|
| `brand/brand-definition.md` | Stamp → "derived from definition v1.3.1" (content already Revenant-house-only and dedpixel-free; label sync only, now agrees with the private master) |
| `README.md` | Added "### foundation — the eight smiths" table (per-smith one-liners) + a "Before you install" trust/audit line in the Install section |

Commit line:

    docs: sync public brand edition to v1.3.1, add smith breakdown + install trust note

No skill files touched → no build.py run needed, no version bumps, no tag.

## Note — private install definition also corrected (NOT in this bundle)
Your PRIVATE brandsmith definition was rebuilt v1.3.0 → v1.3.1: stale
`revenantlabs` handle strings (inherited from the v1.2.0 base) corrected to
`revenantworks` in the handle map, GitHub rule, marks rule, and migration
note. That file ships install-side only, never to the repo. Re-run the swap
script with the v1.3.1 definition and re-upload brandsmith to claude.ai.
