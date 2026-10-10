---
id: D-0008-003
kind: decision
title: Separate portable requirements, language contracts, and examples
status: open
spec: SPEC-0008
requirements: [R-0000-007]
depends_on: []
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-003: Separate Portable Requirements, Language Contracts, and Examples

## Objective

Define how normative portable requirements, explicitly language-specific
contracts, rationale, and non-normative examples are labeled and separated.

## Scope and exclusions

R-0000-007 keeps portable semantics language-neutral. This item does not make
the illustrative C# interface normative or change an existing requirement
fingerprint merely to restyle prose.

## Questions to resolve

Define labels and placement, ownership of language-specific normative contracts,
example boundaries, fingerprint effects, and review rules for mixed content.

## Acceptance criteria

- [ ] Readers and tooling can distinguish every content category.
- [ ] Language examples cannot silently redefine portable contracts.
- [ ] Existing requirement identifiers and fingerprint rules are preserved or explicitly amended.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Record accepted semantics in SPEC-0008 and any affected traceability
authority.

## Validation and review

No validation or approval recorded.
