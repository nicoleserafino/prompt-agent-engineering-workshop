# Change log: Contoso Trail Gear triage prompt and agent

All entries are fictional workshop examples. Format: version, date, change, evidence, approver role.

The versioning, release, and rollback rules are in
[../governance/versioning-release-rollback.md](../governance/versioning-release-rollback.md).

## [1.2.0] - 2026-09-10

- Added an explicit severity ladder with stop-at-first-match ordering.
- Added an untrusted-content rule so instructions inside an intake message are reported, not followed.
- Evidence: 10/10 schema validity, 3/3 safety cases passed on two consecutive runs, no regressions
  against the 1.1.0 results.
- Approved by: prompt owner + governance reviewer.

## [1.1.0] - 2026-08-27

- Added `missing_information` and `needs_human_review` to the output contract so the agent asks
  instead of guessing.
- Evidence: 10/10 schema validity; TC-05 (degenerate input) moved from fail to pass.
- Approved by: prompt owner.

## [1.0.0] - 2026-08-12

- First released version of the triage prompt with a fixed JSON output contract.
- Evidence: 8/10 test cases passing; known gaps logged as issues for 1.1.0.
- Approved by: prompt owner.

## Unreleased

- Candidate change from Activity B3: sharpen the distinction between `hardware_defect` and
  `safety_concern` when a structural failure happens under load (see TC-07).
