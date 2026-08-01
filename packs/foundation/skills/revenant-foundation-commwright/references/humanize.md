# Humanize: the deep catalog

The hard rules **H1 to H9 live in the SKILL body**, with their counting units and their thresholds. This file states no hard rule and never restates one. It carries what will not fit inline: how each rule is detected and repaired, the judgement-tier tells no hard rule catches, the lexicon decision procedure, one worked repair, and an honest account of what this doctrine gets wrong. Nothing here outranks the body: if a line reads like a hard rule, the body is right and this file is wrong.

**When to open it.** Not on a standard draft, which touches the matching section of `channel-profiles.md` and nothing else. Open this one for **Entry - Humanize**, for a `commwright audit` scoring tell density, and when a draft is long or tell-dense enough that the catalog earns its cost.

**Scope.** These rules govern the *messages commwright writes*, never this pack's own docs, SKILL bodies, or any other repo file. Humanize operates on a message bound for a channel; where a repo file's tone ask routes instead (skillwright owns that prose) is homed once in the body's Scope note, and this file restates none of it. Two surfaces self-apply H1 as a demonstration, this file and the body's hard-rules block, which is why neither carries a dash in its own prose (the worked repair's BEFORE block is a specimen and carries three on purpose, as *Worked repair* says on the spot) and why this file spells the entry `Entry - Humanize`. Every other doc in the pack stays exempt.

## Entry - Humanize: what the SKILL body cannot fit

- **Why the quirks promise has no density carve-out.** The ask behind Humanize is that no dash and no emoji comes back. A threshold or a keep-the-habit exception would defeat the request it serves, which is why H1 and H2 run absolute over handed-in text.
- **A gap you created is not yours to fill.** When a recast or a lexicon fix needs a fact the source does not contain, keep the source's wording and ask, per the Restraint clause.
- **The quoted-material exemption reaches every entry.** A Build draft quoting a customer email, or a release note quoting a commit message, reproduces that text as written, dashes and all.

## Applying the hard rules

Three tiers, not two. H1 and H2 settle on a codepoint scan. H5 and H7 have an exact-match core plus a judgement rim: the listed strings are mechanical, the family around them is not, and the anchors below are how you judge it. H3, H4, H6, H8, and H9 turn on a counting unit or a register floor, both of which the body states; what follows is how to see the breach and repair it.

- **H1, repair order.** Full stop first, and usually right. Then the colon, when the second half delivers on the first; parentheses, when the aside is genuinely optional; the comma, only when the aside is short and the sentence is grammatical without it. Substitution without recast is the failure: it leaves a limp aside or a splice.
- **H1, where the habit migrates.** Parentheses are the recommended repair and therefore where the banned rhythm reappears, which is what the body's per-paragraph cap is for. Promote the aside to its own sentence, or cut it.
- **H2, shortcodes.** Rendering is platform-dependent, so no fixed list is possible. Treat any colon-wrapped token the target platform renders as an emoji; where the platform is unknown, cut it.
- **H3, what uniformity looks like.** When nearly every sentence lands in the 15-to-25 band, the band is the tell, not any one sentence. A bulleted output gets the check on its own terms: not every bullet the same shape and length.
- **H4, what is not preamble.** The opening move a formal letter or a legal notice is expected to make. What H4 does bite: restated requests, enthusiasm inflation, runway, and meta-commentary about the edit itself.
- **H5 and H6, reading the close.** Ask what the last paragraph does: name a date, make an ask, promise a future action, or only signal that you are around. "I will share updates as they come" does the third.
- **H7, recognizing the family.** The list is exact-match; the family is wider than any list. An inflation frame promotes a claim without adding a fact, which is the shape to look for once the listed strings are gone.
- **H8, seeing the count.** Segment the sentence into its independent clauses first, then count inside each. Most false passes come from reading a two-clause sentence as one unit.
- **H8, the guard in practice.** "Low risk for downstream consumers" cut to "nothing changes for downstream consumers" is a fact change wearing a tell removal's clothes. If the sentence got stronger, the qualifier was a fact. When both qualifiers in a clause survive that test, as in "roughly 200 accounts may be affected", the exit is a recast that moves one into the verb: "We expect roughly 200 accounts to be affected."
- **H9, the specimen.** "A decision was made to defer the migration, and clarification will be provided following the completion of the review" clears H1 through H8 and is unmistakably machine: the largest source of dead institutional prose, and the one class no other rule catches. Repaired: "The platform team deferred the migration and will explain once the review finishes." Same facts, half the words, an actor in both clauses.
- **H9, the two tests.** Point at the subject who acts in each sentence; if you cannot, the actor is missing ("was made", "will be provided", "is being addressed", "it was determined"). Then ask whether the real action sits in a word ending in -tion, -ment, -ance, or -ing, propped up by do, make, provide, perform, conduct, or undertake. Fixes: provide clarification becomes clarify; conduct a review becomes review; the implementation of becomes implementing.
- **H9, the middle move.** Naming the actor is first, asking is last, and most drafts die in between. The recast gets you out where the sentence never needed a subject: an intransitive verb, or a nominal bullet label. Reach for a stative verb only where the source itself reports a state; a stative recast of a source that reported an act is not the exit, it is the breach the "Transport is arranged" specimen below shows. That is where the freeze breaks, under the step-two constraints the body states. How to see it: count the source's events and then the repair's, and read the repair's verb back as a claim of its own. "Turned up at 09:14" for "was first identified at 09:14, when elevated error rates were observed" reports one event where the source reported two. "The clinic faxed the referral" for "the referral was faxed from the clinic" reports a sender where the source reported a place. "Transport is arranged" for "Transport has been arranged" reports a standing state where the source reported an act, and "needed a manual fix" for "were fixed by hand" reports a need where the source reported a completion. The merge is the loudest of the four. The other three add no actor the source lacks and drop no manner or means word, so a two-item diff clears all three, and the clinic one clears even a zero-novel-token check, because every word in it appears in the source. Reading a repair for words is not the check. Reading each repaired verb back as a claim is.
- **H9, the register floor in practice.** The body states the floor; what it cannot fit is the judgement call at the seam, where the artifact and the update about it travel together. Worked through in Contested repairs.

## Tell catalog

### Punctuation and typography

- **Dashes** (H1) and **emoji** (H2) are the body's business. See Residual risks for what those two rules actually are.
- **Bold mid-sentence.** Emphasis bolded inside a running sentence. Fix: cut it; if the phrase needs weight, move it to the front. Bold is for lead lines and labels a channel profile requires.
- **Headers on short content.** A `##` over two sentences. Fix: under roughly 150 words, no headers. The lead line is the header.
- **Title Case section labels.** "Key Takeaways", "Next Steps", "TL;DR", "Overview". Same fix as headers, and they survive only where the profile asks for them.
- **Nested bullets for one-sentence ideas.** A sub-bullet under a bullet, both one line. Fix: flatten, or merge into the parent.
- **Listification.** An argument chopped into bullets so it looks scannable, losing the connective tissue that made it an argument. Fix: bullets carry parallel items, prose carries reasoning.

### Sentence shape: rhythm

- **Uniform sentence length** (H3). **Opener uniformity** is the louder cousin: every sentence starting subject-first, or on "The" or "This". Fix: vary the entry point, and name the noun instead of a bare anaphoric "This helps ensure".
- **Paragraph uniformity.** Three-sentence blocks forever. One paragraph that is a single sentence fixes it.
- **Rule of three.** "clear, concise, and compelling". *Judgement:* a tell when the third adds nothing the first two lack. Test: delete the third term. If no fact is lost, it was a tell; if a reader would ask a new question, keep it.
- **Machined parallelism.** Every limb the same shape at the same length. *Judgement anchor:* parallelism a reader scans (release-note items, options, steps) is structure and stays; parallelism inside running prose is a tell. Fix: break one limb.
- **Zero fragments.** *Judgement:* over roughly 200 words with no fragment anywhere reads machined. Fix: at most one, and only where it lands the point of the paragraph it ends. Never mid-paragraph, never as a topic sentence. This is the one repair that adds a tic, and a fragment dropped in for rhythm alone is itself a tell. Register floor: formal email, legal notices, and release notes take complete sentences, so the fix does not apply there.

### Lexicon

A smell test, not a filter. A flagged word is sometimes the right word. One question decides it: **does a plainer word lose anything?** If yes, keep it, and under Entry - Humanize say so in the report line. If no, it was a tell.

**High smell** (presume tell; keep only on a stated reason): delve, leverage (verb), seamless, holistic, multifaceted, intricate, pivotal, realm, landscape (metaphorical), tapestry, testament, underscore, foster, garner, elevate, unlock, harness, navigate (metaphorical), embark, journey (metaphorical), arsenal, treasure trove, game-changer, cutting-edge, best-in-class, synergy, resonate.

**Context-dependent** (presume fine unless the plainer word costs nothing): robust, comprehensive, nuanced, crucial, vital, align, streamline. Precise in a spec or a benchmark. Filler in a sentence about a project going well.

**A term of art in the reader's field is not a smell word.** "Threat landscape" is the standard security term, "leverage" is standard finance and ops, "escalate" and "elevate" are standard support register. The list catches the metaphor, not the trade word.

**Density.** The plainer-word question is per instance and misses the real signal, which is repetition. Flag when one smell word repeats inside roughly 200 words, or when three or more distinct smell words share a paragraph.

**Fix pattern.** Replace the abstraction with the concrete thing behind it, *when that thing is in the source or the thread*. "Robust improvements in performance" becomes the number. If the concrete thing is not there, delete the abstraction or keep the source's own wording, and ask. Substituting a plausible specific is fabrication, which is the more serious defect.

### Wordiness and verb inflation

- **Exact-match pairs.** "in order to" becomes to; "due to the fact that" becomes because; "a number of" becomes the number or some; "at this point in time" becomes now; "in terms of", "when it comes to", and "the fact that" usually delete outright.
- **Inflated verbs.** ensure and help ensure, serves to, plays a key role in, acts as a, is designed to, enables. Fix: the plain verb the sentence was reaching for.

### Structure and rhetoric

- **Preamble and enthusiasm inflation** (H4), **recap close** (H6), **trailing help offer** (H5), **hedge stacking** (H8), **the missing actor** (H9).
- **Email boilerplate.** "I hope this email finds you well", "I wanted to reach out regarding", "circling back", "touching base", "just following up". Fix: open at the point. The greeting stays; the runway after it does not.
- **Over-signposting.** "First... Second... Finally..." across three short points. Fix: cut the ordinals, three sentences are already three sentences. Keep them where sequence is load-bearing.
- **Both-sides framing.** A balanced survey when the writer has a position. *Judgement anchor:* if the request or the thread shows that position, the draft states it. Fix: lead with the position, then the strongest objection, once.
- **Terminal qualifier.** Refusing to let a sentence end: "...though of course this may vary depending on the context." Test first: does the tail after the comma name a condition, a scope, an exception, or a date? Then it is content, and it may deserve its own sentence. Delete from the comma only when the tail adds no condition.

### What replaces a tell

The subtractive half is easy and it is not enough; a draft can pass every rule above and still be dead. The additive moves, with the H9 specimen as the worked case: **name the actor** in the subject slot; **use the specific verb** rather than a weak verb plus a noun; **insert the number** where an adjective is doing the work; **take a position, then a full stop**. Contractions follow the register floor: formal and legal take none, neutral professional and below take them, and `channel-profiles.md` sets the register. On actorless source text that floor is often unreachable, because contractions live on the subject-verb pairs the freeze forbids inventing; no contractions is a pass, not a shortfall, when the source supplies no subjects. And, But, or So can head a sentence when the rhythm wants it.

## Where humanize yields

Humanize operates inside the channel profile. It never overrides one.

- **Required structure is not a tell.** A Slack bold lead line, a Discord `**bold headline**`, Keep-a-Changelog buckets, YouTube chapter lists, release-note bullets: contracts, not decoration. The typography rules bite only on structure the profile did not ask for.
- **A handed-in voice profile.** Its lexicon-do list beats the smell list. The collisions worth expecting: a profile sign-off carrying a dash gets recast, and a profile emoji allowance does not fire.
- **The profile owns register, humanize owns humanity.** Formal register plus humanize is plain, complete, tell-free sentences. It is not casual.

## Residual risks

- **H1 and H2 are house policy, not laws of writing.** Em dashes are normal in good human prose, and the real tell is uniform overuse, not the codepoint. This pack bans the character outright because a bright line is cheaper to enforce than a density judgement, and because the owner asked for it. The costs are real: some sentences lose their best punctuation, and legitimate en-dash typography is collateral. Emoji are worse on their own ground, since on Discord, social, and YouTube they are native convention rather than a machine tell. That is what the per-message override is for.
- **A repair can keep every word and still move a claim.** The near-miss in the worked repair below: "the team spent several weeks on the dependencies" uses only source nouns and still re-attaches a duration the source put on the whole migration. Modifiers travel quietly. Check what each one is attached to on both sides, and work the body's complete fact-movement list rather than a noun-membership scan.
- **A large shrink is a signal, not a success.** If the AFTER is under half the BEFORE, look at what did the shrinking. An evaluative sentence that still says something once its smell words are gone stays, in plainer words; one that says nothing without its frames can go.
- **One voice across a set.** The rules are uniform, so their output is too, and a cadence set is where it shows: five messages, one metabolism, each individually clean. The body's Cadence sets line carries the countermove.
- **Over-application reads dead.** Symptoms: every sentence clipped under ten words, fragments used as decoration, contractions forced into a legal notice, a release note stripped of its precise term. Tic-free is not the goal. Sounding like a person wrote it is. If the repair makes the sentence worse, the tell was not the problem.
- **The word list is a smell test.** Run as find-and-replace it produces prose that dodges words instead of saying things. Ask the plainer-word question, then decide.
- **Humanize never fakes humanity.** No invented typos, no manufactured casualness, no slang the writer does not use, no anecdote that did not happen, no personality transplant. It removes what a machine added. It does not add what a person would have.
- **A hedge is not always padding.** Some hedges describe real uncertainty, and a draft that deletes one has deleted the uncertainty with it. Where something is genuinely unknown, the honest repair says so once, plainly.
- **Never called a voice.** Humanize is not defined, saved, named, or exported. Requests to store a way of writing route to brandwright.

## Worked repair

A handed-in Slack update, run through Entry - Humanize. The BEFORE block deliberately contains banned characters and a banned shortcode. It is the specimen, not the doctrine.

BEFORE:

```
Great question! I'd be happy to give an update on where things stand.

It's worth noting that the database migration — which the team has been
working diligently on for several weeks — is now complete as of Tuesday.
:tada: They did a **truly comprehensive** job navigating a complex and
multifaceted landscape of dependencies. Moreover, we've seen robust
improvements in p95 query latency, which fell from 840ms to 210ms.

It's not just faster, it's more reliable — there were no failed writes
during the cutover window.

**Next Steps**
- We will continue to monitor
  - Monitoring runs through Friday

At the end of the day, this is a game-changer for the platform. Let me know
if you have any questions!
```

AFTER:

```
**The database migration is complete** as of Tuesday. The team worked
diligently on it for several weeks, and the dependencies were complex.

p95 query latency fell from 840ms to 210ms, and no writes failed during
the cutover window.

We're monitoring through Friday.
```

Report line: removed the opener, three em dashes, an emoji shortcode, mid-sentence bold, a header over two lines, a nested one-line bullet, the help offer, six smell words, four inflation frames, and a closing sentence that made no claim; kept the bold lead, which the Slack profile requires, and kept the writer's read of the team and the dependencies, in plainer words.

One line, because it reports by category and not by instance. The fact audit runs before it and is not printed, and it runs at the claim level, on the terms the body sets under **Fact integrity on repair**. Tuesday, the several weeks, the dependencies, 840 to 210, the failed writes, and Friday all trace, each with the subject it had in the source.

A noun-membership check ("no noun in the AFTER is missing from the BEFORE") is weaker, and its failures are the point. It catches the invented "dependency graph", which is why the repair says dependencies. It clears "the team spent several weeks on the dependencies", which narrows the object that duration was attached to, and it clears "we deployed the fix at 11:02", because "we" and "the team" are both in the source, while inventing an attribution nobody made. The claim-level test rejects both.

## Contested repairs

Three cases where the mechanical answer is wrong or missing, which is what this file is for.

**An incident update posted to Slack.** The passive floor exempts the postmortem, the status-page notice, and the legal disclosure. A channel post about the same incident is a different artifact, and the topic does not carry the exemption across: on Slack, Teams, or email, incident comms names the actors the source supplies and recasts the rest. Why that ruling and not the other: the exemption exists to keep a person out of a formal record, and a team update is not a record.

**A flagged word that stays.** "Robust under 3x load, per the soak test." Robust is on the context-dependent list, and the plainer words lose: strong and good do not carry surviving stress, and the benchmark next to it makes the term precise. Keep it, and say so in the report line: *kept "robust", the engineering sense, next to the soak-test number.*

**A repair that is refused.** A release note lists four items in the same shape and length. Machined parallelism says break one limb; the profile says these are scannable items. The profile wins, the limb stays, and nothing is reported. When a judgement fix makes the sentence worse or fights a contract, the tell was not the problem.
