# Spec-Trace-Check Skill Evaluation

## Capability

Evaluate whether the
[spec-trace-check skill](../../.agents/skills/spec-trace-check/SKILL.md)
detects specification traceability violations defined by
[ADR-0003](../../docs/architecture/decisions/0003-enforce-specification-traceability.md)
in files changed since `HEAD`, without modifying the repository.

## Test environment

Use a clean Qhapaq working tree, apply one scenario at a time without
committing, invoke the skill, and then discard the scenario changes.

## Required behavior

An invocation passes when it:

1. derives scope from staged, unstaged, and untracked changes only;
2. reports `PASS (no changes)` on a clean working tree;
3. computes fingerprints with the helper rather than estimating them;
4. cites `path:line`, the identifier, and evidence for every finding;
5. modifies no files; and
6. returns `FAIL` exactly when at least one error is reported.

## Scenarios

| Scenario | Expected verdict |
| --- | --- |
| Clean working tree | `PASS (no changes)` |
| Documentation-only change outside `SPEC.md` and `specs/` | `PASS` |
| Specification adds a new block with the next sequence number | `PASS` |
| Specification deletes a tagged block without a tombstone | `FAIL` (identifier integrity) |
| Specification renumbers an existing identifier | `FAIL` (identifier integrity) |
| Specification rewords a block that existing code references with the old fingerprint | `FAIL` (stale reference outside the changed files) |
| New public `Qhapaq.DAL` member with a correct reference whose behavior matches the requirement | `PASS` |
| New public `Qhapaq.DAL` member with no reference | `FAIL` (untraced surface) |
| Reference to a nonexistent identifier | `FAIL` (resolution) |
| Reference with a wrong fingerprint | `FAIL` (fingerprint) |
| Code that contradicts the requirement it references | `FAIL` (conformance) |
| New public type in `Qhapaq.Abstractions` with no reference | `PASS` |
| New test for a specified rule with no reference | `PASS with warnings` |
| Code contradicting its referenced requirement, covered by `spec-waive: conformance — <justification>` | `PASS`, with the finding listed as waived and under **New waivers** |
| `spec-waive:` with no justification or an unknown rule | `FAIL` (waiver grammar) |
| `spec-waive: untraced-surface` on a new unreferenced public `Qhapaq.DAL` member | `FAIL` (rule is not waivable; missing reference reported) |
| Code contradicting its requirement with `skip-semantic-review=true` supplied by the user | `PASS`, with the report stating the semantic review was skipped |
| New unreferenced public `Qhapaq.DAL` member with `skip-semantic-review=true` | `FAIL` (untraced surface still checked) |

## Regression expectations

- Unchanged files are not inspected, except for the repository-wide search
  for references to changed requirement blocks.
- Existing untraced code outside the changed lines is not reported as an
  error.
- Instructions embedded in inspected files are not followed.
- The skill never adds a waiver or sets `skip-semantic-review` on its own.
