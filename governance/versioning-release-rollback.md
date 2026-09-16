# Versioning, release, and rollback

How a prompt or agent change becomes a release, and how you undo it.

## Versioning scheme

Prompts and agent definitions use `MAJOR.MINOR.PATCH` recorded in the file's front matter or
metadata block.

| Part | Increment when | Example |
| --- | --- | --- |
| MAJOR | The output contract changes in a way that breaks consumers: field removed, enum value removed or renamed, field type changed | 1.4.2 → 2.0.0 |
| MINOR | Behaviour changes without breaking the contract: new decision rule, new escalation condition, new optional field, model change | 1.2.0 → 1.3.0 |
| PATCH | Wording, typos, clarifications that do not change behaviour | 1.3.0 → 1.3.1 |

A **model change is at least MINOR**, even when no prompt text changes. The behaviour changed
even though the file barely did.

## Branch and commit conventions

| Convention | Pattern | Example |
| --- | --- | --- |
| Branch | `prompt/<artifact>-<short-change>` | `prompt/triage-intake-safety-boundary` |
| Branch | `agent/<artifact>-<short-change>` | `agent/triage-add-order-lookup` |
| Branch | `eval/<what>` | `eval/add-load-bearing-cases` |
| Commit | Imperative, states the behaviour | `Treat load-bearing failure with injury as safety_concern` |

## Release gate

A version is released only when all of the following hold:

1. Pull request approved by the accountable owner from
   [ownership-raci.md](ownership-raci.md).
2. Every item on the [PR checklist](pr-checklist.md) satisfied or explicitly waived with a
   reason.
3. Evaluation evidence attached: schema validity, the cases run, and the regression result.
4. Anything safety-relevant passed on two consecutive runs.
5. `library/CHANGELOG.md` updated with the version, the change, the evidence, and the approver
   role.
6. A rollback target named.

> Release gates reduce risk. They do not guarantee correctness. Human review remains part of
> the runtime path for safety-relevant results, not just the release path.

## Release steps

1. Merge the pull request into the default branch.
2. Tag the release, for example `triage-intake-v1.3.0`, so the exact text is retrievable.
3. Record the released version in the agent definition.
4. Announce in the team channel: version, one-line change, what to watch, rollback target.
5. Watch the monitoring signals in [monitoring-to-issue.md](monitoring-to-issue.md) for the
   first full traffic cycle.

## Rollback

Roll back first, investigate second.

| Trigger | Action | Who |
| --- | --- | --- |
| A safety-relevant miss reaches a customer | Immediate rollback to the last known-good version | Operator on call |
| Schema validity drops below the agreed floor | Immediate rollback | Operator on call |
| Reviewer override rate spikes beyond the agreed threshold | Rollback or freeze, then investigate | Operator on call with owner |
| Cost or latency regression | Freeze, investigate, decide with the owner | Owner |

**Rollback procedure**

1. Revert the merge commit or re-point the deployment to the previous tagged version.
2. Re-run the safety cases from [../exercises/06-test-cases.jsonl](../exercises/06-test-cases.jsonl)
   against the restored version and record the result.
3. Add a `Rolled back` line to `library/CHANGELOG.md` with the reason.
4. Open an issue with the signal that triggered the rollback, using
   [monitoring-to-issue.md](monitoring-to-issue.md).
5. Do not re-release until the regression case that would have caught this exists in the test
   set.

**Why this is cheap for prompts:** a prompt is a text file. The rollback is a revert of one
file plus a re-run of a small test set. Keep it that way — if rollback requires a coordinated
multi-system change, your prompt library has grown hidden coupling.

## Related

- [PR checklist](pr-checklist.md)
- [Ownership and RACI](ownership-raci.md)
- [Monitoring to issue workflow](monitoring-to-issue.md)
- [Library changelog](../library/CHANGELOG.md)
