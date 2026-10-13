---
id: D-0009-001
kind: decision
title: Select repository validation derived-state architecture
status: open
spec: SPEC-0009
requirements:
  - R-0009-001
  - R-0009-002
  - R-0009-003
  - R-0009-004
  - R-0009-005
  - R-0009-006
  - R-0009-007
  - R-0009-008
  - R-0009-009
  - R-0009-010
  - R-0009-011
  - R-0009-012
  - R-0009-013
  - R-0009-014
depends_on: []
artifacts:
  - docs/architecture/decisions/0006-repository-validation-derived-state.md
---

# D-0009-001: Select Repository Validation Derived-state Architecture

## Objective

Select the repository-owned tool boundary and architecture that can reuse
validated derived state while preserving authoritative-source, equivalence,
diagnostic, recovery, security, and independent-validation requirements.

## Scope and exclusions

This decision covers R-0009-001 through R-0009-014. It may select tool and
shared-library ownership, implementation technology, storage representation,
owned local location, atomicity and concurrency behavior, cache and algorithm
versioning, machine-readable results, command modes, and integration
boundaries.

It must not change requirement fingerprint meaning, SPEC-0008 checker
semantics, exact workflow hashes, approval evidence, or SPEC-0007/SPEC-0008
completion gates. It does not implement the selected architecture or approve
delivery slices.

## Questions to resolve

- Which repository-owned tool and shared libraries own parsing, fingerprinting,
  exact-byte digests, indexing, cache validation, and machine-readable output?
- Which implementation technology and package boundary preserve repository
  dependency direction?
- Where is local state stored, how is its format identified, and how is
  bounded cleanup performed?
- How do writes become atomically reusable and how do concurrent processes
  coordinate?
- Which uncached, incremental, and full-verification command modes are
  maintained?
- Which measurements and tests demonstrate reuse, equivalence, safe
  invalidation, and worthwhile performance improvement?
- Which complete input manifest and resolver versions prove runbook freshness?
- Which validation classes support receipts and which environment identities
  invalidate them?

## Acceptance criteria

- [ ] An ADR records the selected architecture and rejected alternatives.
- [ ] The design preserves every R-0009-001 through R-0009-014 trust and
  equivalence boundary.
- [ ] Dependencies remain one-way from SPEC-0009 to existing validation and
  orchestration work.
- [ ] Ownership, inputs, outputs, failure behavior, cleanup, concurrency, and
  maintenance expectations are explicit.
- [ ] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

Open.

## Validation and review

No resolution, validation evidence, or approval is recorded.
