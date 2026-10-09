---
id: I-0007-027
kind: implementation
granularity: milestone
change_kind: requirement
title: Portable invocation-skill contracts and snapshot generation
status: open
spec: SPEC-0007
requirements: [R-0007-370, R-0001-048, R-0001-049, R-0001-053]
depends_on: [I-0007-016, I-0007-017, I-0007-010]
artifacts: [specs/0001-core-pipeline-model.md, schemas, conformance, implementations/dotnet]
---

# I-0007-027: Invocation Skills

## Objective and coverage

Specify bundle schema/vectors, implement snapshot generation and required CLI/MCP
mappings under SPEC-0001. These product artifacts are not repository workflow skills.

## Entry gates

Exact contract validation, canonical identity, host/disclosure policy and approved
bundle decisions. Invocation uses Phase 9; optional reference mode additionally
requires I-0007-026. Do not block snapshot generation on optional reference mode.

## File and ownership manifest

Pending owner-spec decision extraction and exact generation/adapter/test slices.

## Design and integration

No second parameter language or authority path. Skills delegate to a conforming host.

## Tests and validation

Bundle/version/schema/digest boundaries, disclosure redaction and ordinary host
permission checks; reference-mode cases only when that capability is enabled.

## Exit criteria

- [ ] Required bundle contracts/vectors and snapshot mappings are delivered.
- [ ] Invocation authority and optional-mode gates are tested; review passes.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No bundle format or product skill generated during bootstrap.
