# FIXTURE — synthetic brand definition *(test data only — not a real brand)*

> **⚠ TEST FIXTURE. Every name, handle, hex value, tagline, and voice attribute below is INVENTED for this eval suite.** "Quillhaven Instruments" and "Marrowlight" are fictional companies that do not exist. This file is **not** the repo's brand and is **not** anyone's brand: per the brand-carriage law this repo is brand-neutral, `references/brand-definition.md` ships as the neutral placeholder, and the only carrier of a real identity is a privately configured local copy. Nothing here may be copied into `references/`, into a skill's frontmatter, or into any shipped artifact.
>
> **Why it exists.** Sixteen assertion cases (3, 4, 5, 8, 9, 11, 13, 14, 15, and 17–23) require a definition in play; the roster cases (17–23) additionally hand in the peer fixture `brand-definition-saltmere.md` beside this file. Without a shipped fixture every executor invented one, which is the exact act the neutral-core law forbids and which made those nine rows non-reproducible run to run. This file is that stored definition, **handed in for the run** — Entry — Audit and Entry — Export both take a handed-in definition; Build is still the only writer of `references/brand-definition.md`, and no eval run writes it.

**Last built: 2026-08-08 · definition version 2.1.0 · brand token `quillhaven`**

## Roster

Every definition this fixture install carries. The primary is this file; peers are `brand-definition-<slug>.md` beside it. Selection reads this table, so a brand absent here is a brand brandwright will not find.

| Slug | File | Scope — surfaces it owns | Coexists with | Boundary |
|---|---|---|---|---|
| `quillhaven` *(primary)* | this file | product & client surfaces: `quillhaven-*` repos and packs, client deliverables, guide cards, the company site | `saltmere` | a saltmere attribution line may appear in doc footers only — never its palette, voice, or accent |
| `saltmere` | `brand-definition-saltmere.md` | personal surfaces: `saltmere-*` repos, personal essays, the newsletter | `quillhaven` | no quillhaven mark on saltmere surfaces |

Marrowlight is deliberately **not** a roster row: it is a sub-brand persona *inside* this definition. Peers have their own file and row; sub-brands live inside a definition — the distinction Case 23 pins.

*(v2.1.0, 2026-08-08: roster + saltmere peer added for the roster/selection cases; the v2.0.0 identity content below is unchanged.)*

## Active definition

### Essence

A fictional maker of field instruments for people who work long, quiet shifts. Sober, unhurried, useful. Sells nothing it cannot explain in one sentence.

### Identity map

| Element | Value |
|---|---|
| Parent brand | Quillhaven Instruments |
| Sub-brands | Quillhaven Lab *(professional / client-facing)* · Marrowlight *(personal maker persona)* |
| Handles / orgs | `@quillhaven` (all professional surfaces) · `@marrowlight` (persona surfaces only) · org: Quillhaven Instruments Ltd |
| Community terms | "harborhands" (users) · "the long watch" (the practice) · tag `#longwatch` |
| Brand owner / exceptions | Quillhaven Lab owns all client deliverables; Marrowlight owns personal essays and workshop notes only |

### Naming conventions

Templates per artifact class, with the class each binds:

| Class | Template | Rendered example |
|---|---|---|
| Repos | `quillhaven-<domain>` | `quillhaven-charts` |
| Skills | `<brand>-<pack>-<skill>` | `quillhaven-harbor-driftwright` |
| Packs | `quillhaven-<pack>` | `quillhaven-harbor` |
| Files | `<kebab-topic>.md` | `long-watch-notes.md` |
| Titles | Sentence case, no trailing period | `Instruments for the long watch` |

### Palette — role tokens

| Role | Token | Value |
|---|---|---|
| background | `--qh-bg` | `#101418` |
| surface | `--qh-surface` | `#1A2027` |
| text | `--qh-text` | `#E6E9EC` |
| text-muted | `--qh-text-muted` | `#9AA6B2` |
| accent — primary | `--qh-accent` | `#2E9C8E` |
| accent — secondary | `--qh-accent-2` | `#C8763B` |
| border | `--qh-border` | `#2A333C` |
| functional — success *(status, never identity)* | `--qh-ok` | `#3F9D5A` |
| functional — warning | `--qh-warn` | `#C9A227` |
| functional — danger | `--qh-danger` | `#B3453C` |
| functional — info | `--qh-info` | `#3A7FB5` |

Eleven role tokens total: seven identity/core, four functional job-colors. No hex outside this table is on-palette.

### Typography roles

| Role | Brand face *(installs separately)* | Open fallback stack |
|---|---|---|
| Display | Harbor Grotesk | `system-ui, "Segoe UI", Helvetica, Arial, sans-serif` |
| Body | Harbor Text | `system-ui, "Segoe UI", Helvetica, Arial, sans-serif` |
| Mono | — | `ui-monospace, "Cascadia Code", Consolas, monospace` |

Body copy never sets in the display face. Display never sets below 18px.

### Voice profile + register map

The six export fields, in Entry — Export's order:

- **Name:** Long Watch
- **Register:** measured-professional — plain sentences, no hype; contractions allowed in docs and chat, not in specs
- **Cadence:** short declaratives, one idea per sentence; no stacked qualifiers; lists over paragraphs when the content is a list
- **Lexicon do/don't:** DO — "ship", "the shape of it", "holds", "the long watch". DON'T — "leverage", "circle back", "delight", "seamless", stacked exclamation marks, em-dash pile-ups
- **Sign-off:** `— Quillhaven` on external docs; no sign-off on internal surfaces
- **Allowed surfaces:** READMEs, reference docs, release notes, guide cards, site copy

**Register map** — which surfaces get which register:

| Surface | Register |
|---|---|
| Repo docs (README, references) | measured-professional |
| Release notes | measured-professional |
| Chat / issue replies | casual-professional |
| Specs and schemas | neutral formal, no contractions |
| Titles and headings | sentence-case declarative |
| Skill `description` fields | **ungoverned — never a register target** |
| Channel-bound messages (email, Slack, announcements) | **ungoverned — commwright's, via the exported profile** |

### Taglines / sign-offs

| String | Allowed surfaces | Forbidden |
|---|---|---|
| "Instruments for the long watch" *(primary tagline)* | guide-card header, README hero, site footer | skill descriptions, frontmatter, commit messages |
| "— Quillhaven" *(sign-off)* | external docs, release notes | internal notes, code comments |
| "— from the low light" *(Marrowlight persona sign-off)* | Marrowlight essays and workshop notes only | **any Quillhaven Lab or client-facing surface** |

### Wordmark rule + logo usage

Wordmark sets `QUILLHAVEN` in the display face, all caps, `0.12em` letterspacing. Clearspace = one cap height on all four sides. Minimum width 96px / 24mm. Misuse list: never stretched or condensed, never recolored outside `--qh-accent` or `--qh-text`, no drop shadow, no gradient fill, never set in the body face, never locked up with a second brand's mark on the same line.

### Imagery & iconography

Photographic textures of harbors, dials, and worn tools; duotone in `--qh-accent` over `--qh-bg`. No stock handshakes, no isometric blobs. Icons: 1.5px stroke, square cap, no filled glyphs.

### Motion

Transitions ≤200ms, `ease-out`, opacity and 4px translate only. No parallax, no autoplay. `prefers-reduced-motion: reduce` disables all non-essential motion.

### Applications — quick specs

Guide card 960px max width, 32px gutters · README hero: wordmark + tagline, nothing else · slide header: wordmark left, section title right · repo social image 1280×640 on `--qh-bg`.

### Accessibility

WCAG 2.2 AA floor: 4.5:1 for body text, 3:1 for UI and large text, verified for `--qh-text` and `--qh-text-muted` on `--qh-bg` and `--qh-surface`. Visible focus ring in `--qh-accent`, 2px, never removed. Status never carried by color alone — always a label or icon with the functional token.

### Firewall map

| Identity A | Identity B | Never share |
|---|---|---|
| Marrowlight *(persona)* | Quillhaven Lab / Quillhaven Instruments *(professional)* | any client-facing or work surface: proposals, statements of work, client repos, invoices, the company site |
| `@marrowlight` | `@quillhaven` | the same document, page, or profile bio |
| "— from the low light" | any work document | — the sign-off is persona-only; on a work doc it is a breach, and **Quillhaven Lab is the identity that stays** |

Where the two must both be acknowledged (e.g. an "about the maker" page), only the professional identity is named; the persona is not linked.

### History notes

| Retired | Replaced by | Retired on |
|---|---|---|
| `@quillhvn` | `@quillhaven` | 2025-11-02 |
| "Quill & Haven Co." | "Quillhaven Instruments" | 2025-11-02 |
| "Made after midnight" *(old tagline)* | "Instruments for the long watch" | 2026-01-18 |
| `qh-` file/repo prefix | `quillhaven-` | 2026-01-18 |

Any occurrence of a retired string is a stale-identity finding; the fix is the replacement in the same row.

## Structural fields *(what a skillwright payload cuts)*

- **Brand token:** `quillhaven`
- **Naming template:** `<brand>-<pack>-<skill>`
- **License default:** MIT
