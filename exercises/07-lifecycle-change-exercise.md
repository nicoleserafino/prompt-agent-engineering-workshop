# Exercise 7 — Lifecycle change exercise (Activities B1, B2, B3)

**Objective.** Move a prompt change through a real multi-author lifecycle: propose it on a
branch, open a pull request, review it against the governance checklist, and turn a monitoring
signal into a tracked, human-approved improvement.

**Timeboxes.** B1 minutes 115-130 (15), B2 minutes 137-149 (12), B3 minutes 156-168 (12).

CORE — GitHub web UI in a browser plus Microsoft Copilot chat. No local `git` required, no
GitHub Copilot license required, no Microsoft Foundry access required.

## Setup (do this once, during welcome or the break)

1. Sign in to GitHub in a browser.
2. Open the workshop repository and choose **Fork** to create your own copy. You have full
   write access to your fork, so every step below works without any organization permission.
3. Check whether the fork has an **Issues** tab. If not, and you control the fork, open
   **Settings → General → Features** and enable Issues. If settings are unavailable, plan to
   draft the B3 issue in the workbook instead.
4. If you cannot fork, see the FALLBACK section at the end. You lose nothing pedagogically.

---

## B1 — Parallel authoring via branch and pull request (minutes 115-130)

**Objective.** Two or more authors change the same prompt library at the same time without
overwriting each other, and the change arrives as a reviewable proposal.

**Timebox.** 15 minutes: 3 setup, 8 edit and open PR, 4 compare across authors.

### Your change assignment

Pick one. In a pair or table, pick **different** ones so you can see parallel authoring.

| Author role | Change to make in `library/prompts/triage-intake.prompt.md` |
| --- | --- |
| A | Sharpen the `hardware_defect` vs `safety_concern` boundary: structural failure *under load* with any injury is always `safety_concern`. |
| B | Add a rule that `confidence` below 0.6 must list at least one entry in `missing_information`. |
| C | Add an explicit non-goal: the assistant never estimates repair cost or shipping dates. |
| D | Bump the version in the front matter and add the matching `library/CHANGELOG.md` entry. |

### Steps (GitHub web UI)

1. In your fork, open `library/prompts/triage-intake.prompt.md`.
2. Choose the pencil (**Edit this file**).
3. Make your assigned edit inside the fenced prompt block. Keep the section headings.
4. Scroll down, choose **Create a new branch for this commit and start a pull request**.
5. Name the branch using the convention: `prompt/triage-intake-<short-change>` (for example
   `prompt/triage-intake-safety-boundary`).
6. Commit with a message that states the intent, for example
   `Clarify safety_concern boundary for load-bearing failures`.
7. On the pull request form, use the repository pull request template. Fill in: what changed,
   why, which test cases were run, the evaluation evidence, and the rollback plan.
8. Open the PR against the default branch **of your fork**.

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

1. Swap PRs with your partner (post the link in chat, or swap laptops in the room).
2. Open [../governance/pr-checklist.md](../governance/pr-checklist.md) and work top to bottom.
3. Leave at least three review comments on specific lines:
   - one that blocks (a governance or safety gap),
   - one that asks a question,
   - one that is a concrete suggestion.
4. Check [../governance/ownership-raci.md](../governance/ownership-raci.md) and state who
   would have to approve this change for real, and why.
5. Respond to the review you received. Accept, push back with a reason, or defer with an issue.

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
2. In your fork, open **Issues** and create an issue using this structure. If Issues is not
   available, draft the same issue in your workbook and review it with a partner.

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

## Reference

[solutions/07-lifecycle-change-solution.md](solutions/07-lifecycle-change-solution.md)
