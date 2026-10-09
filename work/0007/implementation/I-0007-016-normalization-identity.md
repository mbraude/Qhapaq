---
id: I-0007-016
kind: implementation
granularity: milestone
change_kind: requirement
title: Exact-contract normalization and canonical definition identity
status: open
spec: SPEC-0007
requirements: [R-0007-358, R-0007-359]
depends_on: [I-0007-012, I-0007-013, I-0007-009, I-0007-004]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-016: Normalization and Identity

## Objective and coverage

Phase 6A: resolve exact descriptor configuration schemas, materialize optional
defaults, preserve explicit null/required values, validate canonical normalized
configuration and compute canonical bytes/digests.

## Entry gates

Parsing, instance validation, shared digest primitives and normalization vectors.
Reference-host metadata comes from registry; an allowed verified offline source
may replace that prerequisite only through explicit concrete replanning.

## File and ownership manifest

Pending exact normalizer, identity, descriptor-source and test slices.

## Design and integration

Normalize before hashing/persistence/review/binding. No operation activation or
credentials are needed to resolve exact contract metadata.

## Tests and validation

Exact defaults, missing contracts/conflicts, omission/null/required distinctions,
canonicalization and identity reproducibility.

## Exit criteria

- [ ] Canonical definitions contain executable defaults with reproducible identities.
- [ ] Checks and explicit human review pass without execution-time construction.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No canonical definition identity delivered here.
