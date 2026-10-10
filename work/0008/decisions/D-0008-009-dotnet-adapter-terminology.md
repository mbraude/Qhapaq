---
id: D-0008-009
kind: decision
title: Resolve .NET adapter terminology and assembly naming
status: open
spec: SPEC-0008
requirements: [R-0006-001, R-0006-002, R-0006-021, R-0006-023]
depends_on: []
artifacts:
  - specs/0006-dotnet-layered-architecture.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-009: Resolve .NET Adapter Terminology and Assembly Naming

## Objective

Decide whether the .NET Service Implementations layer becomes Adapters and
whether assembly and namespace renames are separate, compatible changes.

## Scope and exclusions

SPEC-0006 remains authoritative. Source relocation, layer terminology,
assembly identity, namespace identity, package identity, and public behavior
are separate concerns and must not be bundled implicitly.

## Questions to resolve

Choose layer terminology; assess short versus role-qualified assembly names;
define compatibility and migration effects; and identify required SPEC-0006
amendments and ADRs.

## Acceptance criteria

- [ ] Layer terminology is unambiguous across language runtime and .NET architecture usage.
- [ ] Assembly, namespace, package, and path decisions are separated explicitly.
- [ ] Every affected SPEC-0006 requirement and architecture test is identified.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Amend SPEC-0006 and record architecture rationale if a rename is accepted.

## Validation and review

No validation or approval recorded.
