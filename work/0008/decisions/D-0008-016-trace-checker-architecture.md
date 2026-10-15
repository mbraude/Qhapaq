---
id: D-0008-016
kind: decision
title: Select deterministic trace-checker architecture and ownership
status: complete
spec: SPEC-0008
requirements:
  - R-0008-016
  - R-0008-017
  - R-0008-018
  - R-0008-021
depends_on: [D-0008-008, D-0008-011, D-0008-014, I-0008-001]
artifacts:
  - docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md
---

# D-0008-016: Select Deterministic Trace-checker Architecture and Ownership

## Objective

Select the host, implementation technology and language, package boundary,
ownership, and dependency/toolchain expectations for the deterministic
multi-language trace checker before I-0008-007 is decomposed into executable
slices.

## Scope and exclusions

R-0008-016 through R-0008-018 govern the portable marker and waiver payloads,
language-aware extractor boundary, shared rules engine, diagnostics,
fingerprints, reverse-impact checks, and waiver limits. R-0008-021 requires
the checker to remain a non-bypassable validation group while leaving root
orchestration to I-0008-009.

This decision selects an implementation architecture for those existing
requirements. It does not change traceability behavior, implement the checker,
register an extractor, define root CI orchestration, publish a contract, or
claim language support.

## Questions to resolve

- Is the checker owned by a repository-standard-library script, a
  workspace-native tool, or another package/tool boundary?
- Which implementation language and host own the shared rules engine and the
  first registered extractor?
- Which parser and package dependencies are permitted, and which workspace or
  root commands build and test the tool?
- Where do extractor registration, policy-match evidence, fixtures, and
  stable diagnostic contracts reside?
- What dependency direction keeps language syntax parsing in extractors,
  portable validation in one shared engine, and root orchestration outside
  I-0008-007?

## Acceptance criteria

- [x] An ADR records the selected host, implementation language, package
  boundary, ownership, dependencies, and rejected alternatives.
- [x] The architecture preserves the extractor/shared-engine boundary and
  traceability-support condition in R-0008-016 through R-0008-018.
- [x] The checker remains a required validation group while root impact
  selection and CI orchestration remain owned by I-0008-009.
- [x] The decision identifies the Python and .NET workspace paths, shared
  workflow-helper location, generic build/dispatch behavior, output location,
  and documented command that I-0008-007 may plan without implementing them.
- [x] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

The previous review snapshot is superseded by a requested revision.
The revised proposal in
[ADR-0006](../../../docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md)
uses the repository's `dotnet` workspace convention for the native Roslyn C#
extractor, with `src/` and `tests/` beneath its workspace. The shared Python
rules engine is in a sibling tool workspace under `src/tools/`; its code and
tests use the same workspace structure. A generic common helper under
`.agents/scripts/` builds and dispatches the language-native extractor for the
language being checked, validates its versioned JSON CLI contract, and passes
normalized facts to the Python engine. Workspace build outputs are kept in
ignored `bin/` directories. The Python engine alone owns portable semantic
checks. One documented deterministic command is invoked by the traceability
skill and CI; I-0008-009 retains ownership of root adapters, impact selection,
and required CI integration.

The decision does not change the behavior in R-0008-016 through R-0008-018,
register an extractor, establish language support, or authorize implementation.
I-0008-007 remains blocked from concrete slice planning until this decision is
approved and implementation readiness is reassessed.

## Validation and review

### Initial proposal validation (superseded)

Validated 2026-10-15:

- Confirmed SPEC-0008 R-0008-016 through R-0008-018 and R-0008-021 already
  define the portable checker behavior and required validation boundary; no
  product requirement or fingerprint changed.
- `python .agents/scripts/plan_reconciliations.py check work/0008/plan.md`:
  PASS (one plan; reconciliation indexes and records valid).
- `spec-trace-check`: PASS; classified as `maintenance`, no `Spec:` trailer.
  The change is documentation and work-item evidence only.
- `git diff --check`: PASS. Git reported only the existing CRLF-to-LF
  normalization warning for this work-item file.
- No build or unit tests were run because the change adds documentation and
  workflow evidence only; it changes no build inputs or implementation.
- Reconciliation is recorded in
  [the SPEC-0008 reconciliation record](../reconciliations/2026-10-15-d-0008-016-trace-checker-architecture.md).

The validation above covered the initial proposal only. Its exact input and
output hashes are retained in the linked reconciliation record as history, not
as the current review target.

Branch: `master`; review base at that time:
`bc64ea0128052fce377772dce87ca0d961a56c2b`. Approval was absent.

### Revised proposal validation and review

The latest requested clarification moves language selection and extractor
invocation into the generic helper, which then feeds the shared engine. The
preceding proposal's validation history is preserved in the reconciliation
record.

- Confirmed SPEC-0008 R-0008-016 through R-0008-018 and R-0008-021 still govern
  the portable checker behavior, shared semantic engine, and required
  validation boundary. No requirement or fingerprint changed.
- Confirmed the tool workspace paths follow SPEC-0008 R-0008-002 and R-0008-019,
  with the common Python workflow helper remaining under `.agents/scripts/`.
- `python .agents/scripts/trace_facts.py`: PASS; classified as `maintenance`,
  no `Spec:` trailer. All changed files are documentation and work evidence.
- `python .agents/scripts/plan_reconciliations.py check work/0008/plan.md`:
  PASS (one plan; reconciliation indexes and records valid).
- `python .agents/scripts/work_hashes.py verify` for the plan and revised
  reconciliation: all recorded sources current.
- `git diff --check`: PASS, with only the recorded CRLF normalization warning
  for this work-item file.
- No build or unit tests were run because the revision changes only
  architecture and workflow documentation.
- Exact inputs and latest ADR output hash are recorded in
  [the revised reconciliation record](../reconciliations/2026-10-14-d-0008-016-trace-checker-architecture-revision.md).

Review base: `bc64ea0128052fce377772dce87ca0d961a56c2b` on branch `master`.
The latest ADR output SHA-256 is
`759dc91c963cfdba47901afdcd0113d5f42e259c0533c63d9d24eb649da184a0`.

### Approval record

Explicit approval was given in this session on 2026-10-15 for the exact
architecture proposal and snapshot below.

Scope: select the trace-checker architecture and ownership, including the
Python and .NET workspace layouts, generic build/dispatch helper, versioned
JSON CLI contract, and ignored build-output locations.

Exclusions: implementation, extractor registration, root CI orchestration,
contract publication, staging, committing, and pushing.

Approved material SHA-256: `588d2f53c633f32f16d6b8d6f5bdb18f51cc6817b771da51901d17f8bdda7846` (`work/0008/decisions/D-0008-016-trace-checker-architecture.md`).

| Path | SHA-256 |
| --- | --- |
| `docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md` | `759dc91c963cfdba47901afdcd0113d5f42e259c0533c63d9d24eb649da184a0` |
