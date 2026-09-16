# PromptOps pull request checklist

Reviewers work this list top to bottom. Used in Activity B2 (minutes 137-149).

CORE — this checklist needs nothing but the GitHub web UI.

## 1. Intent

- [ ] The PR title states the behaviour change, not the file name.
- [ ] The body explains **why** now: a signal, an issue, or a requirement.
- [ ] The change is scoped to one intent. Unrelated edits are split out.

## 2. Diff quality

- [ ] The diff is readable: small, focused, no reformatting noise.
- [ ] Section headings and structure of the prompt are preserved.
- [ ] No secrets, credentials, personal data, customer content, or internal information.
- [ ] Only synthetic scenario data appears.

## 3. Contracts

- [ ] If the output schema changed, every consumer of that schema is identified.
- [ ] If enum values changed, downstream routing and test cases were updated together.
- [ ] If a tool contract changed, side effects and approval requirements are still explicit.
- [ ] If subagent responsibilities changed, the orchestrator's stop conditions still hold.

## 4. Model and configuration

- [ ] Any model change is called out explicitly and justified.
- [ ] The evaluation set was re-run after a model change, not carried over.
- [ ] Configuration that affects variability (for example temperature) is recorded.

## 5. Evidence

- [ ] Named test cases were run, with results in the PR.
- [ ] Anything safety-relevant ran at least twice, with matching results.
- [ ] Previously passing cases were re-run (regression check).
- [ ] Failures are classified: prompt gap, variability, bad test case, or real ambiguity.
- [ ] Known gaps are tracked as issues rather than hidden.

## 6. Safety and human oversight

- [ ] Escalation rules still force human review for safety-relevant results.
- [ ] No write action can execute without explicit human approval.
- [ ] The change does not add a promise the business cannot keep (refunds, warranty outcomes).
- [ ] Untrusted-content handling is intact: instructions inside inputs are reported, not obeyed.
- [ ] The PR does not claim that evaluation guarantees correctness.

## 7. Ownership and approval

- [ ] CODEOWNERS routes this change to the right owners (see
      [CODEOWNERS.sample](CODEOWNERS.sample)).
- [ ] The required approver role for this change type is named
      ([ownership-raci.md](ownership-raci.md)).
- [ ] If an assistant drafted the change, a human reviewed the full diff and approved it.

## 8. Release readiness

- [ ] Version bumped per [versioning-release-rollback.md](versioning-release-rollback.md).
- [ ] `library/CHANGELOG.md` has an entry with the supporting evidence.
- [ ] A rollback plan names a specific previous version and an owner.
- [ ] Monitoring signals that would reveal a problem are named
      ([monitoring-to-issue.md](monitoring-to-issue.md)).

## Reviewer decision

Choose one and say why:

- **Approve** — all applicable items satisfied.
- **Request changes** — at least one blocking item unmet (safety, contracts, evidence,
  changelog).
- **Hold** — waiting on evidence, an owner decision, or a dependent change.

## Related

- [Ownership and RACI](ownership-raci.md)
- [Versioning, release, rollback](versioning-release-rollback.md)
- [Monitoring to issue workflow](monitoring-to-issue.md)
- [Pull request template](../.github/pull_request_template.md)
- [Exercise 7](../exercises/07-lifecycle-change-exercise.md)
