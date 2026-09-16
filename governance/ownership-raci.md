# Ownership and RACI

Who is accountable for what in a multi-author prompt and agent library. The role names match
the placeholder teams in [CODEOWNERS.sample](CODEOWNERS.sample) — replace
`@your-org/*` with real teams before adopting this in your organization.

## Roles

| Role | Placeholder team | Owns |
| --- | --- | --- |
| Prompt owner | `@your-org/prompt-owners` | Prompt wording, decision rules, prompt versions |
| Agent owner | `@your-org/agent-owners` | Agent definitions, tool exposure, subagent contracts, model choice |
| Quality owner | `@your-org/quality-owners` | Test set, rubric, evaluation runs, regression policy |
| Governance owner | `@your-org/governance-owners` | Policy, approval gates, safety rules, release gates |
| Workshop maintainer | `@your-org/workshop-maintainers` | Delivery content: guide, workbook, slides |
| Operator on call | rotation | Monitoring, incident response, rollback execution |

## RACI by change type

R = responsible (does the work), A = accountable (single owner of the decision),
C = consulted, I = informed.

| Change | Prompt owner | Agent owner | Quality owner | Governance owner | Operator |
| --- | --- | --- | --- | --- | --- |
| Prompt wording, no rule change | R/A | I | C | I | I |
| New or changed decision rule | R | C | C | A | I |
| Safety rule or escalation change | R | C | C | A | I |
| Output schema or enum change | C | R/A | C | C | I |
| Tool added, removed, or scope changed | C | R/A | I | C | I |
| Write action or approval boundary change | I | R | I | A | C |
| Subagent added or responsibility moved | C | R/A | C | I | I |
| Model selection change | C | R | R | A | I |
| Test case added or expectation changed | C | I | R/A | C | I |
| Release of a new version | C | C | R | A | I |
| Emergency rollback | I | C | I | A | R |
| Workshop delivery content | I | I | I | C | I |

## Standing rules

1. **One accountable owner per decision.** If two people think they are accountable, nobody is.
2. **Safety rules are governance-owned.** A prompt author may propose, but governance approves.
3. **Model choice is a governed configuration**, not a detail buried in a prompt edit.
4. **Assistant-drafted changes follow the identical path.** Disclosure is required; the
   approval boundary does not move.
5. **Evaluation evidence informs the accountable owner. It does not replace them.**
6. **Rollback authority sits with the operator on call** and needs no committee.

## Minimum viable governance (start here)

If your team has none of this today, adopt in this order:

1. A single repository as the source of truth for prompts and agent definitions.
2. One named owner per prompt, recorded in the file itself.
3. Pull requests required; no direct pushes to the default branch.
4. A ten-case test set and a two-run rule for anything safety-relevant.
5. A one-line changelog per release and a rollback target.

Everything else is refinement.

## Related

- [PR checklist](pr-checklist.md)
- [Versioning, release, rollback](versioning-release-rollback.md)
- [Monitoring to issue workflow](monitoring-to-issue.md)
- [Shared library](../library/README.md)
