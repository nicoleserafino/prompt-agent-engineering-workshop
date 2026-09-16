# Governance

Reusable governance artifacts for a multi-author prompt and agent library. Everything here is
a sample you adapt, not a policy you inherit.

CORE — all of it is plain text, reviewable in the GitHub web UI.

| File | Use it for |
| --- | --- |
| [CODEOWNERS.sample](CODEOWNERS.sample) | Annotated ownership routing; the live copy is [../.github/CODEOWNERS](../.github/CODEOWNERS) |
| [pr-checklist.md](pr-checklist.md) | Reviewing any prompt, agent, contract, or governance change |
| [ownership-raci.md](ownership-raci.md) | Deciding who is accountable for which change type |
| [versioning-release-rollback.md](versioning-release-rollback.md) | Version scheme, release gate, rollback procedure |
| [monitoring-to-issue.md](monitoring-to-issue.md) | Turning a production signal into a tracked change |
| [../.github/pull_request_template.md](../.github/pull_request_template.md) | The PR body authors fill in |

## Placeholder teams

Every `@your-org/...` reference is a placeholder. Those teams do not exist, so GitHub cannot
request reviews from them; the sample is not a dependable merge gate until you substitute
real owners and configure branch rules. Replace them in both
[CODEOWNERS.sample](CODEOWNERS.sample) and [../.github/CODEOWNERS](../.github/CODEOWNERS).

CODEOWNERS routes review requests; it does not define distinct role approvals. When multiple
owners appear on one pattern, GitHub's code-owner requirement can be satisfied by an approval
from any listed owner. If your policy requires both quality and governance approval, enforce
those roles with your repository rules and review process. In this workshop, participants
name both roles manually in the PR and do not treat the placeholder file as enforcement.

## The three governance ideas worth keeping

1. **Ownership beats process.** One accountable owner per decision type.
2. **Evidence beats opinion.** Test cases and results in the pull request.
3. **Human approval is a boundary, not a formality.** Especially for write actions and anything
   safety-relevant. Evaluation reduces risk; it never guarantees correctness.

## Related

- [Shared library](../library/README.md)
- [Exercise 7, the lifecycle change](../exercises/07-lifecycle-change-exercise.md)
- [Facilitator guide](../facilitator-guide.md)
