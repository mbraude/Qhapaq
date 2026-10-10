---
id: D-0008-003
kind: decision
title: Separate portable requirements, language contracts, and examples
status: complete
spec: SPEC-0008
requirements: [R-0000-007, R-0008-005]
depends_on: []
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/architecture/decisions/0003-enforce-specification-traceability.md
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

- [x] Readers and tooling can distinguish every content category.
- [x] Language examples cannot silently redefine portable contracts.
- [x] Existing requirement identifiers and fingerprint rules are preserved or explicitly amended.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-005](../../../specs/0008-multi-language-conformance-and-repository-organization.md#normative-content-categories)
  keeps portable requirements implementation-neutral and assigns normative
  language contracts to explicitly scoped numbered implementation
  specifications, using SPEC-0006 for the current .NET runtime.
- R-0008-005 makes examples outside requirement blocks illustrative and
  non-normative, while examples inside blocks are labeled normative and remain
  part of the block fingerprint and conformance expectations.
- [ADR-0003](../../../docs/architecture/decisions/0003-enforce-specification-traceability.md#stable-requirement-identifiers)
  records the corresponding block-boundary and labeling clarification without
  changing identifier or fingerprint algorithms.
- The illustrative C# interface remains non-normative. Auditing existing mixed
  content and defining language-native marker placement remain excluded and
  belong to I-0008-002 and D-0008-008 respectively.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source hashes, five sequential SPEC-0008 requirement
  identifiers, unique work-item identities, and resolvable direct
  dependencies.
- Confirmed all 46 relative links in the changed Markdown resolve and `git
  diff --check` passes.
- Derived `R-0008-005@107883` with no previous fingerprint references to
  update. Existing requirement identifiers and the ADR-0003 fingerprint
  algorithm remain unchanged.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement`; the warning identifies the specification paths and current
  .NET implementation authority necessarily named by the content-ownership
  requirement. No product or test code changed.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `d9f5fe531c6dcd139329c847e994d0d15f6329115ef27b77572f276622c73760` |
| `docs/architecture/decisions/0003-enforce-specification-traceability.md` | SHA-256 `d384fa75572c08d86a46911a54c4792905511c01c3cb047d01774a0132cf6704` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | Material SHA-256 `8dd62a8d33871880f7c6281433c337c2213e0afed73d59595af53504ef48ccaf` |
| `work/0008/decisions/D-0008-008-language-native-traceability.md` | SHA-256 `b0da69229e66f1d919979af66e435e62b947b421318bb328e9efe02b97721100` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | SHA-256 `52bd62829f9372a54c23ba06e61168f76ffcd590f0dfc328a3feeba200df4363` |
| `work/0008/plan.md` | SHA-256 `5222bf1c5477b3f663c541ea212264cd6e078f326ea687d1cb60d3091a463c5d` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot above.
The approved scope is the separation of portable requirements, explicitly
scoped language-specific contracts, non-normative prose, illustrative
examples, and normative examples defined by R-0008-005, including the
corresponding ADR-0003 clarification. The content audit, language-native marker
design, conformance profiles, implementation, and publication remain excluded.
