# OPTIONAL — MICROSOFT FOUNDRY

**This path is optional. Nothing in the workshop depends on it.** If you have no Microsoft
Foundry (formerly Azure AI Foundry) project, use the no-access simulation in this file. It
meets the same learning objective: understand how an agent is authored, tested, and evaluated
as a governed artifact.

No command line, no `azd`, and no deployment is used or needed here. Everything below is
portal-oriented and conceptual, because product UI changes frequently — treat the steps as
*shapes of work*, not as literal click paths.

## Where this fits in the run of show

- Teaching segment S1.4, minutes 60-66 — author, test, evaluate.
- Referenced again in Activity A4, minutes 66-76, as the optional way to run the test set.
- Referenced in Session 2 quality and operations, minutes 149-156.

## What Foundry adds over chat

| Concern | Chat window | Foundry project |
| --- | --- | --- |
| Where the instructions live | Your clipboard | A named, saved agent configuration |
| Tools | Simulated by pasting results | Real tool/function definitions the service can invoke |
| Testing | You re-paste by hand | A repeatable test surface over a saved dataset |
| Evaluation | Your CSV and your judgment | Built-in evaluators plus your own criteria, with stored runs |
| Observability | None | Traces and run history you can inspect later |
| Governance | Your repository | Your repository, plus project-level roles and resource controls |

The important idea: **the repository stays the source of truth.** Foundry is where a
configured agent runs and is measured; the reviewable text still lives in Git.

## The four activities, conceptually

1. **Author.** Create an agent in a Foundry project: give it a name, a model deployment,
   instructions (the same prompt you wrote in Exercise 2), and optionally tools. Your
   instructions are the artifact you already own in
   [../library/prompts/triage-intake.prompt.md](../library/prompts/triage-intake.prompt.md).
2. **Test.** Interact with the agent in the portal's playground-style surface with the same
   synthetic intake messages from [../exercises/06-test-cases.jsonl](../exercises/06-test-cases.jsonl).
   Watch how tool definitions turn into tool-call proposals and how results feed back.
3. **Evaluate.** Point an evaluation run at a dataset of inputs and expected results, choose
   evaluators (built-in quality and safety evaluators, plus criteria of your own), and review
   scores per case and in aggregate.
4. **Observe and iterate.** Inspect traces, find the failing pattern, change the prompt in the
   repository, open a pull request, re-run the evaluation, and attach the results as evidence.

## Try it (if you have access)

Timebox this to the same 6-10 minutes as the core path; do not let it stretch the room.

1. Open your Foundry project in the portal.
2. Create a new agent. Paste the reference instructions from
   [../exercises/solutions/01-improved-prompt.md](../exercises/solutions/01-improved-prompt.md).
3. Send the three synthetic messages from
   [../exercises/03-structured-output.md](../exercises/03-structured-output.md) and check the
   output against [../exercises/03-structured-output.schema.json](../exercises/03-structured-output.schema.json).
4. Create a small evaluation dataset from the ten cases in
   [../exercises/06-test-cases.jsonl](../exercises/06-test-cases.jsonl) and run an evaluation.
5. Export or screenshot the per-case results and attach them to your Activity B1 pull request
   as evidence.

Expected result: the same failure patterns you saw in chat, now with a record you can link to
from a pull request.

## No-access simulation (equally valid)

FALLBACK — do this if you have no Foundry project. It takes the same time and produces the
same artifact.

1. Treat [../library/agents/triage-agent.agent.yaml](../library/agents/triage-agent.agent.yaml)
   as the agent configuration you would have created in a project. Read it aloud as a group:
   model choice, instructions pointer, tools allowed, write actions requiring approval,
   subagents, guardrails, evaluation gate.
2. Run the same synthetic cases in Microsoft Copilot chat, exactly as in Exercises 3, 4, and 6.
3. Record results in [../exercises/06-eval-results-template.csv](../exercises/06-eval-results-template.csv).
   That CSV is your evaluation run record.
4. Write the release decision sentence. That decision — not the tool — is the learning
   objective.

## Honest limits to state out loud

- Built-in evaluators score *signals*; they do not certify correctness. Two evaluators can
  disagree with each other and with a human reviewer.
- A good evaluation score on ten synthetic cases tells you about ten synthetic cases.
- Evaluation and content safety features reduce risk. They do not remove the need for human
  review on safety-relevant results.
- Any capability you rely on should be re-checked against current product documentation before
  you build a process on it.

## Cost, quota, and access notes

- A Foundry project needs an Azure subscription, a deployed model, and appropriate role
  assignments. Getting them is a procurement and administration task, not a workshop task.
- Model deployments consume quota and incur cost. Do not create one during the workshop simply
  to follow along.
- If you want this capability for your team, the follow-up action is a conversation with your
  Azure administrator, not a signup during the break.

## Official documentation

Product documentation changes faster than any workshop file. Start at the docs root and
navigate:

- Microsoft Foundry documentation: <https://learn.microsoft.com/azure/ai-foundry/>
- Foundry agents: <https://learn.microsoft.com/azure/ai-foundry/agents/>
- Evaluation of generative AI applications: <https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai>
- Responsible AI in Microsoft Foundry: <https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview>
- Foundry portal: <https://ai.azure.com>

More links in [../resources.md](../resources.md).

## Related

- [Facilitator guide](../facilitator-guide.md)
- [Participant workbook](../participant-workbook.md)
- [OPTIONAL — GITHUB COPILOT path](github-copilot.md)
- [Exercise 6, evaluation](../exercises/06-evaluation-rubric.md)
