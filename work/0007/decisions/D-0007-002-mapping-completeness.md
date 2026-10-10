---
id: D-0007-002
kind: decision
title: Audit and close the complete v1 mapping operator set
status: complete
spec: SPEC-0007
requirements: [R-0007-064, R-0007-132, R-0007-334, R-0007-340, R-0007-341, R-0007-342, R-0007-343, R-0007-385, R-0007-386, R-0007-387, R-0007-388, R-0007-389, R-0007-390, R-0007-391, R-0007-392, R-0007-393, R-0007-394, R-0007-395, R-0007-396]
depends_on: [D-0007-001]
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-002: Mapping Completeness

## Objective

Audit the closed operator set against all capability-completeness dimensions in
R-0007-340 without creating duplicate work for the same gate.

## Scope and exclusions

All selected v1 mapping capabilities, including existing collection, string,
regex, object, and newly decided numeric operators. Conformance expectations
must be complete; publishing their actual artifact families remains Phase 1.

## Questions to resolve

Which operators lack any closed shape, typing, missing/null, failure, deterministic
evaluation, portable accounting, or conformance requirement? Are all cross-cutting
tables and examples mutually consistent? Does any unresolved candidate remain?

## Acceptance criteria

- [x] Audit each operator against every closure dimension in R-0007-340.
- [x] Resolve gaps in authoritative requirements, not only in this item.
- [x] Reconcile operand tables, inference, budgets, examples, and conformance groups.
- [x] Account for all selected/rejected capabilities and R-0007-343's version gate.
- [x] Traceability and relevant checks pass; record the exact outcome snapshot
  for explicit human review.

## Resolution

Resolved in
[SPEC-0007 Sections 8.5 through 8.17](../../../specs/0007-portable-pipeline-definitions-and-binding.md#85-closed-operator-set-and-operand-shapes):

- R-0007-392 through R-0007-395 close the successful-result and accounting
  semantics that the foundational constructors/selectors, state/control
  operators, scalar operators, and `map`/`filter` previously left distributed
  or implicit.
- R-0007-396 requires complete language-neutral conformance groups for those
  core operators.
- R-0007-334 now inventories the numeric, regex, object-shaping, and core
  conformance groups alongside the existing collection and string groups.
- R-0007-064, R-0007-132, and R-0007-340 identify Sections 8.5 through 8.17 as
  the complete v1 operator closure.

The audit changes no operator shape or selected/rejected capability. It does
not publish the schema or vectors; R-0007-343 continues to prohibit publication
until the required artifacts exist.

## Validation and review

Decision input: on 2026-10-09 the user accepted explicit core semantics and
conformance coverage rather than treating scattered generic clauses as
sufficient or repairing only the aggregate inventory.

Validation performed on 2026-10-09:

- Operator audit: PASS. Audited every R-0007-072 operator family against the
  R-0007-340 dimensions. Specialized collection, string, regex, object-shaping,
  and numeric groups were already closed. R-0007-392 through R-0007-396 close
  the foundational result and conformance gaps without adding or removing an
  operator or operand.
- Work-artifact structure: PASS. Checked 48 unique item identities, required
  sections by item kind, 95 dependency edges, acyclic ordering, no cancelled
  prerequisite, and one phase membership per item.
- Specification structure: PASS. All 396 R-0007 identifiers are unique; the
  five additions use the next unused sequence R-0007-392 through R-0007-396;
  no prior identifier was removed or retired.
- Specification trace check: PASS. Classified as `requirement`; nine requirement
  blocks are in scope. Repository-wide reverse-impact search found no stale
  code or test fingerprint, no changed implementation, no new waiver, and no
  semantic conflict with the closed v1 set or R-0007-343's publication gate.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  changed local links resolve, and all 11 plan source hashes match the exact
  current bytes.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot is recorded below.

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `b6a2bf61fe59f885739395c86b70dbb5243dda8267d8081a2a067f65ef816df3` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `7cc2dcd95281961244fd747f009820bd1f75ef3d3a41a7d124ed7f28ea37fa6e` |
| `work/0007/plan.md` | SHA-256 `39e3b5a7285c045b54874e3a3dfba5722ea53e0043ea33f3868fa9e2ee708184` |

Approval recorded on 2026-10-09: the user explicitly approved this exact
snapshot in this session.

Approved scope: completion of D-0007-002 and its normative mapping-completeness
outcome, including reconciliation of the 0007 plan fingerprints and downstream
readiness impact. The approved commit scope is exactly this decision,
SPEC-0007, and `work/0007/plan.md`. Exclusions: implementation, schemas,
conformance vectors, readiness approval, and publication of
`qhapaq.mapping/v1`.

The approval covers this unchanged material content with SHA-256
`b6a2bf61fe59f885739395c86b70dbb5243dda8267d8081a2a067f65ef816df3`, plus
these exact input/output snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `7cc2dcd95281961244fd747f009820bd1f75ef3d3a41a7d124ed7f28ea37fa6e` |
| `work/0007/plan.md` | `39e3b5a7285c045b54874e3a3dfba5722ea53e0043ea33f3868fa9e2ee708184` |

Completion does not publish schemas, vectors, or `qhapaq.mapping/v1`, and does
not by itself authorize implementation.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-064@b95ba5, R-0007-132@40e26a, R-0007-334@ec9a8a, R-0007-340@dfeb2c
Spec: R-0007-392@692baa, R-0007-393@792bd9, R-0007-394@3444fe, R-0007-395@2d07f8, R-0007-396@405b1b
```
