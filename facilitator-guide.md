# Facilitator guide

Minute-by-minute run of show for the 180-minute Prompt & Agent Engineering Workshop. The same
content is delivered twice: once virtually, once in person. Timings are identical in both
modes and come from [schedule.json](schedule.json).

Companion files: [participant-workbook.md](participant-workbook.md),
[slides/slide-outline.md](slides/slide-outline.md),
[facilitator-materials.md](facilitator-materials.md),
[contingency-plan.md](contingency-plan.md), [train-the-trainer.md](train-the-trainer.md).

## How to read this guide

- **Say** = talk track, paraphrase freely, do not read aloud.
- **Do** = your actions, including demos.
- **Ask** = audience question with the response you are steering toward.
- **Time check** = the clock position you must be at, or you are behind.
- **FALLBACK** = what to do when something breaks.

Golden rule: **the activities are the workshop.** If you are behind, cut teaching content, not
activity time. Every teaching segment below has an explicit "cut this first" line.

---

## Master schedule

| Minutes | Block |
| --- | --- |
| 0-7 | Welcome, objectives, setup check |
| 7-82 | Session 1 — Prompt & Agent Engineering Foundations |
| 82-87 | Transition and knowledge check |
| 87-102 | Break |
| 102-177 | Session 2 — Multi-Author PromptOps & Governance |
| 177-180 | Close and handoff |

---

## Welcome, objectives, setup check — minutes 0-7 (7 minutes)

Slides 1-4.

**Do (before minute 0).** Room or meeting open 10 minutes early. Repository link and the
workbook link visible on screen and posted in chat. Timer running.

**Say (2 minutes).**
> "In three hours you will write a prompt you would actually trust, turn it into an agent
> design with tools and subagents, evaluate it against test cases, and run a change through a
> review process the way a team of authors has to. Everything uses a fictional outdoor gear
> retailer, Contoso Trail Gear, and synthetic messages. Never paste real customer data or
> anything confidential into a chat window today."

**Say (1 minute) — expectations about access.**
> "Everything core today works with a browser, a GitHub account, and Microsoft Copilot chat.
> If you have Microsoft Foundry or GitHub Copilot, there are optional extensions. If you do
> not, you will not miss a single learning objective. Those paths are clearly marked."

**Do (3 minutes) — setup check.** Ask everyone to confirm in chat or by show of hands:
1. Repository open.
2. Microsoft Copilot chat open in another tab.
3. Signed in to GitHub in a browser.

Anyone missing item 3 pairs up now. Note the pairs; you will need them in Session 2.

**Say (1 minute) — ground rules.** Cameras optional. Questions in chat any time. Two-minute
warnings before every activity ends. Parking lot for off-scope questions — name it and show
where you will keep it.

**Time check: you must start Session 1 at minute 7.** If setup is dragging, start anyway and
fix stragglers during Activity A1.

FALLBACK — If a large share of the room cannot reach GitHub, announce now that Session 2 runs
in "draft mode" using the workbook, and see [contingency-plan.md](contingency-plan.md).

---

# Session 1 — Prompt & Agent Engineering Foundations (minutes 7-82, 75 minutes)

## S1.1 Prompt fundamentals — minutes 7-14 (7 minutes)

Slides 5-7. **Cut this first if behind:** the vocabulary slide; the workbook has it.

**Teaching points.**
1. A prompt has parts that each remove a specific failure: role and task, scope and authority,
   grounding rules, decision rules, output contract, untrusted-content rule, escalation rule.
2. Grounding means supplying the facts and forbidding invention — "use only what I gave you,
   and name what is missing."
3. Specificity beats politeness. "Be accurate and helpful" removes no failure mode.
4. Prompts are artifacts, not chat messages. They get versions, owners, and reviews.

**Say.**
> "Most disappointing model output traces back to an instruction nobody wrote down. Today we
> make the implicit explicit, and then we make it testable."

**Ask.** "Who has had a model invent a policy or a fact that sounded completely plausible?"
*Expected:* most hands. Follow with: "What instruction was missing?" Steer to: *nothing told
it what to do when it did not know.*

**Do — 60-second demo.** Paste the starter prompt from
[exercises/01-starter-prompt.md](exercises/01-starter-prompt.md) plus ticket CTG-10421 into
Microsoft Copilot chat on screen. Read the output out loud and circle the invented parts.

**Time check: activity brief starts at minute 14.**

## Activity A1 — improve the starter prompt — minutes 14-26 (12 minutes)

Slides 8-9. Workbook step 1. Exercises
[01-starter-prompt.md](exercises/01-starter-prompt.md) and
[02-improved-prompt-template.md](exercises/02-improved-prompt-template.md).

**Objective.** Diagnose three failure modes in a weak prompt and rewrite it with the seven-part
template.

**Inclusive budget.** 2 minutes brief/read; 3 minutes run and diagnose; 5 minutes rewrite and
rerun; 2 minutes checkpoint/debrief. For virtual delivery, keep participants in the main room
for A1 so breakout transitions do not consume the work time. In person, participants work at
their existing tables.

**Brief (2 minutes).**
> "Run the starter prompt twice on the same message. Write down every failure you see. Then
> rewrite it using the seven-part template in Exercise 2 and run it twice again. Twelve
> minutes. I will give you a two-minute warning."

**Do.** Virtual: assign named pairs in the main room and collect their checkpoint lines in
chat. In person: use tables of 4-6. Circulate; ask each group "which failure would a customer
actually notice?"

**Success criteria.** Two runs agreeing on category and severity; no invented order number,
SKU, or warranty outcome; missing information named; exactly one next action.

**Checkpoint (last 2 minutes, in the room).** One line per group: the single line they added
that made the biggest difference.

**Debrief (inside the 12 minutes, final 2).**
- *Ask:* "What did the model invent before, and what stopped it?" *Expected:* grounding rule
  plus "name what is missing".
- *Ask:* "Did anything get worse?" *Expected:* longer output, over-escalation. Name the
  trade-off out loud — prompts are edited, not just added to.

FALLBACK — Chat unavailable or slow: use the captured weak output in
[exercises/solutions/01-improved-prompt.md](exercises/solutions/01-improved-prompt.md) and run
the diagnosis on paper. Do not let a slow tool eat the rewrite.

**Time check: you must be teaching structured outputs at minute 26.**

## S1.2 Structured outputs and failure modes — minutes 26-33 (7 minutes)

Slides 10-11. **Cut this first if behind:** the failure-mode table; keep the schema walk.

**Teaching points.**
1. A structured output contract is a promise about *shape*, not truth. Valid JSON can be wrong.
2. Enums beat free text: they make disagreement visible and routing possible.
3. Required fields like `missing_information` and `needs_human_review` force the model to
   surface uncertainty instead of hiding it.
4. Applications validate output. The prompt asks; the application enforces.
5. Model variability is normal. Two runs of the same prompt can differ — that is the reason
   evaluation exists.

**Do.** Show [exercises/03-structured-output.schema.json](exercises/03-structured-output.schema.json)
on screen. Point at `required`, at the `severity` enum, and at `additionalProperties: false`.

**Ask.** "If the model returns valid JSON with the wrong severity, what caught it?" *Expected:*
nothing — which is exactly why we evaluate and why humans review safety cases.

**Time check: activity brief at minute 33.**

## Activity A2 — add a structured output contract — minutes 33-43 (10 minutes)

Slide 12. Workbook step 2. Exercise
[03-structured-output.md](exercises/03-structured-output.md).

**Objective.** Produce schema-valid JSON for three synthetic messages and record every
compliance failure.

**Brief (1 minute).** "Append the strict output contract to your prompt. Run the three messages
in Exercise 3. Check each result against the six-box compliance list. Ten minutes."

**Success criteria.** At least two of three schema-valid on the first try; one compliance
failure captured with its fix.

**Checkpoint.** One line each: `TC id | valid? | severity | one problem`.

**Debrief (final 2 minutes).**
- *Ask:* "Did valid JSON ever hide a wrong answer?" *Expected:* yes, at least once in the room.
- *Ask:* "What should the application do when parsing fails — retry, repair, or fail closed?"
  *Expected:* it depends on blast radius; for safety routing, fail closed to a human.

FALLBACK — If the model keeps wrapping JSON in prose or code fences, give the room the line
"Your entire response must start with { and end with }." If it still fails, call it a genuine
finding and move on.

**Time check: minute 43, on to agents.**

## S1.3 From prompts to agents — minutes 43-50 (7 minutes)

Slides 13-15. **Cut this first if behind:** the orchestration patterns slide.

**Teaching points.**
1. **Agent** = prompt + tools + a loop that can take multiple steps. The loop is what is new.
2. **Tool / function calling**: the model emits a structured *proposal*. It cannot execute
   anything. Your application decides. Say this twice.
3. Tool contracts need names, typed parameters, side effects, failure modes, and an approval
   requirement for writes.
4. **Orchestration** is deciding what runs next and when to stop: stop conditions, max turns,
   and human-in-the-loop points are design, not afterthoughts.
5. **Subagents** are worth it when a step has a different owner, different risk, or a different
   failure mode — not for tidiness. Each hop costs latency, cost, and context.

**Say.**
> "The single most expensive misunderstanding in this space: the model said it created the
> ticket, so the ticket exists. It does not. A function-call proposal is not proof that an
> action executed."

**Ask.** "Where does the approval gate for a write action live?" *Expected:* in the
application. If someone says "in the prompt", correct it warmly — the prompt is a request, not
a control.

**Time check: activity brief at minute 50.**

## Activity A3 — tool contract and subagent decomposition — minutes 50-60 (10 minutes)

Slide 16. Workbook step 3. Exercises
[04-tool-contract.md](exercises/04-tool-contract.md) and
[05-subagent-contract-template.md](exercises/05-subagent-contract-template.md).

**Objective.** Get a well-formed tool-call proposal with no invented arguments, then decompose
triage into four subagents with contracts.

**Inclusive budget.** 1 minute brief; 4 minutes tool proposal and failure result; 2 minutes
for three compact subagent rows; 1 minute checkpoint; 2 minutes debrief. For virtual delivery,
keep participants in the main room for this rapid activity so no breakout transition consumes
the work time.

**Brief (1 minute).** "Start a new chat with the complete released prompt, then switch to
tool-proposal mode. Build one proposal, inspect the failed lookup, then fill three compact
subagent rows. The tool output shape temporarily replaces the triage shape; switch back
explicitly before final triage."

**Success criteria.** One clean proposal; the write action marked as requiring approval and
never 'performed'; the failed lookup does not produce an invented order; three subagent rows
with a 'must not' rule each.

**Checkpoint.** "Did your assistant ever claim an action happened? What in the output would
prove it did or did not?"

**Debrief (final 2 minutes).**
- *Ask:* "Which subagent has the highest blast radius if it is wrong?" *Expected:* the safety
  checker.
- *Ask:* "Would one good prompt have been enough?" *Expected:* often yes — decomposition is a
  cost, justified by ownership and risk.

FALLBACK — If the model narrates tool use in prose instead of emitting a proposal, resend the
TOOL RULES block; if it still narrates, record it as a finding. That behaviour *is* the risk.

**Time check: minute 60, Foundry segment.**

## S1.4 Building agents in Microsoft Foundry — minutes 60-66 (6 minutes)

Slides 17-18. OPTIONAL — MICROSOFT FOUNDRY. **Cut this first if behind:** cut to 3 minutes and
show only the agent definition file.

**Teaching points.**
1. Microsoft Foundry (formerly Azure AI Foundry) is where a configured agent is authored,
   tested, evaluated, and observed. The repository stays the source of truth for the text.
2. Author: name, model deployment, instructions, tools. Test: playground-style interaction with
   your synthetic cases. Evaluate: a dataset plus evaluators, with stored runs. Observe: traces
   you can inspect later.
3. Built-in evaluators score signals; they do not certify correctness.
4. Product UI changes often — learn the shape of the work, then check current documentation.

**Do — demo (3 minutes), pick one.**
- *If you have a project:* show an agent's instructions, one synthetic case, and an evaluation
  result list. Do not create resources live.
- *If you do not:* walk through
  [library/agents/triage-agent.agent.yaml](library/agents/triage-agent.agent.yaml) as "the
  configuration you would create", and read
  [optional/foundry.md](optional/foundry.md) aloud from "No-access simulation".

**Say.**
> "This segment is optional for a reason. Nothing in your objectives today depends on having a
> Foundry project, and I will not ask anyone to create cloud resources during a workshop."

**Ask.** "Who in the room already has a Foundry project?" Use the answer to decide whether the
optional path is worth mentioning again at the close.

**Time check: minute 66, evaluation activity.**

## Activity A4 — evaluate against synthetic test cases — minutes 66-76 (10 minutes)

Slides 19-20. Workbook step 4. Exercise
[06-evaluation-rubric.md](exercises/06-evaluation-rubric.md).

**Objective.** Score four cases across two runs, classify every failure, and make an explicit
ship / do-not-ship decision.

**Inclusive budget.** 1 minute brief and pair assignment; 4 minutes to run eight pooled
outputs; 2 minutes to score and classify; 1 minute to decide and post the checkpoint; 2 minutes
for the room debrief. Keep pairs in the main room virtually.

**Brief (1 minute).** "Reset to the released v1.2.0 triage prompt. Each pair runs TC-02,
TC-07, TC-05, and TC-08 twice, splitting the eight runs between partners. Include the Ticket
ID with each intake; never paste the expectations. Pool and score all eight outputs, then
write one sentence: ship or hold, and why."

**Do.** Split the other six cases across rooms or tables if you have time; do not require it.

**Success criteria.** Four cases scored across two runs; every failure classified as prompt
gap, variability, bad test case, or real ambiguity; a written decision.

**Checkpoint.** `cases run | blocking failures | ship or hold`.

**Debrief (final 2 minutes) — this is the most important debrief of Session 1.**
- *Ask:* "Who saw the same input produce different answers?" *Expected:* several. Name it:
  variability is a property of the system, not a bug you can prompt away.
- *Ask:* "What can this evaluation set never tell you?" *Expected:* coverage of real traffic,
  tone, latency, cost, and anything nobody thought to test.
- *Say:* "Evaluation reduces risk. It never guarantees correctness and never replaces human
  review."

FALLBACK — Score the raw pre-captured outputs in
[exercises/solutions/06-pre-captured-outputs.jsonl](exercises/solutions/06-pre-captured-outputs.jsonl),
then reveal the separate answer key in
[exercises/solutions/06-eval-results.reference.csv](exercises/solutions/06-eval-results.reference.csv).

**Time check: minute 76.**

## S1.5 Reusable templates and train-the-trainer handoff — minutes 76-82 (6 minutes)

Slide 21. **Cut this first if behind:** cut to 3 minutes, point at the files, move on.

**Teaching points.**
1. What participants take away, concretely: the seven-part prompt template, the output schema,
   the tool contract shape, the subagent contract template, and the evaluation rubric.
2. Swap the scenario, keep the structure. Never put confidential content in a shared library.
3. Teaching this to their own team is an explicit goal — [train-the-trainer.md](train-the-trainer.md)
   contains the rehearsal plan, the misconceptions, and the FAQs.
4. Session 2 answers the obvious next question: what happens when five people author these at
   once?

**Ask.** "Which of these five templates will you use next week?" Collect two or three answers;
they seed the Session 2 discussion.

**Time check: you must hand off to the knowledge check at minute 82.**

---

## Transition and knowledge check — minutes 82-87 (5 minutes)

Slide 22.

**Do.** Five rapid questions. Virtual: poll or chat. In person: hands or sticky dots.

1. *Ask:* "A model returns a function-call proposal. Did the ticket get created?" **Expected:
   no — an application must execute it, and in our design a human approves it first.**
2. *Ask:* "Your output is valid JSON. Is it correct?" **Expected: not necessarily; shape is not
   truth.**
3. *Ask:* "Same prompt, same input, two different answers. Bug or expected?" **Expected:
   expected variability; run twice, tighten decision rules, do not declare victory on one run.**
4. *Ask:* "When must a human review a triage result?" **Expected: any safety flag, low
   confidence, or missing material information.**
5. *Ask:* "What does a passing evaluation prove?" **Expected: that those cases passed, this
   time.**

**Say.** "After the break we stop working alone. Same scenario, five authors, one library, and
the question becomes: how does a change get in safely?"

**Time check: break starts at minute 87. Start it on time even mid-sentence.**

---

## Break — minutes 87-102 (15 minutes)

**Do.**
- Put the return time on screen as a clock time, not "15 minutes".
- Virtual: leave the meeting running, share the repository link again, mute yourself.
- In person: point to refreshments and restrooms; leave the timer visible.
- Use the first 5 minutes to help anyone who still cannot reach GitHub. Pair them now.
- Use the last 3 minutes to preload Session 2: the library files and the pull request template.

FALLBACK — If more than a third of the room is blocked on GitHub access, decide during the
break to run Session 2 in draft mode. See [contingency-plan.md](contingency-plan.md).

---

# Session 2 — Multi-Author PromptOps & Governance (minutes 102-177, 75 minutes)

## S2.1 PromptOps lifecycle and the shared library — minutes 102-108 (6 minutes)

Slides 24-25. **Cut this first if behind:** the library layout table; it is in the workbook.

**Teaching points.**
1. The lifecycle: author, review, evaluate, release, monitor, improve. It is a loop, not a line.
2. A prompt is not "shared" until it has an owner, a version, an output contract, and a test
   set. Say those four out loud.
3. The library is plain text so it can be diffed, reviewed, and reverted — that is the whole
   trick.
4. Copy-paste prompt sharing in chat threads is how organizations end up with six divergent
   versions and no owner.

**Do.** Show [library/README.md](library/README.md) and
[library/prompts/triage-intake.prompt.md](library/prompts/triage-intake.prompt.md). Point at
the front matter: id, version, owner, schema, test set.

**Ask.** "Where does your team's best prompt live today?" *Expected:* a chat thread, a
document, someone's laptop. No shaming; that is the starting point for everyone.

## S2.2 GitHub as source of truth — minutes 108-115 (7 minutes)

Slides 26-27. **Cut this first if behind:** the branch naming table.

**Teaching points.**
1. Repository structure: prompts, agents, contracts, tests, governance, changelog.
2. Branch per change, named for the change: `prompt/triage-intake-safety-boundary`.
3. Pull requests are where intent, evidence, and review live — the diff alone is never enough.
4. Parallel authoring works when changes are small and files are focused; conflicts are a
   signal that two people are editing the same rule and need to talk.
5. Protect the default branch; require review. The rule is cheap and prevents the worst day.

**Do — demo (2 minutes).** In the GitHub web UI: open the prompt file, click the pencil, show
the "create a new branch" option on the commit form, and show the pull request template
appearing in the PR body. Narrate that no local tooling was used.

**Ask.** "Who has ever lost a prompt improvement because someone overwrote it?" *Expected:*
several. That is the problem branches solve.

**Time check: activity brief at minute 115. This is the longest activity; protect it.**

## Activity B1 — parallel authoring via branch and pull request — minutes 115-130 (15 minutes)

Slide 28. Workbook step 5. Exercise
[07-lifecycle-change-exercise.md](exercises/07-lifecycle-change-exercise.md), section B1.

**Objective.** Each participant lands a small, reviewable prompt change as a pull request in
their own fork, with different partners making different changes at the same time.

**Brief (3 minutes).** Assign roles A, B, C, D within each pair or table so changes differ. Show
the branch naming convention on screen. Remind them to fill the PR template properly — the
body is the artifact being reviewed.

**Success criteria.** A focused diff; a PR body with intent, evidence, and rollback; a branch
name that says what changed; no direct edit of the default branch.

**Checkpoint.** Post the PR title and the changed line.

**Debrief (final 3 minutes).**
- *Ask:* "What if you had both edited the same line?" *Expected:* a conflict — which is the
  system telling you to have a conversation.
- *Ask:* "What belongs in the PR body that a diff can never show?" *Expected:* why, evidence,
  blast radius, rollback.

FALLBACK — Forking blocked: everyone drafts the change as a hand-written diff plus PR body in
the workbook. B2 then reviews those drafts in pairs. Announce the switch in one sentence and
keep the energy up.

**Time check: minute 130.**

## S2.3 Governance and ownership — minutes 130-137 (7 minutes)

Slide 29. **Cut this first if behind:** the RACI table detail; teach the three standing rules.

**Teaching points.**
1. CODEOWNERS routes review automatically by path — the highest-leverage governance file you
   can add in ten minutes. Placeholder teams like `@your-org/prompt-owners` must be replaced
   with real teams or nothing is enforced.
2. One accountable owner per decision type. See
   [governance/ownership-raci.md](governance/ownership-raci.md).
3. **Model selection is a governed decision**, not a detail inside a prompt edit. Change the
   model, re-run the evaluation.
4. Subagent contracts are governance artifacts: responsibility, allowed tools, must-nots,
   failure handling, owner.
5. Assistant-drafted changes follow the identical path. Disclosure required; approval boundary
   unchanged.

**Do.** Show [.github/CODEOWNERS](.github/CODEOWNERS) and
[governance/CODEOWNERS.sample](governance/CODEOWNERS.sample) side by side; point at the
placeholder warning.

**Ask.** "Who owns the safety rule in your organization today?" *Expected:* often silence.
That silence is the finding.

## Activity B2 — governance review — minutes 137-149 (12 minutes)

Slide 30. Workbook step 6. Exercise
[07-lifecycle-change-exercise.md](exercises/07-lifecycle-change-exercise.md), section B2.

**Objective.** Review a partner's pull request against
[governance/pr-checklist.md](governance/pr-checklist.md) and reach an explicit decision.

**Brief (2 minutes).** "Swap PRs. Leave at least three comments: one blocking, one question,
one suggestion. Name the approver role who would have to sign this off for real. Then respond
to the review you received."

**Success criteria.** Every checklist item satisfied or explicitly waived with a reason; at
least one comment citing evidence rather than taste; the required approver named.

**Checkpoint.** `PR reviewed | blocking items found | decision`.

**Debrief (final 3 minutes).**
- *Ask:* "Which checklist item caught the most problems?" *Expected:* evidence, or the missing
  changelog entry.
- *Ask:* "What would you automate and what must stay human?" *Expected:* automate schema
  validity and regression runs; keep safety judgment and release approval human.

FALLBACK — Review the reference PR body in
[exercises/solutions/07-lifecycle-change-solution.md](exercises/solutions/07-lifecycle-change-solution.md)
against the checklist, on paper, in pairs.

**Time check: minute 149.**

## S2.4 Quality and operations — minutes 149-156 (7 minutes)

Slides 31-32. **Cut this first if behind:** the signals table; keep release gate and rollback.

**Teaching points.**
1. Evaluation before release; regression on every change; monitoring after release. Three
   different jobs, often confused.
2. A release gate you can actually hold: owner approval, checklist, evidence attached, two runs
   for safety cases, changelog entry, rollback target.
3. Rollback for a prompt should be a one-file revert plus a re-run of the safety cases. If it is
   not, you have hidden coupling.
4. Monitoring signals worth having on day one: schema validity, `needs_human_review` rate,
   reviewer override patterns, safety misses, tool failure rates.
5. OPTIONAL — MICROSOFT FOUNDRY: stored evaluation runs and traces make this evidence easier to
   produce. The manual CSV meets the same bar for a small team.

**Ask.** "What is the smallest rollback you could perform today?" Let two people answer; it
usually reveals whether prompts live in code, config, or a chat thread.

## Activity B3 — monitoring signal to issue to proposed change — minutes 156-168 (12 minutes)

Slide 33. Workbook step 7. Exercise
[07-lifecycle-change-exercise.md](exercises/07-lifecycle-change-exercise.md), section B3.

**Objective.** Convert a synthetic monitoring digest into an issue with signal, impact,
proposal, required evidence, rollback, and owner.

**Brief (3 minutes).** Read the digest on screen. Ask which number matters most — steer away
from the 18 percent review rate toward the 22 consistent override pattern, because it is
specific, repeatable, and safety-relevant.

**Do.** Participants create the issue in their fork using the structure in the exercise.
Mention the OPTIONAL — GITHUB COPILOT path once, then keep the room on the core path; people
without a license must not feel like spectators.

**Success criteria.** Signal and impact stated separately; specific checkable evidence
requirements; a rollback plan naming a version; an explicit human approver.

**Checkpoint.** `issue created | evidence required | approver`.

**Debrief (final 3 minutes).**
- *Ask:* "How do you stop the prompt growing one rule per incident forever?" *Expected:*
  periodic pruning and consolidation, owned by someone.
- *Ask:* "Who approves this change, and does the answer change if an assistant wrote it?"
  *Expected:* same owner, same checklist, same evidence.

FALLBACK — Write the issue body in the workbook and read it aloud. The artifact is the point.

**Time check: minute 168. Do not run long; the closing discussion is where commitments happen.**

## S2.5 Discussion, recommendations, next steps — minutes 168-177 (9 minutes)

Slide 34.

**Do (4 minutes) — open discussion.** Seed with:
- "What is the smallest version of this you could adopt next week?"
- "Where would governance help you today, and where would it just slow you down?"
- "What would you need to convince your team to move prompts into a repository?"

**Say (3 minutes) — recommendations, in adoption order.**
1. One repository as the source of truth for prompts and agent definitions.
2. One named owner per prompt, written in the file.
3. Pull requests required; no direct pushes to the default branch.
4. A ten-case test set, run twice for anything safety-relevant.
5. A one-line changelog per release and a named rollback target.
6. One monitoring signal reviewed weekly, with an issue when it moves.
7. Everything else later.

**Do (2 minutes) — next steps.** Ask each person to write one commitment with a date in their
workbook. Virtual: post it in chat. In person: say it to the table.

## Close and handoff — minutes 177-180 (3 minutes)

Slide 35.

**Say.**
> "Three things to take with you. One: a prompt is an artifact — it gets an owner, a version,
> and a test set. Two: an agent is a prompt plus tools plus a loop, and a function-call proposal
> is not proof that an action executed. Three: evaluation reduces risk, but it never guarantees
> correctness and never replaces human review."

**Do.**
- Point at the repository: workbook, exercises, governance, and
  [train-the-trainer.md](train-the-trainer.md) for anyone teaching this to their team.
- Point at [resources.md](resources.md) for official Microsoft and GitHub documentation.
- Thank the room. Stay 5 minutes after for questions if you can.

**End at minute 180.**

---

## Virtual and in-room adaptations

| Moment | Virtual | In person |
| --- | --- | --- |
| Setup check (0-7) | Ask for three chat confirmations | Show of hands, walk the room |
| Activities | Breakout rooms of 3-4, named reporter, facilitator hops rooms | Tables of 4-6, circulate constantly |
| Two-minute warnings | Broadcast message to all rooms | Say it loudly, twice |
| Checkpoints | One line per person in chat | Sticky notes on a wall, or round-robin |
| Sharing PRs (115-149) | Paste links in chat, swap in pairs | Swap laptops or project one PR |
| Knowledge check (82-87) | Poll or chat answers | Hands, or dots on a flip chart |
| Break (87-102) | Leave the meeting open, post return clock time | Post return clock time on the screen |
| Discussion (168-177) | Call on named people; silence is normal online | Open floor works better |
| Biggest risk | Nobody speaks; work happens invisibly | Tables drift into off-scope debates |

## Fallback plans at a glance

| Problem | Response |
| --- | --- |
| Chat surface unavailable or slow | Use captured outputs in `exercises/solutions/`; shift time to analysis |
| GitHub unreachable or forking blocked | Draft-mode Session 2 in the workbook; pair review verbally |
| Nobody has Foundry access | Run the no-access simulation; it is a first-class path |
| Nobody has GitHub Copilot | Run the core manual path; mention the optional path once |
| Running 5+ minutes behind | Cut the "cut this first" items in each teaching segment; never cut activity time |
| Running ahead | Add test cases in A4; add a second review round in B2 |
| Room is silent | Switch from open questions to named questions; use the checkpoint format |
| A participant pastes real customer data | Stop sharing/recording and do not repeat it; remove it where possible, follow your organization's incident process, and do not promise retained copies were deleted |

Full detail: [contingency-plan.md](contingency-plan.md).

## Pre-delivery prep checklist

Complete these before each delivery. Total time: about 45 minutes.

**Content (20 minutes)**
- [ ] Read this guide end to end once, out loud, watching the clock.
- [ ] Run the A1 demo yourself in Microsoft Copilot chat and capture the output as a backup
      screenshot.
- [ ] Run TC-02 and TC-07 once each so you know what the room will see.
- [ ] Skim [exercises/solutions/](exercises/solutions/) so you can reveal the right file fast.
- [ ] Decide your Foundry demo choice: live project, or the no-access walkthrough.

**Logistics (15 minutes)**
- [ ] Fork the repository yourself and confirm the web-UI branch-and-PR flow works end to end.
- [ ] Confirm the repository link you will share is reachable from a browser without special
      access.
- [ ] Prepare the chat messages you will paste: repository link, workbook link, activity briefs,
      return-from-break clock time.
- [ ] Set up the timer you will actually use.
- [ ] Virtual: pre-create breakout rooms. In person: confirm table layout and screen.

**Risk (10 minutes)**
- [ ] Read [contingency-plan.md](contingency-plan.md).
- [ ] Download or open offline copies of the workbook and the solutions folder.
- [ ] Have the captured weak-output text ready to paste if chat is down.
- [ ] Confirm a co-facilitator or helper for chat monitoring (virtual) or room support
      (in person).
- [ ] Send [participant-preflight.md](participant-preflight.md) if you have not already.

## Related

- [Participant workbook](participant-workbook.md)
- [Slide outline](slides/slide-outline.md)
- [Train the trainer](train-the-trainer.md)
- [Facilitator materials](facilitator-materials.md)
- [Contingency plan](contingency-plan.md)
- [Exercises](exercises/README.md)
- [Governance](governance/README.md)
- [Resources](resources.md)
