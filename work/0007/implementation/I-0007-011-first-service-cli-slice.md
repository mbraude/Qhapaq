---
id: I-0007-011
kind: implementation
granularity: milestone
change_kind: requirement
title: First non-executing Service and CLI vertical slice
status: open
spec: SPEC-0007
requirements: [R-0007-352, R-0007-400, R-0007-401, R-0007-402, R-0007-403, R-0007-404, R-0007-405, R-0007-406, R-0007-407, R-0007-408, R-0007-409, R-0007-410, R-0006-033, R-0006-035, R-0006-036, R-0006-037, R-0006-038]
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
Use SPEC-0006's boundary-first retrieval flow: public Service DTOs and descriptor
values, distinct internal Business/DAL port outcomes, and Service-owned safe
projection. Concrete registry, provenance, policy, and factory state must not
escape through public descriptor members or unavailable responses.

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
