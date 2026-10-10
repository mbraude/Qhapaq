---
id: D-0008-002
kind: decision
title: Assign convention ownership and applicability
status: complete
spec: SPEC-0008
requirements:
  - R-0008-004
depends_on: []
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/development/coding-conventions.md
---

# D-0008-002: Assign Convention Ownership and Applicability

## Objective

Decide which engineering conventions are common, language-specific, or
artifact-specific and how applicability is expressed without duplicating
portable behavior.

## Scope and exclusions

R-0008-004 owns the policy categories, locations, applicability, and
precedence. This item does not define detailed rules for an unselected
language, website framework, or integration platform and does not perform the
downstream extraction of existing specialized content.

## Questions to resolve

Define common policy, specialized policy, document locations, precedence,
path-specific instruction linkage, and how architectural rules remain in ADRs.

## Acceptance criteria

- [x] Policy categories, owners, precedence, and applicability are explicit.
- [x] Portable requirements are linked rather than copied into language guides.
- [x] Accepted product behavior and engineering policy are recorded in the correct authorities.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-004](../../../specs/0008-multi-language-conformance-and-repository-organization.md#5-engineering-policy-ownership-and-applicability)
  keeps the common baseline in `docs/development/coding-conventions.md`, places
  real specialized guides beneath `docs/development/conventions/`, defines
  cumulative applicability and specialization precedence, and makes
  path-specific instructions a routing layer rather than a competing policy
  source.
- [Coding conventions policy ownership](../../../docs/development/coding-conventions.md#policy-ownership-and-applicability)
  records the corresponding engineering practice.
- Detailed specialized rules, speculative guides, and the physical extraction
  of existing .NET material remain excluded. I-0008-001 owns that future
  delivery after its other decision prerequisites are complete.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source hashes, four sequential SPEC-0008 requirement
  identifiers, 19 unique work-item identities, 11 resolvable requirement
  references, one phase membership per item, resolvable dependencies, and an
  acyclic dependency graph.
- Confirmed all 46 local relative links in changed Markdown resolve and `git
  diff --check` passes.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement` and derived `R-0008-004@a2dab0`. The warning identifies the
  source paths and language/artifact scopes necessarily named by this
  repository-policy ownership requirement. No product or test code changed.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `ad41d1afbc3c94b7cb5f7e9d6fe42a397cf32c30f0d885836a3ae43d12fa37de` |
| `docs/development/coding-conventions.md` | SHA-256 `782e590a86419f9001469bc9faa0c2491e93a11728c0da1df0eaf4bbf70f7305` |
| `work/0008/decisions/D-0008-002-convention-ownership.md` | Material SHA-256 `2bca706b18069a7c4ef95ea361236d8a82c00fe56f3ac78f082c8d379b054334` |
| `work/0008/implementation/I-0008-001-engineering-policy-separation.md` | SHA-256 `c81da6f4bb7277569ae783220c49043b3e3ce86393bbdb3bcf1d63fc2c1f09d8` |
| `work/0008/plan.md` | SHA-256 `a1f512cba7f6c8d5b086ed580d1c2c7808d6b33bdcacfce9e18f9270e36e5874` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot above.
The approved scope is the common engineering-policy baseline, specialized
policy location and precedence, authority boundaries, and path-specific
instruction routing role defined by R-0008-004. Detailed rules for unselected
languages, frameworks, and platforms; extraction of existing .NET content;
implementation; workspace creation; and publication remain excluded.
