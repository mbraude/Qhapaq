---
id: I-0007-010
kind: implementation
granularity: milestone
change_kind: requirement
title: Trusted host configuration, sources and independent policy boundaries
status: open
spec: SPEC-0007
requirements: [R-0007-351, R-0007-399, R-0007-413, R-0007-414, R-0007-415]
depends_on: [D-0007-005, I-0007-009, I-0007-007]
artifacts: [specs/0002-operation-catalogs-and-host-configuration.md, specs/0004-ai-assisted-connections.md, schemas, conformance, implementations/dotnet]
---

# I-0007-010: Trusted Host Policy

## Objective and coverage

Phase 3A: exact trusted profile/source/connection/policy contracts and vectors,
provider/cache/integrity/reload decisions, fail-closed effective registry,
descriptor filtering, bind/invocation policies, credentials and immutable snapshots.
It also owns immutable catalog-version membership, policy-projection snapshots,
capability availability, and trusted enablement/reload boundaries.

## Entry gates

Governing contracts are owned by SPEC-0002/0004. Their detailed decisions remain
unassessed and must be extracted/approved before corresponding slices execute.
Host contract decisions may proceed before registry implementation; only delivery
has these dependencies. Explicitly defer unsupported sources/providers.

## File and ownership manifest

Pending contract-decision extraction and enabled-capability slice manifests.

## Design and integration

Independent execution/payload-disclosure policy, default-denied MCP disclosure,
destination/scope/cancellation/redaction restrictions, invalidation and no workspace
trust elevation. Real trusted-host behavior cannot be replaced by test policy stubs.

## Tests and validation

Profile selection, invalid startup/reload, integrity, source conflicts, policy
separation, credential non-disclosure, snapshots and cache invalidation.

## Exit criteria

- [ ] Supported host slice has reviewed exact contracts/vectors and fail-closed policy.
- [ ] Required checks and human review pass before capability enablement.

## Plan approval

Absent; milestone only. Companion sources are not yet planned or approved.

## Delivery evidence and review

No provider, consent, host-profile or extension decision made during extraction.
