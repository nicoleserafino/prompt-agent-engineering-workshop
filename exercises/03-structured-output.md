# Exercise 3 — Structured output contract (Activity A2, minutes 33-43)

**Objective.** Turn free-form triage text into a machine-checkable JSON object that matches a
published schema, and see what happens when the model does not comply.

**Timebox.** 10 minutes inclusive: 1 minute facilitator brief, 2 minutes read and append the
contract, 4 minutes run, 1 minute check/checkpoint, and 2 minutes debrief.

CORE — Microsoft Copilot chat plus the schema file in this repository.

## Files

- Schema: [03-structured-output.schema.json](03-structured-output.schema.json)
- Example of a valid result: [03-structured-output.example.json](03-structured-output.example.json)

## Step 1 — Read the contract

Open the schema and note three things: the `required` list, the `enum` values for `severity`,
and `additionalProperties: false`. A structured output contract is a promise about **shape**,
not about truth. Valid JSON can still be wrong.

## Step 2 — Add the contract to your prompt

Append this block to the prompt you built in
[02-improved-prompt-template.md](02-improved-prompt-template.md).

```text
OUTPUT CONTRACT (STRICT)
Return exactly one JSON object and nothing else. No markdown fences, no commentary.
Fields, all required:
- ticket_id: string, matches CTG-#####, echoed from the input
- category: one of hardware_defect | sizing_fit | order_and_shipping | warranty_claim |
  usage_guidance | safety_concern | other
- product_line: one of tents | sleeping_bags | backpacks | camp_stoves | apparel |
  accessories | unknown
- severity: one of s1_safety | s2_high | s3_normal | s4_low
- safety_flag: boolean
- recommended_next_action: one of request_more_info | route_to_warranty |
  route_to_safety_review | send_self_service_guide | route_to_order_support
- missing_information: array of short strings, may be empty, at most 5 items
- confidence: number between 0 and 1
- needs_human_review: boolean
- rationale: string, at most 280 characters, grounded only in the intake message
Do not add any field that is not in this list.
```

## Step 3 — Run three synthetic messages

Run each one in a fresh chat with your prompt.

```text
Ticket CTG-10421
Hi - the pole on my tent snapped while I was putting it up last weekend and now the whole
thing sags. I bought it a while back, I think from your site. Can you help?
```

```text
Ticket CTG-10422
My camp stove flared up and I burned my hand. I put it out but the valve still hisses when
it is closed.
```

```text
Ticket CTG-10425
hey
```

## Step 4 — Check compliance by hand

For each result, tick the boxes:

- [ ] Parses as JSON with no surrounding text
- [ ] Contains all ten required fields and no extra fields
- [ ] Every enum value is spelled exactly as listed
- [ ] `confidence` is a number, not a string or a percentage
- [ ] `safety_flag` and `severity` agree with each other
- [ ] `rationale` is under 280 characters and cites only the message

## Expected output

CTG-10422 should be `s1_safety` with `safety_flag: true`, `route_to_safety_review`, and
`needs_human_review: true`. CTG-10425 should refuse to guess and ask for information. Compare
your CTG-10421 result with
[03-structured-output.example.json](03-structured-output.example.json) — your values may
reasonably differ on `confidence` and wording.

## Success criteria

- [ ] At least two of three results are schema-valid on the first try.
- [ ] You captured at least one compliance failure and the fix you would make. If all live
      runs comply, diagnose the deliberate failure fixture in
      [03-structured-output.flawed-example.md](03-structured-output.flawed-example.md).

## Checkpoint

Paste one line: `TC id | schema valid? | severity | one problem you saw`.

## Debrief prompts

1. Did "valid JSON" ever hide a wrong answer? That distinction is the whole point of
   evaluation later.
2. What would your application do when the output does not parse — retry, repair, or fail
   closed? Who decides?
3. Which enum value was most often misspelled or invented?

## Recovery and fallback

FALLBACK — If the model keeps wrapping JSON in prose or code fences:
1. Add the line `Return raw JSON only. Your entire response must start with { and end with }.`
2. If it still fails, accept the fenced output and strip the fence by hand. Note it as a real
   finding: strict formatting is a known weak point and is why applications validate output.
3. If chat is entirely unavailable, use the example file as your input for
   [Exercise 6](06-evaluation-rubric.md) and keep moving.

## Next

Continue to [Exercise 4 — Simulated tool contract](04-tool-contract.md).
