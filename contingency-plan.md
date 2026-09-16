# Contingency plan

One page. Keep it open on a second screen during delivery.

## Decision rule

**Protect activity time and protect the break.** Cut teaching content, never exercises. Any
single failure below has a path that still meets the learning objectives.

## Outage and access matrix

| Problem | Detect | Immediate response | Objective still met? |
| --- | --- | --- | --- |
| Microsoft Copilot chat is down or very slow | Two people report it in the first activity | Switch the room to the captured outputs in [exercises/solutions/](exercises/solutions/); analyse instead of generate | Yes — diagnosis and decision-making are the objectives |
| A few people have no chat access | Setup check at minutes 0-7 | Pair them immediately; one drives, one records | Yes |
| GitHub is unreachable | Multiple failures at the start of Session 2 | Draft mode: hand-written diffs and PR bodies in the workbook; pair review verbally | Yes — the review conversation is the lesson |
| Forking is blocked by policy | People report a permission error in B1 | Draft mode, or one person shares a screen and the table reviews one PR together | Yes |
| Nobody has Microsoft Foundry | Show of hands at minutes 60-66 | Run the no-access simulation in [optional/foundry.md](optional/foundry.md) | Yes — it is a first-class path |
| Nobody has GitHub Copilot | Show of hands in Session 2 | Run the CORE manual path; narrate the optional path in two minutes | Yes |
| Meeting platform fails (virtual) | You lose audio or the room drops | Post the backup link in the calendar invite chat; resume from the last checkpoint; extend nothing — cut a teaching segment | Yes |
| Projector or screen fails (in person) | Obvious | Participants follow the workbook on their own screens; facilitate verbally from the guide | Yes |
| Breakout rooms fail (virtual) | Rooms will not open | Run activities in the main room with named pairs reporting in chat | Yes |
| Room is silent, nothing is produced | No checkpoint lines appear | Switch to named questions and the one-line checkpoint format; shorten the next activity brief | Yes |
| You are 5+ minutes behind | Clock check at minutes 43 and 130 | Cut the named teaching points in S1.3 and S2.4; use the pre-captured A3/A4 assets; never shorten an activity boundary or the break | Yes |
| You are 5+ minutes ahead | Clock check at minutes 66 and 149 | Add test cases in A4; add a second review round in B2; extend the discussion at minutes 168-177 | Yes |
| A participant pastes real customer or confidential data | You see it in chat or on a screen | Stop further sharing and recording, do not repeat the content, ask the participant to remove it where possible, and follow your organization's established incident process. Do not promise deletion removed retained copies. | Pause until contained |
| A participant asks for confidential internal detail | Question during discussion | Answer from public documentation only; park anything else | Yes |
| Co-facilitator unavailable | Before start | Prioritize: timer, then chat monitoring, then circulating; accept fewer debrief voices | Yes |

## Pre-staged assets to have open before minute 0

- [participant-workbook.md](participant-workbook.md) and [facilitator-guide.md](facilitator-guide.md)
- [exercises/solutions/](exercises/solutions/) — the entire folder
- A screenshot of the weak starter prompt output from your own rehearsal
- The chat messages you will paste: repository link, activity briefs, break return time
- A timer that everyone can see

## Minimum viable workshop

If everything fails except a screen and your voice, this still works:

1. Minutes 7-26: walk the weak prompt and the rewrite from
   [exercises/solutions/01-improved-prompt.md](exercises/solutions/01-improved-prompt.md); the
   room critiques out loud.
2. Minutes 26-43: walk the schema; the room predicts which fields the model will get wrong.
3. Minutes 43-60: walk the tool contract and the subagent contracts; the room decides which
   actions need human approval.
4. Minutes 66-76: score the captured results in
   [exercises/solutions/06-eval-results.reference.csv](exercises/solutions/06-eval-results.reference.csv)
   as a group and make the ship or hold call.
5. Minutes 102-168: walk the reference pull request and issue in
   [exercises/solutions/07-lifecycle-change-solution.md](exercises/solutions/07-lifecycle-change-solution.md)
   against [governance/pr-checklist.md](governance/pr-checklist.md).
6. Minutes 168-180: discussion, commitments, close.

Participants leave with the same templates, the same vocabulary, and the same decisions
practised.

## Related

- [Facilitator guide](facilitator-guide.md)
- [Facilitator materials](facilitator-materials.md)
- [Participant preflight](participant-preflight.md)
