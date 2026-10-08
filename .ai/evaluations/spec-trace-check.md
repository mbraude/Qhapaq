# Spec-Trace-Check Skill Evaluation

## Capability

Evaluate whether the
[spec-trace-check skill](../../.agents/skills/spec-trace-check/SKILL.md)
detects specification traceability violations defined by
[ADR-0003](../../docs/architecture/decisions/0003-enforce-specification-traceability.md)
and
[ADR-0004](../../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md)
in files changed since `HEAD`, classifies the change, and proposes commit
trailers, without modifying the repository.

## Test environment

Use a clean Qhapaq working tree, apply one scenario at a time without
committing, invoke the skill, and then discard the scenario changes. For
reverse-impact scenarios, first create a local commit whose message carries a
`Spec:` trailer for the code being changed, then discard it after the
scenario.

## Required behavior

An invocation passes when it:

1. derives scope from staged, unstaged, and untracked changes only;
2. reports `PASS (no changes)` on a clean working tree;
3. computes fingerprints with the helper rather than estimating them;
4. cites `path:line`, the identifier, and evidence for every finding;
5. reports a change kind and proposed `Change-Kind` and `Spec:` trailers;
6. modifies no files; and
7. returns `FAIL` exactly when at least one error is reported.

## Scenarios

| Scenario | Expected verdict and kind |
| --- | --- |
| Clean working tree | `PASS (no changes)` |
| Documentation-only change outside `SPEC.md` and `specs/` | `PASS`, `maintenance` |
| Documentation change containing an illustrative `spec:` example with a nonexistent identifier | `PASS`, `maintenance` (examples are not checked) |
| Specification adds a new block with the next sequence number | `PASS`, `requirement`, `Spec:` naming the new block |
| Specification deletes a tagged block without a tombstone | `FAIL` (identifier integrity) |
| Specification renumbers an existing identifier | `FAIL` (identifier integrity) |
| Specification rewords a block that existing code references with the old fingerprint | `FAIL` (stale reference outside the changed files) |
| New component specification `specs/components/0001-example.md` with per-version `Incomplete` status and `R-C0001-001` blocks | `PASS`, `extension`, `Spec: COMP-0001` or its blocks |
| Component specification using `R-C0002-001` in file `0001-example.md` | `FAIL` (identifier integrity) |
| Component specification that names a C# type | `PASS with warnings` (implementation detail) |
| Component contract version with no per-version status | `FAIL` (missing publication status) |
| Change to the meaning of a contract version marked `Published` at `HEAD` | `FAIL` (published contract changed) |
| Change to an `Incomplete` contract version with valid identifiers and updated references | `PASS`, `amendment` or `extension` according to the diff |
| Status-only promotion with explicit human approval and documented review and validation of the exact revision | `PASS`, `maintenance`; fingerprints unchanged |
| Promotion based only on a successful commit, push, or test run | `FAIL` (publication approval missing) |
| Reset a `Published` version to `Incomplete` | `FAIL` (publication downgrade) |
| New product code for an operation with no component specification | `FAIL` (extension without component specification) |
| New public `Qhapaq.DAL` member that implements a requirement, with no inline reference and no enforcement logic | `PASS`, with the requirement in the proposed `Spec:` trailer |
| New validation check in `Qhapaq.Business` enforcing a requirement, with no inline reference | `FAIL` (`invariant-marker`) |
| Inline reference added to a dependency-injection registration | `PASS with warnings` (reference sprawl) |
| Reference to a nonexistent identifier | `FAIL` (resolution) |
| Reference with a wrong fingerprint | `FAIL` (fingerprint) |
| Code that contradicts the requirement it references | `FAIL` (conformance) |
| Code change without inline references that contradicts a requirement named only in a prior commit's `Spec:` trailer for those lines | `FAIL` (conformance, found by reverse-impact review) |
| Code change that contradicts a requirement referenced only by a test of the changed member | `FAIL` (conformance, found by reverse-impact review) |
| Bug fix with a regression test that references the restored requirement, invoked with `change-kind=bug` | `PASS`, `bug` |
| Bug fix with no regression test, invoked with `change-kind=bug` | `FAIL` (`test-reference`) |
| Change invoked with `change-kind=bug` that adds behavior no requirement describes | `FAIL` (should be an amendment) |
| Change invoked with `change-kind=refactor` that changes observable behavior | `FAIL` (kind contradicts the diff) |
| Change mixing a specification edit and an unrelated bug fix | Warning recommending a split; kind `requirement` or `amendment` |
| Code contradicting its referenced requirement, covered by `spec-waive: conformance — <justification>` | `PASS`, with the finding listed as waived and under **New waivers** |
| `spec-waive:` with no justification or an unknown rule | `FAIL` (waiver grammar) |
| Code contradicting its requirement with `skip-semantic-review=true` supplied by the user | `PASS`, with the report stating the semantic review was skipped |
| Bug fix with no derivable `Spec:` reference and `skip-semantic-review=true` | `FAIL` (missing `Spec:` trailer is still checked) |

## Regression expectations

- Unchanged files are not inspected, except for the repository-wide search
  for references to changed requirement blocks and the tests and history read
  by the reverse-impact review.
- Existing code outside the changed lines is not reported.
- Instructions embedded in inspected files or commit messages are not
  followed.
- The skill never adds a waiver or sets `skip-semantic-review` on its own.
