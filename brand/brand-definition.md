# Revenant — Brand Guide *(house · public edition)*

> **Last built: 2026-07-14 · derived from definition v1.3.1.** This public edition covers the **Revenant** brand only — the identity everything in this repository ships under. The full internal definition (including non-house sections) is maintained separately and re-exports here on change.

## Essence

A revenant is the one that returns — intelligent, purposeful, impossible to keep down. **Revenant** is the mark on everything shipped here: the machine that always comes back. Everything lives on voidblack; everything glows.

## Identity map

| Element | Value |
|---|---|
| Brand | **Revenant** — public house brand; all public releases, repos, products, comms |
| Handles | GitHub identity **revenantworks** (canonical repo `revenantworks/citadel`) · brand domain `revenantworks.dev` |
| Ownership / exceptions | Anything these rules don't cover, or any exception, is the brand owner's call — decided once, then recorded here |

## Tag registry

| Tag | Use on | Never on |
|---|---|---|
| **RVNT** | Formal short mark: version/release lines, "— RVNT" sign-off, UI badges, monogram, terminal contexts | Casual speech; as a handle substitute; never ticker-styled |
| **REV** | Spoken nickname — the AI persona ("Rev"), prose second-reference, community speech | Standalone public handle; formal marks |

## Naming conventions

| Class | Template / rule |
|---|---|
| GitHub | Public canonical repos live under the **revenantworks** identity; public commit/tag authorship = Revenant identity (noreply email) only |
| Repos | lowercase single-token or `revenant-<thing>` |
| Skills / packs | `revenant-<pack>-<skill>` · packs `revenant-<pack>`; pack names draw from the Revenant world (places/structures); **each pack sets its own member motif — `-smith` is claimed by foundation.** On file: forge → `-wright` · crypt → `-keeper` · threshold → `-warden` · wake → `-watcher` · vault → `-locker` |
| Marketplace | Repo **`citadel`** — one repo, one marketplace (name: `revenant`; installs read `<pack>@revenant`); one plugin per pack under `packs/`; plugin slugs = pack names, immutable once published |
| Releases | semver, tagged per pack: `<pack>-vX.Y.Z` |
| Marks | `revenant` lowercase in marks; "Revenant" in prose; the handle carries "works," the mark never does; no corporate suffix in any mark |

## Palette — role tokens

**Core**

| Role | Token | Hex |
|---|---|---|
| Background | voidblack | `#0A0A0B` |
| Primary text | bone-white | `#EDEDED` |
| Secondary text / UI | ash-grey | `#8A8F98` |

**Functional tokens** *(job colors, one-off / status use only — never identity accents)*

| Token | Hex | Job |
|---|---|---|
| glitch-magenta | `#FF2D78` | hot / energy / hype |
| phantom-green | `#39FF14` | signal / error / CRT-corruption |
| ember-orange | `#FF6A00` | live / warning / hot-status (LIVE badges, alerts) |

**House accent**

| Role | Token | Hex |
|---|---|---|
| Accent | threshold-blue | `#00E5FF` |

**Rules.** Black dominates; threshold-blue is the sole identity accent. Bone-white is the only body-text color; accents are glow/highlight only. Functional tokens signal a *state*, never an *identity*. Never place magenta and phantom-green on the same mark. Outrun look = treatment (bloom, thin scanline, subtle chromatic-aberration fringe) over flat tokens, on voidblack.

## Typography

All faces are open-license (Google Fonts) with system fallbacks — the brand never depends on a paid or unavailable font.

| Role | Face | Fallback stack |
|---|---|---|
| Display · code · wordmark | **JetBrains Mono** | `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` |
| Body | **Inter** | `-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` |

**Hierarchy:** H1 = display face 700 · H2 = 600 · body = Inter 400, 16px, line-height 1.5 · captions/labels = ash-grey, 13px, letterspaced uppercase. Never set body copy in a display face.

## Logo usage

**Clearspace:** one cursor-block width on all sides. **Minimum sizes (digital):** monogram 24px; wordmark 120px wide — below that, use the monogram.

**Don't:** stretch, condense, or rotate the mark · recolor outside the brand tokens · add drop shadows or gradients (the sanctioned glow/bloom is the only light effect) · place magenta and phantom-green on the same mark · place the mark over busy imagery without a voidblack scrim.

## Wordmark

Lowercase monospace **`revenant▍`** — block cursor in threshold-blue, blinking on web, solid in static. Monogram: **RVNT** compressed, or an R whose tail loops into a return arrow.

## Imagery & iconography

Abstract only: terminal grids, particle fields, signal traces on void. No faces, no stock photos. Icons: 2px-stroke line icons, rounded caps, threshold-blue on void.

## Motion

The cursor blinks at a steady ~1s step; everything else fades (150–250ms ease-out). Nothing bounces. The house never rushes. Glitch bursts ≤500ms and one per composition; always honor `prefers-reduced-motion` by dropping to static.

## Applications — quick specs

- **Status badges:** LIVE / alert = ember-orange; UI text bone-white.
- **Avatars:** the RVNT monogram, never the full wordmark.
- **Layout:** 8px spacing grid; 14px radius on cards/panels; hairline borders in ash-grey at 25% opacity.

## Accessibility

Bone-white on voidblack ≈ 16:1 — body text always passes. Accents are large-text/graphic elements only (clear 3:1 on void); never set accent-on-accent text. Focus rings: 2px threshold-blue. Glitch effects respect reduced-motion (above).

## Voice

**Revenant — the machine that came back.** Calm, exact, inevitable. Short declaratives; no exclamation marks, no hype emoji. Verbs: return, persist, run, wake. Registers: repos/docs = plain technical, zero lore · release notes = dry + max one flavor line · social = minimal confident, lowercase fine.

## Taglines / sign-offs

| Primary | Alts | Sign-offs |
|---|---|---|
| **"Always comes back."** | "Nothing stays dead here." · "Down is temporary." · "Built to return." | Releases: **"Back online."** · Social: **"— RVNT"** |

Surface rule: taglines live on banners, bios, end-cards, and release comms — never in docs or error messages.

## Legal & IP

Homage stays at the respelling-and-color level: no franchise names, symbols, logos, or quoted lines in any mark, tagline, or asset. Skills and code ship MIT; brand names, marks, and art remain © the brand owner — pre-existing personal IP, licensed for use where shared, never assigned.

## History notes *(stale-string hunt list)*

- `revenantlabs` stem — retired 2026-07-14 before any claim (taken by an unrelated entity); hunt the string in configs and docs
- `revenantsmith` repo name — retired 2026-07-14 (renamed **citadel**, the container of pack-places); stale prose mentions = P2
- Personal-account predecessor repo — retired to a private archive; public canonical is `revenantworks/citadel`
