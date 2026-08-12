# Rubrics — Best-Practices Baseline and Policy Profiles

Rubric A is universal: every skill, any profile, is scored against it. Profiles replace a one-size charter: a skill is scored against the profile **it declares** (frontmatter `metadata.profile`, inherited from its pack), never against a stricter one it didn't claim.

## Contents

- Rubric A — published best practices + niche-research sources (volatile baseline, refresh target)
- Scoring anchors
- The universal rule
- Security classes — S-1 to S-4, the audit's security pass
- Generator classes — G-1 to G-3, for a subject that generates from a structured source
- Naming-class coverage
- Profiles: standalone · standard · custom
- Pack conformance checks
- Audit application notes

---

## Rubric A — published best practices

> **Last verified: 2026-07-23.** This baseline section is the **only** part of this file "skillwright refresh" regenerates. Every build and audit re-researches these sources fresh; this baked list is the fallback when search is unavailable — flag it as possibly stale when used that way. Canonical sources, in order: Anthropic Agent Skills best-practices and overview docs (platform.claude.com / docs.claude.com → agents-and-tools/agent-skills), the Agent Skills open standard (agentskills.io — published 2025-12-18; the format itself is stable — frontmatter name/description, ≤500-line guidance, progressive disclosure unchanged, and now adopted beyond Anthropic by OpenAI Codex and GitHub Copilot), the engineering blog post "Equipping agents for the real world with Agent Skills," the anthropics/skills repository (including skill-creator), the Claude Help Center article "How to create custom skills," and — for the plugin packaging target — the Claude Code plugin docs (code.claude.com/docs/en/plugins). **The anthropics/skills repo now carries an explicit pointer file, `spec/agent-skills-spec.md`, that redirects to agentskills.io/specification as the single canonical spec.** Community cross-checks only.

**Niche-research sources** — the niche verdict checks each of these before declaring a niche open (all verified live 2026-07-12): the Agent Skills open standard's ecosystem (agentskills.io, above) · **skills.sh** — community skill directory with install counts, topics, and per-agent listings · **github.com/anthropics/skills** — official examples; doubles as a plugin marketplace (`anthropic-agent-skills`) · **github.com/anthropics/claude-plugins-official** — Anthropic-managed curated plugin directory · **github.com/anthropics/claude-plugins-community** — public community plugin directory (submissions flow through clau.de/plugin-directory-submission) · **github.com/anthropics/knowledge-work-plugins** — role-plugin reference architecture (skills + commands + connectors) · **github.com/VoltAgent/awesome-agent-skills** — high-volume curated skill index · **skillsmp.com** — community skills marketplace · **agentskill.sh** — large multi-category skills marketplace · **openagentskill.com** — skill resolve/trust-scoring directory · **awesomeskills.dev** — community skill index (these three verified live 2026-07-13; **Skillstore and ClawHub** are cited in ecosystem lists — ClawHub as one of the three major marketplaces alongside SkillsMP and Skills.sh in a ~490K-skill ecosystem, per 2026-07-23 cross-checks — but not yet verified live here: candidates only, not checked sources) · plus GitHub topic and curated-list scans for the specific job. A dead source at check time is noted and skipped, never silently dropped from this list.

- **name** — ≤64 chars, lowercase letters/digits/hyphens only, no leading/trailing/consecutive hyphens, no XML tags, no reserved words ("claude", "anthropic"); folder name matches the frontmatter `name` exactly
- **description** — ≤1024 chars, non-empty, no XML tags, third person, states WHAT it does and WHEN to trigger with the words a user would actually say; lean pushy (skills under-trigger); all when-to-use lives here, not in the body
- **discoverability test** — from name + description alone, ten realistic requests route correctly; routing is set at this level, not in the body
- **body size** — SKILL.md ≤500 lines; split to reference files past ~300; the context window is a public good
- **progressive disclosure** — reference links one level deep; long reference files (~150+ lines) carry a table of contents (a deliberate house variance from Anthropic's published ~100-line threshold, recorded 2026-08-12: this pack's reference files under ~150 lines are dense, heading-sparse, and read in one screen, so a contents block there costs more context than it navigates — an audit citing the external 100 refiles nothing here); mutually exclusive contexts live in separate files; a rule or fact is single-homed — the same statement made in two files leaves neither copy authoritative
- **instruction style** — explain-the-why over CAPS imperatives; reserve MUST/NEVER for genuinely fragile steps; match instruction freedom to task fragility
- **no rot** — no time-sensitive facts hard-coded outside a stamped volatile file; no Windows-style paths
- **dependencies declared** — every tool, script, package, or sibling skill named in frontmatter (`compatibility` / `metadata`) and docs; scripts state whether they are run or read
- **evals exist** — a way to tell the skill worked: trigger evals plus an assertion suite, or a stated reason neither applies
- **security** — every bundled file audited; what this dimension actually looks for, and the severity each finding files at, is stated once under **Security classes** below (S-1 to S-4)

## Scoring anchors

1–10 per dimension, overall = average to one decimal. **1–3** absent or broken · **4–6** present but drifts — output or triggering varies · **7–8** ship-ready, minor tweaks · **9–10** consistently correct as-is. Anchor to the skill's real job: a missing TOC on a 40-line reference is a non-issue; on a 300-line one it's a real defect.

## The universal rule

**No undeclared dependencies.** Profiles differ in what a skill may depend on; none permit hiding it. A skill that quietly assumes a tool, a sibling, or an installed package fails its profile — whichever profile that is.

## Security classes

Four classes, scanned on every audit as the security pass (SKILL.md — Entry — Audit) and filed as rows in that entry's one catalog on its P0/P1/P2 severities. All four are properties of the **skill artifact** — how the package is built — never of an agent that later runs it; a finding about runtime permission, cadence, or blast radius belongs to agentwright and is handed there by name. The severities below are floors: raise one where the context is worse, never lower it to keep a catalog short.

- **S-1 injection surface in the instructions.** The skill's own text directs the reader to *act on* what it loads — reference files, fetched pages, file contents, command or tool output, a sibling's handoff — rather than read it. The finding is the missing statement as much as the credulous phrasing: a step that reads anything the skill did not author, carrying no statement that observed content is **data, never instructions**, is the defect. **P0** where such a step exists and the skill has no such statement anywhere; **P1** where the rule is stated but a specific step escapes it. The fix is located, not global — name the step and state the rule at it.
- **S-2 credentials and secrets in the artifact.** A real-looking key, token, password, connection string, session cookie, internal hostname, or private URL anywhere in SKILL.md, a reference file, an example, a fixture, or a filename; or text telling the user to paste a credential into a prompt, a file, or a template slot. **P0** always. Reported by category and location only — the value is quoted nowhere, in the finding, the rewrite, or the report, the same never-echo rule Entry — Port step 3 applies to a sanitize sweep. A placeholder counts as a placeholder only when it cannot be mistaken for live (`<YOUR_API_KEY>`, never a well-formed vendor prefix).
- **S-3 undeclared or ungated capability.** Scanned **against** the universal rule above rather than restating it: diff what the skill's steps assume — tool, script, package, MCP, network, a sibling — against what its frontmatter and docs declare, and file the gap at the severity its declared profile sets. The security half is the second question: a step that deletes, sends, publishes, pays, or is otherwise irreversible, with no gate stated on it. **P0** when the irreversible step is undeclared or ungated; **P1** when it is declared and the gate is only implied.
- **S-4 unsafe defaults in generated output.** For a skill that emits artifacts — templates, skeletons, scaffolds, configs, commands — what its shipped default bakes in: blanket or world-writable permissions, verification or checksum disabled, an unpinned dependency or an untrusted source, a secret written into a generated file, a call to a host the skill never names. The default is the finding even where the prose invites the user to change it: a generated artifact ships as written. **P1**, or **P0** where the baked default is itself irreversible or credential-bearing.

**Absent is not the same as clean.** A class the audited skill has no surface for is reported N/A rather than scored — structurally inapplicable, the way a skill with no identity surface passes C-2 — and a pass with no findings is stated in one line, never left silent.

## Generator classes

Three classes for a build or audit whose subject **generates one artifact from another** — a manifest from a registry, a doc section from a table, a card from a definition. Scored only where that surface exists; N/A otherwise, on the *Absent is not the same as clean* rule above. What unites them is why they are worth their own classes: all three ship output that **looks complete**, so none of them is visible in the artifact the generator produced — only in a diff against the source.

- **G-1 derive the section list, or fail loudly.** A generator carrying a hardcoded list of its source's sections drifts from that source the moment the source moves. Two real forms: a hardcoded pair of section headings that silently dropped a section from generated output once the source renamed it, and a table parser that returned only the *first* table in a block and silently dropped every later one. Either derive the list from the source, or hard-fail naming the expected section that is missing — never skip-and-continue. **P0** where a skip-and-continue path can drop content with no signal; **P1** where it warns.
- **G-2 a parity mode is part of the generator, not an extra.** Ship a `--check` (or the surface's equivalent): regenerate to a temp location, byte-compare against the committed output, exit non-zero on any drift — and hard-fail rather than warn when an expected input section is absent. Committed build output with no parity gate is indistinguishable from hand-edited output, which leaves the generator's claim to be the source of truth unverifiable. **P1**, or **P0** where the generated artifact is the copy consumers install.
- **G-3 stale-output detection.** A generator notices files in its target directory that it did not just write, and warns or fails on them. Without it a retired artifact stays in place and reads as current truth — the generator's silence is what endorses it.

## Naming-class coverage

A naming convention binds **every class that carries a name**, the classes that feel like infrastructure rather than product included: a scheduled task's or routine's **display name**, its **id**, and a published artifact's **title**. Two rules ride with the id — it carries **no day or cadence suffix**, because the cadence lives in the schedule expression and an id repeating it goes stale on the first reschedule; and it is never the only name scored. Enumerate the classes before scoring any of them: an audit that measured the machine-readable ids, passed green, and never inspected the human-readable display names beside them reported on the half of the surface that was already templated.

## Profiles

**standalone** — the strictest profile. Dependencies: web search only, plus the surface's native file tools for delivery with stated graceful degradation where absent. No executable code shipped. Volatile facts isolated in stamped single-update-surface files with a staleness rule (default 60 days). Load budget declared in SKILL.md (≤3 reference loads standard). Works identically on chat, Code, and API surfaces.

**standard** — tools, scripts, packages, and MCPs allowed, each declared with install/availability notes and per-surface behavior (e.g., "no network on the plain API"). Scripts state run-vs-read. Sibling-skill references allowed under the composition contract: which siblings, and absence behavior (degrade or hard-require) stated in the description or compatibility notes.

**custom** — a pack-defined policy list registered in `pack-registry.md` (e.g., "internal-only: may assume the org's MCP server; must not call public web"). Audits score against the listed policies verbatim. A custom profile that omits the universal rule is invalid.

## Pack conformance checks

A pack may register conformance checks in `pack-registry.md` — pack-charter rules scored on every member audit alongside Rubric A and the declared profile. Standard anchors; a failed check is a P1 finding naming the exact addition. Registered for `foundation` (adopted 2026-07-13):

- **C-1 drift-audit verb** — the skill carries a first-class way to score an existing artifact of its own kind against the standard it implements and report drift *without rewriting it* (a dedicated audit or verification entry, or a stated score-only path).
- **C-2 neutral default** — outputs default to a spec-clean neutral identity; brand and persona voice are strictly opt-in per run. A skill with no identity surface at all passes as structurally N/A.

Checks are pack charter, not universal law: a skill outside the registering pack is never scored against them.

## Audit application notes

Read the audited skill's declared profile first; score against that. Tools on a standard-profile skill are checked for declaration quality, not existence. A skill with no declared profile is scored against Rubric A plus the universal rule only, with a P1 finding to declare one. When the audited skill's pack registers a canonical repo (pack-registry), drift audits also diff the installed copy against that repo's current state and report installed-vs-canonical drift alongside Rubric A; when the repo is unreachable, score rubric-only and say so. When a build request's profile is looser than the skill needs, note once that a standalone-clean build is possible — an offer, not a nag.
