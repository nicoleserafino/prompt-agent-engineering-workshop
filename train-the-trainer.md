# Train the trainer

How to rehearse and deliver this workshop yourself, in either modality. Read this with
[facilitator-guide.md](facilitator-guide.md) open.

## Who can facilitate this

You do not need to be a machine learning expert. You need to be able to:

- write and critique a prompt out loud,
- read a JSON schema and a diff,
- run a branch-and-pull-request flow in the GitHub web UI,
- keep a clock and protect activity time,
- say "I do not know, let us find the documentation" without discomfort.

If you have delivered this once as a participant and rehearsed once, you are ready.

## Rehearsal plan

### Rehearsal 1 — do the workshop yourself (about 90 minutes)

Work through [participant-workbook.md](participant-workbook.md) exactly as a participant would.
Actually run the prompts. Actually open a pull request in your own fork. You cannot facilitate
an exercise you have not personally completed, because half the questions are about the exact
thing that just went differently for you.

Capture as you go:
- a screenshot of the weak starter output (your FALLBACK asset),
- one schema-invalid response,
- one tool-call proposal,
- your evaluation CSV with at least one disagreement between two runs.

### Rehearsal 2 — timed dry run of Session 1 (75 minutes)

Run minutes 7-82 out loud against a clock, alone or with one colleague. Watch for:
- teaching segments running long — they always do,
- the demo at minutes 7-14 taking more than 60 seconds,
- the A4 debrief at minutes 66-76 being squeezed; it is the most important one in Session 1.

Mark your personal "cut this first" items in the guide.

### Rehearsal 3 — Session 2 mechanics (30 minutes)

Do the fork, branch, PR, review, and issue flow twice in the web UI until it is muscle memory.
Practise narrating while clicking. Have the repository, the library file, and the PR template
in separate tabs.

### Rehearsal 4 — the hard moments (20 minutes)

Say these out loud until they sound natural:
- "The model proposed a function call. Nothing was created. An application decides."
- "That JSON is valid and it is also wrong. Those are different questions."
- "Evaluation reduces risk. It never guarantees correctness and it never replaces human review."
- "That is outside what I can speak to. Let us check the official documentation together."
- "Stop sharing and recording. Please remove that content where possible; do not repeat it.
  We will follow our established incident process and will not assume retained copies are gone."

## Modality differences

| Dimension | Virtual | In person |
| --- | --- | --- |
| Energy | Drops silently; you will not see it | Visible; you can respond to the room |
| Grouping | Breakout rooms of 3-4, named reporter | Tables of 4-6, you circulate |
| Checking work | Ask for one line in chat per person | Walk past screens, glance, prompt |
| Debriefs | Call on named people, always | Open floor usually works |
| Timing | Breakout transitions cost 60-90 seconds; budget it | Transitions are faster; watch table chatter |
| Demos | Zoom the browser to 150 percent; narrate every click | Check the back row can read the screen |
| Break | Post the return clock time in chat and on screen | Post it on screen; announce it twice |
| Co-facilitator | Essential for chat monitoring | Helpful for table support |
| Recovery | Have the solutions folder open; paste text fast | Print the key solution pages |

**Virtual-specific traps.** Silent rooms; people who never open the repository; breakouts that
end with nothing produced. Counter all three with the named-reporter rule and the one-line
checkpoint format.

**In-person-specific traps.** Tables that debate architecture instead of doing the exercise;
laptops closed; one person doing all the typing. Counter by circulating constantly and asking
each table the same debrief question in advance.

## Facilitation techniques that work here

1. **Timebox out loud.** Announce the minutes, give the two-minute warning, end on time even
   mid-sentence. Predictability buys you goodwill for the hard parts.
2. **Checkpoint format.** Always ask for one structured line, never "any thoughts?" —
   `cases run | blocking failures | ship or hold` gets answers; open questions get silence.
3. **Steer, do not correct.** When someone says the prompt enforces the approval gate, say
   "that is the intuition everyone has; here is why the application has to own it."
4. **Use their output, not yours.** The best teaching moment is a participant's own invented
   warranty promise. Ask permission, then show it.
5. **Protect activities.** Cut lecture content first, always. The "cut this first" lines in the
   facilitator guide exist for exactly this.
6. **Name the trade-off.** Every improvement in this workshop costs something: tokens, latency,
   review time, false positives. Saying so builds credibility.
7. **Park cleanly.** Write off-scope questions on a visible list and return to them at minutes
   168-177 if there is room.

## Frequently asked questions

**"Which model should we use?"**
Model choice is a governed decision and it changes often. Teach the process: record the model,
re-run the evaluation set when it changes, and treat a model change as at least a MINOR version
bump. Point at current official documentation for capabilities.

**"Can we just use a bigger model instead of all this structure?"**
A stronger model raises the floor; it does not give you ownership, reviewability, regression
tests, or rollback. Those are process properties, not model properties.

**"Does temperature 0 make it deterministic?"**
Lower settings reduce variability. They do not guarantee identical output across runs, versions,
or providers. Design for variability regardless.

**"Is prompt injection solved by the untrusted-content rule?"**
No. The rule reduces a common failure. Real defenses are layered: limited tool scope, approval
gates for writes, output validation, and human review of consequential actions.

**"Can we skip evaluation if a human reviews everything?"**
Human review catches individual errors; evaluation catches systematic ones and tells you
whether a change made things better or worse. They answer different questions.

**"Do we need Microsoft Foundry for this?"**
No. It is optional throughout. It helps when you want stored evaluation runs, traces, and a
managed place for agents to run. The repository stays the source of truth either way.

**"What about cost?"**
Longer prompts, more subagents, and more evaluation runs all cost money and latency. Track cost
per task as a monitoring signal and prune rules periodically.

**"Can an assistant approve its own pull request?"**
No. A proposal is not an approval. The named human owner approves, using the same checklist.

**"How do we start on Monday with no budget?"**
One repository, one owner per prompt, PRs required, a ten-case test set, a changelog line.
That is a week of work and most of the benefit.

## Misconceptions to correct on sight

| Misconception | Correction |
| --- | --- |
| "It called the tool, so the action happened." | The model emitted a proposal. Execution and approval live in the application. |
| "Valid JSON means correct." | Shape is not truth. Evaluate separately. |
| "Different answers on the same input means it is broken." | Variability is expected. Run safety cases twice and tighten decision rules. |
| "Evaluation proves the prompt is safe." | It reduces risk on the cases you thought of. Nothing more. |
| "Agents are always better than a prompt." | A loop adds cost, latency, and failure modes. Use one when the task needs steps and tools. |
| "More subagents means better design." | Split on owner, risk, or failure mode — not tidiness. |
| "Governance slows us down." | Ownership and rollback are what let you move fast without incidents. |
| "The prompt enforces the rules." | The prompt requests. The application enforces. |
| "Prompt files are documentation." | They are configuration. Version, review, release, and roll them back. |
| "Foundry replaces the repository." | The reviewable text stays in Git; Foundry runs and measures it. |

## Adapting the material

| Constraint | Adaptation |
| --- | --- |
| 90 minutes instead of 180 | Keep A1, A2, and B1; teach evaluation and governance conceptually; drop A3 and B3 |
| 60 minutes, executive audience | Slides 1-4, 10-11, 13-15, 24-27, 31-32, 34-35, with one live demo and no activities |
| Half-day extension | Add a second evaluation round, a conflict-resolution exercise, and the optional Foundry path in full |
| Engineering-heavy audience | Add local git, schema validation in CI, and a real tool integration discussion |
| Non-technical audience | Skip the JSON internals; use the enums as a vocabulary exercise and stay on the web UI |
| Your own scenario | Replace Contoso Trail Gear with a fictional version of your own domain. Keep every field synthetic and confirm no confidential detail leaks in |
| Very large room | Add a co-facilitator per 25 participants; extend each activity by 2 minutes and cut a teaching segment to pay for it |

If you change the scenario, update the schema, the test cases, and the solutions together, then
run `python validate.py` before you deliver.

## Related

- [Facilitator guide](facilitator-guide.md)
- [Facilitator materials](facilitator-materials.md)
- [Contingency plan](contingency-plan.md)
- [Participant workbook](participant-workbook.md)
- [Slide outline](slides/slide-outline.md)
- [Resources](resources.md)
