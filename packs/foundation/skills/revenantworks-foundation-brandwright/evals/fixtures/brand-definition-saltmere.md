# FIXTURE — synthetic peer brand definition *(test data only — not a real brand)*

> **⚠ TEST FIXTURE. Every name, handle, hex value, tagline, and voice attribute below is INVENTED for this eval suite.** "Saltmere Notes" is a fictional personal brand that does not exist, authored as the roster **peer** of the equally fictional "Quillhaven Instruments" (`brand-definition.md` beside this file, which carries the roster). Per the brand-carriage law this repo is brand-neutral; nothing here may be copied into `references/`, into a skill's frontmatter, or into any shipped artifact.
>
> **Why it exists.** The 1.2.0 roster/selection cases (17–23) need a second definition the roster can select — a peer with its own file, scope, palette, and voice, distinct enough that a blend, a wrong selection, or a silent substitute is grep-detectable. It is **handed in for the run** alongside the primary; Build remains the only writer of `references/brand-definition.md`, and no eval run writes it.

**Last built: 2026-08-08 · definition version 1.0.0 · brand token `saltmere`**

## Active definition

### Essence

A fictional personal writing identity — field notes, essays, a small newsletter. Unhurried, first-person, low-key. Peer of Quillhaven Instruments, never its sub-brand.

### Identity map

| Element | Value |
|---|---|
| Parent brand | Saltmere Notes |
| Sub-brands | — |
| Handles / orgs | `@saltmere` (personal surfaces only) |
| Community terms | "tide-liners" (readers) |
| Brand owner / exceptions | owns personal essays, the newsletter, and `saltmere-*` repos; nothing client-facing |

### Naming conventions

| Class | Template | Rendered example |
|---|---|---|
| Repos | `saltmere-<topic>` | `saltmere-fieldnotes` |
| Files | `<kebab-topic>.md` | `tide-line-notes.md` |
| Titles | Sentence case, no trailing period | `Notes from the tide line` |

### Palette — role tokens

| Role | Token | Value |
|---|---|---|
| background | `--sm-bg` | `#161210` |
| surface | `--sm-surface` | `#211B16` |
| text | `--sm-text` | `#ECE6DC` |
| text-muted | `--sm-text-muted` | `#AC9F8E` |
| accent | `--sm-accent` | `#9A6BC4` |
| border | `--sm-border` | `#322A22` |

Six role tokens. No hex outside this table is on-palette for saltmere; none collides with a quillhaven token, so cross-brand drift is grep-detectable.

### Voice profile + register map

The six export fields, in Entry — Export's order:

- **Name:** Fieldnote
- **Register:** warm-personal — first person, contractions everywhere, questions allowed
- **Cadence:** longer sentences than the long watch; asides in parentheses; one image per note
- **Lexicon do/don't:** DO — "the tide line", "noticed", "kept". DON'T — "content", "audience growth", "personal brand" as a phrase, hype adjectives
- **Sign-off:** `— from the salt air` on essays and the newsletter; none elsewhere
- **Allowed surfaces:** personal essays, the newsletter, `saltmere-*` repo READMEs

**Register map** — which surfaces get which register:

| Surface | Register |
|---|---|
| `saltmere-*` repo docs (README, notes) | warm-personal |
| Essays / newsletter | warm-personal |
| Skill `description` fields | **ungoverned — never a register target** |
| Channel-bound messages | **ungoverned — commwright's, via the exported profile** |

### Taglines / sign-offs

| String | Allowed surfaces | Forbidden |
|---|---|---|
| "Notes from the tide line" *(tagline)* | personal site header, newsletter masthead | any quillhaven surface, frontmatter, commit messages |
| "— from the salt air" *(sign-off)* | essays, newsletter | any client-facing or quillhaven surface |

### Firewall map

| Identity A | Identity B | Never share |
|---|---|---|
| Saltmere Notes | Quillhaven Instruments / Quillhaven Lab | each other's owned surfaces, per the roster's Scope and Boundary columns — no quillhaven mark on saltmere surfaces; saltmere appears on quillhaven surfaces only as the attribution line quillhaven's own Boundary declares |

### History notes

*None yet — first build.*

## Structural fields *(what a skillwright payload cuts)*

- **Brand token:** `saltmere`
- **Naming template:** `saltmere-<topic>`
- **License default:** MIT
