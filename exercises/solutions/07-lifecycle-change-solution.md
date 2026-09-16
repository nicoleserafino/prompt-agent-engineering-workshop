# Reference solution — Exercise 7 (lifecycle change)

Facilitators: use during the B2 and B3 debriefs, or as the FALLBACK artifact if GitHub is
unavailable.

## Reference pull request

**Branch:** `prompt/triage-intake-safety-boundary`

**Title:** Treat load-bearing failure with injury as safety_concern

**Diff (conceptual)**

```diff
 Severity ladder (apply in order, stop at the first match)
 1. s1_safety - the message describes injury, burn, fire, fumes, gas smell, or structural
-   failure under load. Set safety_flag to true.
+   failure under load. A strap, pole, frame, or seam that fails while the product is loaded
+   or being carried is a structural failure under load. If the message also mentions any
+   injury, category must be safety_concern. Set safety_flag to true.
```

```diff
---
 id: triage-intake
-version: 1.2.0
+version: 1.3.0
 status: released
```

**PR body**

```text
## What changed
Clarified that a strap, pole, frame, or seam failing while loaded or carried counts as
structural failure under load, and that any accompanying injury forces category
safety_concern.

## Why
Weekly monitoring digest (2026-09-08 to 2026-09-14) showed 22 reviewer overrides where
hardware_defect was corrected to safety_concern. Three involved a minor injury. All were
caught in human review; none reached customers.

## Risk and blast radius
Higher false-positive rate on safety routing is acceptable; a missed safety case is not.
Expect the safety review queue to grow modestly.

## Evidence
- TC-07 passed on two consecutive runs after the change (previously failed on both).
- TC-02, TC-10 (existing safety cases) still pass on two runs: no regression.
- TC-01, TC-03, TC-04, TC-05, TC-06, TC-08, TC-09 unchanged.
- Schema validity 10/10.
- Results attached as a CSV in the evaluation format.

## Human review
Every s1_safety result still routes to a human safety reviewer before any customer reply.
Evaluation evidence supports this change; it does not prove correctness.

## Rollback
Revert to prompt version 1.2.0 (single-file revert) and re-run the three safety cases.
Rollback owner: prompt owner on call.

## Checklist
See governance/pr-checklist.md - all items satisfied; no waivers.
```

## Reference review comments

1. **Blocking.** "Version bumped to 1.3.0 but `library/CHANGELOG.md` has no matching entry.
   Release rules require one line per released version with its evidence."
2. **Question.** "Does 'while being carried' cover a pack that fails while being lifted onto a
   shoulder? One sentence in the rule will prevent a repeat of this ambiguity."
3. **Suggestion.** "Add the injury-plus-load phrasing to `missing_information` guidance too, so
   the agent asks for load weight when it is not stated."
4. **Governance.** "`library/agents/triage-agent.agent.yaml` names the owner team. Per
   `governance/ownership-raci.md`, this change needs the prompt owner's approval and a
   governance reviewer because it touches a safety rule."

## Reference decision

Request changes: add the CHANGELOG entry, then approve. Do not merge on evaluation evidence
alone without the changelog, because rollback depends on knowing what shipped when.

## Reference issue (B3)

Title: `Triage misclassifies load-bearing failures as hardware_defect`

Body: see the structure in
[../07-lifecycle-change-exercise.md](../07-lifecycle-change-exercise.md) under B3. The three
things people most often leave out are the **required evidence**, the **rollback plan**, and
the **named approver**.

## Teaching points to land

- The issue, the PR, the evidence, and the rollback are all plain text in one repository.
  That is what makes multi-author prompt work reviewable.
- Whether a human or an assistant drafted the change, the approval boundary is identical.
- Evaluation evidence supports a decision. It never replaces the human who makes it.
