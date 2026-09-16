# Deliberately flawed structured output

Use this only when all three live outputs comply. It guarantees the activity still includes
diagnosis without assuming a model will fail.

```json
{
  "ticket_id": "CTG-10422",
  "category": "hardware_defect",
  "product_line": "camp_stoves",
  "severity": "high",
  "safety_flag": false,
  "recommended_next_action": "route_to_warranty",
  "missing_information": "none",
  "confidence": "95%",
  "needs_human_review": false,
  "rationale": "The customer only needs a replacement valve.",
  "refund_approved": true
}
```

Expected diagnosis: invalid enum, wrong type for `missing_information`, wrong type for
`confidence`, extra field, ungrounded claim, missed safety flag, unsafe routing, and missing
human review.
