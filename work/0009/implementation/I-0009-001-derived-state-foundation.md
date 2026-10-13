---
id: I-0009-001
kind: implementation
granularity: milestone
change_kind: requirement
title: Deliver repository validation derived-state foundation
status: open
spec: SPEC-0009
requirements:
  - R-0009-001
  - R-0009-002
  - R-0009-003
  - R-0009-004
  - R-0009-005
  - R-0009-008
  - R-0009-009
  - R-0009-010
  - R-0009-011
depends_on: [D-0009-001, I-0008-007]
artifacts: []
---

# I-0009-001: Deliver Repository Validation Derived-state Foundation

## Objective and coverage

Deliver the central exact-content index, runbook input manifest, and local
derived-state lifecycle for
incremental repository validation. Cover non-authoritative state, complete
identity, unchanged-content reuse, cached-versus-uncached equivalence,
diagnostics, invalidation, concurrent access, sensitive-content exclusions,
cleanup, and recovery.

R-0009-006 required-validation integration and R-0009-007 adoption by existing
workflow digest consumers remain incomplete until later milestones.

## Entry gates

D-0009-001 and I-0008-007 are complete. SPEC-0009 and the resulting ADR are
approved for the scope. Current implementation readiness, concrete slices, and
their exact manifests and plan approvals exist.

## File and ownership manifest

Pending the D-0009-001 architecture decision, scoped readiness, and concrete
slice planning. This milestone does not authorize implementation.

## Design and integration

Consume the deterministic checker behavior delivered by I-0008-007 rather
than redefining parsing, normalization, fingerprinting, or diagnostic rules.
Keep local state outside authoritative and portable contracts. Expose stable
machine-readable results for later workflow consumers.

## Tests and validation

Cover every case in SPEC-0009 verification expectations for exact identity,
rule-version changes, reuse, equivalence, malformed and interrupted state,
concurrency, sensitive-content exclusion, deletion, and regeneration. Record
phase measurements that distinguish derivation costs from semantic review.
Cover complete versus incomplete runbook input manifests and resolver-version
changes without trusting aggregate metadata alone.

## Exit criteria

- [ ] Complete matching entries are reused for unchanged exact content.
- [ ] Cached and uncached results are equivalent.
- [ ] Invalid and partial state cannot produce incorrect reuse or false success.
- [ ] Cleanup and recovery are bounded and preserve authoritative inputs.
- [ ] Required tests and validation pass.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition into approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
