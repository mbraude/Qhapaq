---
id: I-0007-003
kind: implementation
granularity: milestone
change_kind: requirement
title: Descriptor, manifest, digest and compatibility artifact family
status: open
spec: SPEC-0007
requirements: [R-0007-347, R-0007-290, R-0007-291, R-0007-298]
depends_on: [D-0007-003, D-0007-015, I-0007-005]
artifacts: [schemas, conformance]
---

# I-0007-003: Descriptor Artifacts

## Objective and coverage

Publish manifest envelope and next descriptor schema, compatibility matrix,
contract-digest/manifest goldens, vocabulary/idempotency/declared-failure,
decorator-preservation, unsafe-retry, and contract-comparison vectors.

## Entry gates

Applicable descriptor decisions, approved current-scope readiness,
and portable vector envelope. Unrelated mapping/numeric closure does not block
this family. Required profile/diagnostic foundations come from I-0007-005.

## File and ownership manifest

Pending planning of exact versions/paths under schemas and conformance.

## Design and integration

Preserve v1alpha1 schema/vectors; never silently mutate that earlier format.
Initial placeholder digests are not digest goldens.

## Tests and validation

Schema, canonical digest, valid/invalid/mixed/unknown-format, compatibility,
ordering and byte-equality cases; consume via I-0007-002 for implementation gates.

## Exit criteria

- [ ] Every listed family has versioned portable artifacts and expected results.
- [ ] Earlier artifacts remain intact; applicable checks and review pass.

## Plan approval

Absent; milestone only. Split artifact subfamilies before execution if necessary.

## Delivery evidence and review

Existing alpha fixtures are structural evidence only; no new publication claimed.
