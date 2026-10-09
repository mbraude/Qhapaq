---
id: I-0007-019
kind: implementation
granularity: milestone
change_kind: requirement
title: Transform boundaries and final output
status: open
spec: SPEC-0007
requirements: [R-0007-363]
depends_on: [I-0007-018, I-0007-017]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-019: Transforms and Final Output

## Objective and coverage

Phase 7B: pre-bound serialization/projectors/evaluators/validators/materializers,
safe last-consumer slot release and validated final output projection.

## Entry gates

Primitive frame runner, complete pre-binding and relevant output/transform vectors.

## File and ownership manifest

Pending exact transform, projection, lifetime and test slices.

## Design and integration

No implicit conversions, undeclared frame access or payload disclosure.

## Tests and validation

Transform/final-output failure, serialization and slot lifetime cases.

## Exit criteria

- [ ] Transform/output vectors pass with safe frame scope and lifetime.
- [ ] Required checks and explicit delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No transform runner delivered by extraction.
