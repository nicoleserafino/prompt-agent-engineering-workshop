# Prompt & Agent Engineering Workshop

A facilitator-ready, 180-minute workshop on writing reliable prompts, turning prompts into
agents, and running a shared prompt library as a governed, multi-author practice.

Delivered twice with identical content: once **virtually** and once **in person**.

- Scenario: **Contoso Trail Gear** (fictional) public product-support intake and triage
- Core path needs only a browser, a GitHub account, and Microsoft Copilot chat
- Microsoft Foundry and GitHub Copilot are **optional** everywhere, with a no-access
  alternative for every step

## Purpose

By the end of the workshop, participants can:

1. Write a prompt with explicit instructions, grounding rules, decision rules, and an output
   contract — and explain which failure each part removes.
2. Convert free-form output into a schema-checked structured output.
3. Describe a tool/function contract and recognize that a function-call proposal is not proof
   that an action executed.
4. Decompose a workflow into an orchestrator plus subagents with explicit contracts.
5. Evaluate prompts against synthetic test cases and tell a real defect from model variability.
6. Operate a shared prompt library in GitHub: branches, pull requests, CODEOWNERS, versioning,
   release, rollback, and monitoring-driven improvement.
7. Teach this material to their own team using the included train-the-trainer materials.

## Audience

Microsoft employees who write prompts or build agent-assisted workflows: engineers, PMs,
support and operations leads, content and program managers. No AI background assumed. No
coding required on the core path.

## Prerequisites and access matrix

| Capability | Needed for | Required? | If you do not have it |
| --- | --- | --- | --- |
| Browser and a GitHub account | Session 2 activities | Yes (core) | Pair with someone who has one; draft changes in the workbook |
| Microsoft Copilot chat | Sessions 1 and 2 activities | Yes (core) | Use the pre-captured outputs in `exercises/solutions/`; pair up |
| Ability to fork a public repository | Activities B1-B3 | Recommended | Draft the diff and PR body by hand in the workbook |
| Microsoft Foundry (formerly Azure AI Foundry) project | Extension only | No — OPTIONAL | Use the no-access simulation in [optional/foundry.md](optional/foundry.md) |
| GitHub Copilot / coding agent | Extension only | No — OPTIONAL | Use the manual path in [optional/github-copilot.md](optional/github-copilot.md) |
| Local `git` and an editor | Alternative to the web UI | No | The GitHub web UI is the supported path |
| Python 3.8+ | Running the repository validator | No | Only maintainers need it |

Send [participant-preflight.md](participant-preflight.md) before each delivery.

## Exact agenda (180 minutes)

Canonical source: [schedule.json](schedule.json). Minutes are elapsed from minute 0.

| Minutes | Duration | Block |
| --- | --- | --- |
| 0-7 | 7 | Welcome, objectives, setup check |
| 7-82 | 75 | **Session 1 — Prompt & Agent Engineering Foundations** |
| 82-87 | 5 | Transition and knowledge check |
| 87-102 | 15 | Break |
| 102-177 | 75 | **Session 2 — Multi-Author PromptOps & Governance** |
| 177-180 | 3 | Close and handoff |

Session 1 internals (75 minutes):

| Minutes | Duration | Segment |
| --- | --- | --- |
| 7-14 | 7 | Prompt fundamentals: instructions, context, grounding |
| 14-26 | 12 | Activity A1 — improve the starter triage prompt |
| 26-33 | 7 | Structured outputs and common failure modes |
| 33-43 | 10 | Activity A2 — add a structured output contract |
| 43-50 | 7 | From prompts to agents: tools, function calling, orchestration, subagents |
| 50-60 | 10 | Activity A3 — simulated tool contract and subagent decomposition |
| 60-66 | 6 | Building agents in Microsoft Foundry: author, test, evaluate |
| 66-76 | 10 | Activity A4 — evaluate against synthetic test cases |
| 76-82 | 6 | Reusable templates and train-the-trainer handoff |

Session 2 internals (75 minutes):

| Minutes | Duration | Segment |
| --- | --- | --- |
| 102-108 | 6 | PromptOps lifecycle and the shared library |
| 108-115 | 7 | GitHub as source of truth: structure, branches, PRs, parallel authoring |
| 115-130 | 15 | Activity B1 — parallel authoring via branch and pull request |
| 130-137 | 7 | Governance and ownership: CODEOWNERS, model choice, subagent contracts |
| 137-149 | 12 | Activity B2 — review a PromptOps pull request |
| 149-156 | 7 | Quality and operations: evaluations, regression, releases, monitoring, rollback |
| 156-168 | 12 | Activity B3 — monitoring signal to issue to proposed change |
| 168-177 | 9 | Discussion, recommendations, next steps |

The 15 minutes outside the two sessions and the break are deliberate: 7 for welcome and setup,
5 for the transition and knowledge check, 3 for the close.

## Quick navigation

| I am... | Start here |
| --- | --- |
| Facilitating a session | [facilitator-guide.md](facilitator-guide.md), then [facilitator-materials.md](facilitator-materials.md) |
| A participant | [participant-workbook.md](participant-workbook.md) |
| Presenting | [slides/slide-outline.md](slides/slide-outline.md) |
| Doing the exercises | [exercises/README.md](exercises/README.md) |
| Looking at governance | [governance/README.md](governance/README.md) |
| Learning to teach this | [train-the-trainer.md](train-the-trainer.md) |
| Worried about outages | [contingency-plan.md](contingency-plan.md) |
| Looking for the shared library | [library/README.md](library/README.md) |
| Looking for official docs | [resources.md](resources.md) |
| Exploring optional paths | [optional/foundry.md](optional/foundry.md), [optional/github-copilot.md](optional/github-copilot.md) |

## Two delivery modes

| | Virtual | In person |
| --- | --- | --- |
| Activities | Breakout rooms of 3-4, facilitator visits each | Tables of 4-6, facilitator circulates |
| Checkpoints | Meeting chat, one line per person | Sticky notes or verbal round-robin |
| Sharing work | Paste links in chat | Screen at the front, or swap laptops |
| Timing discipline | On-screen timer, 2-minute warnings | Visible timer, 2-minute warnings |
| Biggest risk | Silent rooms and unshared screens | Tables that drift off-scope |
| Mitigation | Name a reporter per room; drop the debrief question in chat first | Circulate constantly; use the same question at every table |

Both modes run the identical schedule above. Mode-specific adaptations are marked in the
[facilitator guide](facilitator-guide.md) and [train-the-trainer.md](train-the-trainer.md).

## Callout labels used in this repository

| Label | Meaning |
| --- | --- |
| CORE | Works with a browser, a GitHub account, and Microsoft Copilot chat |
| OPTIONAL — MICROSOFT FOUNDRY | Needs a Microsoft Foundry project; always has a no-access alternative |
| OPTIONAL — GITHUB COPILOT | Needs GitHub Copilot; always has a manual alternative |
| FALLBACK | What to do when something is unavailable, slow, or out of time |

## Safety, data handling, and honest limits

- **Synthetic data only.** Every message, order, and ticket here is fictional. Never paste real
  customer messages, personal data, credentials, or company-confidential content into any chat
  surface during this workshop.
- **Models vary.** The same prompt and input can produce different answers on different runs
  and different models. Expect it, design for it, and always run safety-relevant cases twice.
- **Evaluation reduces risk. It does not guarantee correctness and does not replace human
  review.** A passing score on synthetic cases describes those cases only.
- **A function-call proposal is not proof that an action executed.** Execution and approval
  live in the application, not in the model's words.
- **Placeholder ownership.** `@your-org/...` teams in `.github/CODEOWNERS` and
  `governance/CODEOWNERS.sample` are placeholders. Replace them before reuse — see
  [governance/README.md](governance/README.md).
- **Public sources only.** Every external link in [resources.md](resources.md) is public
  Microsoft or GitHub documentation.

## Terminology

| Term | Working definition used here |
| --- | --- |
| Prompt | The instructions and context you send to a model for one task |
| Grounding / context | The facts you supply that the model must rely on instead of memory |
| Structured output | Output constrained to an agreed shape, such as a JSON schema |
| Agent | A prompt plus tools plus a loop that can take multiple steps toward a goal |
| Tool / function calling | A described capability the model can *propose* to use; your application executes it |
| Workflow | The ordered business steps the agent is supporting |
| Orchestration | Deciding which step runs next and when to stop |
| Subagent | A narrow agent owning one step with a defined input and output contract |
| Evaluation | Scoring outputs against expectations on a fixed input set |
| Regression test | Re-running previously passing cases after a change |
| Monitoring | Watching real usage after release for unanticipated signals |
| Governance | Ownership, review, approval, release, and rollback rules |

"Microsoft Foundry" is the current product name (formerly Azure AI Foundry).

## Validating this repository

Maintainers only. Requires Python 3.8+ and no third-party packages.

```powershell
python validate.py
```

```powershell
python validate.py --verbose
```

The structural validator checks the canonical timing in [schedule.json](schedule.json) against the
README, facilitator guide, workbook, and slide outline; parses every JSON, JSONL, and CSV
example; checks the structured-output example against its schema; resolves every relative
Markdown link; and confirms the callout labels. Exit code 0 means those structural checks
passed. A facilitator-readiness review and rehearsal are still required before delivery.

## Repository map

```text
README.md                     this file
facilitator-guide.md          minute-by-minute run of show
participant-workbook.md       numbered follow-along for participants
train-the-trainer.md          rehearsal, facilitation, FAQs, misconceptions
facilitator-materials.md      virtual and in-person materials checklist
participant-preflight.md      email-ready pre-work checklist
contingency-plan.md           one-page outage and access contingency
resources.md                  official Microsoft and GitHub references
schedule.json                 canonical timing source
validate.py                   repository validator (Python standard library only)
slides/                       slide outline with speaker notes and timings
exercises/                    starter prompt through lifecycle change, plus solutions
library/                      the shared prompt and agent library
governance/                   CODEOWNERS sample, checklist, RACI, release, monitoring
optional/                     Microsoft Foundry and GitHub Copilot extensions
.github/                      pull request template and CODEOWNERS placeholder
```

## Reuse

Adapt this content for your own team: replace the placeholder owner teams, swap the fictional
scenario for one of your own that contains no confidential data, and rehearse with
[train-the-trainer.md](train-the-trainer.md).

No LICENSE file is included, because licensing depends on where you publish this and who owns
it. Add the license your organization requires before distributing the repository externally.
