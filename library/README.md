# Shared prompt and agent library

This folder is the workshop's example of a **shared library**: the reviewable, versioned
source of truth for prompts, agent definitions, and the contracts they depend on.

CORE — everything here is plain text you can read, diff, and review in the GitHub web UI.

## Layout

| Path | What lives here | Who owns it |
| --- | --- | --- |
| [prompts/](prompts/) | Released prompt files with version, owner, schema, and test set in the front matter | Prompt owners |
| [agents/](agents/) | Agent definitions: model choice, tools, subagents, guardrails, evaluation gate | Agent owners |
| [CHANGELOG.md](CHANGELOG.md) | One line per released version, with the evidence that supported it | Release approvers |
| [../exercises/](../exercises/) | Schemas, tool contracts, test cases used by the library | Prompt owners |
| [../governance/](../governance/) | Review, ownership, release, rollback, monitoring rules | Governance owners |

## Rules of the library

1. A prompt is not "shared" until it has an owner, a version, an output contract, and a test set.
2. Every change arrives as a pull request. No direct edits to the default branch.
3. Changing the model is a governed change, not a cosmetic one. Re-run the evaluation set.
4. Evaluation results are evidence, not proof. Human review stays in the loop.
5. Every file here uses synthetic Contoso Trail Gear data. Never add real customer content.

## Files in this library

- [prompts/triage-intake.prompt.md](prompts/triage-intake.prompt.md)
- [agents/triage-agent.agent.yaml](agents/triage-agent.agent.yaml)
- [CHANGELOG.md](CHANGELOG.md)

## Where this is used in the workshop

- Session 2 teaching segment on the lifecycle and the shared library (minutes 102-108)
- Activity B1, parallel authoring via branch and pull request (minutes 115-130)
- Activity B2, governance review (minutes 137-149)
- Activity B3, monitoring signal to issue to proposed change (minutes 156-168)

See the [participant workbook](../participant-workbook.md) and the
[facilitator guide](../facilitator-guide.md).
