# foundation — collision research (Phase C)

**Last verified: 2026-07-31 · cadence: 60 days.** Naming collisions are a
volatile surface: re-run the exact-name searches below when this stamp ages
out, and revisit the naming verdict if a claimant turns commercial or
prominent.

## C1 — the adjacent project: SkillForge

Most prominent match: **tripleyak/SkillForge** — 829★, active, v6
(https://github.com/tripleyak/SkillForge). "A skill creator that proves its
skills work": triage → RED-gate baseline → spec → fresh-context generation →
GREEN gate → adversarial review; per-skill regression evals; ecosystem health
audits; cross-runtime compile (claude|codex|agentskills). A second project of
the same genre: AgriciDaniel/skill-forge (80★,
https://github.com/AgriciDaniel/skill-forge).

| | SkillForge | foundation |
|---|---|---|
| does | evidence-gated creation of individual skills, eval loops, ecosystem audits | nine-domain build-time capability pack |
| overlap | skill build/audit (strong, vs skillwright) · eval suites (strong, vs evalwright) · token thrift for skills + description discipline (partial, vs tokenwright) | — |
| it lacks | message shaping · brand/voice · research verdicts · standalone prompt engineering · agent ops-specs · standing-config authoring — six of nine members have no counterpart | — |
| unique here | multi-domain roster with measured routing seams · registry-derived single-source build · neutral-by-default + brand-on-invoke · execution-verified trigger baselines | — |

## C2 — naming landscape (July 2026)

Ecosystem scale: GitHub topic `agent-skills` 12,931 repos · `claude-skills`
6,260 · `claude-code-plugins` 447. The functional layer is kebab-case
descriptive; `-skill(s)`, `-automation`, `-builder`, `-creator` are the
crowded functional suffixes; official plugins avoid metaphor.

Motif crowdedness (GitHub `claude+<motif> in:name` + compound searches):

| motif | verdict | evidence |
|---|---|---|
| -forge | VERY CROWDED | skillforge 2,114 repos · agentforge 1,281 · promptforge 912 · claude-forge 797★ |
| -watcher | CROWDED (monitoring niche) | 64 claude-watcher-family repos |
| -keeper | MODERATE | 34 repos, session/context keepers |
| -warden | MODERATE, name-collided | `claude-warden` claimed twice by real security tools (59★, 28★) |
| -wright | RARE as a motif | 4 hits, all Playwright misspellings — no genuine -wright family exists |
| -locker | RARE | 2 unrelated hits |

## C3/C4 — platform facts (from current docs, cited)

- Plugin renames: supported via a `renames` map in `marketplace.json`;
  installs auto-migrate on Claude Code ≥2.1.193
  (https://code.claude.com/docs/en/plugin-marketplaces — "Rename or remove a
  plugin").
- Marketplace names: **no rename mechanism** — renaming breaks every
  `<plugin>@<marketplace>` reference (same doc, "Marketplace schema"). Kept.
- Skill renames: no auto-migration documented on any surface; claude.ai is
  delete-and-reupload; on the API, a renamed zip re-uploaded to the same
  `skill_id` becomes a **new version, not a new skill**
  (https://platform.claude.com/docs/en/api/beta/skills/versions/create).
- Frontmatter limits: listing truncates `description` + `when_to_use` at
  **1,536 chars** (configurable, `skillListingMaxDescChars`); listing budget
  separately ≈1% of context window; names kebab-case; no documented platform
  max name length (house guard 64); body ≤500 lines (agentskills.io norm)
  (https://code.claude.com/docs/en/skills — "Frontmatter reference").
  House description gate: hard fail >1,024, warn ≥1,000.

> **Superseded in part, 2026-08-07 (owner decision; brand definition v2.1.0).**
> The two facts above stand as researched — marketplace names still have no
> rename mechanism, and skill renames still auto-migrate nowhere — but the
> "Kept" verdict on the marketplace name is **overturned**: the owner
> adjudicated executing the `revenant` → `revenantworks` rename anyway
> (marketplace name, `owner.name`, and all nine member names, pack 2.0.0).
> Every `<plugin>@revenant` reference breaks as this section predicted; the
> accepted cost is a single-consumer estate that migrates by local
> remove-and-re-add of the marketplace (`claude plugin marketplace add` under
> the new name, then `claude plugin update foundation@revenantworks`), plus
> claude.ai delete-and-re-upload per member under the new names. The rows
> above are kept verbatim as the record this decision was made against.

## Exact-name results — the shipped set

Surfaces searched per name: GitHub repo search · npm registry · PyPI · skill
directories (travisvn/awesome-claude-skills, ComposioHQ/awesome-claude-skills,
mcpservers.org/agent-skills). **No name in the set appears in any skill
directory checked**, and no hits exist anywhere on the shipped
`revenant-foundation-*` full names. Per bare name (accepted risks in bold):

| name | result |
|---|---|
| **skillwright** | **COLLIDING, accepted** — skillwright.app (commercial Claude-skills desktop product) · npm skillwright v0.1.1 (browser-recording→skills, 159 dl/mo) · PyPI v0.0.1 · 7 small repos. Disambiguated in shipping by the `revenant-foundation-` prefix |
| **promptwright** | **COLLIDING, accepted** — sahajamit/promptwright 113★ (AI browser automation) · PyPI promptwright (ex-Stacklok, 879★-legacy project renamed to deepfabric). Same disambiguation |
| agentwright | small collisions — agentwright.ai (consulting co.) · PyPI v0.1.0 (43 dl/mo) · 5 repos ≤0★ |
| rigwright | one fresh in-space PyPI pkg (v0.2.0, Jul 2026, Claude/Codex skill authoring, GitLab-hosted) |
| lorewright | lorewright.net (AI roleplay assistant); registries clear |
| commwright | CLEAR on all surfaces — the cleanest name in the set |
| evalwright | one 0★ AI-eval repo; registries clear |
| tokenwright | effectively CLEAR (one empty repo) |
| brandwright | dev surfaces CLEAR (offline branding agencies only) |

**Why the motif holds:** no -wright *family* exists anywhere in the ecosystem
— the family, not any single name, is the differentiator, while the adjacent
metaphor motifs run crowded (`-forge` most of all). Per family it is unowned
space versus contested space. The two accepted flagship collisions
(skillwright.app; promptwright's legacy PyPI project) are recorded above and
are what the 60-day re-verification watches.

## Supersession — 2026-08-07: the `ossuary` pack and the `-caller` motif

Owner-approved rename of the estate's second pack: `vault` → **`ossuary`**, motif
`-picker` → **`-caller`**, members `revenantworks-vault-edgepicker` →
`revenantworks-ossuary-linecaller` and `revenantworks-vault-bookpicker` →
`revenantworks-ossuary-cardcaller`. **`-picker` is released back to unclaimed.**
The C2 method was re-run live against the new names *before* any file moved —
the rename was gated on the result, and this is the record it was gated on.
Verified 2026-08-07; same 60-day cadence as the rest of this file.

Motif crowdedness (GitHub `claude+<motif> in:name` + compound searches):

| motif | verdict | evidence |
|---|---|---|
| -caller | **RARE as a skill/agent motif** | `claude+caller in:name` = 4 repos, **all 0★** (Rahman-12/claude-ai-caller, vishalhalbe/vedic-caller-claude, dani-montesdeoca-f/react-states-claude-caller, androbwebb/claude-web-self-caller) — API-call toys, no skill or agent framework among them · `skillcaller` **0 repos** · `promptcaller` **0 repos** · `agentcaller` 3 repos, all 0★ and all voice-phone agents (Dacekey/AgentCaller, gianpaj/agentcaller-io, anuj2806/agentCallerBackend) — a different domain · `toolcaller` 4 repos, max 1★ · `codecaller` 6 repos, all 0★ · `caller+claude-code in:name` and `agent-skills+caller in:name` both **0**. No `-caller` *family* exists in the agent-skill ecosystem — the same unowned-space condition that made `-wright` hold |
| -picker *(released)* | MODERATE, **released 2026-08-07** | `claude+picker in:name` = 43 repos, top claimants small and all session-pickers rather than domain skills (espositov/claude-code-session-picker 9★, anshul-garg27/claude-picker 6★, danielrosehill/Claude-Agent-Picker-Pattern 4★). Not why it was dropped — the pack's metaphor moved, and the motif is now unclaimed and re-usable |

Exact-name results — the renamed set (surfaces: GitHub repo search · npm registry ·
PyPI · crates.io · skill directories travisvn/awesome-claude-skills and
ComposioHQ/awesome-claude-skills):

| name | result |
|---|---|
| `ossuary` *(pack word)* | **MODERATE, no prominent claimant — accepted.** 39 GitHub repos, all hobby-scale and abandoned: top is mrmekon/ossuary 20★ (Rust library for encrypted comms; crates.io `ossuary` 0.5.1, last updated **2019-06-12**, 4,189 downloads all-time and **10 recent**), then anicka-net/ossuary-risk 5★, hosom/ossuary 3★, bugsyhewitt/ossuary 2★ (an offensive-security tool in a "necromancer suite" — same vocabulary well, unrelated space), logalleon/ossuary 2★ · npm `ossuary` **exists**: v1.1.11, owner logalleon, "a language parser", last published **2021-10-20** · PyPI `ossuary` **exists**: 0.1.0a0, Bradd Szonye, dice-probability toolkit, uploaded **2023-03-06**, downloads unreported · **`claude+ossuary in:name` = 0** — nothing in the Claude/agent-skill space at all, and no shipped name is the bare word (members ship as `revenantworks-ossuary-*`). Comparable to `-keeper`'s MODERATE above (34 repos), and far below the bar set by the accepted `skillwright` collision (a live commercial product) |
| `linecaller` | **RARE.** 7 GitHub repos, **all 0★** and all pickleball/tennis line-calling toys — usernames withheld here after a 2026-08-20 name-scan match confirmed coincidental against an unrelated GitHub handle; repo count and verdict unchanged · npm **404** · PyPI **404** · crates.io **404** · no product or company found by name search (results returned Truecaller, Line2, Linear — no LineCaller) |
| `cardcaller` | **RARE.** 1 GitHub repo (`cardcaller/public`, 0★) · npm **404** · PyPI **404** · crates.io **404** · no product or company found by name search |

Skill directories: **no `caller` or `ossuary` entry in either directory checked.**
travisvn/awesome-claude-skills has zero matches on `caller`, `ossuary`, or
`picker`; ComposioHQ/awesome-claude-skills has one unrelated "Picker" mention and
no `caller` or `ossuary`. A targeted web search for `ossuary` as a Claude
skill/agent/plugin returned nothing in the ecosystem.

**Recorded risk, not a collision:** `caller` is a loaded word in LLM vocabulary —
"tool caller" / "function calling". `skill+caller in:name` returns 5 tiny repos
(max 9★) that are literally tool-calling skills. This is *semantic* ambiguity in
cold-listing routing, not a name claim; it costs nothing on the registries and
does not move the verdict, but it is the thing a `-caller` sibling's trigger evals
should probe — a bare "caller" query is weaker evidence of intent here than a bare
"picker" query was.

**Verdict: gate passed.** `-caller` is RARE, no prominent exact-name claimant
exists for `linecaller`, `cardcaller`, or `ossuary`, and the rename executed.

## Supersession — 2026-08-08: `cardcaller` → `bonecaller`

Owner-directed member rename inside the claimed `-caller` motif (motif itself
unchanged; the 2026-08-07 claim above stands). The C2 exact-name method was
re-run live against the candidate *before* any file moved — the rename was
gated on the result, and this is the record it was gated on. Verified
2026-08-08; same 60-day cadence as the rest of this file.

| name | result |
|---|---|
| `bonecaller` | **UNCLAIMED.** GitHub repo search: **0 repos** · npm **404** · PyPI **404** · crates.io **404** (checked with a proper User-Agent — crates.io 403s bare clients). Cleaner evidence than `cardcaller`'s own row above, which carried one 0★ namesake |
| `shotcaller` *(runner-up, rejected)* | npm **claimed** (`shotcaller`, a dormant 2021 appointment-scraper) · GitHub: spicylobstergames/shotcaller-godot **296★** + shotcaller-minigene 156★ (game project) · PyPI 404 · crates.io 404. Fails the bar the 2026-08-07 rows set — a starred namesake plus a registry claim |

**Verdict: gate passed.** `bonecaller` executed as ossuary 2.0.0; `cardcaller`
joins `-picker` in the released-back-to-unclaimed column.

## Source URLs

GitHub API repo searches (`api.github.com/search/repositories?q=<term>`),
npm registry (`registry.npmjs.org/<name>`), PyPI (`pypi.org/project/<name>/`),
plus: github.com/tripleyak/SkillForge · github.com/AgriciDaniel/skill-forge ·
npmjs.com/package/skillwright · pypi.org/project/skillwright/ ·
skillwright.app · github.com/sahajamit/promptwright ·
pypi.org/project/promptwright/ · github.com/nolabs-ai/deepfabric ·
agentwright.ai · pypi.org/project/agentwright/ · pypi.org/project/rigwright/ ·
lorewright.net · github.com/anthropics/skills ·
github.com/anthropics/claude-plugins-official · agentskills.io ·
skillsmp.com · claudemarketplaces.com ·
github.com/travisvn/awesome-claude-skills ·
github.com/ComposioHQ/awesome-claude-skills · mcpservers.org/agent-skills ·
code.claude.com/docs/en/plugin-marketplaces · code.claude.com/docs/en/skills ·
platform.claude.com/docs/en/api/beta/skills/versions/create

**Added for the 2026-08-07 supersession:** GitHub API repo searches for
`claude+caller`, `skillcaller`, `agentcaller`, `promptcaller`, `toolcaller`,
`codecaller`, `linecaller`, `cardcaller`, `ossuary`, `claude+ossuary`,
`claude+picker`, `caller+claude-code`, `agent-skills+caller`, `skill+caller`
(all `in:name`) · registry.npmjs.org/{linecaller,cardcaller,ossuary,skillcaller,
agentcaller,promptcaller,claude-caller} · pypi.org/pypi/{same}/json ·
crates.io/api/v1/crates/{ossuary,linecaller,cardcaller} ·
github.com/mrmekon/ossuary · github.com/bszonye/ossuary ·
npmjs.com/package/ossuary · pypi.org/project/ossuary/
