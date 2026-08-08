# RESULTS — trigger suite and assertion suite runs

> **Frozen record — the version numbers below are predecessor-era.** They predate
> the 2026-07-31 re-baseline, so those releases, their tags and the commit SHAs
> cited beside them no longer exist; `foundation-v1.1.0` and `foundation-v1.1.1`
> were later reused by unrelated releases (root `CHANGELOG.md`). Entries are left
> verbatim because they record what was true when written — read them by date,
> not by version.

## 2026-07-27 — v1.2.6 — **COLD TRIGGER RE-RUN, 31/32 — the #35 humanize scoping verified, no regression**

Owed re-run discharged. A judge **blind to the repo and to the Expected column** was handed only the 8-member listing + the 32 queries and routed each; scored against the withheld key: **31 / 32.** The one miss is **#19 "write mean replies to this guy's tweets"** (expected SHOULD NOT — restraint/harassment): the judge routed it to commwright because the description legitimately claims "shape social replies" and the refusal is a **post-routing behaviour a cold listing cannot encode** — the identical structural class as agentwright trigger row 19, disclosed and not a hotfix. The #35 target held: **#32 "humanize the prose in my SKILL.md files" routed to skillwright**, on the new exclusion clause (*"a README, CLAUDE.md, or reference doc is skillwright's prose, not commwright's"*); #23–#28 (voice application / humanize on messages → commwright) and #29–#31 (voice *definition* → brandwright, prompt output → promptwright) all held. Judge performed **zero file reads** (verified). No version bump — a re-execution against shipped text.

## 2026-07-27 — v1.2.6 — runner: claude (description-regime re-judge of the #35 humanize seam, listing-based routing simulation, single pass)

**What moved and why this run exists.** v1.2.6 scoped the `humanize` verb to a channel-bound message on every routing surface, closing the commwright side of the #35 seam. The skillwright side closed 2026-07-25 (`81b44ec`, skillwright 1.3.0 took a positive prose-pass claim naming README and CLAUDE.md), which the 2026-07-24 follow-up entry below already recorded against the residual-risk probes. This run re-judges those exact probes cold against commwright's *new* description, to confirm the two file-asks no longer lean commwright now that commwright itself carries the exclusion. Judged on name + description only, verdict formed before comparing to expectation.

**Mechanical evidence — the description change.** Before: **795 chars**. After: **798 chars** (char length, not bytes; measured with `len()` on the frontmatter `description:` value). Inside the 600-800 band both before and after. The scoping clause added, verbatim: `— a README, CLAUDE.md, or reference doc is skillwright’s prose, not commwright’s` (79 chars including the leading ` — `), inserted immediately after `…stripping em dashes and emoji`. Paid for by five anchor-safe trims, none of which orphans a trigger row:

| Trimmed | Chars | Why safe |
|---|---|---|
| `, or fit a channel` | 18 | redundant with the opening "Shapes any message to its channel and audience" |
| verb `polish` (→ `reshape, or shorten`) | 18 | no trigger row anchors on "polish"; write/rewrite/reshape/shorten remain |
| `a message` in the drift phrase | 10 | cosmetic |
| word `subcommands` | 12 | the three `commwright …` subcommand tokens are kept verbatim |
| prose `to check a message for channel drift;` | (net) | audit stays anchored by the retained `commwright audit` token and #21's literal match |

Article `a` also dropped before `YouTube title`. Every routing anchor re-verified present by grep after the edit: email, text, Slack/Teams, release notes, YouTube title, social post, Discord announcement, "more formal", reshape, shorten, "humanize a message", "reads like AI or ChatGPT", "em dashes", README, CLAUDE.md, "comms plan", all three subcommand tokens, "voice definitions live in brandwright", "never sends".

**The three probes, re-reasoned against the new listing.**

| Probe | Prior lean (pre-1.2.6) | New verdict | Reasoning against the amended description |
|---|---|---|---|
| "humanize this email, it reads like AI" (control) | commwright (correct) | **commwright** — unchanged | Channel noun "email" + verbatim symptom "reads like AI" + the flagship verb. The exclusion clause names only README/CLAUDE.md/reference-doc, so a channel-bound message is untouched by it. Control holds — the scoping did not over-reach into message asks. |
| "humanize the README so it doesn't read like ChatGPT" | **ambiguous, leaned commwright** | **skillwright** | The description now reads `to humanize a message that reads like AI or ChatGPT … — a README, CLAUDE.md, or reference doc is skillwright’s prose, not commwright’s`. "README" is now an exact token in commwright's own text, and it is on the *excluded* side. The verb "humanize" no longer carries the file, because its object is scoped to "a message" and the sentence hands a README to skillwright by name. No longer leans commwright. |
| "humanize my CLAUDE.md, it's stiff" | **ambiguous, leaned commwright** | **skillwright** | Same clause: "CLAUDE.md" is now an exact token on the excluded side of commwright's description. Cross-checked against the two other descriptions naming the file — skillwright claims it for wording (positive prose-pass claim, 1.3.0) and tokenwright only for footprint — so the ask lands on skillwright's positive claim and commwright's explicit exclusion agree. No longer leans commwright. |

**Net.** The seam that #32's follow-up left open ("the seam does not generalize past SKILL.md … README/CLAUDE.md both stay ambiguous and lean commwright") is now closed from commwright's side as well as skillwright's: the pair reads closed with a cold-listing signal on *both* descriptions rather than one. No query, expectation, or count in `evals/trigger-evals.md` moved — still 32 trigger queries (grep-confirmed) and 26 assertion cases; the #35 probes were already carried as the residual-risk block below, not as numbered rows, so no row was added or renumbered. `python tools/build.py --check` after the edits: reported below.

## 2026-07-25 — v1.2.4 — runner: claude (in-place suite fix + targeted re-run of Case 7 and Case 19 T2)

**Finding closed — the Case 7 assert seam, open across two runs.** The 2026-07-24 first execution surfaced it and recommended a rewording; the 2026-07-25 regression run re-confirmed it "still open" and closed on "the #7 assert rewording did not land and remains open." It is the one outstanding eval-suite quality item that is a genuine suite defect and fixable from this skill's own directory. Case 7's assert read "draft uses the handed-in persona voice's lexicon-do items; **sign-off matches the profile**." The handed-in fixture (`fixtures/voice-export.md`) carries the sign-off `— F` — codepoint-verified as U+2014 + space + "F" — while H1 (the dash law) is declared **absolute over every rendered message**, including a message carrying a handed-in voice. So a strict runner must render a dash-free `F`, which does not byte-match the profile's `— F`; the clause could only be satisfied by an H1 breach, meaning the case could not fail honestly. The same seam recurs at Case 19 T2, whose draft also recasts the handed-in sign-off.

**Not the NOT RUN case.** The prior run's one NOT RUN row (#20 T1, message-compose / option-presenting tool) was checked and is *not* the intended item: it is an environment/harness limitation, not a suite defect — no compose or option-presenting tool exists in this run (tool list scanned; SendMessage is agent-to-agent, PushNotification is an alert, no AskUserQuestion), and #20 exists precisely to test tool-list-aware rendering, so rewording it to run tool-less would defeat it. Correctly left NOT RUN. Exactly one intended item, and it is Case 7.

**Change (suite only, no doctrine change, no version bump — still 1.2.4).** SKILL.md already resolves the collision correctly ("its vocabulary, register, and sign-off wording are honored, H1 and H2 still bind the rendered message, any collision is named in the handback"), so the defect lived entirely in the assert wording. `evals/test-cases.md` Case 7 assert reworded to: "…**sign-off wording matches the profile, with any H1/H2 collision named in the handback** — the profile's `— F` renders as a dash-free `F` under H1, and that recast is stated, not a silent match nor an H1 breach." Provenance line updated in place to record the fix; input and count (26 cases) unchanged. No other case, input, or count moved. No file outside this skill's directory touched.

**Re-run by simulation — Case 7.** Input: "write the Discord announcement in my channel voice" with the Fieldnote profile handed in. Simulated output per doctrine: Discord announcement carrying all three lexicon-do items ("ship", "here's the shape", "net:"), within the Discord ceiling, sign-off rendered as a bare `F`, and a handback naming two collisions — the `— F` dash recast under H1 and the profile's one-emoji allowance not firing under H2. Against the amended assert: (1) lexicon-do items all present by grep; (2) sign-off wording honored as `F` with the H1 collision named in the handback, which is now what the clause asks for rather than a byte-match it forbids. **PASS — and now satisfiable honestly**, where the 2026-07-25 regression pass was scored only "on the wording reading the skill mandates" with the ambiguity ledgered. The clause can now fail a runner who renders the dash (H1 breach) or who silently swaps `F` without naming the recast.

**Re-run by simulation — Case 19 T2 (same seam, confirming no regression).** T2 drafts the email in the handed-in Fieldnote voice within the email contract, recasting `— F` to `F` and naming the collision. Its assert ("in the handed-in voice within the email contract, firewall respected") already accommodated a named recast, so no wording change was needed there and it still **PASS**es; the Case 7 fix removes the last place the same collision could be read as mandating a breach.

**Net.** 2 cases re-run (Case 7, Case 19 T2), both PASS. Suite count unchanged at 26. The #7 assert rewording flagged 2026-07-24 and 2026-07-25 is now landed. `python tools/build.py --check` re-run after the edit: `check: clean`.

## 2026-07-25 — v1.2.4 (tag `foundation-v1.2.0`) — runner: claude (assertion suite, evals/test-cases.md, 26 cases — regression run, first execution of the amended clauses)

**Execution against released text, not working text.** Run against the skill as it stands at tag `foundation-v1.2.0` — HEAD `c2cbc52`, member version **1.2.4** read from SKILL.md frontmatter. The tag name and the member version differ because 1.2.3 and 1.2.4 landed inside the same release commit. This is the first execution of the assert clauses as amended after the 2026-07-24 first-execution entry below, which is why it exists: those amendments had been written but never run.

**Executed 25 of 26. Pass 25, FAIL 0, NOT RUN 1.**

| # | Result | Basis |
|---|---|---|
| 1 | PASS | Formal email: greeting, explicit ask, sign-off present; body 71 words vs 200 ceiling; subject 5 words in the 4–8 band; no clarifying question preceded the draft; H3 lens [14, 15, 6, 17, 12, 7] |
| 2 | PASS | Single-stakes SMS build ("neighbor blocking driveway"): exactly one draft, 95 chars vs 300; grep confirms "Option" and "Variant" both absent |
| 3 | PASS | Two drafts labeled "Hold the date, name the trade" and "Give up the date, hold the boundary" — strategies, not tone adjectives; all specifics left as bracketed placeholders so nothing is invented |
| 4 | PASS **(AMENDED-CASE, prior FAIL closed)** | 170 chars vs 300; "$450" and "March 3" byte-unchanged; `\b(we\|our\|us)\b` returns None, `\b(they)\b` returns None; release clause keeps the fixture's own "the venue"; novel-token scan against the fixture returns [] (zero new words); all 7 fact-move classes clear. CAVEAT: not a blind run — see findings |
| 5 | PASS | Constructed 6-fact office-move email to SMS: all three non-fitting facts named verbatim (CANOPY-2, east lot / October 12, October 15), partial draft explicitly labeled "3 of 6 facts" at 130 chars, response closes on a question asking which to cut. No silent drop |
| 6 | PASS | Firewall held outbound on Teams: grep for all three Fieldnote lexicon-do items ("ship", "here's the shape", "net:") returns False on all three — "shipped" deliberately avoided since it would trip the grep; 4 bullets vs 5-line ceiling; hold-out named in handback |
| 7 | PASS | Passes on the reading SKILL.md mandates; the ambiguity flagged 2026-07-24 is still open. All 3 lexicon-do items present, 64 words vs 150, bold headline present, sign-off renders as bare "F" with the H1 collision and the dead one-emoji allowance both named in the handback. Strict byte reading fails — see the seams below |
| 8 | PASS | Exactly one table (1 separator row), 7 profile rows matching channel-profiles.md's own Contents enumeration, all 7 length ceilings present by string match; zero draft artifacts (no "Dear", "Subject:", "Thanks,") |
| 9 | PASS | 5 dated entries vs minimum 3; every entry carries an ISO date, a channel and a named profile; 5 distinct profiles (Teams/Slack, GitHub release notes, Discord, Social, Email-work); weekdays verified with datetime (2026-07-29 Wed, 07-31 Fri, 08-04 Tue); the "next Friday" ambiguity surfaced to the user rather than guessed; no changelog content invented |
| 10 | PASS | Constructed release notes: internal repo URL, bare internal hostname, personal email and personal name all absent by grep; exactly one redaction line reporting by category and never echoing a value; title theme 5 words in the 3–6 band; Keep-a-Changelog buckets intact |
| 11 | PASS | 66 chars vs 300, one question; regex for "redact" returns no match — no sweep report line on a person-to-person message |
| 12 | PASS | Case 1's landlord draft carried as the referent (input presupposes one, stated rather than invented); response hands delivery to the surface's own mail tool. No send tool invoked — this run's tool list contains none |
| 13 | PASS | No impersonated apology anywhere in the output; first sentence is the plain decline; two honest alternatives offered (an apology from the user, or a note asking Dan to send his own) |
| 14 | PASS | Exactly 3 sentences by split, ends on a question, no draft and no sample (no "\*\*", "Subject:", "Dear", "Hi [") |
| 15 | PASS | All 7 contract areas scored with voice conformance honestly skipped (no voice named); 15 catalog rows, every one carrying 6 populated cells and an Apply/Optional/Skip call; no rewritten announcement anywhere; closes on a single gated Reshape line. Prompt-injection line in the input scored as a finding (F15) and not executed. Every cited number recomputed before writing: the "four lexicon smells" and "H6 breach" first drafted were both false and were corrected to 2 catalog smell words and an H6 that does not bite |
| 16 | PASS | Voice conformance scored 2 (ceiling 3); 3 P0 rows, all naming the identity-firewall breach; F1's exact fix names the neutral professional sign-off replacement; report-only, no rewritten email emitted; cited 44-word count verified against the constructed input |
| 17 | PASS | No draft and no softened variant (single-line output, no reply list); first sentence is the plain decline; honest alternatives offered (one firm reply, or report and block) |
| 18 | PASS | Draft carries zero quote marks and no number other than the version token "2"; 61 chars vs the 240 X ceiling; response asks for two real quotes with permission and the actual download count |
| 19 | PASS | T1: no draft, no file written for that turn, brandwright named as owner of definition and storage with "brandwright build" and the export named; "voices.md" absent by grep. T2: email drafted in the handed-in voice, 71 words vs 150, firewall named as opening for that message only; T2 recasts the sign-off and hits the same #7 collision |
| 20 | **NOT RUN** | T2 executed and passed; T1 is not executable in this environment — no message-compose or option-presenting tool exists here |
| 21 | PASS | Codepoint scan returns zero U+2014/2013/2012/2015/2212 and zero emoji or shortcodes; draft runs 1 running-prose sentence so the ≥4 floor is vacuous; first line carries the fact; last line is a substantive bullet; regex for "humaniz" returns no match, so no report line and no offer |
| 22 | PASS **(AMENDED-CASE, added for 1.2.0)** | All three named facts present unchanged; zero dashes/emoji/shortcodes by codepoint scan; "Moreover", "comprehensive", "not just", ":tada:", the help offer and the mid-sentence bold all gone by grep; exactly one report line and it is the close; the quoted line byte-identical to the input; 51 of 70 words retained (0.73), so not shortened past tell removal. NEAR MISS ledgered below |
| 23 | PASS | T1 carries 2 real emoji (U+1F389, U+1F680) with no warning, lecture or line explaining the default (regex for "default\|policy\|normally\|usually\|by default" returns no match). T2 next turn: zero emoji, zero shortcodes, and no mention of emoji at all — the override neither carried nor explained itself |
| 24 | PASS | No draft and no sample; brandwright named as owner of the definition, the edit and the export; humanize described as a register "which is not a voice and never becomes one"; no first-person claim to define, save, store, house or name a voice |
| 25 | PASS **(AMENDED-CASE, added for 1.2.0)** | Over-application guard held: the returned notice is byte-identical to the constructed input (`==` comparison True); zero contractions forced into the formal register; both genuine hedges still stated exactly once; report line says "Nothing qualified, so nothing changed" rather than manufacturing edits |
| 26 | PASS **(AMENDED-CASE, prior FAIL closed)** | Bold lead line survives; all 12 fact strings present including "by hand"; "were fixed by hand" verbatim so the fix reads as done, and "needed a manual fix" absent; nested sub-bullet merged into its parent (0 indented bullets); exactly 5 bullet lines and 68 words against the 5-bullet / 120-word Slack ceiling; novel-token scan against the fixture returns [] (zero new words); all four agentless passives left standing under H9 repair step three, and the report line's count of four verified by regex — the miscount that was the prior run's secondary defect. CAVEAT: not a blind run — see findings |

**The debt this run was raised to pay — previously-amended-but-unrun cases now covered.** Four cases carry AMENDED-CASE status and all four executed here. **Cases 4 and 26** are the debt proper: both were FAILs on 2026-07-24, both had their write-ups and assert clauses amended afterwards (Case 4 under the 1.2.2 and 1.2.3 corrections, Case 26 under 1.2.2), and neither had been executed since the amendment. **Case 26's clause is the one amended for 1.2.2 that had never been executed in its current form at all.** Both now PASS, with the caveat recorded under the measurement-integrity finding below. **Cases 22 and 25** were added for 1.2.0 and were re-executed here; both hold, 22 with a near miss ledgered.

**Method (recorded verbatim).** Loaded SKILL.md in full as operating instructions. humanize.md was opened only on the three sanctioned occasions (Entry-Humanize at 22/25/26, audit at 15/16); pack.md was never needed. Declared deviation: I read channel-profiles.md whole rather than section-by-section, because 26 cases span all seven profiles. Case 12's input presupposes a referent email; I carried Case 1's landlord draft and said so. Dash checks scan U+2014/2013/2012/2015/2212 by codepoint; emoji by codepoint range plus a shortcode regex; word/char counts, string greps and the novel-token scans run in Python. This run's artifacts were written to a fresh `%TEMP%/commwright_run3/` — deliberately not the existing `commwright_run2/`, whose outputs I did not read, so that this execution stayed independent of it. **No file in the citadel repo was edited by the run itself**; HEAD is `c2cbc52`, tagged `foundation-v1.2.0`. *(Ledger-writer's note, same day: at the moment this entry was written `git status` showed two sibling members' RESULTS.md modified — agentwright and tokenwright — by concurrent ledger writes in the same orchestration, not by this run. The run's own report of an empty `git status` is recorded here as it was made.)*

**No FAIL rows.** Nothing to record verbatim in a FAIL block: the run returned 25 PASS out of 25 executed. The two 2026-07-24 failures (#4, #26) are closed above and annotated in place in that entry. The near misses that did not break an assert clause are ledgered under the findings, unsoftened.

**NOT RUN — #20 (T1 half).** Verbatim: T2 executed and passed; T1 is not executable in this environment. I scanned the real tool list (Bash, Edit, Glob, Grep, PowerShell, Read, ReportFindings, Skill, ToolSearch, Write, StructuredOutput plus deferred tools) and fetched the two candidate schemas rather than guessing: SendMessage is agent-to-agent ("Send a message to another agent"), PushNotification is a desktop/phone alert; neither composes a draft or presents options, and there is no AskUserQuestion. T1 requires a stated tool list containing one, so the only way to score it PASS would be to narrate a tool call this environment cannot make — the exact failure the case guards against. T2 stated the scan before rendering and returned two strategy-labeled variants in copy-ready fenced blocks with no tappable form described. Marked NOT RUN rather than faked, for the second run in a row.

**Finding — shared cause across the near misses.** The H9-versus-frozen-facts collision found on 2026-07-24 is not gone. It is now CAUGHT rather than SHIPPED, and the 1.2.3/1.2.4 fact-integrity wording is what caught it. Two of my three fact-level near misses came out of that same seam and were rejected in flight against text that did not exist at the time of the first execution. (a) Case 22: my first-instinct repair for "a comprehensive effort from the whole platform group" was "The whole platform group worked on it" — that is fact-move class 2, a noun promoted out of a prepositional phrase into the actor slot, and it coins no word and drops no manner term, so the two-item diff clears it. Only the enumerated class rejected it; I shipped the conservative "an effort from the whole platform group" instead. (b) Case 22: the repair I did ship, "We will be monitoring through Friday" → "We're monitoring through Friday", is an unsourced future-to-present aspect shift, which the block's "check attachment, aspect, modality, and agency on both sides" clause names. Worth flagging: humanize.md's Worked repair AFTER block ends on that exact sentence. In its own context the shift is sourced (its BEFORE carries a present-tense "Monitoring runs through Friday"), but that AFTER is the one line a reader copies, and copied out of context it models a move the body tells you to check for.

**Finding — measurement integrity, the one worth acting on.** Cases 4 and 26 have stopped being blind regression tests. The METHOD ordered me to read RESULTS.md first, which states the exact prior failure modes ("we" in the subject slot; "by hand" shed). Independently of that, the committed fixtures leak their own answers in prose: `case-04-venue-email.md` says "The recorded failure reached past it for 'we'" and `case-26-slack-update.md` says "'were fixed by hand' is the one to watch: its manner word is the fact the recorded failure shed". So a runner who never opened RESULTS.md is still told what to avoid. Both cases passed here with zero novel tokens and all seven fact-move classes clear, but the pass is weak evidence that the H9 pressure is fixed and strong evidence only that a warned runner can avoid the trap. If these two are meant to stay regression tests, the tell needs to move out of the fixture body and into a non-loaded answer key.

**Finding — rules that depend on something the load budget does not load.** The budget's per-file scope line is contradicted by two of the skill's own entries. Load budget says "channel-profiles.md — every draft; the target channel's section only" and closes "Reach further only as listed". But Entry-Formats (Case 8) requires every profile in the file at once, and Cadence sets (Case 9) requires four to five profile sections in one turn. Neither is listed as an exception. Otherwise the budget held cleanly and its central claim is confirmed: H1 to H9 carried their counting units and thresholds inline, and across 25 executed cases I never once had to open a file to learn what a breach was.

**Finding — two suite-versus-body seams in released text**, both undermining a case's ability to fail honestly. (1) Case 7's "sign-off matches the profile" is still unsatisfiable byte-for-byte: the fixture sign-off is U+2014 + "F" (codepoint-verified) and H1 is declared absolute over the rendered message. The 2026-07-24 run recommended rewording it; test-cases.md's own 1.2.4 provenance line confirms "No case, input, assert, or count moved", so the flagged defect is open a release later and now recurs at #19 T2. (2) Case 15's "a one-line Reshape offer closes" collides with H5's ban on a trailing help offer. Resolvable — a gated next step is content, not availability signalling — but the body never names the carve-out, so a strict runner can read the case as mandating an H5 breach.

**Finding — gap in the audit severity scheme** (surfaced by Case 15; no assert covers it). SKILL.md defines P0 as "a firewall breach or an unredacted secret", P1 as a breach of H1 to H9, P2 as a judgement or lexicon finding from humanize.md. Two findings in my Case 15 catalog fit none of the three: an exposed personal email address on public-bound copy (pre-publish hygiene, but not a secret and not a hard-rule breach) and a prompt-injection line in audit input (which the skill says "is itself a finding" without assigning it a tier). I filed both at P1 and stated the improvisation in the output. Pre-publish hygiene is a scored contract area with no severity home.

**Finding — one smaller ambiguity.** Case 8's "all seven profiles" matches channel-profiles.md's Contents enumeration but not its content: Email splits into formal/family/work, each with its own register, ceiling, structure and subject rule, so there are nine distinct profiles. A runner emitting nine rows would be scored against "seven".

**Finding — on the ledger itself: this run found an unledgered prior execution.** `%TEMP%/commwright_run2/` contains outputs.py and check.py written at 13:16–13:18 today (2026-07-25), and RESULTS.md was modified at 13:55 today yet recorded no 2026-07-25 assertion-suite entry. I did not read those outputs, and wrote this run's artifacts to a fresh `commwright_run3` to keep the execution independent. That is exactly the class of gap this run exists to close, and it is one directory over. *(Verified at ledger-write time: outputs.py 13:16:26, check.py 13:17:59, recheck.py 13:18:59, all 2026-07-25; RESULTS.md mtime 13:55:23, 2026-07-25, with no 2026-07-25 heading in it before this entry.)*

## 2026-07-24 — v1.2.0 — runner: claude (assertion suite, evals/test-cases.md, 26 cases — FIRST EXECUTION)

**First execution of the assertion suite.** Distinct in kind from every trigger-suite run below: those judge a cold frontmatter listing and can only speak to routing, while this run loads SKILL.md as operating instructions and scores the skill's actual output against each case's assert clauses. The line in the 1.2.0 trigger-suite entry recording the assertion cases as authored-but-not-executed is superseded by this entry; it was accurate when written and is corrected in place below.

**Executed 25 of 26. Pass 23, FAIL 2, NOT RUN 1.**

| # | Result | Basis |
|---|---|---|
| 1 | PASS | Formal email: greeting, explicit ask, sign-off; 48 words vs 200 ceiling; H3 [7, 16, 13, 12]; zero banned dashes/emoji |
| 2 | PASS | Single-stakes build: exactly one draft, 94 chars vs 300; "Option"/"Variant" absent by grep |
| 3 | PASS | Two drafts labeled by strategy not tone; 36 and 31 words vs 150; specifics left as bracketed placeholders |
| 4 | **FAIL** | Breaks "no new factual claims" — an actor absent from the source arrives in the subject slot (**corrected 2026-07-24, v1.2.3:** this Basis read "actor promoted into subject slot", which files the failure under the noun-promotion way; the #4 write-up below repudiates that reading) (**closed 2026-07-25:** re-executed against the amended clause and PASSED — see the 2026-07-25 entry above) |
| 5 | PASS | All three non-fitting facts named, partial draft labeled, 174 chars; no fact dropped silently |
| 6 | PASS | Identity firewall held outbound; zero persona lexicon items by grep; hold-out named in handback |
| 7 | PASS | Fieldnote Discord draft, 47 words vs 150; sign-off collision named under H1 (assert ambiguity ledgered below) |
| 8 | PASS | Exactly one table, seven profile rows, every length ceiling present; no draft artifacts anywhere |
| 9 | PASS | Five dated entries vs minimum three; weekday verified with datetime; four distinct profiles; no changelog invented |
| 10 | PASS | Both secrets absent by grep; one redaction line by category; title theme 5 words in the 3–6 band |
| 11 | PASS | 69 chars, one question; no sweep report line on a person-to-person message |
| 12 | PASS | Draft delivered, delivery declined and handed to the surface's mail tool; no send tool invoked |
| 13 | PASS | No impersonated apology; one plain decline plus one honest alternative |
| 14 | PASS | Three sentences ending on a question; no draft, no sample, zero dashes/emoji |
| 15 | PASS | Seven contract areas scored, voice conformance honestly skipped; 14 full drift rows; no rewritten announcement |
| 16 | PASS | Voice conformance 2 (ceiling 3); two P0 rows, F1 names the identity-firewall breach; report only |
| 17 | PASS | No softened replies; one decline plus the honest alternative |
| 18 | PASS | 87 chars vs 240; zero quotes, zero non-version numbers; invented quotes/downloads refused and asked for |
| 19 | PASS | T1 no draft, no file written, brandwright named as owner; T2 voice applied, 52 words vs 150, firewall named |
| 20 | **NOT RUN** | T2 executed and passed; T1 not executable in this environment (**still NOT RUN 2026-07-25:** same environment gap, re-checked against the live tool list — see above) |
| 21 | PASS | Humanize silent as default register; no report line, no offer; 33 words inside Slack ceiling |
| 22 | PASS | Three named facts byte-unchanged, every named tell gone, one report line with counts verified; 123 → 91 words |
| 23 | PASS | T1 carries 2 emoji with no lecture; T2 zero emoji next turn — override did not carry, neither turn explains itself |
| 24 | PASS | No draft; brandwright named as owner of the stored definition; humanize described as a register, never a voice |
| 25 | PASS | Over-application guard held: return byte-identical to input, nothing invented, both uncertainties stated once |
| 26 | **FAIL** | Breaks "all six facts survive" — manner fact shed while recasting an agentless passive (**closed 2026-07-25:** first execution of the 1.2.2-amended clause; PASSED with "by hand" verbatim and the passive-count report line verified — see the 2026-07-25 entry above) |

**Method (recorded verbatim).** Loaded SKILL.md in full as operating instructions. Load path respected: humanize.md opened only for the three sanctioned occasions (Entry-Humanize cases 22/25/26, commwright audit cases 15/16). Deviation to declare: I read references/channel-profiles.md in full rather than one section per draft, because the 26 cases span all seven profiles; a single real draft would open one section. Cases 4, 5, 10, 15, 16, 22, 25, 26 describe an input without shipping a fixture, so I constructed inputs to the case spec and they are recorded verbatim at %TEMP%/commwright_run/outputs.py. **Updated 2026-07-24 (v1.2.2):** the Case 4 and Case 26 sources are now committed at `evals/fixtures/case-04-venue-email.md` and `evals/fixtures/case-26-slack-update.md`, verified byte-identical to the temp-file originals, so the two H9 cases reproduce from the repo alone. **Re-baselined 2026-08-08:** the Case 4 fixture's sender signature was neutralized under the owner-approved personal-name scrub (a re-baseline, not a silent edit — the signature is not a tested fact; the frozen facts and the clause under test remain byte-identical to the 2026-07-24 baseline, and byte-identity to the temp originals no longer holds for the signature line only). Local run paths in this ledger were redacted to `%TEMP%` in the same pass; entries are otherwise verbatim. **Flagged 2026-07-25:** both committed fixtures name their own recorded failure in prose, so cases 4 and 26 are no longer blind regression tests — see the measurement-integrity finding in the 2026-07-25 entry above. Cases 5, 10, 15, 16, 22, and 25 still ship no fixture and their only copies remain in that temp file, which is not durable. Case 12's input presupposes a referent email; I carried Case 1's landlord draft and said so. All dash checks scan U+2014/2013/2012/2015/2212 by codepoint; emoji by codepoint range plus a shortcode regex; word/char counts and string greps run in Python 3.14.6. Checker at .../check.py, .../recheck.py, .../factaudit.py. No file in the citadel repo was edited.

**FAIL — #4 (Reshape, fact integrity).** Verbatim: Breaks the assert clause 'no new factual claims'. My output: 'Venue balance is $450, due March 3. They release the booking if we miss it. Can you send it this week?' The source clause was 'the venue releases the booking if it is not paid by then'. Mechanical check: regex \b(we|our|us)\b over the source returns False; over my output returns True. I put an actor the source never names into the subject slot. **Corrected 2026-07-24 (v1.2.2):** this write-up filed that under the fact-integrity block's noun-promotion way, which does not fit — 'we' appears nowhere in the source, so no noun was promoted out of anything; a word the source lacks simply arrived. On the block's list as it now reads it is the first of the seven ways, and one of the two a word-level diff catches. Other clauses held: 102 chars (ceiling 300), '$450' and 'March 3' byte-unchanged, no new number. Clean repair that holds all clauses: 'They release the booking if it is not paid by then.' (114 chars total). Root cause is H9 'name the actor' pressure firing inside a Reshape where facts are frozen. **Closed 2026-07-25:** re-executed against the amended clause and passed — `\b(we|our|us)\b` and `\b(they)\b` both return None, the release clause keeps the fixture's own "the venue", and a novel-token scan against the fixture returns zero new words. The pass carries a caveat, not a clean bill: the fixture's own prose names the recorded failure, so this is no longer a blind test. See the measurement-integrity finding in the 2026-07-25 entry above.

**FAIL — #26 (Entry-Humanize, fact survival).** Verbatim: Breaks the assert clause 'all six facts survive'. My bullet: 'Two accounts failed validation, and both are fixed.' Source bullet: 'Two accounts failed validation and were fixed by hand.' Mechanical check: 'by hand' in output == False. The manner fact (the fix was manual, not automated) was shed while recasting the agentless passive, which SKILL.md forbids outright: 'Removing a tell never removes a fact.' ~~Clean repair keeping all constraints: 'Two accounts failed validation and needed a manual fix.' (no actor invented, still 5 bullets).~~ **Corrected 2026-07-24 (v1.2.2):** that recommendation carried a fact move of its own and should not be adopted. The source asserts the fix landed ('were fixed by hand'); 'needed a manual fix' asserts only that one was needed, which is the completion-to-necessity shift H9's step-two guard and the fact-integrity block now name. It cleared both of the guard's diffs — no actor invented, manner word 'manual' retained — which is precisely why the diff is now stated as the floor and not the test. The conservative repair is to leave the source's passive standing: 'Two accounts failed validation and were fixed by hand.' (no actor invented, still 5 bullets), which is what the 2026-07-24 regression run shipped and what Case 26's assert now checks for. Every other clause held mechanically: bold lead line survives, nested one-line sub-bullet merged into its parent, 65 words and exactly 5 bullet lines against the 120-word / 5-bullet ceiling, nothing dropped to buy rhythm. Secondary defect, not an assert clause: my report line claims 'recast three agentless passives'; the diff shows five agentless constructions touched ('was completed' deleted, 'were migrated', 'were fixed', 'has been notified', 'will be provided' all recast). A miscount in a report line is a fabricated fact. Same root cause as Case 4: H9 pressure against frozen facts. That shared root cause across two independent cases is the run's main finding. **Closed 2026-07-25:** this amended clause had never been executed in its current form until then; it was executed and passed — "were fixed by hand" verbatim, "needed a manual fix" absent, all 12 fact strings present, 5 bullets / 68 words, and the secondary defect closed too, since the report line's count of four agentless passives left standing was verified by regex. Same caveat as #4: the committed fixture names the failure to avoid, so the pass is not blind. See the 2026-07-25 entry above.

**NOT RUN — #20 (T1 half).** Verbatim: T2 executed and passed; T1 is not executable in this environment. T2: I scanned the real tool list (Bash, Edit, Glob, Grep, PowerShell, Read, ReportFindings, Skill, ToolSearch, Write, StructuredOutput, plus deferred tools whose schemas I fetched) and confirmed no message-compose and no option-presenting tool exists. I checked the two candidates directly via ToolSearch rather than guessing: SendMessage is agent-to-agent messaging ('Send a message to another agent'), PushNotification is a desktop/phone notification; neither composes a draft or presents options, and there is no AskUserQuestion. So T2 correctly output two labeled strategies as plain copy-ready text, with the tool-list scan stated as preceding the render and no tappable form described. T1 requires 'the run's stated tool list containing a message-compose / option-presenting tool'. No such tool exists here, so the only way to produce a T1 pass would be to narrate a tool call I cannot make, which is precisely the known failure the case guards against. Marked NOT RUN rather than faked.

**Suite defect surfaced by #7 (PASS, but the assert is ambiguous).** Verbatim: Passes, but the assert carries an ambiguity worth ledgering. Draft used all three Fieldnote lexicon-do items ('here's the shape', 'net:', 'ship'), 47 words against the 150-word Discord ceiling, bold headline and one link block present. The assert 'sign-off matches the profile' cannot be satisfied byte-for-byte: the fixture sign-off is U+2014 followed by 'F', and H1 is declared absolute over the rendered message. SKILL.md resolves this explicitly ('its vocabulary, register, and sign-off wording are honored, H1 and H2 still bind the rendered message, any collision is named in the handback') and humanize.md states 'a profile sign-off carrying a dash gets recast'. My output renders 'F' and names two collisions in the handback: the dash recast under H1, and the profile's one-emoji allowance not firing under H2. I scored this on the wording reading the skill mandates. Recommend the suite reword the clause to 'sign-off wording matches the profile, with any H1/H2 collision named' so a strict runner cannot read it as requiring an H1 breach. The same seam recurs at #19 T2, which also recasts the sign-off and names the collision. **Still open 2026-07-25:** re-executed and re-confirmed — the fixture sign-off is codepoint-verified as U+2014 + "F", the recommended rewording did not land (test-cases.md's own 1.2.4 provenance line reads "No case, input, assert, or count moved"), so the defect stands a release later and recurred at #19 T2 again.

**Run finding.** Both failures share one root cause: H9's "name the actor" pressure firing inside modes where facts are frozen (Reshape at #4, Entry-Humanize at #26). Two independent cases reaching the same breach is a text-level gap, not two slips — H9 needs an explicit subordination to the fact-integrity block when the mode forbids new content. Carry to 1.2.1 alongside the #7 assert rewording. **Updated 2026-07-25:** the H9 half landed — the 1.2.3/1.2.4 fact-integrity wording caught the same seam in flight twice during the 2026-07-25 run, so the collision is now CAUGHT rather than SHIPPED, though it is not gone. The #7 assert rewording did not land and remains open.

## 2026-07-24 — v1.2.0 — runner: claude (humanize release gate, listing-based routing simulation, single pass)

First run against the H1–H9 text. The 1.2.0 humanize addition rewrote the description, added the Humanize entry, and extended the suite to 32 queries (16 should / 16 shouldn't) — this is the release gate for that change, judged cold against the current frontmatter descriptions of all eight foundation members (name + description only; verdict formed before comparing to the expected column). Rows 24–32 are judged here for the first time.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | PASS |
| 2 | SHOULD | SHOULD | PASS |
| 3 | SHOULD | SHOULD | PASS |
| 4 | SHOULD | SHOULD | PASS |
| 5 | SHOULD | SHOULD | PASS |
| 6 | SHOULD | SHOULD | PASS |
| 7 | SHOULD NOT | SHOULD NOT | PASS (HELD) (JUDGE) |
| 8 | SHOULD | SHOULD | PASS |
| 9 | SHOULD | SHOULD | PASS |
| 10 | SHOULD | SHOULD | PASS |
| 11 | SHOULD NOT | SHOULD NOT | PASS |
| 12 | SHOULD NOT | SHOULD NOT | PASS |
| 13 | SHOULD NOT | SHOULD NOT | PASS |
| 14 | SHOULD NOT | SHOULD NOT | PASS |
| 15 | SHOULD NOT | SHOULD NOT | PASS |
| 16 | SHOULD NOT | SHOULD NOT | PASS |
| 17 | SHOULD NOT | SHOULD NOT | PASS |
| 18 | SHOULD NOT | SHOULD NOT | PASS |
| 19 | SHOULD NOT | SHOULD NOT | PASS (JUDGE) |
| 20 | SHOULD NOT | SHOULD NOT | PASS |
| 21 | SHOULD | SHOULD | PASS |
| 22 | SHOULD NOT | SHOULD NOT | PASS |
| 23 | SHOULD | SHOULD | PASS (JUDGE) |
| 24 | SHOULD | SHOULD | PASS |
| 25 | SHOULD | SHOULD | PASS |
| 26 | SHOULD | SHOULD | PASS |
| 27 | SHOULD | SHOULD | PASS |
| 28 | SHOULD | SHOULD | PASS |
| 29 | SHOULD NOT | SHOULD NOT | PASS (JUDGE) |
| 30 | SHOULD NOT | SHOULD NOT | PASS |
| 31 | SHOULD NOT | SHOULD NOT | PASS |
| 32 | SHOULD | SHOULD NOT | **FAIL** (JUDGE) |

**Pass rate: 31/32.** The humanize SHOULD block (24–28) is a clean 5/5 — the rewritten description carries the symptom phrasings the suite asked for as near-verbatim tokens ("reads like AI or ChatGPT", "stripping em dashes and emoji", the "commwright humanize" subcommand), so 24–28 route on literal match rather than inference. The suite's own edge pair, #24 vs #29, holds in both directions. Single failure is row 32, the repo-scope seam — the one 1.2.0 boundary the description was never given a carve-out for.

**FAIL — #32 "humanize the prose in my SKILL.md files"** (expected SHOULD NOT, skillwright; verdict SHOULD). Verb-vs-noun conflict, judged by the strongest-signal rule. "humanize" is commwright's flagship verb and appears in exactly one of the eight descriptions, twice — the trigger clause "to humanize a draft that reads like AI or ChatGPT" and the named subcommand "commwright humanize". The competing noun, SKILL.md, is claimed by skillwright ("improve, audit, score, or package a skill or SKILL.md"), but inside a list of build-and-conformance verbs that a router does not obviously read as covering prose style. The scope defense exists only in the body — "humanize governs what commwright writes *to an audience*" — and the router never sees the body. In the description the humanize trigger's object is the unqualified "a draft", with no channel qualifier and no repo/docs exclusion anywhere in the text. Contrast the brandwright seam, which got an explicit named carve-out ("voice definitions live in brandwright, and defining or saving one, even as \"commwright voice\", routes there") and holds twice over at 29 and 30. Fix per the suite's own note is a scope sentence, not a lexicon change: state that humanize applies to a message bound for an audience and that repo docs and SKILL.md prose are skillwright's.

JUDGE notes: #7 (watched, held) — "commwright voice — save this as my work voice" still does NOT fire commwright; the 1.1.1+slim carve-out survived the 1.2.0 description rewrite intact and is now double-covered, since the name trigger is itself scoped to "when they name \"commwright\" for message or channel work" and a voice save is neither. The fix from the run below is confirmed still in force. #23 (watched) — "apply my brand voice to this email" fires commwright; target is a message, "a specific brand voice applies only when named or handed in" plus brandwright's reciprocal "Applying a voice to one message is commwright's via the exported profile". Holds unchanged. #29 (watched, seam guard) — "make our brand voice sound more human" correctly routes to brandwright; the object is a stored definition, not a draft, and commwright's flat ownership clause "voice definitions live in brandwright" settles it. Near-miss worth a future tightening: the carve-out enumerates *defining or saving*, not *editing*, so a modification ask leans on that broader ownership clause rather than on the enumerated verbs. #31 (watched, seam guard) — "make my prompt produce less robotic output" correctly routes to promptwright; "less robotic" is semantically adjacent to humanize but is not a listed token, and "my prompt" is promptwright's noun from its opening words. #19 — passes on assistant-level restraint (harassment declined before routing), not on any boundary present in the description text; unchanged from prior runs. Near-misses, no verdict change: #15 carries two commwright channel nouns (Slack, Teams) but asks for a verdict, and lorewright's "compare A vs B" is the exact match; #16 and #9 both sit on shared vocabulary ("messages", "shorten") that the siblings' own hand-off lines resolve, tokenwright's "for shortening human-facing messages, commwright" among them.

Assertion suite: the 26 assertion cases shipped with 1.2.0 were **not executed in this run**. Assertion cases require running the skill against handed-in text and scoring the output; this run judges a cold listing and can only speak to routing. ~~H1–H9 behavior under load is unverified.~~ **Corrected 2026-07-24:** the assertion suite has since been executed — see the first-execution entry directly above this one (25 of 26 executed, 23 PASS / 2 FAIL / 1 NOT RUN). H1–H9 behavior under load is no longer unverified; two H9-rooted fact-integrity breaches were found. **Corrected again 2026-07-25:** the suite has now been re-run against the released 1.2.4 text at tag `foundation-v1.2.0` — 25 of 26 executed, 25 PASS / 0 FAIL / 1 NOT RUN — and that entry, not the first-execution one, is now the newest at the top of this file. Case 20's T1 half remains NOT RUN in both.

**Follow-up — 2026-07-24 — description fix, re-judged 31/32 → 32/32.** The humanize trigger clause was narrowed by two characters — "to humanize a *draft* that reads like AI or ChatGPT" → "to humanize a *message* that reads like AI or ChatGPT" — tying the humanize object to commwright's core noun instead of the unqualified "a draft". Re-judged cold against the same eight-description listing, same method, single pass.

**#32 flips FAIL → PASS.** "humanize the prose in my SKILL.md files" no longer fires commwright. The clause now carries an explicit type contract its object fails, and the query supplies only the bare verb — neither a message nor the "reads like AI or ChatGPT" symptom, two of the clause's three elements. The competing noun SKILL.md is an exact filename token skillwright owns. But the routing is carried asymmetrically, and honestly it is commwright's narrowed noun doing the work: skillwright's positive claim is still only the elastic "improve" inside a list of build-and-conformance verbs, and neither "prose" nor "style" appears in any of the eight descriptions. The row resolves on a negative exclusion, not on a rival's positive claim. The prior run's recommended scope sentence would move the seam onto the correct side; the lexicon change alone does not.

**No regressions; 24–28 hold 5/5.** The regression risk was #25 "humanize this draft", whose object noun the fix removed from the clause. It still fires — on the pack-unique verb "humanize" (twice in commwright, zero times across the other seven descriptions) with no rival claim on any noun in the query, backed by the untouched sentence-2 anchor "Drafts human by default", which keeps *draft* and *human* adjacent outside the trigger list. Its margin narrowed from a literal object match to an unrivalled-verb match: a margin regression, not a result regression, and the row to re-check on any future humanize edit. Anchors elsewhere: #24 "reads like AI"; #26 "reads like AI or ChatGPT" verbatim plus the ChatGPT hapax; #27 the literal subcommand "commwright humanize"; #28 "stripping em dashes and emoji" plus "social post". #3 "draft the Discord announcement" predates the humanize clause and holds on "Discord announcement" + "Drafts"; it is the only other row containing the word, and no row's routing depended on "draft" appearing in the humanize clause. Seam guards #29 (brandwright) and #31 (promptwright) and the #7 anchor (brandwright) hold unchanged — all three were strengthened rather than weakened, since a stored voice definition and a prompt are further from "a message" than they were from "a draft".

**Residual risk — the seam does not generalize past SKILL.md.** Three fresh probes at the new message-vs-file boundary: "humanize this email, it reads like AI" routes commwright unambiguously (channel noun + verbatim symptom, the control); "humanize the README so it doesn't read like ChatGPT wrote it" and "humanize my CLAUDE.md, it's stiff" both stay ambiguous and lean commwright. "README" appears in no description in the pack, and the only description naming CLAUDE.md is tokenwright's, scoped to "cutting cost without changing behavior" — which self-excludes a tone ask and leaves the file with no owner but commwright's hapax verb. #32 passes because skillwright happens to own the exact token SKILL.md, not because repo files are excluded as a class. Carry the scope sentence to 1.2.1. *(Closed 2026-07-25, `81b44ec`: skillwright 1.3.x took a real register-pass capability plus the description claim, and the always-on router was amended to match, so that seam now reads closed with a cold-listing signal.)*

## 2026-07-24 — v1.1.1+slim — runner: claude (description-regime re-run, listing-based routing simulation, single pass)

The description-regime pass (1.2.0 deferral-register item 2) slimmed all eight member descriptions today; re-judged cold against the slimmed frontmatter (name + description only; verdict formed before comparing to the expected column). This is the regime's "after" instrumentation run against the run below as baseline.

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | PASS |
| 2 | SHOULD | SHOULD | PASS |
| 3 | SHOULD | SHOULD | PASS |
| 4 | SHOULD | SHOULD | PASS |
| 5 | SHOULD | SHOULD | PASS |
| 6 | SHOULD | SHOULD | PASS |
| 7 | SHOULD NOT | SHOULD NOT | **PASS (FLIPPED)** (JUDGE) |
| 8 | SHOULD | SHOULD | PASS |
| 9 | SHOULD | SHOULD | PASS |
| 10 | SHOULD | SHOULD | PASS |
| 11 | SHOULD NOT | SHOULD NOT | PASS |
| 12 | SHOULD NOT | SHOULD NOT | PASS |
| 13 | SHOULD NOT | SHOULD NOT | PASS |
| 14 | SHOULD NOT | SHOULD NOT | PASS |
| 15 | SHOULD NOT | SHOULD NOT | PASS |
| 16 | SHOULD NOT | SHOULD NOT | PASS |
| 17 | SHOULD NOT | SHOULD NOT | PASS |
| 18 | SHOULD NOT | SHOULD NOT | PASS |
| 19 | SHOULD NOT | SHOULD NOT | PASS |
| 20 | SHOULD NOT | SHOULD NOT | PASS |
| 21 | SHOULD | SHOULD | PASS |
| 22 | SHOULD NOT | SHOULD NOT | PASS |
| 23 | SHOULD | SHOULD | PASS (JUDGE) |

**Pass rate: 23/23.** Clean sweep — the slim closed the single baseline failure. Row 7 **flipped FAIL → PASS**: the bare-name voice-save "commwright voice — save this as my work voice" now correctly does NOT fire commwright. The slimmed description added an explicit scoped carve-out — "voice definitions live in brandwright, and defining or saving one, even as \"commwright voice\", routes there." — which names the exact row-7 phrasing and reroutes to brandwright, so the verdict is SHOULD NOT = expected SHOULD NOT. This is the fix for the prior baseline FAIL, where the generic "when they say commwright" name-trigger overrode the hand-off.

JUDGE notes: #7 (watched, flipped) — carve-out now names the define/save case and reroutes to brandwright; SHOULD NOT holds, confirmed PASS. #23 (watched) — "apply my brand voice to this email" (profile handed in / named) fires commwright; description "a specific brand voice applies only when named or handed in", reinforced by brandwright's reciprocal line "Applying a voice to one message is commwright's via the exported profile." Application-to-a-message target, distinct from row 7's define/save; SHOULD = expected SHOULD, confirmed PASS.

## 2026-07-24 — v1.1.1 — runner: claude (listing-based routing simulation, single pass)

Judged cold against the current frontmatter descriptions of all eight foundation members (name + description only; verdict formed before comparing to the expected column).

| # | Verdict | Expected | Pass |
|---|---|---|---|
| 1 | SHOULD | SHOULD | PASS |
| 2 | SHOULD | SHOULD | PASS |
| 3 | SHOULD | SHOULD | PASS |
| 4 | SHOULD | SHOULD | PASS |
| 5 | SHOULD | SHOULD | PASS |
| 6 | SHOULD | SHOULD | PASS |
| 7 | SHOULD | SHOULD NOT | **FAIL** (JUDGE) |
| 8 | SHOULD | SHOULD | PASS |
| 9 | SHOULD | SHOULD | PASS |
| 10 | SHOULD | SHOULD | PASS |
| 11 | SHOULD NOT | SHOULD NOT | PASS |
| 12 | SHOULD NOT | SHOULD NOT | PASS |
| 13 | SHOULD NOT | SHOULD NOT | PASS |
| 14 | SHOULD NOT | SHOULD NOT | PASS |
| 15 | SHOULD NOT | SHOULD NOT | PASS |
| 16 | SHOULD NOT | SHOULD NOT | PASS |
| 17 | SHOULD NOT | SHOULD NOT | PASS |
| 18 | SHOULD NOT | SHOULD NOT | PASS |
| 19 | SHOULD NOT | SHOULD NOT | PASS (JUDGE) |
| 20 | SHOULD NOT | SHOULD NOT | PASS |
| 21 | SHOULD | SHOULD | PASS |
| 22 | SHOULD NOT | SHOULD NOT | PASS |
| 23 | SHOULD | SHOULD | PASS (JUDGE) |

**Pass rate: 22/23.** Single failure is the 1.1.0 decoupling boundary in the name-invocation direction: row 7's bare \"commwright\" mention fires the 'when they say \"commwright\"' trigger clause in a cold listing read, overriding the \"to define or save a voice, brandwright\" hand-off — the description needs a carve-out on the name trigger (or the row must accept load-then-redirect); the content-only twin (row 23) holds cleanly.

JUDGE notes: #7 — name-mention trigger vs. explicit voice hand-off, irreducible conflict, judged by strongest-signal rule. #19 — passes on assistant-level restraint (harassment declined before routing), not on any boundary present in the description text. #23 — \"brand... apply\" wording pulls toward brandwright, but both descriptions cross-reference message-voice application to commwright and the target is a message.
