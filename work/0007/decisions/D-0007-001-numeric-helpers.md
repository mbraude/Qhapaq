---
id: D-0007-001
kind: decision
title: Numeric helpers and array reductions
status: complete
spec: SPEC-0007
requirements: [R-0007-064, R-0007-072, R-0007-093, R-0007-097, R-0007-098, R-0007-103, R-0007-107, R-0007-108, R-0007-114, R-0007-117, R-0007-118, R-0007-129, R-0007-132, R-0007-167, R-0007-308, R-0007-340, R-0007-341, R-0007-343, R-0007-385, R-0007-386, R-0007-387, R-0007-388, R-0007-389, R-0007-390, R-0007-391]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-001: Numeric Helpers and Array Reductions

## Objective

Resolve the numeric capabilities identified by R-0007-340 and Section 8.12.

## Scope and exclusions

Decide purpose-built v1 scalar helpers and array reductions within the existing
portable numeric domain. No general reducer, interpreter, executable code, or
implicit future-version deferral. Read the existing arithmetic, inference,
evaluation, and accounting requirements before choosing semantics.

## Questions to resolve

- Which absolute, minimum, maximum, clamp, and rounding operations belong in v1?
- What are their closed operands, domain restrictions, and exact rounding modes?
- Are sum, minimum, maximum, and average reductions supported? What happens for
  empty arrays, accumulation order, intermediate rounding, and overflow?
- How do missing/null, static inference, evaluation order, failure, and resource
  accounting interact with every selected operator?

## Acceptance criteria

- [x] Record included and rejected candidates explicitly in normative requirements.
- [x] Define closed shapes, typing, missing/null, order, failures, and budgets.
- [x] Define exact numeric and rounding behavior, including reduction boundaries.
- [x] Define required language-neutral conformance cases and consistent examples.
- [x] Preserve R-0007-343 publication gates; do not publish schemas prematurely.
- [x] Traceability and relevant checks pass; record the exact outcome snapshot
  for human review.

## Resolution

Resolved in
[SPEC-0007 Section 8.12](../../../specs/0007-portable-pipeline-definitions-and-binding.md#812-closed-numeric-capabilities-and-later-version-candidates):

- R-0007-129 and R-0007-385 select and reject the v1 candidates.
- R-0007-386 through R-0007-390 define numeric, typing, state, order, failure,
  and resource semantics.
- R-0007-391 defines language-neutral conformance coverage.
- R-0007-064, R-0007-072, R-0007-093, R-0007-097, R-0007-098, R-0007-103,
  R-0007-107, R-0007-108, R-0007-114, R-0007-117, R-0007-118, R-0007-132,
  R-0007-308, R-0007-340, and R-0007-343 integrate the decision with the
  closed language, inference, failures, accounting, and publication gates.

The cross-operator audit remains
[D-0007-002](D-0007-002-mapping-completeness.md).

## Validation and review

Decision input: on 2026-10-09 the user explicitly selected the complete
purpose-built set, distinct scalar/reduction shapes, integral-only fixed
rounding modes, source-order reductions with empty sum zero, static plus
runtime clamp-bound validation, and one examination plus one collection visit
per reduction item.

Validation performed on 2026-10-09:

- Work-artifact structure: PASS. Checked 48 unique item identities, requirement
  references, one phase membership per item, 95 dependency edges, acyclic
  ordering, no cancelled prerequisite, repository-relative links, and all 11
  exact source hashes.
- Specification structure: PASS. All 391 R-0007 identifiers are unique; the
  seven additions use the next unused sequence R-0007-385 through R-0007-391;
  no prior identifier was removed or retired.
- Specification trace check: PASS. Classified as `requirement`; 23 requirement
  blocks are in scope. Repository-wide reverse-impact search found no stale
  implementation or test fingerprint, no changed code, no new waiver, and no
  semantic conflict with R-0007-108, R-0007-167, R-0007-340, R-0007-341, or
  R-0007-343.
- Documentation checks: PASS. `git diff --check` reported no whitespace error;
  changed local links resolve; source snapshots match exact current bytes.
- Follow-up plan fingerprint reconciliation: refreshed the six historical
  requirement references in `work/0007/plan.md` to match the current SPEC-0007
  blocks, then reran repository-wide stale-fingerprint checks with no remaining
  matches. The exact resulting plan hash is recorded below.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `4d4d42dc36b59055d15e47c4ab9e61a4354ef458075202ef125ac84a603de051` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `89cd50096b1cac49160fd67dbc97aad10207a11b1f950ddbbbbec6e9da86cadf` |
| `work/0007/plan.md` | SHA-256 `a056f7261c23c2134f55b27ce5b85d49e278a0241bf2854d3d1bb5916b7e9395` |
| `work/0007/decisions/D-0007-002-mapping-completeness.md` | SHA-256 `0fbc52dfb5130b903cad4ba858726f3a82e41ddca5ea2b4aabc9cbbae126bb8c` |

Approval recorded on 2026-10-09: the user explicitly approved this exact
snapshot in this session.

Approved scope: completion of D-0007-001 and its numeric-helper specification
outcome, including reconciliation of the related plan fingerprints and
D-0007-002 references. The approved commit scope is exactly this decision,
SPEC-0007, `work/0007/plan.md`, and D-0007-002. Exclusions: implementation,
schemas, vectors, and publication of `qhapaq.mapping/v1`.

The approval covers the unchanged material content with SHA-256
`4d4d42dc36b59055d15e47c4ab9e61a4354ef458075202ef125ac84a603de051`, plus
these exact input/output snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `89cd50096b1cac49160fd67dbc97aad10207a11b1f950ddbbbbec6e9da86cadf` |
| `work/0007/plan.md` | `a056f7261c23c2134f55b27ce5b85d49e278a0241bf2854d3d1bb5916b7e9395` |
| `work/0007/decisions/D-0007-002-mapping-completeness.md` | `0fbc52dfb5130b903cad4ba858726f3a82e41ddca5ea2b4aabc9cbbae126bb8c` |

Completion does not publish schemas, vectors, or `qhapaq.mapping/v1`.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-064@11dacd, R-0007-072@e1cc74, R-0007-093@02bc90, R-0007-097@d13124, R-0007-098@03c461, R-0007-103@2b6481
Spec: R-0007-107@e81b13, R-0007-108@793d67, R-0007-114@e2771f, R-0007-117@f525c4, R-0007-118@9f010e, R-0007-129@8f3c40
Spec: R-0007-385@71ddfa, R-0007-386@b4cb20, R-0007-387@33b7cc, R-0007-388@154590, R-0007-389@5cd51f, R-0007-390@218d68
Spec: R-0007-391@549f8b, R-0007-132@b393aa, R-0007-308@ca69b1, R-0007-340@461e39, R-0007-343@028495
```
