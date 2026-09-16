# Monitoring to issue workflow

How a production signal becomes a tracked, reviewed, releasable change. Used in Activity B3
(minutes 156-168).

## Signals worth watching

| Signal | Why it matters | Example threshold to agree on |
| --- | --- | --- |
| Schema validity rate | Invalid output breaks downstream routing | Alert below 99 percent |
| `needs_human_review` rate | Sudden change means the input mix or the prompt shifted | Alert on a 50 percent relative change week over week |
| Reviewer override rate and pattern | The clearest evidence of a prompt gap | Alert above an agreed percentage, always inspect the top pattern |
| Safety misses caught in review | Near misses predict escapes | Any miss triggers review |
| Safety misses that reached a customer | Incident | Any occurrence triggers rollback |
| Tool failure rate by tool | Distinguishes model problems from system problems | Alert on a sustained increase |
| Latency and cost per triage | Prompt growth is not free | Track the trend, review monthly |

Aggregate signals only. Never copy customer message content into an issue; quote the pattern,
not the person.

## Workflow

```text
signal -> triage the signal -> issue -> proposal -> evidence -> review -> release -> watch
                                   \-> no action, with a recorded reason
```

1. **Detect.** A digest, dashboard, or reviewer report shows something outside the agreed band.
2. **Triage the signal.** Is it input mix, a prompt gap, a model change, or a system failure?
   Say which, out loud, before proposing a fix.
3. **Open an issue** using the template below.
4. **Propose a change** as a pull request on a branch, following
   [versioning-release-rollback.md](versioning-release-rollback.md).
5. **Attach evidence**: the new regression case plus the re-run of existing cases.
6. **Review** against [pr-checklist.md](pr-checklist.md) with the accountable owner from
   [ownership-raci.md](ownership-raci.md).
7. **Release and watch** the same signal for one full traffic cycle.

## Issue template

```text
Title: <behaviour> <what is wrong> (<artifact>)

Signal
- What was observed, over what window, at what volume. Aggregate only.

Triage
- Input mix / prompt gap / model change / system failure, and the evidence for that call.

Impact
- Who is affected and how badly. Whether anything reached a customer.

Proposed change
- The specific file and the specific rule to add or change.

Evidence required before release
- Named test cases, number of runs, regression scope, schema validity floor.

Rollback plan
- Target version and who executes it.

Owner
- Accountable role per governance/ownership-raci.md.
```

## Rules

1. **Every incident adds a regression case.** If the test set would not have caught it, the
   test set is the first fix.
2. **One rule per incident is a smell.** Periodically prune and consolidate prompt rules, or
   the prompt becomes unreadable and unreviewable.
3. **Aggregate, never paste.** Issues describe patterns, not customer content.
4. **A drafted fix is a proposal.** Whether a person or an assistant wrote it, a human owner
   approves it. See [../optional/github-copilot.md](../optional/github-copilot.md) for the
   OPTIONAL — GITHUB COPILOT path and its manual equivalent.
5. **Monitoring is not evaluation.** Evaluation tests what you thought of; monitoring finds
   what you did not.

## Related

- [PR checklist](pr-checklist.md)
- [Ownership and RACI](ownership-raci.md)
- [Versioning, release, rollback](versioning-release-rollback.md)
- [Exercise 7, Activity B3](../exercises/07-lifecycle-change-exercise.md)
