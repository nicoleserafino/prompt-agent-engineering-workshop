# Exercise 5 — Subagent contract template (Activity A3, minutes 50-60)

**Objective.** Decompose the single triage prompt into an orchestrator plus a small number of
subagents, each with an explicit contract, so ownership and failure handling become concrete.

**Timebox.** 2 minutes inside Activity A3 (minutes 50-60). Fill three compact rows; complete
contracts are a post-workshop extension.

CORE — paper, this template, and optionally Microsoft Copilot chat to run one subagent.

## Vocabulary check

- **Agent**: a prompt plus tools plus a loop that can take multiple steps toward a goal.
- **Workflow**: the ordered set of steps that solve the business problem.
- **Orchestration**: deciding which step runs next, and when to stop.
- **Subagent**: a narrow agent that owns one step and returns a defined output.

Decompose when a step has a **different owner, different risk, or a different failure mode**.
Do not decompose for its own sake: every hop adds latency, cost, and a place to lose context.

## Template — fill one row per subagent

| Field | Your answer |
| --- | --- |
| Subagent id | |
| Single responsibility (one sentence) | |
| Inputs (names and types) | |
| Outputs (names and types) | |
| Tools allowed | |
| Must not (2-3 hard rules) | |
| Failure handling (what it returns when unsure) | |
| Owner (team or role) | |
| How it is evaluated | |

## Orchestrator contract — fill once

| Field | Your answer |
| --- | --- |
| Goal | |
| Order of subagents | |
| Routing rules (if X then Y) | |
| Stop conditions (max turns, repeated invalid output, tool failure) | |
| Human-in-the-loop points | |
| Final output contract | |

## Suggested decomposition for Contoso Trail Gear

Use this if your table is stuck; it is the decomposition used by the rest of the workshop.

1. `intake-normalizer` — extract stated facts, list missing information.
2. `safety-escalation-checker` — decide only whether a person is at risk.
3. `triage-classifier` — assign category, severity, confidence.
4. `action-recommender` — propose exactly one next action, plus any tool call for approval.

Reference implementation:
[solutions/05-triage-subagent-contracts.yaml](solutions/05-triage-subagent-contracts.yaml)

## Optional run

Run just the `safety-escalation-checker` in Microsoft Copilot chat:

```text
You decide one thing only: does this support message describe a risk to a person (injury,
burn, fire, fumes, gas smell, or structural failure under load)?
Return JSON: {"safety_flag": true|false, "safety_evidence": "<quote from the message>"}
Rules: never downgrade a risk because the customer says nothing has happened yet; never give
medical advice; when uncertain return true and explain why.

Message:
Stove smells like gas inside my tent but nothing has happened yet. Still safe to use?
```

## Expected output

`{"safety_flag": true, "safety_evidence": "smells like gas inside my tent"}` — a narrow
subagent is easier to get right, easier to test, and easier to own than one prompt that does
everything.

## Success criteria

- [ ] At least three subagent rows are filled with a single responsibility each.
- [ ] Every subagent has at least one "must not" rule.
- [ ] The orchestrator has an explicit stop condition and a human-in-the-loop point.

## Checkpoint

Name the one subagent your team would own, and the one you would refuse to own.

## Debrief prompts

1. Where does context get lost between subagents, and what would you pass explicitly?
2. Which subagent has the highest blast radius if it is wrong?
3. Would a single well-written prompt have been enough here? Say why or why not.

## Recovery and fallback

FALLBACK — If the table takes too long, fill only `safety-escalation-checker` completely and
list the others by name. The reference YAML covers the rest and Session 2 works either way.

## Next

Continue to [Exercise 6 — Evaluation rubric and test cases](06-evaluation-rubric.md).
