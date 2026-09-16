# Pull request

Use this template for any change to a prompt, agent definition, contract, or governance rule.
The full checklist lives in [../governance/pr-checklist.md](../governance/pr-checklist.md).

## What changed

<!-- One or two sentences. Name the file and the behaviour that changes. -->

## Why

<!-- The signal, issue, or requirement behind the change. Link the issue if there is one. -->

## Type of change

- [ ] Prompt wording or rules
- [ ] Output contract or schema (breaking for consumers)
- [ ] Tool or function contract
- [ ] Subagent or orchestration change
- [ ] Model selection change
- [ ] Test cases or evaluation rubric
- [ ] Governance, ownership, or release process
- [ ] Workshop delivery content only

## Risk and blast radius

<!-- Who or what is affected if this is wrong? Is a safety-relevant path involved? -->

## Evidence

- Test cases run:
- Runs per case (two runs minimum for anything safety-relevant):
- Results (paste or attach in the evaluation CSV format):
- Regressions checked:
- Schema validity:

## Human review and approval

- [ ] A named human reviews this change before merge.
- [ ] Any write action still requires explicit human approval at execution time.
- [ ] If an assistant drafted this change, that is disclosed below.

Drafted by: <!-- human / human with assistant help / assistant proposal reviewed by human -->

## Rollback plan

<!-- Which version do we return to, who does it, and how do we confirm it worked? -->

## Safety and data

- [ ] No real customer, personal, or company-confidential data appears in this change.
- [ ] Only synthetic scenario data is used.
- [ ] No claim is made that evaluation guarantees correctness.

## Version and changelog

- [ ] Version bumped where required.
- [ ] `library/CHANGELOG.md` updated with the evidence for this version.
