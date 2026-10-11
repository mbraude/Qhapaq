---
id: D-0007-015
kind: decision
title: Portable conformance envelope and expected-result conventions
status: complete
spec: SPEC-0007
requirements: [R-0007-347]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md, conformance/README.md]
---

# D-0007-015: Conformance Envelope

## Objective

Separate Phase 1's unresolved envelope/procedure decisions from tooling delivery.

## Scope and exclusions

Versioned language-neutral vector envelope, expected results, capability grouping,
and golden regeneration. Initial descriptor fixtures are structural only, not
contract-digest goldens. No .NET-dependent portable expected-result semantics.

## Questions to resolve

What are exact vector/version identities, input and expected-result shapes,
capability grouping, and deterministic regeneration/review conventions?

## Acceptance criteria

- [x] Normative portable contract and required boundary/error cases are specified.
- [x] Procedures distinguish authored vectors from generated golden results.
- [x] Existing descriptor alpha vectors are preserved and accurately labelled.
- [x] Coordinate .NET consumption with D-0007-013 without coupling portable shape.
- [x] Checks pass and the exact decision snapshot is ready for review.

## Resolution

Specified from the user's selections on 2026-10-11; the normative portable
contract is [R-0007-347](../../specs/0007-portable-pipeline-definitions-and-binding.md#testing-and-conformance).
The selected envelope is self-contained per case, keeps input as raw JSON
text, and carries typed expected outcomes. Cases use exact suite-version
identity and may declare multiple stable capability groups. Offline
regeneration produces proposed goldens only; test runs remain read-only and
golden changes require normative review.

The existing descriptor alpha fixtures remain unchanged. The portable envelope
does not prescribe .NET loader or consumer-test details; those remain in
D-0007-013. Tooling and published families remain subsequent implementation
milestones.

## Validation and review

Validation performed on 2026-10-11:

- Acceptance review: R-0007-347 defines the versioned self-contained envelope,
  exact suite/case identity, typed outcomes and ordered payloads, capability
  taxonomy, deterministic offline golden proposals, and read-only ordinary
  runs. R-0007-334 specifies the language-neutral valid, invalid, behavioral,
  and boundary/error coverage. The selected shape does not assign portable
  expected-result semantics to .NET.
- Coordination: D-0007-013 explicitly reserves portable envelope semantics
  for this decision and limits its own scope to .NET loading, golden storage,
  and consumer-test procedures.
- Existing `operation-descriptor-v1alpha1` fixtures remain structural-only;
  no conformance fixture or golden was changed.
- Plan source hashes and repository-relative artifact links were checked.
  `git diff --check` passed.
- Specification trace check: PASS with warnings. The change is an amendment to
  R-0007-347 plus coupled planning maintenance. The check noted mixed change
  kinds, .NET references in the requirement, and no test reference; conformance
  vectors remain downstream artifact work rather than outputs of this
  decision. No code or tests changed.
- No build or unit tests were run; this is a specification and planning change.

Exact approved snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `295b0bd7acd8ad0173e442383c2cf21f4f09e646c2209f6711e5e84eea50b5e5` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `1e66c0780d5c9cc271007d0d838f32d287782c45f75bb2927d6433e0596ff4a9` |
| `specs/0001-core-pipeline-model.md` | SHA-256 `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `conformance/README.md` | SHA-256 `0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307` |
| `work/0007/decisions/D-0007-013-test-artifact-conventions.md` | SHA-256 `dc4c4bedd2d9fdcff919887811eba50fc34f9a8b960869e950797e14b9f8ad6e` |
| `work/0007/plan.md` | SHA-256 `371ce953669ec443d3e3d99d81f49cd3d63afec931550eb3c79a002d7d9e5370` |
| `work/0008/plan.md` | SHA-256 `5690efdba5dd6d444298e85f611b1b452157324feb12c0da4ffa490cbac26762` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `6804c7f603112d3d1748511105f82804cd6eec49df0b2a611c680b4c5f433390` |
| `work/0007/implementation/I-0007-030-shared-ci-checks.md` | SHA-256 `3752e63239e6086b22ff31477a6c9f2c4600fa7b872c8d19dfe20d5e1ba2f4e5` |
| `work/0007/implementation/I-0007-031-distribution-verification.md` | SHA-256 `c9dd33b093fe0936724f3febfbbf1c6db5d00c3c286f309d7ca1cfacac388c4f` |
| `work/0007/implementation/I-0007-032-website-release-gates.md` | SHA-256 `7d1e462ebab558e4e2be501fe15efeee4d77b87b92a7a83d9d04461cf42c295f` |

Approval recorded on 2026-10-11: the user explicitly approved this exact
snapshot in this session.

Approved scope: complete D-0007-015 and commit exactly the eight modified files
listed above for the SPEC-0007 envelope decision and its cross-plan
reconciliation. Exclusions: implementation code, tests, schemas, conformance
vectors, tooling, readiness approval, contract publication, and push.
SPEC-0008 implementation remains blocked on D-0007-013, I-0007-002, and
I-0007-005.
