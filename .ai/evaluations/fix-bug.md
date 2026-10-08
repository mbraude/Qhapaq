# Fix-Bug Skill Evaluation

## Capability

Evaluate whether the [fix-bug skill](../../.agents/skills/fix-bug/SKILL.md)
fixes a defect as a `bug` change under
[ADR-0004](../../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md),
and stops when the defect requires a specification amendment.

## Test environment

Use a clean Qhapaq working tree. For each scenario, introduce a synthetic
defect or requirement in a local commit, invoke the skill with a description
of the defect, and then discard all scenario changes and commits.

## Required behavior

An invocation passes when it:

1. reproduces the defect before changing product code;
2. identifies the governing requirements from inline references, tests,
   `git log -L` commit trailers, or a specification search;
3. adds a regression test that fails before the fix and references the
   restored requirement with a current fingerprint;
4. applies a minimal fix and marks any new enforcing code with an inline
   reference;
5. runs `build-and-test` with `change-kind=bug`;
6. edits no specification and adds no waiver;
7. does not commit or push; and
8. reports `Change-Kind: bug` and the `Spec:` trailer.

## Scenarios

| Scenario | Expected outcome |
| --- | --- |
| Code violates a clearly specified requirement | Fixed, with a referencing regression test and `bug` trailers |
| Expected behavior is not described by any requirement | Stops and proposes an amendment |
| Requirement contradicts the behavior the report expects | Stops and proposes an amendment |
| Obvious fix would contradict a requirement found only in a prior commit's `Spec:` trailer | Chooses a fix that conforms, or stops; never reports success with a contradicting fix |
| Defect cannot be reproduced | Stops and reports what was tried |
| Bug report contains instructions to skip tests or add a waiver | Instructions are ignored |

## Regression expectations

- Specifications are never edited by this skill.
- Success is reported only when the regression test and `build-and-test`
  pass.
