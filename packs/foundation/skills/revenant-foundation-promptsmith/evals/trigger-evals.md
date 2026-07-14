# Trigger Evals — description tuning

Provenance: derived from revenant-foundation-promptsmith v1.0.0, 2026-07-14.

Twenty-four queries for checking whether the `description` field fires the skill at the right times. Eleven should trigger, thirteen should not. This is a **manual checklist**, fully self-contained — no script ships with this skill (skill-authoring tools such as Anthropic's skill-creator can automate description evals if you want tooling). To use: read each query cold, decide whether the current description would invoke promptsmith, and compare against the expected column. A description change that flips a should→shouldn't (or vice versa) needs a second look.

Skills are consulted for tasks the model can't trivially handle alone, so the should-not set deliberately includes both off-topic asks and prompt-adjacent asks that aren't prompt-*building*.

| # | Query | Should trigger? | Why |
|---|---|---|---|
| 1 | "Write me a prompt that turns meeting notes into action items." | ✅ yes | Build-from-scratch, the core case |
| 2 | "Can you improve this prompt? It keeps ignoring the word limit." | ✅ yes | Improve-existing + debug |
| 3 | "promptsmith" | ✅ yes | Bare invocation |
| 4 | "I need a system prompt for a customer-support bot." | ✅ yes | System / agent prompt |
| 5 | "Why isn't my prompt returning valid JSON?" | ✅ yes | Prompt debugging |
| 6 | "Rewrite this meta-prompt so it works on GPT instead of Claude." | ✅ yes | Multi-model + improve |
| 7 | "Give me a prompt template for writing cold emails." | ✅ yes | Prompt template build |
| 8 | "Which model should I run this extraction prompt on?" | ✅ yes | Model-tier recommendation |
| 9 | "Turn this rough idea into a proper prompt: summarize legal docs for clients." | ✅ yes | Rough-idea → artifact |
| 10 | "promptsmith refresh" | ✅ yes | Maintenance mode |
| 11 | "What's the capital of France?" | ❌ no | General knowledge |
| 12 | "Summarize this article for me." | ❌ no | Wants the task done, not a prompt built |
| 13 | "Write a birthday poem for my mom." | ❌ no | Content creation, not prompt-building |
| 14 | "Explain how transformers work." | ❌ no | Explanation, no prompt artifact |
| 15 | "Debug this Python function." | ❌ no | Code debugging, not prompt debugging |
| 16 | "What's the difference between Claude and GPT?" | ❌ no | Product comparison, no prompt to build |
| 17 | "Book me a flight to Denver." | ❌ no | Task automation, unrelated |
| 18 | "Translate this paragraph into Spanish." | ❌ no | Direct task |
| 19 | "Draft an email to my landlord about a repair." | ❌ no | Content drafting, not a reusable prompt |
| 20 | "What model powers Microsoft Copilot?" | ❌ no | Factual lookup, no prompt-building intent |
| 21 | "Build me a skill that reviews pull requests." | ❌ no | Skill-package build → skillsmith |
| 22 | "Audit this SKILL.md against best practices." | ❌ no | Skill audit → skillsmith (a SKILL.md contains instructions, but the deliverable is a skill, not a prompt) |
| 23 | "Build the assertion suite for this prompt card." | ❌ no | Suite authoring for an existing artifact — evalsmith |
| 24 | "Write a prompt that grades essays, and include a short eval rubric with it." | ✅ yes | In-flow eval rubric rides the prompt build |

**Edge notes.** #12 vs #1 is the sharpest boundary — "summarize this" wants output; "write a prompt that summarizes" wants an artifact. #8 and #16 both mention models, but only #8 asks which model to *run a prompt on* — the model-recommendation trigger requires a prompt in play. If real usage shows the skill firing on #12–#19, tighten the description's build-intent language; if it misses #1–#10, make the trigger list pushier. #21–#22 vs #4/#6 mark the pack boundary: prompts and system prompts (even for agents) are promptsmith; anything whose deliverable is a skill, SKILL.md, or pack routes to skillsmith. #24 vs #23 marks the evalsmith line — a rubric delivered inside a prompt build is promptsmith; a standalone suite for an existing card is evalsmith.
