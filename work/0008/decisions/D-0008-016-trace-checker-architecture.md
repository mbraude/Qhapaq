---
id: D-0008-016
kind: decision
title: Select deterministic trace-checker architecture and ownership
status: open
spec: SPEC-0008
requirements:
  - R-0008-016
  - R-0008-017
  - R-0008-018
  - R-0008-021
depends_on: [D-0008-008, D-0008-011, D-0008-014, I-0008-001]
artifacts:
  - docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md
---

# D-0008-016: Select Deterministic Trace-checker Architecture and Ownership

## Objective

Select the host, implementation technology and language, package boundary,
ownership, and dependency/toolchain expectations for the deterministic
multi-language trace checker before I-0008-007 is decomposed into executable
slices.

## Scope and exclusions

R-0008-016 through R-0008-018 govern the portable marker and waiver payloads,
language-aware extractor boundary, shared rules engine, diagnostics,
fingerprints, reverse-impact checks, and waiver limits. R-0008-021 requires
the checker to remain a non-bypassable validation group while leaving root
orchestration to I-0008-009.

This decision selects an implementation architecture for those existing
requirements. It does not change traceability behavior, implement the checker,
register an extractor, define root CI orchestration, publish a contract, or
claim language support.

## Questions to resolve

- Is the checker owned by a repository-standard-library script, a
  workspace-native tool, or another package/tool boundary?
- Which implementation language and host own the shared rules engine and the
  first registered extractor?
- Which parser and package dependencies are permitted, and which workspace or
  root commands build and test the tool?
- Where do extractor registration, policy-match evidence, fixtures, and
  stable diagnostic contracts reside?
- What dependency direction keeps language syntax parsing in extractors,
  portable validation in one shared engine, and root orchestration outside
  I-0008-007?

## Acceptance criteria

- [ ] An ADR records the selected host, implementation language, package
  boundary, ownership, dependencies, and rejected alternatives.
- [ ] The architecture preserves the extractor/shared-engine boundary and
  traceability-support condition in R-0008-016 through R-0008-018.
- [ ] The checker remains a required validation group while root impact
  selection and CI orchestration remain owned by I-0008-009.
- [ ] The decision identifies the concrete repository surfaces and documented
  commands that I-0008-007 may plan without implementing them.
- [ ] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

Unresolved. I-0008-007 remains blocked from concrete slice planning until this
decision is accepted and its scoped implementation readiness is reassessed.

## Validation and review

Approval is absent.
