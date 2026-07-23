# Description Crafting — Routing Is Set Here

The description decides whether a built skill ever runs. Load this file when writing or fixing one.

## Rules

- **≤1024 characters, third person, what + when.** State what the skill does, then the conditions that should fire it — in the words a user would actually type, not the author's jargon. All when-to-use information lives here; the body is never consulted for routing. **No unquoted colon-space inside the text** — YAML parses `: ` as a nested mapping and the frontmatter fails validation; use an em-dash or quote the whole scalar.
- **Lean pushy.** Skills under-trigger. After the plain triggers, widen deliberately: "…even if they don't explicitly say <keyword>." Push toward the task, never past it.
- **Name the invocation keywords.** If the skill answers to a word ("promptsmith", "skillsmith") or subcommands ("<name> refresh"), quote them — quoted keywords route hardest.
- **Cover every entry point.** A skill with build/audit/configure modes lists trigger phrases for each; an entry point absent from the description effectively doesn't exist.
- **Close with the boundary sentence.** One line that routes the nearest neighbor away: "For <adjacent job>, <other skill> is the right tool." Boundaries beat breadth — a description that grabs a neighbor's traffic fails the set.

## The discoverability test

Write ten realistic requests before finalizing: seven that should trigger, three near-misses that shouldn't. Reading only name + description, route all ten. Any miss is a description defect, not a body defect. For suites, run the test across the whole sibling set — requests must land on the right member.

## Anti-patterns

Vague capability statements ("helps with documents"); author-side vocabulary the user won't type; when-to-use guidance buried in the body; breadth that annexes an adjacent skill's triggers; brand language occupying trigger budget (brand belongs in name and README, and is applied by brandsmith — never in the description).
