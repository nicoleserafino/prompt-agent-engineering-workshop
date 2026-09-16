# Participant workbook

Your follow-along for the 180-minute Prompt & Agent Engineering Workshop. Work top to bottom.
Everything uses the fictional **Contoso Trail Gear** scenario and synthetic messages.

> **Safety rule:** never paste real customer messages, personal data, credentials, or
> company-confidential content into any chat surface today. Synthetic inputs only.

**Labels used here**

| Label | Meaning |
| --- | --- |
| CORE | Do this. Needs only a browser, a GitHub account, and Microsoft Copilot chat. |
| OPTIONAL — MICROSOFT FOUNDRY | Only if you have a Foundry project. Skipping costs you nothing. |
| OPTIONAL — GITHUB COPILOT | Only if you have GitHub Copilot. Skipping costs you nothing. |
| FALLBACK | Use when something is unavailable, slow, or you run out of time. |

## Before you start (minutes 0-7)

- [ ] This workbook open.
- [ ] [exercises/README.md](exercises/README.md) open in another tab.
- [ ] Microsoft Copilot chat open.
- [ ] Signed in to GitHub in a browser.
- [ ] Optional but useful: fork this repository now so Session 2 is ready.

Your name / table / breakout room: `______________________`

Partner(s): `______________________`

---

# Session 1 — Prompt & Agent Engineering Foundations

## Step 1 — Improve the starter prompt (Activity A1, minutes 14-26)

CORE. Exercises: [01-starter-prompt.md](exercises/01-starter-prompt.md),
[02-improved-prompt-template.md](exercises/02-improved-prompt-template.md).

**Objective.** Find three concrete failure modes in a weak prompt, then remove them.

### 1.1 Run the starter prompt twice

Copy this into Microsoft Copilot chat:

```text
You are a helpful support assistant for an outdoor gear company. Read the customer message
and figure out what is wrong. Give the category, how bad it is, and what we should do next.
Be accurate and helpful.
```

Then paste this synthetic message:

```text
Ticket CTG-10421
Hi - the pole on my tent snapped while I was putting it up last weekend and now the whole
thing sags. I bought it a while back, I think from your site. Can you help?
```

Run the same pair again in a **new** chat.

### 1.2 Record what went wrong

| Failure I saw | Evidence from my output | Missing instruction |
| --- | --- | --- |
| | | |
| | | |
| | | |

### 1.3 Rewrite with the seven-part template

Parts: role and task, scope and authority, grounding rules, decision rules, output contract,
untrusted-content rule, escalation rule. The fill-in-the-blank version is in
[02-improved-prompt-template.md](exercises/02-improved-prompt-template.md).

Paste your rewritten prompt here (or keep it in your editor):

```text



```

### 1.4 Expected result

Two runs that agree on category and severity, no invented order number or warranty outcome,
missing information named explicitly, exactly one next action proposed.

### Checkpoint 1

The one line I added that made the biggest difference:

`______________________________________________________________`

### Reflection 1

- What got better? `____________________________________________`
- What got worse or longer? `___________________________________`
- What would I want a second author to review? `________________`

FALLBACK — Out of time or chat unavailable: use
[exercises/solutions/01-improved-prompt.md](exercises/solutions/01-improved-prompt.md) and
compare it with your draft. Continue from that prompt for the rest of the workshop.

---

## Step 2 — Add a structured output contract (Activity A2, minutes 33-43)

CORE. Exercise: [03-structured-output.md](exercises/03-structured-output.md). Schema:
[03-structured-output.schema.json](exercises/03-structured-output.schema.json).

**Objective.** Make the output machine-checkable, and see what "valid but wrong" looks like.

### 2.1 Append the strict contract to your prompt

```text
OUTPUT CONTRACT (STRICT)
Return exactly one JSON object and nothing else. No markdown fences, no commentary.
Fields, all required:
- ticket_id: string, matches CTG-#####, echoed from the input
- category: one of hardware_defect | sizing_fit | order_and_shipping | warranty_claim |
  usage_guidance | safety_concern | other
- product_line: one of tents | sleeping_bags | backpacks | camp_stoves | apparel |
  accessories | unknown
- severity: one of s1_safety | s2_high | s3_normal | s4_low
- safety_flag: boolean
- recommended_next_action: one of request_more_info | route_to_warranty |
  route_to_safety_review | send_self_service_guide | route_to_order_support
- missing_information: array of short strings, may be empty, at most 5 items
- confidence: number between 0 and 1
- needs_human_review: boolean
- rationale: string, at most 280 characters, grounded only in the intake message
Do not add any field that is not in this list.
```

### 2.2 Run three synthetic messages

```text
Ticket CTG-10421
Hi - the pole on my tent snapped while I was putting it up last weekend and now the whole
thing sags. I bought it a while back, I think from your site. Can you help?
```

```text
Ticket CTG-10422
My camp stove flared up and I burned my hand. I put it out but the valve still hisses when
it is closed.
```

```text
Ticket CTG-10425
hey
```

### 2.3 Score compliance

| Ticket | Parses as JSON | All 10 fields, no extras | Enums exact | safety_flag and severity agree | Problem seen |
| --- | --- | --- | --- | --- | --- |
| CTG-10421 | | | | | |
| CTG-10422 | | | | | |
| CTG-10425 | | | | | |

### 2.4 Expected result

CTG-10422 should be `s1_safety`, `safety_flag: true`, `route_to_safety_review`,
`needs_human_review: true`. CTG-10425 should refuse to guess and ask for information.

### Checkpoint 2

`TC id | valid JSON? | severity | one problem I saw`:

`______________________________________________________________`

### Reflection 2

- Did valid JSON ever hide a wrong answer? `____________________`
- What should the application do when parsing fails? `__________`

FALLBACK — If the model insists on code fences, add: `Your entire response must start with {
and end with }.` If it still fails, record it as a finding and move on. Reference outputs:
[exercises/solutions/03-structured-output.solution.json](exercises/solutions/03-structured-output.solution.json).

---

## Step 3 — Tools, function calling, and subagents (Activity A3, minutes 50-60)

CORE. Exercises: [04-tool-contract.md](exercises/04-tool-contract.md),
[05-subagent-contract-template.md](exercises/05-subagent-contract-template.md). Contract:
[04-tool-contract.json](exercises/04-tool-contract.json).

**Objective.** Produce a tool-call proposal with no invented arguments, then decompose the
workflow.

> The tools are simulated. A function-call proposal is **not** proof that an action executed.

### 3.1 Switch to tool-proposal mode

Start a **new chat**. First paste the complete prompt block from
[library/prompts/triage-intake.prompt.md](library/prompts/triage-intake.prompt.md), which
includes the strict triage schema. Then paste this block. It temporarily replaces that output
shape; do not combine the proposal and triage shapes in one response.

```text
MODE: TOOL PROPOSAL
AVAILABLE TOOLS (SIMULATED - YOU CANNOT EXECUTE THEM)
1. lookup_order(order_number: "CTG-ORD-######") - read only
2. search_product_knowledge(query: string, product_line?: enum, max_results?: 1-5) - read only
3. create_support_ticket(ticket_id, category, severity, summary, assign_to_queue?) - WRITE

TOOL RULES
- When you need a tool, do not describe it in prose. Emit a proposal object:
  {"tool_call_proposal": {"name": "<tool>", "arguments": { ... }, "why": "<one sentence>",
   "requires_human_approval": <true|false>}}
- Identifiers and customer facts must appear in the intake message or a supplied tool result.
  Never invent them. category, severity, and summary may be derived using the triage rules,
  but the summary may contain only grounded facts.
- If a required identifier or customer fact is missing, return
  {"missing_required_input":["<field>"]} instead of proposing the call.
- create_support_ticket always has requires_human_approval true. You never execute it.
- After a proposal, stop and wait. Do not describe a result you have not been given.
- In TOOL PROPOSAL mode, return only the proposal or missing_required_input object. The
  ten-field triage output contract does not apply until the user switches back to TRIAGE mode.
```

### 3.2 Run the core message

```text
Ticket CTG-10423
Order CTG-ORD-884120 was supposed to arrive Tuesday and the tracking has not moved in six
days.
```

### 3.3 Feed back a simulated failure

```text
TOOL RESULT for lookup_order:
{"error":"order_not_found","message":"No matching order in the synthetic workshop dataset."}

MODE: FINAL TRIAGE
Tool-proposal mode is finished. Return only the ten-field triage JSON object from Step 2.
Use the intake message and supplied tool result as grounding. Do not invent a successful
lookup or claim that any action executed.
```

Did the assistant invent an order record? `______`

Did it claim an action happened? `______`

If you finish early, test CTG-10426 in a separate fresh chat by repeating Step 3.1. Because no
order number is supplied, the assistant should return `missing_required_input` rather than
inventing one. Separate chats keep the failed CTG-10423 lookup out of this ticket's context.

### 3.4 Decompose into subagents

Fill at least three rows.

| Subagent id | Single responsibility | Tools allowed | One "must not" rule | Owner |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

Orchestrator stop condition I would set: `_____________________`

Human-in-the-loop point: `_____________________________________`

### Checkpoint 3

The subagent my team would own: `______________________________`

The one I would refuse to own: `_______________________________`

### Reflection 3

- Where does the approval gate for a write action live? `_______`
- Would one well-written prompt have been enough here? `________`

FALLBACK — If the model narrates tool use instead of emitting a proposal, resend the TOOL RULES
block. If it still narrates, write that down — "model describes actions it cannot take" is a
genuine risk. Reference:
[exercises/solutions/04-tool-call-proposal.example.json](exercises/solutions/04-tool-call-proposal.example.json).

---

## Step 4 — Evaluate against synthetic test cases (Activity A4, minutes 66-76)

CORE. Exercise: [06-evaluation-rubric.md](exercises/06-evaluation-rubric.md). Cases:
[06-test-cases.jsonl](exercises/06-test-cases.jsonl). Results template:
[06-eval-results-template.csv](exercises/06-eval-results-template.csv).

**Objective.** Score four cases twice, classify the failures, and decide ship or hold.

### 4.1 Reset to the released evaluation prompt

Do not evaluate the temporary tool-proposal mode from Step 3. Open
[library/prompts/triage-intake.prompt.md](library/prompts/triage-intake.prompt.md) and copy
the complete v1.2.0 prompt block into a new chat.

### 4.2 Run these four cases, twice each

As a pair, run TC-02 (stove burn), TC-07 (strap tore under load, injury), TC-05 ("hey"), and
TC-08 (message that tries to change your instructions) twice each. Split the runs between
partners, then pool the eight outputs. For every run, paste the `ticket_id` and
`intake_message` from the JSONL as:

```text
Ticket CTG-#####
<intake_message>
```

Do not paste the `expected` object into chat.

### 4.3 Score

| Case | Run | Valid JSON | Category | Severity | Safety + route | Missing info | Human review | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-02 | 1 | | | | | | | |
| TC-02 | 2 | | | | | | | |
| TC-07 | 1 | | | | | | | |
| TC-07 | 2 | | | | | | | |
| TC-05 | 1 | | | | | | | |
| TC-05 | 2 | | | | | | | |
| TC-08 | 1 | | | | | | | |
| TC-08 | 2 | | | | | | | |

### 4.4 Classify every failure

| Case | Prompt gap | Variability | Bad test case | Real ambiguity |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |

Treat the classification as a hypothesis. Two matching failures are stronger evidence of a
prompt gap, not proof; inspect the prompt, expected result, and human disagreement before
changing anything.

### 4.5 Decide

My release decision, one sentence:

`______________________________________________________________`

### Checkpoint 4

`cases run | blocking failures | ship or hold`:

`______________________________________________________________`

### Reflection 4

- What can this evaluation set never tell me? `_________________`
- Which case would I add permanently? `_________________________`

> Evaluation reduces risk. It never guarantees correctness and never replaces human review.

FALLBACK — Score the eight raw responses in
[exercises/solutions/06-pre-captured-outputs.jsonl](exercises/solutions/06-pre-captured-outputs.jsonl),
then compare with the separate answer key in
[exercises/solutions/06-eval-results.reference.csv](exercises/solutions/06-eval-results.reference.csv).
The fixtures identify prompt version 1.2.0 and support the same scoring and release decision.

OPTIONAL — MICROSOFT FOUNDRY: run the same set as a portal evaluation,
[optional/foundry.md](optional/foundry.md). The CORE path above meets the same objective.

---

## Knowledge check (minutes 82-87)

Answer without looking back.

1. A model returns a function-call proposal. Did the ticket get created? `______`
2. The output is valid JSON. Is it correct? `______`
3. Same prompt, same input, two different answers. Bug or expected? `______`
4. When must a human review a triage result? `______`
5. What does a passing evaluation prove? `______`

---

## Break (minutes 87-102)

Return on time. If GitHub access is a problem for you, sort it out now or pair with someone.

---

# Session 2 — Multi-Author PromptOps & Governance

Setup for Session 2: fork this repository in the GitHub web UI so you have write access to your
own copy. If your fork has no **Issues** tab and you control its settings, enable Issues under
**Settings → General → Features**. Otherwise use the documented draft-mode fallback for B3.
Full steps in
[exercises/07-lifecycle-change-exercise.md](exercises/07-lifecycle-change-exercise.md).

## Step 5 — Parallel authoring via branch and pull request (Activity B1, minutes 115-130)

CORE. GitHub web UI only. Local `git` is an alternative, never required.

**Objective.** Land a small, reviewable prompt change as a pull request while your partner
changes the same library at the same time.

### 5.1 My assigned change

| Role | Change |
| --- | --- |
| A | `hardware_defect` vs `safety_concern`: structural failure under load with injury is always `safety_concern` |
| B | `confidence` below 0.6 must list at least one `missing_information` entry |
| C | Non-goal: never estimate repair cost or shipping dates |
| D | Version bump plus matching `library/CHANGELOG.md` entry |

Mine: `______`

### 5.2 Steps

1. In your fork, open `library/prompts/triage-intake.prompt.md`.
2. Pencil icon, edit inside the fenced prompt block, keep the section headings.
3. Commit with **Create a new branch for this commit and start a pull request**.
4. Branch name: `prompt/triage-intake-______________________`
5. Fill in the pull request template: what changed, why, evidence, rollback.

### 5.3 Expected result

A focused diff, a complete PR body, and a branch name that says what changed.

### Checkpoint 5

PR title: `_____________________________________________________`

Line I changed: `______________________________________________`

### Reflection 5

- What if you and your partner had edited the same line? `______`
- What belongs in the PR body that a diff can never show? `_____`

FALLBACK — Forking blocked: write the change here as a hand diff.

```diff
- (line removed)
+ (line added)
```

PR body fields: what changed / why / evidence / rollback:

`______________________________________________________________`

OPTIONAL — GITHUB COPILOT: you may ask it to draft the edit or the PR body. You still read
every line and own the review. See [optional/github-copilot.md](optional/github-copilot.md).

---

## Step 6 — Governance review (Activity B2, minutes 137-149)

CORE. Checklist: [governance/pr-checklist.md](governance/pr-checklist.md). Roles:
[governance/ownership-raci.md](governance/ownership-raci.md).

**Objective.** Review a partner's change like an owner: against the checklist, not against
taste.

### 6.1 Leave three comments

| Type | My comment | Line or file |
| --- | --- | --- |
| Blocking | | |
| Question | | |
| Suggestion | | |

### 6.2 Checklist findings

| Checklist section | Satisfied? | Gap found |
| --- | --- | --- |
| Intent | | |
| Diff quality | | |
| Contracts | | |
| Model and configuration | | |
| Evidence | | |
| Safety and human oversight | | |
| Ownership and approval | | |
| Release readiness | | |

Required approver role for this change: `______________________`

My decision: approve / request changes / hold — because `______`

### Checkpoint 6

`PR reviewed | blocking items found | decision`:

`______________________________________________________________`

### Reflection 6

- What would I automate, and what must stay human? `____________`

FALLBACK — Review the reference PR body in
[exercises/solutions/07-lifecycle-change-solution.md](exercises/solutions/07-lifecycle-change-solution.md).

---

## Step 7 — Monitoring signal to issue to proposed change (Activity B3, minutes 156-168)

CORE. Workflow: [governance/monitoring-to-issue.md](governance/monitoring-to-issue.md).

**Objective.** Turn a synthetic monitoring digest into a tracked, approvable change.

### 7.1 The signal

```text
WEEKLY TRIAGE MONITORING DIGEST (synthetic)
Window: 2026-09-08 to 2026-09-14
Volume: 1,240 triaged intake messages
Schema validity: 99.4 percent (7 failures, all truncated output)
needs_human_review rate: 18 percent (previous week 12 percent)
Reviewer overrides of recommended_next_action: 9 percent
Top override pattern: 22 cases classified hardware_defect where the reviewer changed the
  result to safety_concern. All 22 mention a strap, pole, or frame failing "while loaded",
  "while carrying", or "mid-hike". 3 of them mention a minor injury.
Safety misses reported by reviewers: 0 escaped to customers; all 22 were caught in review.
Rollback events: 0
```

The number that matters most and why: `_______________________`

### 7.2 Write the issue

In your fork: **Issues → New issue**. Use this structure.

```text
Title: Triage misclassifies load-bearing failures as hardware_defect

Signal
-
Impact
-
Proposed change
-
Evidence required before release
-
Rollback plan
-
Owner
-
```

### 7.3 Expected result

Signal and impact stated separately, specific and checkable evidence requirements, a rollback
plan naming a version, and a named human approver.

### Checkpoint 7

`issue created | evidence required | approver`:

`______________________________________________________________`

### Reflection 7

- How do I stop the prompt growing one rule per incident forever? `______`
- Does the approval boundary change if an assistant drafted the fix? `______`

FALLBACK — Write the issue body here and read it aloud in the debrief.

OPTIONAL — GITHUB COPILOT: assign the issue to the coding agent and review the resulting pull
request as a proposal. Human approval is unchanged:
[optional/github-copilot.md](optional/github-copilot.md).

---

## Discussion and next steps (minutes 168-177)

Adoption order that works for most teams:

1. One repository as the source of truth.
2. One named owner per prompt, written in the file.
3. Pull requests required; no direct pushes to the default branch.
4. A ten-case test set, run twice for anything safety-relevant.
5. A one-line changelog per release and a named rollback target.
6. One monitoring signal reviewed weekly.

### My commitment

By `____ / ____` I will: `_____________________________________`

The person I need to talk to: `________________________________`

The first file I will create: `________________________________`

---

## Close (minutes 177-180)

Three things to take with you:

1. A prompt is an artifact: owner, version, output contract, test set.
2. An agent is a prompt plus tools plus a loop — and a function-call proposal is not proof that
   an action executed.
3. Evaluation reduces risk. It never guarantees correctness and never replaces human review.

## Where to go next

- [Exercises](exercises/README.md) and [solutions](exercises/solutions/)
- [Shared library](library/README.md)
- [Governance](governance/README.md)
- [Train the trainer](train-the-trainer.md) if you will teach this
- [Official Microsoft and GitHub resources](resources.md)
- OPTIONAL — MICROSOFT FOUNDRY: [optional/foundry.md](optional/foundry.md)
- OPTIONAL — GITHUB COPILOT: [optional/github-copilot.md](optional/github-copilot.md)
