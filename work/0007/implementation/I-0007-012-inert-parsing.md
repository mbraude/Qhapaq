---
id: I-0007-012
kind: implementation
granularity: milestone
change_kind: requirement
title: Inert parsing and portable structural validation
status: open
spec: SPEC-0007
requirements: [R-0007-353, R-0007-400, R-0007-401, R-0007-402, R-0007-403]
depends_on: [D-0007-006, I-0007-001, I-0007-002, I-0007-004, I-0007-005, I-0007-007]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-012: Inert Parsing

## Objective and coverage

Phase 4: strict JSON/duplicates, immutable inert models, exact offline schema,
node identities/structure/control-flow/scope/dominance, bounded safe diagnostics,
and rejection before registry binding or effects.

## Entry gates

Applicable pipeline/profile/scope/diagnostic artifacts, Phase 0A ownership and
shared parsing/validation foundations. No dependency on generator or host phases.

## File and ownership manifest

Pending exact model, parser, validator and test slice manifests.

## Design and integration

No activation, external resources or credentials. Raw parsed definitions remain
distinct from normalized canonical definitions; no premature canonical digest.

## Tests and validation

Shared parsing/structural/scope/diagnostic vectors and negative activation tests.

## Exit criteria

- [ ] Portable structural results pass independently of an active registry.
- [ ] Safe diagnostics and inertness are verified; checks and review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No semantic validity, normalization or execution claim made.
