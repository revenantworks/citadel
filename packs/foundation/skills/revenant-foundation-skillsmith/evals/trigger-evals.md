# Trigger Evals — description tuning

Provenance: derived from revenant-foundation-skillsmith v1.0.0, 2026-07-14 (queries 27–30 added at 1.1.0 for Entry — Integrate; 31–34 added at 1.2.0 for Entry — Pack).

Thirty-four queries for checking whether the `description` fires skillsmith at the right times. Eighteen should trigger, sixteen should not. Manual checklist, fully self-contained — read each cold against name + description only and compare to the expected column.

| # | Query | Should trigger? | Why |
|---|---|---|---|
| 1 | "Build me a skill that summarizes legal contracts into risk memos." | ✅ yes | Build-from-scratch, the core case |
| 2 | "Turn the workflow we just did into a skill." | ✅ yes | Extract-from-conversation build |
| 3 | "skillsmith" | ✅ yes | Bare invocation |
| 4 | "Audit my skill against current best practices." | ✅ yes | Audit-existing |
| 5 | "Does this SKILL.md meet the spec? Score it." | ✅ yes | Audit + scoring |
| 6 | "Is there actually a niche for a skill that does invoice triage?" | ✅ yes | Niche/market analysis |
| 7 | "skillsmith configure" | ✅ yes | Brand/naming configuration |
| 8 | "Apply my company's branding to the skills we generate." | ✅ yes | Brand inheritance setup |
| 9 | "Package this skill folder so I can install it." | ✅ yes | Release packaging |
| 10 | "skillsmith refresh" | ✅ yes | Baseline maintenance |
| 11 | "Write me a prompt that summarizes legal contracts." | ❌ no | Prompt, not skill — promptsmith's job |
| 12 | "Improve this system prompt for my support agent." | ❌ no | Prompt improvement — promptsmith |
| 13 | "What are Claude skills and how do they work?" | ❌ no | Explanation, no artifact to build |
| 14 | "Install the PDF skill for me." | ❌ no | Installation, not authoring |
| 15 | "Build me a web app that tracks invoices." | ❌ no | Software build, not a skill package |
| 16 | "Summarize this document." | ❌ no | Wants the task done, not a skill built |
| 17 | "Design a logo and brand palette for my company." | ❌ no | Brand creation, not brand-to-skill configuration |
| 18 | "Write a README for my Python library." | ❌ no | Docs for code, not a skill package |
| 19 | "Which model should I run this prompt on?" | ❌ no | Model routing — promptsmith |
| 20 | "Make me a project plan for Q3." | ❌ no | Planning task, unrelated |
| 21 | "Port this skill pack so I can use it at my job — branding out, new names." | ✅ yes | Port — rebrand for a new owner |
| 22 | "Strip the branding and any personal references out of these skills." | ✅ yes | Port — sanitize sweep |
| 23 | "Make this skill set neutral and rename everything for a client handoff." | ✅ yes | Port — neutral re-issue |
| 24 | "Port this python app to linux." | ❌ no | Software porting — no skill set involved |
| 25 | "Write the trigger evals and test cases for my existing skill — don't touch the skill itself." | ❌ no | Suite authoring for an existing target — evalsmith |
| 26 | "Build me a skill that triages invoices, and make sure it ships with a full eval suite." | ✅ yes | The build owns the package; the suite ships via the evalsmith handoff |
| 27 | "skillsmith integrate tokensmith" | ✅ yes | Direct integrate invocation |
| 28 | "Add the new member to the pack and update the rest of the skills with the integration." | ✅ yes | Pack propagation in natural language — roster restamp + registry + release set |
| 29 | "Integrate my app with the Stripe API." | ❌ no | Software integration, not pack propagation — no skill, pack, or roster in sight |
| 30 | "keep going" | ❌ no | Bare continuation outside a pack build's offer — ordinary conversation; only the continuation context routes it |
| 31 | "Build me a pack of skills for a presales engineer at a software company." | ✅ yes | Whole-pack design-and-build from a role — the Entry — Pack core case |
| 32 | "skillsmith pack — research what a technical writer needs and build the roster." | ✅ yes | Direct pack invocation with domain research |
| 33 | "What skills are in the foundation pack?" | ❌ no | Roster lookup, not a design or build — the manifest answers it |
| 34 | "Build me a starter pack of prompts for cold sales emails." | ❌ no | A pack of prompts, not skills — promptsmith's job; "pack" alone doesn't route here |

**Edge notes.** #31 vs #34 is the pack boundary — a pack of *skills* routes here; a pack of *prompts* is promptsmith's even with identical phrasing. #33 marks lookup vs build. #28 vs #29 is the integrate boundary — pack/roster/member vocabulary routes here; "integrate" against an app or API does not. #30 only fires when a pack build just offered the continuation.

**Original edge notes.** #1 vs #11 is the sharpest boundary — "build a skill that does X" wants a package; "write a prompt that does X" wants promptsmith. #8 vs #17 splits applying an existing brand (configure) from inventing one (out of scope). #24 is the port near-miss — "port" alone is ambiguous; the description anchors it to skill sets. #26 vs #25 marks the evalsmith line — a suite for a skill being built ships with the build; a suite for an existing skill routes to evalsmith. If real usage misses the yes-set, push the trigger verbs harder; if it fires on the no-set, tighten the boundary sentences.
