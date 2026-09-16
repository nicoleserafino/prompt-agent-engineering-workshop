# OPTIONAL — GITHUB COPILOT

**This path is optional. Nothing in the workshop requires a GitHub Copilot license.** Every
step below has a manual equivalent that produces the same artifact and teaches the same
lesson.

## Where this fits in the run of show

- Activity B1, minutes 115-130 — drafting a prompt change and a pull request body.
- Activity B3, minutes 156-168 — turning a monitoring issue into a proposed change.
- Session 2 governance, minutes 130-137 — who approves assistant-drafted changes.

## The one rule that matters

> A proposal is not an approval, and a function-call proposal is not proof that an action
> executed. Whether a change was drafted by a person or by an assistant, the same human owner
> reviews the same diff against the same checklist before anything merges.

## Optional path A — Copilot Chat as a drafting partner

If you have GitHub Copilot in your editor or on github.com:

1. Ask it to draft the prompt edit for Activity B1, for example:

```text
Rewrite the severity ladder in this prompt so that a strap, pole, frame, or seam failing while
the product is loaded or carried counts as structural failure under load, and any accompanying
injury forces category safety_concern. Keep the existing section headings and keep the change
as small as possible.
```

2. Ask it to draft the pull request body against the repository template.
3. **Read every line yourself.** Check it against
   [../governance/pr-checklist.md](../governance/pr-checklist.md).

CORE alternative: write the edit by hand in the GitHub web UI, or ask Microsoft Copilot chat
for wording help and paste the result in yourself. Same artifact, same review.

## Optional path B — Copilot coding agent on an issue

If your account and repository have GitHub Copilot's coding agent available, you can assign an
issue to it and it will open a pull request with proposed changes.

Use it here for the Activity B3 issue ("Triage misclassifies load-bearing failures as
hardware_defect"). Then:

1. Review the diff line by line. Small, focused, no unrelated edits?
2. Check the evidence. Did it run the test cases, or only claim the change is safe? A claim in
   a PR body is not evidence.
3. Check the changelog and version bump. These are the items most often missing.
4. Approve, request changes, or close. You are the approver either way.

CORE alternative that meets the same objective: open the issue, then create the branch and pull
request by hand in the GitHub web UI following
[../exercises/07-lifecycle-change-exercise.md](../exercises/07-lifecycle-change-exercise.md).
Participants without the coding agent lose nothing — the review conversation is the lesson.

## Human approval boundaries

| Action | Assistant may | Human must |
| --- | --- | --- |
| Draft prompt wording | Yes | Read and edit |
| Draft a PR body | Yes | Verify the evidence claims are true |
| Open a pull request | Yes, as a proposal | Review and approve before merge |
| Merge to the default branch | No | Approve and merge |
| Change a safety rule | Propose only | Governance owner approves |
| Change the model selection | Propose only | Owner approves, evaluation re-run |
| Execute a write tool (for example, create a ticket) | Propose only | Approve each execution |
| Release a version | Propose only | Accountable owner releases |
| Roll back in an incident | Propose only | Operator on call executes |

## What to watch for when reviewing assistant-drafted changes

- **Plausible but unverified evidence.** "All tests pass" with no results attached.
- **Scope creep.** Reformatting, renamed fields, or extra "improvements" you did not ask for.
- **Silent contract changes.** A new enum value or a removed field breaks consumers.
- **Over-fitting to one case.** A rule that fixes TC-07 and breaks TC-01.
- **Rule accumulation.** Each incident adds a sentence until the prompt is unreadable.
- **Confident tone.** Fluency is not correctness. Ask for the diff and the evidence.

## Facilitator note

If nobody in the room has a Copilot license, run the CORE path and demonstrate this section as
a two-minute narrated walkthrough using
[../exercises/solutions/07-lifecycle-change-solution.md](../exercises/solutions/07-lifecycle-change-solution.md)
as the "proposed" pull request. Ask the room to review it as if an assistant had written it.
The discussion is identical.

## Official documentation

- GitHub Copilot documentation: <https://docs.github.com/en/copilot>
- Responsible use of GitHub Copilot features: <https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features>
- About pull requests: <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>

More links in [../resources.md](../resources.md).

## Related

- [Governance PR checklist](../governance/pr-checklist.md)
- [Monitoring to issue workflow](../governance/monitoring-to-issue.md)
- [OPTIONAL — MICROSOFT FOUNDRY path](foundry.md)
