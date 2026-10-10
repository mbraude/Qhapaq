---
id: D-0008-007
kind: decision
title: Define sufficient conformance evidence
status: open
spec: SPEC-0008
requirements: [R-0000-007, R-0000-009]
depends_on: [D-0008-004, D-0008-005]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-007: Define Sufficient Conformance Evidence

## Objective

Define which shared vectors, language-specific tests, reviews, security checks,
and release evidence are sufficient for each profile claim.

## Scope and exclusions

Passing vectors alone does not prove obligations that require code review,
architecture evidence, concurrency testing, or security analysis. This item
does not implement a harness.

## Questions to resolve

Map obligation types to evidence; define skipped-case handling, synthetic data,
bounded execution, exact build identity, retention, reproducibility, and review.

## Acceptance criteria

- [ ] Every obligation category has sufficient, observable evidence.
- [ ] Skips, missing evidence, failures, and unsupported obligations cannot look successful.
- [ ] Reports exclude credentials and sensitive payloads.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Add accepted evidence requirements to SPEC-0008.

## Validation and review

No validation or approval recorded.
