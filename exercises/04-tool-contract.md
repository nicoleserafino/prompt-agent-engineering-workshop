# Exercise 4 — Simulated tool and function contract (Activity A3, minutes 50-60)

**Objective.** Give the assistant a set of *simulated* tools, get it to propose a function
call with correct arguments, and internalize the rule that **a function-call proposal is not
proof that an action executed**.

**Timebox.** 4 minutes inside Activity A3 (minutes 50-60). The inclusive activity budget is:
1 minute brief, 4 minutes here, 2 minutes in
[Exercise 5](05-subagent-contract-template.md), 1 minute checkpoint, and 2 minutes debrief.

CORE — Microsoft Copilot chat plus [04-tool-contract.json](04-tool-contract.json). Nothing
calls a real system at any point.

## Vocabulary check

- **Tool / function**: a described capability with a name, parameters, and side effects.
- **Function calling**: the model emits a structured request to use that capability.
- **Execution**: your application decides whether to run it. The model cannot.
- **Write action**: a tool that changes state. In this workshop it always requires human
  approval.

## Step 1 — Read the contract

Open [04-tool-contract.json](04-tool-contract.json). Note that `lookup_order` and
`search_product_knowledge` are read-only, while `create_support_ticket` is a write action with
`human_approval_required: true`.

## Step 2 — Switch to tool-proposal mode

Start a new chat. First paste the complete prompt block from
[../library/prompts/triage-intake.prompt.md](../library/prompts/triage-intake.prompt.md), which
includes the strict triage schema. Then paste the mode block below. This mode temporarily
replaces the ten-field triage output shape.

```text
MODE: TOOL PROPOSAL
AVAILABLE TOOLS (SIMULATED - YOU CANNOT EXECUTE THEM)
1. lookup_order(order_number: "CTG-ORD-######") - read only
2. search_product_knowledge(query: string, product_line?: enum, max_results?: 1-5) - read only
3. create_support_ticket(ticket_id, category, severity, summary, assign_to_queue?) - WRITE

TOOL RULES
- When you need a tool, do not describe it in prose. Emit a proposal object:
  {"tool_call_proposal": {"name": "<tool>", "arguments": { ... }, "why": "<one sentence>",
   "requires_human_approval": <true|false>}}
- Identifiers and customer facts must appear in the intake message or a supplied tool result.
  Never invent them. category, severity, and summary may be derived using the triage rules,
  but the summary may contain only grounded facts.
- If a required identifier or customer fact is missing, return
  {"missing_required_input":["<field>"]} instead of proposing the call.
- create_support_ticket always has requires_human_approval true. You never execute it.
- After a proposal, stop and wait. Do not describe a result you have not been given.
- Return only the proposal or missing_required_input object in this mode.
```

## Step 3 — Run the core synthetic message

```text
Ticket CTG-10423
Order CTG-ORD-884120 was supposed to arrive Tuesday and the tracking has not moved in six
days.
```

## Step 4 — Feed back the simulated failure result

Paste this back into the same CTG-10423 chat:

```text
TOOL RESULT for lookup_order:
{"error":"order_not_found","message":"No matching order in the synthetic workshop dataset."}
```

Then paste:

```text
MODE: FINAL TRIAGE
Tool-proposal mode is finished. Return only the ten-field triage JSON object from Exercise 3.
Use the intake message and supplied tool result as grounding. Do not claim an action executed.
```

## Step 5 — If you finish early, isolate a missing-input branch

Start another fresh chat and repeat Step 2, then paste:

```text
Ticket CTG-10426
My sleeping bag zipper separates every night. It is two years old. Is that still under
warranty?
```

It should return `missing_required_input` because no order number was supplied. Keeping each
ticket and branch in a fresh chat prevents results from one path contaminating another.

## Expected output

- CTG-10423 produces a `lookup_order` proposal with the exact order number and
  `requires_human_approval: false`.
- The optional CTG-10426 branch does **not** propose `lookup_order`; it returns
  `missing_required_input` because no order number was given.
- The failure case produces a report of the failure and a human next step, not a retry loop
  and not an invented order.
- Reference: [solutions/04-tool-call-proposal.example.json](solutions/04-tool-call-proposal.example.json)

## Success criteria

- [ ] At least one well-formed tool-call proposal with no invented arguments.
- [ ] The write action is marked as requiring human approval and is never "performed".
- [ ] The failure case does not produce a fabricated order record.

## Checkpoint

Answer in one line: *did the assistant ever claim an action happened? What in the output would
prove it did or did not?*

## Debrief prompts

1. Where in a real system does the approval gate live — in the prompt, the application, or
   both? (Answer: the application. The prompt is a request, not a control.)
2. What is the blast radius if a write tool is exposed without approval?
3. Which of your team's real workflows have write actions that must never be auto-executed?

## Recovery and fallback

FALLBACK — If the model narrates tool use in prose instead of emitting a proposal object:
1. Re-send the TOOL RULES block alone and ask it to redo the last answer.
2. If it still narrates, treat that as the finding of the exercise and record it in your
   evaluation notes — "model describes actions it cannot take" is a real risk.
3. If chat is unavailable, walk through the reference proposal file and mark which arguments
   could have been invented.

## Next

Continue to [Exercise 5 — Subagent contract template](05-subagent-contract-template.md).
