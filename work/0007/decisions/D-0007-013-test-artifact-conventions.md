---
id: D-0007-013
kind: decision
title: Conformance loading, golden files and consumer test conventions
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0007-347, R-0006-031, R-0001-072]
depends_on: []
artifacts:
  - docs/development/coding-conventions.md
  - docs/development/conventions/dotnet.md
  - implementations/dotnet/tests/README.md
---

# D-0007-013: Test Artifact Conventions

## Objective

Define .NET test consumption conventions without duplicating portable cases.

## Scope and exclusions

Vector loading, golden-file regeneration/maintenance, and clean package-consumer
tests. Portable vector envelope semantics are D-0007-015, not host-specific policy.

## Questions to resolve

How are shared vectors located and selected deterministically? How are golden
changes reviewed/regenerated? What makes a consumer test independent of internals?

## Acceptance criteria

- [x] Persistent loading and golden-file procedures identify authoritative inputs.
- [x] Tests report exact artifact versions/capabilities without duplicated cases.
- [x] Clean consumer boundaries and architecture-test implications are explicit.
- [x] Coordinate portable conventions with D-0007-015; checks and review pass.

## Resolution

Resolved under [R-0007-346](../../../specs/0007-portable-pipeline-definitions-and-binding.md#net-organization-and-portable-validation),
[R-0007-347](../../../specs/0007-portable-pipeline-definitions-and-binding.md#20-testing-and-conformance),
[R-0006-031](../../../specs/0006-dotnet-layered-architecture.md#11-enforcement-and-testing),
and [R-0001-072](../../../specs/0001-core-pipeline-model.md#16-compatibility-conformance-and-versioning).
The .NET test harness consumes canonical vectors copied from `conformance/`
into test output, selects exact suite versions and capability groups, and
reports what it exercised. Canonical vector envelopes own expected results;
ordinary runs remain read-only, and offline regeneration produces reviewable
proposals rather than rewriting the source tree. Clean consumer tests use
temporary packed public packages and an external-style project; architecture
tests separately enforce internal boundaries. Portable envelope semantics
remain owned by D-0007-015.

## Validation and review

Validation performed on 2026-10-11:

- Acceptance review: R-0007-346, R-0007-347, R-0006-031, and R-0001-072 are
  reflected in the .NET conventions without changing portable envelope
  semantics or duplicating vector cases.
- Coordination: D-0007-015 remains the owner of the portable envelope and
  expected-result semantics; its accepted outcome is unchanged.
- Documentation link and anchor checks passed; all plan source hashes match
  current bytes; work-item IDs and dependencies have no duplicates, missing
  prerequisites, or cycles; `git diff --check` passed.
- Specification trace check: PASS. Changed files are documentation and work
  planning only; no product requirements or code changed.
- No build or unit tests were run. The change documents conventions and does
  not implement test tooling, vectors, or package-consumer tests.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `cd990b7b397561320fe84cf68b40df29837452683eec4863855ec098162d55ba` |
| `AGENTS.md` | SHA-256 `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `specs/0001-core-pipeline-model.md` | SHA-256 `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `specs/0006-dotnet-layered-architecture.md` | SHA-256 `c044679c4ca4255c75c835cadee8a194685a1206d11ff1aace8167d01db0a65d` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `conformance/README.md` | SHA-256 `0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307` |
| `docs/development/coding-conventions.md` | SHA-256 `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/conventions/documentation.md` | SHA-256 `ee1ab8d0f2237adb5a1fd986ce5c925eb1b0d6bafa51bd5c700bfd3436e7f657` |
| `docs/development/conventions/dotnet.md` | SHA-256 `72ac12a7ae56110729d011ecffe0c551961811dde30462ab2568647ccd6702f1` |
| `docs/development/spec-driven-workflow.md` | SHA-256 `c1045d2891c7ccbe00c833e247d7254c7e4161857dfe6884b47a644cb3e1c11e` |
| `implementations/dotnet/tests/README.md` | SHA-256 `bee794379cdc825498ef09d46758ce733d3b495622f15d2438e56c989db0fb3a` |
| `work/0007/plan.md` | SHA-256 `9fcee23e6ad027d5cb8f1b898c4524c6f6de104ff76a61133f96731f5fe2561a` |
| `work/0007/decisions/D-0007-015-conformance-envelope.md` | SHA-256 `29259afce7c83d3358094baff874adcef2f755aa2701dc4e81889b089af801a5` |

Approval recorded on 2026-10-11: the user explicitly approved this exact
snapshot in this session.

Approved scope: complete D-0007-013 and include exactly the five changed files
listed in the approved worktree scope for the .NET vector-loading, golden
maintenance, and clean package-consumer conventions. Exclusions: implementation
code, test tooling, vectors, package-consumer tests, readiness approval,
component-contract publication, and Git delivery.

No readiness, implementation eligibility, or component-contract publication
is inferred. Git delivery remains separate.
