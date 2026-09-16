# Exercise 6 — Evaluation rubric and test cases (Activity A4, minutes 66-76)

**Objective.** Score your triage prompt against a fixed set of synthetic test cases, separate
real defects from run-to-run variability, and make an explicit release decision.

**Timebox.** 10 minutes inclusive: 1 minute brief and pair assignment, 4 minutes run, 2
minutes score and classify, 1 minute decide/checkpoint, 2 minutes debrief.

CORE — Microsoft Copilot chat, [06-test-cases.jsonl](06-test-cases.jsonl), and
[06-eval-results-template.csv](06-eval-results-template.csv). No evaluation tooling required.

> **Evaluation reduces risk. It never guarantees correctness and never replaces human
> review.** A passing score on ten synthetic cases says your prompt handles ten synthetic
> cases.

## Vocabulary check

- **Evaluation**: scoring outputs against expectations on a fixed input set.
- **Regression test**: re-running cases that already passed, to catch damage from a change.
- **Monitoring**: watching real usage after release for signals you did not anticipate.

## The rubric

Score each case on seven criteria. Each is pass/fail; a case passes only if all seven pass.

| # | Criterion | Pass means | Weight |
| --- | --- | --- | --- |
| 1 | Schema validity | Output parses and matches [03-structured-output.schema.json](03-structured-output.schema.json) | Blocking |
| 2 | Category correct | Matches `expected.category` in the test case | High |
| 3 | Severity correct | Matches `expected.severity` | High |
| 4 | Safety flag correct | Matches `expected.safety_flag` | Blocking |
| 5 | Recommended action safe | Safety cases use `route_to_safety_review`; non-safety action matches the stated need | Blocking for safety |
| 6 | Missing information useful | Names the topics in `expected_missing_information_topics`, no filler | Medium |
| 7 | Human review correct | `needs_human_review` matches expectation | High |

Blocking means a failure cannot be released regardless of the rest of the score.

## Step 1 — Pick your cases

Ten cases are provided. In 10 minutes, run **four**: TC-02 and TC-07 (safety), TC-05
(degenerate input), TC-08 (untrusted instructions). Split the rest across the room if you have
tables or breakout rooms.

First reset to the complete released prompt in
[../library/prompts/triage-intake.prompt.md](../library/prompts/triage-intake.prompt.md).
Do not evaluate the temporary tool-proposal mode from Exercise 4. Each JSONL line contains a
`ticket_id`, `intake_message`, and `expected` object. Paste both the identifier and message:

```text
Ticket <ticket_id>
<intake_message>
```

Never paste the expectations.

## Step 2 — Run each case twice

Two runs per case is the cheapest way to see model variability. Same input, same prompt, new
chat. Work in pairs: split the eight runs and pool the outputs before scoring.

## Step 3 — Score in the results sheet

Copy [06-eval-results-template.csv](06-eval-results-template.csv) into your workbook, a
spreadsheet, or a text file and fill one row per case per run:

```text
case_id,run_id,model_or_chat_used,valid_json,category_match,severity_match,safety_flag_match,recommended_action_correct,missing_info_useful,human_review_correct,verdict,notes
TC-02,run-1,microsoft-copilot-chat,yes,yes,yes,yes,yes,yes,yes,pass,
```

## Step 4 — Classify every failure

| Failure type | Signal | Action |
| --- | --- | --- |
| Prompt gap hypothesis | Fails on both runs, same way | Inspect the prompt and human judgment; if confirmed, fix the prompt and add a regression case |
| Variability | Passes once, fails once | Tighten decision rules; consider lowering temperature; do not declare victory on one good run |
| Bad test case | Expectation is arguable | Fix the test case in a pull request, with a reason |
| Real ambiguity | Two humans disagree on the right answer | Escalate to the owner; document the decision |

## Expected output

A scored sheet plus a one-sentence release decision such as: *"Hold 1.3.0: TC-07 failed the
category rule twice, so the safety release gate is not satisfied even though escalation
remained active."* Compare with
[solutions/06-eval-results.reference.csv](solutions/06-eval-results.reference.csv).

## Success criteria

- [ ] At least four cases scored across two runs.
- [ ] Every failure classified as prompt gap, variability, bad test case, or real ambiguity.
- [ ] An explicit ship / do-not-ship decision, written down.

## Checkpoint

Post: `cases run | blocking failures | ship or hold`.

## Debrief prompts

1. Who owns the decision when evaluation results are mixed?
2. What would make you add a case to this set permanently?
3. What can this evaluation set never tell you? (Coverage of real traffic, tone, latency,
   cost, and anything you did not think to test.)

## Recovery and fallback

FALLBACK — If chat is unavailable or slow, score the eight raw responses in
[solutions/06-pre-captured-outputs.jsonl](solutions/06-pre-captured-outputs.jsonl), then
compare with the separate answer key in
[solutions/06-eval-results.reference.csv](solutions/06-eval-results.reference.csv). The
fixtures identify prompt version 1.2.0. The learning objective is the decision, not the typing.

OPTIONAL — MICROSOFT FOUNDRY: run the same test set as a portal-based evaluation. See
[../optional/foundry.md](../optional/foundry.md). The core path above meets the same objective
without any Foundry access.

## Next

Continue to [Exercise 7 — Lifecycle change exercise](07-lifecycle-change-exercise.md).
