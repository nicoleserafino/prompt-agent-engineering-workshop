# Exercise 7 — Lifecycle change exercise (Activities B1, B2, B3)

**Objective.** Move a prompt change through a real multi-author lifecycle: propose it on a
branch, open a pull request, review it against the governance checklist, and turn a monitoring
signal into a tracked, human-approved improvement.

**Timeboxes.** B1 minutes 115-130 (15), B2 minutes 137-149 (12), B3 minutes 156-168 (12).

CORE — GitHub web UI in a browser plus Microsoft Copilot chat. No local `git` required, no
GitHub Copilot license required, no Microsoft Foundry access required.

## GitHub web setup: create your own fork

Prefer to complete this during participant preflight. Otherwise use minutes 0-7 or the break
at minutes 87-102. **Your fork must be ready by minute 115; do not start this setup for the
first time during B1.** GitHub labels and positions can vary slightly.

1. Sign in to GitHub in a browser.
2. Open the **workshop repository URL supplied by the facilitator**. The published GitHub
   repository is required; a local folder or unpublished placeholder cannot be forked.
3. Find **Fork** near the upper-right of the repository page. Select it, then select
   **Create a new fork** if GitHub shows that choice.
4. In **Owner**, choose your own GitHub account. Do not choose the source owner.
5. Keep GitHub's suggested repository name.
6. Select **Create fork** and wait for GitHub to navigate to the created repository.
7. Verify the header or breadcrumb shows `<your-user>/<repo-name>`. GitHub should also show
   wording near the title indicating it was forked from the facilitator/source repository.
8. Open **library**, then **prompts**, then **triage-intake.prompt.md**.
9. Agree how you will send a PR URL to your partner: meeting chat, direct message, or an
   in-person browser handoff.
10. Look for **Issues** in your fork's repository navigation, near **Code** and
    **Pull requests** or in an overflow menu. If it is absent and you own the fork, open
    **Settings → General → Features** and enable Issues if the option is available. If it is
    unavailable, plan to draft B3 in the workbook.

### You are ready when...

- [ ] The browser is on `<your-user>/<repo-name>`, not the source repository.
- [ ] `library/prompts/triage-intake.prompt.md` is visible.
- [ ] You know how you will share your PR URL with your partner.

Forking is recommended, not a strict prerequisite. If it is blocked, pair with a participant
whose fork works or use the draft fallback below.

---

## B1 — Parallel authoring via branch and pull request (minutes 115-130)

**Objective.** Two or more authors change the same prompt library at the same time without
overwriting each other, and the change arrives as a reviewable proposal.

**Timebox.** 15 minutes: 3 brief and role assignment, 8 edit and open PR, 4 share and compare.
Fork setup must already be complete.

### Your change assignment

Pick one. In a pair or table, pick **different** ones so you can see parallel authoring.

| Author role | Change to make in `library/prompts/triage-intake.prompt.md` |
| --- | --- |
| A | Sharpen the `hardware_defect` vs `safety_concern` boundary: structural failure *under load* with any injury is always `safety_concern`. |
| B | Add a rule that `confidence` below 0.6 must list at least one entry in `missing_information`. |
| C | Add an explicit non-goal: the assistant never estimates repair cost or shipping dates. |
| D | Bump the version in the front matter and add the matching `library/CHANGELOG.md` entry. |

### Steps (GitHub web UI)

Labels can vary slightly. Stop before submitting if the repository owner shown at the top is
not your GitHub user.

1. From your fork's main page, select **library → prompts → triage-intake.prompt.md**.
2. Choose the pencil icon or **Edit this file**. On a narrow window, it may be in an overflow
   menu; use the option whose label or tooltip says edit.
3. Make your assigned edit inside the fenced prompt block. Keep the section headings.
4. Select **Commit changes...** or the equivalent commit button.
5. Enter an intent-based commit message, for example
   `Clarify safety_concern boundary for load-bearing failures`.
6. In the commit dialog, choose **Create a new branch for this commit and start a pull
   request**, not **Commit directly to `main`**. GitHub may phrase these options slightly
   differently; choose the option that creates a branch.
7. Name the branch `prompt/triage-intake-<short-change>`, for example
   `prompt/triage-intake-safety-boundary`, then select **Propose changes**,
   **Commit changes**, or the equivalent.
8. If GitHub displays **Compare & pull request**, select it. Otherwise open the
   **Pull requests** tab in your fork and choose **New pull request**.
9. Inspect the compare/base controls:
   - **Base repository:** `<your-user>/<repo-name>` — your fork.
   - **Base branch:** `main`.
   - **Head/compare repository:** `<your-user>/<repo-name>`.
   - **Compare branch:** your new `prompt/...` branch.
10. Confirm the relationship is equivalent to
    `<your-user>/<repo>:main <- <your-user>/<repo>:prompt/...`.
    **Do not submit against the facilitator/source repository.**
11. If GitHub redirected to an upstream comparison, change **base repository** to your own
    fork. If necessary, return to your fork's **Pull requests → New pull request** and set the
    four controls there.
12. Select **Create pull request**. Complete the template: what changed, why, test cases,
    evaluation evidence, and rollback. Select **Create pull request** again to submit.
13. Copy the PR URL from the browser address bar and share it with your partner.

### Expected output

A pull request in your fork showing a small, readable diff of the prompt file, a filled-in
template body, and a branch name that says what the change is.

### Success criteria

- [ ] The diff touches only the files your change needs.
- [ ] The PR body states intent, evidence, and rollback.
- [ ] Your partner's PR exists independently and does not conflict with yours.
- [ ] Neither of you edited the default branch directly.

### Checkpoint

Post your PR title and the one line of the prompt you changed.

### Debrief prompts

1. What would have happened if both of you had edited the same line of the same file?
2. What in the diff made review easy or hard?
3. What belongs in the PR body that a diff can never show?

### Recovery and fallback

FALLBACK — If forking is blocked or GitHub is unreachable:
- Draft the same change in your workbook as a "diff by hand": show the removed line and the
  added line, plus the PR body fields. Pair review it verbally in B2.
- Local `git` is an equally valid alternative if you already have it configured. It is never
  required.

---

## B2 — Governance review (minutes 137-149)

**Objective.** Review someone else's PromptOps change the way an owner would: against a
checklist, not against taste.

**Timebox.** 12 minutes: 2 orient, 6 review, 4 respond.

### Steps

1. Open the PR URL your partner shared in chat/direct message, or use their browser in person.
2. Confirm their PR targets `main` in **their own fork**, not the source repository.
3. Open [../governance/pr-checklist.md](../governance/pr-checklist.md) and work top to bottom.
4. Open **Files changed**. Hover next to a changed line until a **+** appears, select it, enter
   a line comment, and choose **Start a review** or **Add single comment**.
5. Leave at least three line comments:
   - one that blocks (a governance or safety gap),
   - one that asks a question,
   - one that is a concrete suggestion.
6. Select **Review changes** near the upper-right, add a summary, select **Approve**,
   **Request changes**, or **Comment**, and then select **Submit review**.
7. GitHub may prevent authors from approving their own PR. Partner review is expected: you
   review your partner's PR and they review yours.
8. Check [../governance/ownership-raci.md](../governance/ownership-raci.md) and state who
   would have to approve this change for real, and why.
9. Respond to the review you received. Accept, push back with a reason, or defer with an issue.

### Expected output

A PR with real review comments and an explicit decision: approve, request changes, or hold
pending evaluation evidence.

### Success criteria

- [ ] Every checklist item is either satisfied or explicitly waived with a reason.
- [ ] At least one comment refers to evidence (test cases, evaluation results) rather than
      opinion.
- [ ] The required approver role is named.

### Checkpoint

Post: `PR reviewed | blocking items found | decision`.

### Debrief prompts

1. Which checklist item caught the most issues across the room?
2. Where is the line between a reviewer's judgment and an owner's decision?
3. What would you automate, and what must stay human?

### Recovery and fallback

FALLBACK — Review the reference PR body in
[solutions/07-lifecycle-change-solution.md](solutions/07-lifecycle-change-solution.md) against
the checklist and mark it up on paper.

---

## B3 — Monitoring signal to issue to proposed change (minutes 156-168)

**Objective.** Close the loop: a production signal becomes a tracked issue, a scoped proposal,
a reviewed change, and a rollback plan.

**Timebox.** 12 minutes: 3 read the signal, 5 write the issue, 4 decide the change.

### The synthetic monitoring signal

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

### Steps

1. Read the digest and name the single most important signal. (Hint: it is not the 18 percent.)
2. In your fork, find **Issues** in the repository navigation near **Code** and
   **Pull requests** (or in an overflow menu), then select **New issue**. If the tab is missing
   and you own the fork, open **Settings → General → Features** and enable Issues if that
   option is available. If you cannot enable it, draft the same issue in your workbook and
   review it with a partner.

```text
Title: Triage misclassifies load-bearing failures as hardware_defect

Signal
- 22 reviewer overrides in the 2026-09-08 week, all load-bearing failures, 3 with injury.
- Caught in human review; none reached customers.

Impact hypothesis
- The category mismatch may affect ownership, analytics, or later routing. Current workshop
  fixtures still use route_to_safety_review, so do not claim a delayed safety review without
  trace evidence.

Proposed change
- Add an explicit rule to library/prompts/triage-intake.prompt.md: structural failure under
  load plus any injury is always safety_concern with severity s1_safety.

Evidence required before release
- TC-07 passes on two consecutive runs.
- All existing safety cases still pass (regression).
- Schema validity stays at 100 percent on the test set.

Rollback plan
- Revert to prompt version 1.2.0 and re-run the safety cases.

Owner
- @your-org/prompt-owners (replace with your real team)
```

3. Add the missing regression case to your workbook: a new line for
   [06-test-cases.jsonl](06-test-cases.jsonl) covering "strap tore while carrying a full load,
   bruised wrist" — that is TC-07, which is why it already exists in the set.
4. Decide, as a group, who approves this change and what evidence they require.

OPTIONAL — GITHUB COPILOT: if your account has it, you may ask GitHub Copilot to draft the
prompt change as a pull request from this issue. The proposal is still a proposal: a human
reviews the diff, the evidence, and the rollback plan before anything merges. See
[../optional/github-copilot.md](../optional/github-copilot.md).

CORE alternative that meets the same objective: draft the same change by hand in the GitHub
web UI (or with Microsoft Copilot chat helping you word it) and open the PR yourself.

### Expected output

An issue with signal, impact, proposal, required evidence, rollback, and owner — plus a clear
statement of who approves.

### Success criteria

- [ ] The issue names the signal and the impact separately.
- [ ] Required evidence is specific and checkable.
- [ ] A rollback plan exists and names a version.
- [ ] A human approval step is explicit, regardless of who or what drafted the change.

### Checkpoint

Post: `issue created | evidence required | approver`.

### Debrief prompts

1. Which monitoring signals would you actually instrument first in your own workflow?
2. How do you avoid a prompt that grows by one rule per incident until nobody understands it?
3. What is the smallest rollback you could perform today?

### Recovery and fallback

FALLBACK — If issue creation is blocked, write the issue body in your workbook and read it
aloud during the debrief. The artifact matters more than the tool.

## Troubleshooting GitHub web tasks

| Problem | What to do |
| --- | --- |
| **Fork button is missing** | Confirm you are signed in and the URL is the facilitator's published GitHub repository, not a local path. Labels may vary or the action may be in an overflow menu. If it remains unavailable, pair or use the workbook draft. |
| **Organization policy blocks the fork** | Do not work around policy. Pair with someone whose fork is allowed, or draft the diff and PR body in the workbook. |
| **You started editing the source repository** | Do not commit. Cancel the editor and return to `<your-user>/<repo-name>`. If you already created a source branch or PR, stop, tell the facilitator, close the PR without merging, and repeat in your fork. |
| **The PR targets the upstream/source repository** | Do not submit it. Set **base repository** to your fork and **base branch** to `main`. If already submitted, close it without merging and open a new PR from your fork's **Pull requests → New pull request**. |
| **Issues tab is missing** | In your own fork, try **Settings → General → Features → Issues** if available. Otherwise write the issue in the workbook and partner-review it. |
| **You cannot approve your own PR** | This is expected. Copy the PR URL to your partner; they submit the review. If partner access fails, use a line-by-line verbal or workbook review and record the decision without pretending it was a GitHub approval. |

## Reference

[solutions/07-lifecycle-change-solution.md](solutions/07-lifecycle-change-solution.md)
