# Exercise 1 — Starter prompt (Activity A1, minutes 14-26)

**Objective.** Diagnose why a plausible-looking prompt produces unreliable triage output, then
fix it with explicit instructions, grounding rules, and scope limits.

**Timebox.** 12 minutes inclusive: 2 minutes brief/read, 3 minutes run and diagnose, 5 minutes
rewrite and rerun, and 2 minutes checkpoint/debrief. The rewrite uses
[02-improved-prompt-template.md](02-improved-prompt-template.md).

CORE — Microsoft Copilot chat plus this file. Nothing else required.

## Step 1 — Copy the starter prompt

```text
You are a helpful support assistant for an outdoor gear company. Read the customer message
and figure out what is wrong. Give the category, how bad it is, and what we should do next.
Be accurate and helpful.
```

## Step 2 — Copy the synthetic intake message

Synthetic. This customer does not exist.

```text
Ticket CTG-10421
Hi - the pole on my tent snapped while I was putting it up last weekend and now the whole
thing sags. I bought it a while back, I think from your site. Can you help?
```

## Step 3 — Run it twice

Paste the starter prompt, then the intake message, into Microsoft Copilot chat. Run the same
pair of messages a **second** time in a new chat.

## Expected result

You should see some of these problems. Write down which ones you actually saw:

| Failure mode | What it looks like | Why it happens |
| --- | --- | --- |
| Unstable format | Run 1 returns prose, run 2 returns a bulleted list | No output contract was specified |
| Invented facts | A warranty decision, an order number, or a SKU appears | No grounding rule forbids invention |
| Vague severity | "Pretty urgent", "medium" | No defined severity scale |
| Silent guessing | Missing purchase date is never mentioned | Nothing tells the model to surface gaps |
| Over-helpful | Drafts a customer reply promising a replacement | Scope and authority were never bounded |
| Unclear next action | Two or three suggestions at once | No instruction to choose exactly one |

## Success criteria

- [ ] You ran the starter prompt at least twice.
- [ ] You named at least three concrete failure modes from your own output, or from the
      captured weak outputs in [solutions/01-improved-prompt.md](solutions/01-improved-prompt.md)
      if your live runs did not expose three.
- [ ] You can point to the **missing instruction** that caused each one.

## Checkpoint

Post in chat (virtual) or hold up a sticky note (in person): *the one failure that would
matter most in a real support queue.*

## Debrief prompts

1. Which differences between your two runs were caused by the prompt, and which by ordinary
   model variability?
2. Which failure would a customer notice? Which would only an auditor notice?
3. What is the cheapest instruction that removes the biggest failure?

## Recovery and fallback

FALLBACK — If chat is unavailable or slow:
- Use the pre-captured weak output in
  [solutions/01-improved-prompt.md](solutions/01-improved-prompt.md) (section "Captured weak
  output") and do the diagnosis on paper.
- If you are in a breakout room with no working chat, pair with someone who has one and
  narrate the diagnosis together.

## Next

Continue to [Exercise 2 — Improved prompt template](02-improved-prompt-template.md).
