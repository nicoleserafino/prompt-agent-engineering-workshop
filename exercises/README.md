# Exercises

Hands-on materials for the Prompt & Agent Engineering Workshop. Everything here uses the
fictional **Contoso Trail Gear** public product-support intake and triage scenario with
synthetic messages only.

CORE — every exercise below works with the GitHub web UI, Microsoft Copilot chat, and the
files in this repository. Local `git` commands are an alternative, never a requirement.
No Microsoft Foundry or GitHub Copilot license is needed for the core path.

> **Safety rule for every exercise:** never paste real customer messages, real order data,
> personal data, or company-confidential content into any chat surface. Use the synthetic
> inputs provided here.

## Progression

| # | Exercise | Activity | Minutes | What you produce |
| --- | --- | --- | --- | --- |
| 1 | [Starter prompt](01-starter-prompt.md) | A1 | 14-26 | A diagnosis of a weak prompt |
| 2 | [Improved prompt template](02-improved-prompt-template.md) | A1 | 14-26 | A rewritten, grounded prompt |
| 3 | [Structured output contract](03-structured-output.md) | A2 | 33-43 | Valid JSON that matches a schema |
| 4 | [Simulated tool and function contract](04-tool-contract.md) | A3 | 50-60 | A function-call proposal, not an executed action |
| 5 | [Subagent contract template](05-subagent-contract-template.md) | A3 | 50-60 | A decomposed triage workflow |
| 6 | [Evaluation rubric and test cases](06-evaluation-rubric.md) | A4 | 66-76 | Scored results and a decision |
| 7 | [Lifecycle change exercise](07-lifecycle-change-exercise.md) | B1, B2, B3 | 115-130, 137-149, 156-168 | A reviewed PromptOps change |

## Machine-readable files

| File | Format | Used by |
| --- | --- | --- |
| [03-structured-output.schema.json](03-structured-output.schema.json) | JSON Schema | Exercise 3, evaluation |
| [03-structured-output.example.json](03-structured-output.example.json) | JSON | Exercise 3 |
| [04-tool-contract.json](04-tool-contract.json) | JSON | Exercises 4 and 5 |
| [06-test-cases.jsonl](06-test-cases.jsonl) | JSONL | Exercises 6 and 7 |
| [06-eval-results-template.csv](06-eval-results-template.csv) | CSV | Exercise 6 |

## Reference solutions

Completed references live in [solutions/](solutions/). Facilitators: do not open these on
screen before the matching debrief.

- [solutions/01-improved-prompt.md](solutions/01-improved-prompt.md)
- [solutions/03-structured-output.solution.json](solutions/03-structured-output.solution.json)
- [solutions/04-tool-call-proposal.example.json](solutions/04-tool-call-proposal.example.json)
- [solutions/05-triage-subagent-contracts.yaml](solutions/05-triage-subagent-contracts.yaml)
- [solutions/06-eval-results.reference.csv](solutions/06-eval-results.reference.csv)
- [solutions/07-lifecycle-change-solution.md](solutions/07-lifecycle-change-solution.md)

## Optional paths

- OPTIONAL — MICROSOFT FOUNDRY: [../optional/foundry.md](../optional/foundry.md)
- OPTIONAL — GITHUB COPILOT: [../optional/github-copilot.md](../optional/github-copilot.md)

## Related

- [Participant workbook](../participant-workbook.md)
- [Facilitator guide](../facilitator-guide.md)
- [Shared library](../library/README.md)
- [Governance](../governance/pr-checklist.md)
