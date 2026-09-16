# Slide outline

35 slides for the 180-minute Prompt & Agent Engineering Workshop. Timings come from
[../schedule.json](../schedule.json) and match [../facilitator-guide.md](../facilitator-guide.md)
exactly.

Design rules for whoever builds the deck: no walls of text, at most five short lines per slide,
one idea per slide, speaker notes carry the detail. Slides support the activities; they are not
the content.

Labels: CORE, OPTIONAL — MICROSOFT FOUNDRY, OPTIONAL — GITHUB COPILOT, FALLBACK.

---

## Slide 1 — Prompt & Agent Engineering Workshop
- Segment: `welcome`
- Timing: minutes 0-7
- On-slide:
  - Prompt & Agent Engineering Workshop
  - 180 minutes, two sessions, one 15-minute break
  - Scenario: Contoso Trail Gear support triage (fictional)
- Speaker notes: Welcome people by name as they arrive. State that everything today is synthetic and that no real customer or confidential data belongs in a chat window. Keep this to 60 seconds.
- Activity cue: none

## Slide 2 — What you will leave with
- Segment: `welcome`
- Timing: minutes 0-7
- On-slide:
  - A prompt you would actually trust
  - An agent design: tools, subagents, contracts
  - An evaluation you ran yourself
  - A governed change, reviewed by a peer
- Speaker notes: Frame outcomes, not topics. Mention that the reusable templates are the takeaway and that train-the-trainer material is included for people who will teach this onward.
- Activity cue: none

## Slide 3 — Agenda and timing
- Segment: `welcome`
- Timing: minutes 0-7
- On-slide:
  - 0-7 welcome | 7-82 Session 1
  - 82-87 knowledge check | 87-102 break
  - 102-177 Session 2 | 177-180 close
  - Activities are most of the time
- Speaker notes: Promise the break time out loud and keep it. Say that two-minute warnings precede every activity end. Point out that the schedule is published in the repository.
- Activity cue: none

## Slide 4 — Ground rules and access
- Segment: `welcome`
- Timing: minutes 0-7
- On-slide:
  - Synthetic data only, never real customer content
  - CORE path: browser + GitHub account + Microsoft Copilot chat
  - Foundry and GitHub Copilot are OPTIONAL everywhere
  - Questions in chat any time; parking lot for off-scope
- Speaker notes: Run the three-item setup check here: repository open, chat open, signed in to GitHub. Pair anyone who is blocked and note the pairs for Session 2.
- Activity cue: Setup check, hands or chat, 3 minutes

## Slide 5 — Vocabulary we will actually use
- Segment: `s1-1`
- Timing: minutes 7-14
- On-slide:
  - prompt, grounding, structured output
  - agent, tool/function calling
  - workflow, orchestration, subagent
  - evaluation, regression, monitoring, governance
- Speaker notes: Do not define all twelve now. Say that each term gets defined at the moment it is needed, and that the full table is in the README. Thirty seconds maximum.
- Activity cue: none

## Slide 6 — Anatomy of a prompt that holds up
- Segment: `s1-1`
- Timing: minutes 7-14
- On-slide:
  - Role and task | Scope and authority
  - Grounding rules | Decision rules
  - Output contract | Untrusted content
  - Escalation rule
- Speaker notes: Each part removes a specific failure. Ask the room to keep score during the activity of which part removed which failure in their own output.
- Activity cue: none

## Slide 7 — Grounding: use what I gave you, name what is missing
- Segment: `s1-1`
- Timing: minutes 7-14
- On-slide:
  - Use only supplied facts and tool results
  - Never invent order numbers, dates, policy
  - Name missing facts explicitly
  - "Be accurate and helpful" removes no failure
- Speaker notes: Run the 60-second live demo of the weak starter prompt here and circle the invented warranty promise out loud. Have a backup screenshot ready in case chat is slow.
- Activity cue: Live demo of the weak prompt, 60 seconds

## Slide 8 — Activity A1: improve the starter prompt
- Segment: `a1`
- Timing: minutes 14-26
- On-slide:
  - Run the starter prompt twice
  - Write down every failure mode
  - Rewrite with the seven-part template
  - Run twice again
- Speaker notes: Budget 2 minutes brief/read, 3 diagnose, 5 rewrite/rerun, 2 checkpoint/debrief. Keep virtual pairs in the main room; use existing tables in person. Ask "which failure would a customer notice?"
- Activity cue: CORE activity, 12 minutes, exercises 01 and 02

## Slide 9 — A1 debrief: what changed
- Segment: `a1`
- Timing: minutes 14-26
- On-slide:
  - What did it invent before? What stopped it?
  - Did anything get worse?
  - Prompts get edited, not only appended to
- Speaker notes: Take two or three answers only. Land the trade-off point: every added rule costs tokens, latency, and readability. FALLBACK is the captured weak output in the solutions folder.
- Activity cue: Debrief inside the activity block, final 2 minutes

## Slide 10 — Structured output: shape, not truth
- Segment: `s1-2`
- Timing: minutes 26-33
- On-slide:
  - Fixed fields, fixed enums, no extras
  - Required fields force uncertainty into the open
  - The prompt asks; the application enforces
- Speaker notes: Show the schema file on screen. Point at required, at the severity enum, and at additionalProperties false. Say plainly that valid JSON can be completely wrong.
- Activity cue: Show exercises/03-structured-output.schema.json

## Slide 11 — Common failures and model variability
- Segment: `s1-2`
- Timing: minutes 26-33
- On-slide:
  - Invented facts, unstable format, vague severity
  - Silent guessing, over-helpful promises
  - Same prompt, same input, different answer
- Speaker notes: Normalize variability now so the evaluation activity lands later. Ask what the application should do when parsing fails: retry, repair, or fail closed to a human.
- Activity cue: none

## Slide 12 — Activity A2: add the output contract
- Segment: `a2`
- Timing: minutes 33-43
- On-slide:
  - Append the strict contract
  - Run three synthetic messages
  - Check six compliance boxes each
- Speaker notes: Success is two of three valid on the first try plus one captured compliance failure. FALLBACK line for stubborn code fences: "Your entire response must start with { and end with }."
- Activity cue: CORE activity, 10 minutes, exercise 03

## Slide 13 — From prompt to agent
- Segment: `s1-3`
- Timing: minutes 43-50
- On-slide:
  - Agent = prompt + tools + a loop
  - The loop is what is new and what is risky
  - Stop conditions are design, not afterthoughts
- Speaker notes: Keep this crisp. The loop introduces cost, latency, and the chance of repeated mistakes. Max turns and stop conditions belong in the design from day one.
- Activity cue: none

## Slide 14 — Tools and function calling
- Segment: `s1-3`
- Timing: minutes 43-50
- On-slide:
  - Name, typed parameters, side effects, failures
  - The model proposes; the application executes
  - Write actions require human approval
  - A proposal is not proof anything happened
- Speaker notes: Say the last line twice. Ask where the approval gate lives; correct "in the prompt" warmly — a prompt is a request, not a control.
- Activity cue: Show exercises/04-tool-contract.json

## Slide 15 — Orchestration and subagents
- Segment: `s1-3`
- Timing: minutes 43-50
- On-slide:
  - Split when owner, risk, or failure mode differs
  - Each hop costs latency, cost, context
  - Contract: responsibility, tools, must-nots, failures
- Speaker notes: Warn against decomposition for tidiness. The four-subagent triage design is a reference, not a requirement; many workflows are fine as one good prompt.
- Activity cue: none

## Slide 16 — Activity A3: tool contract and decomposition
- Segment: `a3`
- Timing: minutes 50-60
- On-slide:
  - 1 min brief + 4 min tool proposal/failure
  - 2 min: fill three compact subagent rows
  - 1 min checkpoint + 2 min debrief
- Speaker notes: Success criteria: no invented arguments, write action marked for approval, no fabricated order after a failed lookup. Checkpoint question: did it ever claim an action happened?
- Activity cue: CORE activity, 10 minutes, exercises 04 and 05

## Slide 17 — Building agents in Microsoft Foundry
- Segment: `s1-4`
- Timing: minutes 60-66
- On-slide:
  - Author: instructions, model, tools
  - Test: your synthetic cases, interactively
  - Evaluate: dataset plus evaluators, stored runs
  - Observe: traces you can inspect later
- Speaker notes: Microsoft Foundry, formerly Azure AI Foundry. Teach the shape of the work, not click paths; product UI changes. The repository stays the source of truth for the text.
- Activity cue: OPTIONAL — MICROSOFT FOUNDRY demo, 3 minutes

## Slide 18 — If you have no Foundry access
- Segment: `s1-4`
- Timing: minutes 60-66
- On-slide:
  - The agent definition file is the configuration
  - Run the same cases in Microsoft Copilot chat
  - Record results in the evaluation CSV
  - Same objective, no cloud resources
- Speaker notes: Say clearly that nobody needs to create cloud resources during a workshop and that quota and cost are real. Walk the agent YAML aloud as the no-access path.
- Activity cue: Show library/agents/triage-agent.agent.yaml

## Slide 19 — Evaluation basics
- Segment: `a4`
- Timing: minutes 66-76
- On-slide:
  - Fixed inputs, expected results, a rubric
  - Blocking criteria: schema validity, safety flag, safe routing
  - Two runs for anything safety-relevant
  - Evaluation reduces risk; it proves nothing
- Speaker notes: Distinguish evaluation, regression, and monitoring in one sentence each. Say the limits sentence exactly: evaluation never guarantees correctness and never replaces human review.
- Activity cue: none

## Slide 20 — Activity A4: score and decide
- Segment: `a4`
- Timing: minutes 66-76
- On-slide:
  - Run TC-02, TC-07, TC-05, TC-08 twice each
  - Score with the seven-criterion rubric
  - Classify each failure
  - Write one sentence: ship or hold
- Speaker notes: This is the most important debrief in Session 1. Ask who saw different answers on identical input, then land variability as a property of the system.
- Activity cue: CORE activity, 10 minutes, exercise 06

## Slide 21 — Reusable templates and teaching this onward
- Segment: `s1-5`
- Timing: minutes 76-82
- On-slide:
  - Seven-part prompt template
  - Output schema and tool contract
  - Subagent contract and evaluation rubric
  - Swap the scenario, keep the structure
- Speaker notes: Point at train-the-trainer.md for anyone who will run this for their own team. Ask which template people will use next week; the answers seed the Session 2 discussion.
- Activity cue: none

## Slide 22 — Knowledge check
- Segment: `knowledge-check`
- Timing: minutes 82-87
- On-slide:
  - Did the proposal create the ticket?
  - Valid JSON: is it correct?
  - Two different answers: bug or expected?
  - When must a human review?
  - What does a passing evaluation prove?
- Speaker notes: Five rapid answers, poll or hands. Expected answers: no; not necessarily; expected; safety flag, low confidence, or missing information; that those cases passed this time.
- Activity cue: Poll or hands, 5 minutes

## Slide 23 — Break
- Segment: `break`
- Timing: minutes 87-102
- On-slide:
  - 15 minutes
  - We restart at [clock time]
  - Need GitHub access help? Come find me
- Speaker notes: Put an actual clock time on the slide, not a duration. Use the first five minutes to unblock GitHub access and the last three to preload the Session 2 files.
- Activity cue: Break, 15 minutes

## Slide 24 — The PromptOps lifecycle
- Segment: `s2-1`
- Timing: minutes 102-108
- On-slide:
  - author → review → evaluate → release
  - → monitor → improve → author
  - It is a loop, not a launch
- Speaker notes: Ask where the team's best prompt lives today. Expect chat threads and documents; no shaming, that is everyone's starting point.
- Activity cue: none

## Slide 25 — What makes a prompt "shared"
- Segment: `s2-1`
- Timing: minutes 102-108
- On-slide:
  - An owner
  - A version
  - An output contract
  - A test set
- Speaker notes: Show the library prompt file and its front matter. Four properties, say them out loud; without all four you have a snippet, not a shared asset.
- Activity cue: Show library/prompts/triage-intake.prompt.md

## Slide 26 — GitHub as the source of truth
- Segment: `s2-2`
- Timing: minutes 108-115
- On-slide:
  - prompts, agents, contracts, tests, governance
  - Plain text: diffable, reviewable, revertible
  - History answers "who changed this and why"
- Speaker notes: The trick is that prompts are text. Everything a team already knows about reviewing text applies immediately, with no new tooling.
- Activity cue: none

## Slide 27 — Branches, pull requests, parallel authoring
- Segment: `s2-2`
- Timing: minutes 108-115
- On-slide:
  - One branch per change, named for the change
  - PR carries intent, evidence, rollback
  - Protect the default branch, require review
  - Conflicts mean two people edit one rule
- Speaker notes: Demo in your fork: pencil, commit to a new branch, then inspect the PR compare controls. Base repository must be your fork and base branch main; never target the source. Show where to copy the PR URL. Labels may vary slightly.
- Activity cue: Web UI demo, 2 minutes

## Slide 28 — Activity B1: make a change, open a PR
- Segment: `b1`
- Timing: minutes 115-130
- On-slide:
  - Pick role A, B, C, or D — pick different ones
  - Edit in your fork, commit to a new branch
  - Check: your fork `main` ← your fork `prompt/...`
  - Fill the PR template honestly
- Speaker notes: Forks must already be ready. Assign different roles, require the fork-local base check, and have authors send the browser PR URL to partners. FALLBACK: hand-written diff and PR body.
- Activity cue: CORE activity, 15 minutes, exercise 07 section B1

## Slide 29 — Governance that fits on one page
- Segment: `s2-3`
- Timing: minutes 130-137
- On-slide:
  - CODEOWNERS routes review by path
  - One accountable owner per decision type
  - Model choice is a governed decision
  - Subagent contracts are governance artifacts
- Speaker notes: Show the CODEOWNERS placeholder warning: @your-org teams do not exist and must be replaced. Ask who owns the safety rule today; the silence is the finding.
- Activity cue: Show .github/CODEOWNERS and governance/CODEOWNERS.sample

## Slide 30 — Activity B2: review like an owner
- Segment: `b2`
- Timing: minutes 137-149
- On-slide:
  - Swap PRs with your partner
  - Files changed → line `+` → Start a review
  - Work the checklist top to bottom
  - Three comments: blocking, question, suggestion
  - Name the approver role
- Speaker notes: End with Review changes → decision → Submit review. GitHub may prevent self-approval; partner review is expected. Push comments toward evidence rather than taste.
- Activity cue: CORE activity, 12 minutes, exercise 07 section B2

## Slide 31 — Quality and operations
- Segment: `s2-4`
- Timing: minutes 149-156
- On-slide:
  - Evaluate before release
  - Regression on every change
  - Release gate: owner, evidence, changelog, rollback
  - Rollback = one file revert + re-run safety cases
- Speaker notes: Ask what the smallest rollback they could perform today is. The answer reveals whether prompts live in code, in config, or in a chat thread.
- Activity cue: none

## Slide 32 — Monitoring: finding what you did not test
- Segment: `s2-4`
- Timing: minutes 149-156
- On-slide:
  - Schema validity, human-review rate
  - Reviewer override patterns
  - Safety misses, tool failure rates
  - Aggregate only, never customer content
- Speaker notes: Evaluation tests what you thought of; monitoring finds what you did not. Stress the aggregate-only rule for issues: describe the pattern, never the person.
- Activity cue: none

## Slide 33 — Activity B3: signal → issue → change
- Segment: `b3`
- Timing: minutes 156-168
- On-slide:
  - Read the synthetic weekly digest
  - Which number matters most?
  - Write the issue: signal, impact, proposal
  - Evidence required, rollback, owner
- Speaker notes: Steer from the 18 percent review rate to the 22 consistent overrides. Mention the OPTIONAL — GITHUB COPILOT path once, then keep everyone on the core path.
- Activity cue: CORE activity, 12 minutes, exercise 07 section B3

## Slide 34 — Recommendations and next steps
- Segment: `s2-5`
- Timing: minutes 168-177
- On-slide:
  - One repository, one owner per prompt
  - PRs required, ten-case test set, two runs
  - Changelog line and a rollback target
  - One monitoring signal reviewed weekly
- Speaker notes: Open discussion first, recommendations second, commitments third. Ask everyone to write one dated commitment and to name the person they need to talk to.
- Activity cue: Discussion and commitment writing, 9 minutes

## Slide 35 — Close
- Segment: `close`
- Timing: minutes 177-180
- On-slide:
  - A prompt is an artifact: owner, version, contract, tests
  - An agent is a prompt plus tools plus a loop
  - Evaluation reduces risk; humans still decide
  - Repository link and resources
- Speaker notes: Deliver the three takeaways verbatim, point at the repository and resources.md, thank the room, and offer to stay five minutes for questions.
- Activity cue: none

---

## Related

- [Facilitator guide](../facilitator-guide.md)
- [Participant workbook](../participant-workbook.md)
- [Canonical schedule](../schedule.json)
- [Train the trainer](../train-the-trainer.md)
