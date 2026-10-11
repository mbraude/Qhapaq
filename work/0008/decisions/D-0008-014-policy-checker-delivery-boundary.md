---
id: D-0008-014
kind: decision
title: Resolve engineering-policy and trace-checker delivery boundary
status: complete
spec: SPEC-0008
requirements:
  - R-0008-004
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on: [D-0008-008, D-0008-011]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - work/0008/implementation/I-0008-001-engineering-policy-separation.md
  - work/0008/implementation/I-0008-007-trace-checker.md
---

# D-0008-014: Resolve Engineering-Policy and Trace-Checker Delivery Boundary

## Objective

Resolve the delivery boundary between publishing language-specific traceability
policy and delivering the matching extractor and shared checker, so no policy
milestone implies language support before its required checker exists.

## Scope and exclusions

R-0008-004 and R-0008-016 through R-0008-018 govern policy ownership,
language-native placements, extractor registration, and checker behavior.
This item must not weaken the requirement that a language is unsupported for
traceability until both its placements and a matching extractor are
registered. It does not implement or select a checker technology.

## Questions to resolve

- May common and specialized policy artifacts be delivered before the checker,
  provided they make no claim that the language is supported?
- Which item owns policy authoring, extractor registration, and evidence that
  the registered placements match the extractor?
- Should I-0008-001 and I-0008-007 be split into ordered child slices or remain
  separate milestones with an explicit dependency?
- Do the existing requirements fully define the support boundary, or does the
  authoritative specification or ADR need amendment?

## Acceptance criteria

- [x] The policy-only and traceability-support completion boundaries are
  explicit and consistent with R-0008-016 through R-0008-018.
- [x] Ownership, dependencies, and acceptance gates for I-0008-001 and
  I-0008-007 are reconciled without a cycle or duplicate work.
- [x] Any newly discovered product or architectural semantics are recorded in
  the governing specification or ADR, not only in the work plan.
- [x] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

The accepted delivery boundary uses the existing support conditions in
[R-0008-016](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
and the extractor contract in
[R-0008-017](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability);
no new product or architectural semantics were identified, so neither the
specification nor an ADR requires amendment.

[I-0008-001](../implementation/I-0008-001-engineering-policy-separation.md)
owns policy authoring and its exact language-native placement and attachment
rules. Policy artifacts may be delivered first, but do not register an
extractor or claim language traceability support.
[I-0008-007](../implementation/I-0008-007-trace-checker.md) owns extractor
implementation and registration, and the evidence that each registered
extractor matches its approved policy. It depends on I-0008-001. A language
does not become supported for traceability until both the policy placements
and matching extractor are registered. Tool ownership, implementation
technology, and concrete implementation slices remain outside this decision.
The two milestones remain separate, with I-0008-007 depending on I-0008-001;
decomposition into executable child slices is deferred to implementation
planning after scoped readiness.

## Validation and review

Validated 2026-10-10:

- Confirmed R-0008-004 and R-0008-016 through R-0008-018 already establish
  policy ownership, native placement, extractor matching, and the support
  boundary. No specification or ADR amendment was needed.
- Verified the recorded approval material hashes for D-0008-008,
  D-0008-011, and the preceding D-0008-012 review snapshot.
- All 12 plan source hashes match current bytes. Across the repository, all 74
  work-item IDs are unique, every dependency resolves, and the dependency graph
  is acyclic. Relative Markdown links in all four changed files resolve;
  `git diff --check` passes.
- Specification trace check: `PASS`. The four changed files are work-plan or
  work-item documentation (`maintenance`); no specification block or code/test
  changed. No `Spec:` trailer applies, and semantic code review is not
  applicable. No waivers were added.
- No implementation, scope readiness approval, plan approval, or language-
  support claim is authorized by this decision.

Exact review snapshot:

| Role | Path | Snapshot |
| --- | --- | --- |
| Input | `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a` |
| Input | `docs/architecture/decisions/0003-enforce-specification-traceability.md` | SHA-256 `1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83` |
| Input | `docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md` | SHA-256 `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| Input | `docs/development/coding-conventions.md` | SHA-256 `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` |
| Input | `work/0008/decisions/D-0008-008-language-native-traceability.md` | SHA-256 `e9e6f9fb099ee08b82ddcf6ca491f178ef2099d6aab2109802223619212a89ae` |
| Input | `work/0008/decisions/D-0008-011-build-ci-release-orchestration.md` | SHA-256 `3f0fd4bb00e527cd3ed4f3325472edd9c75a82abbc80ed5de95ff743557a9639` |
| Input | `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `e0127638451b6afa9fcb493b786b5712b2e9c86a41d4a5fdb61e76eb3fbccf08` |
| Input | `work/0008/readiness/engineering-policy.md` | SHA-256 `889329dca612445fc7bd7f49f9fe6a8876ebe80eb67328c4b2f180f824ebb803` |
| Output | `work/0008/implementation/I-0008-001-engineering-policy-separation.md` | SHA-256 `581295daad8283bf22b5b8039053895acf672e561dc7e547f8954abac88a40a8` |
| Output | `work/0008/implementation/I-0008-007-trace-checker.md` | SHA-256 `4f3f7c0e805d1ce515c692ccd49e752fd139d05f4c3ec18c41fa9107ea13e953` |
| Output | `work/0008/plan.md` | SHA-256 `b4a945fe17c7f6dff5007c9300156377656127de18976a04f575bd96dbca2d49` |
| Decision | `work/0008/decisions/D-0008-014-policy-checker-delivery-boundary.md` | Material SHA-256 `b5acf1091308475010e929864fe7e063c30f95526a4b52868d4f2bba988e1f82` |

Proposed trailers:

```text
Change-Kind: maintenance
```

Approved explicitly in this session on 2026-10-10 for the exact snapshot above:
material SHA-256
`b5acf1091308475010e929864fe7e063c30f95526a4b52868d4f2bba988e1f82`. The
approved scope is the policy/checker delivery boundary, ownership, dependency,
and unchanged traceability-support condition recorded in this decision.
Implementation, checker technology selection, readiness or plan approval,
language-support claims, component contract publication, and pushing are
excluded. The full-byte hashes of all reviewed material inputs and outputs are
recorded above. No approval of another snapshot or scope is inferred.
