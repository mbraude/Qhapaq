---
id: I-0007-011
kind: implementation
granularity: milestone
change_kind: requirement
title: First non-executing Service and CLI vertical slice
status: open
spec: SPEC-0007
requirements: [R-0007-352, R-0006-033]
depends_on: [D-0007-004, D-0007-006, I-0007-001, I-0007-009, I-0007-010]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-011: First Service and CLI Slice

## Objective and coverage

Phase 3B: public Service V1 request/results/errors, adjacent Service/Business/DAL
collaboration and CLI mapping for policy-filtered exact descriptor retrieval.

## Entry gates

Exact retrieval/conclusion contracts, Phase 0A, registry, trusted selection and
descriptor-disclosure policy. Narrow prerequisites during concrete planning.

## File and ownership manifest

Pending exact public contracts, internal ports, implementations and tests.

## Design and integration

Adapters access only Service V1. This slice cannot execute operations, resolve
credentials, install extensions, mutate profiles or grant authority.

## Tests and validation

Exact lookup/version/conflicts/unavailability/disclosure denial/cancellation/safe
diagnostics; clean third-party Service consumer and adapter architecture checks.

## Exit criteria

- [ ] Real non-executing CLI/Service use case works without duplicated domain rules.
- [ ] Every prohibited side-effect path is tested; checks and review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

Existing assembly scaffolding is not this use-case delivery.
