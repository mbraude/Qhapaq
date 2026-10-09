---
id: I-0007-014
kind: implementation
granularity: milestone
change_kind: requirement
title: Mapping parsing and static inference
status: open
spec: SPEC-0007
requirements: [R-0007-354, R-0007-356]
depends_on: [I-0007-001, I-0007-004, I-0007-013]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-014: Mapping Inference

## Objective and coverage

Phase 5B: immutable expressions, exact per-site language selection, separate
missing/null inference, source-schema/narrowing and unsupported-language diagnostics.

## Entry gates

Closed mapping artifacts, expression ownership, schema compatibility and readiness.

## File and ownership manifest

Pending exact parser/type-inference/model/test slice manifests.

## Design and integration

Never migrate another site's language implicitly or conflate static validity with
host-supported bindability.

## Tests and validation

Shared parsing, inference, source-schema, narrowing and language-version vectors.

## Exit criteria

- [ ] Typed mapping sites preserve exact identity and static rejection behavior.
- [ ] Applicable checks and exact-snapshot delivery approval pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No expression parser or inference implemented by extraction.
