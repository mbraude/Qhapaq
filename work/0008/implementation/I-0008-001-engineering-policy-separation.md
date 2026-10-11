---
id: I-0008-001
kind: implementation
granularity: milestone
change_kind: maintenance
title: Separate common and specialized engineering policy
status: complete
spec: SPEC-0008
requirements:
  - R-0008-004
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on:
  - D-0008-002
  - D-0008-003
  - D-0008-008
  - D-0008-014
  - I-0008-010
  - I-0008-011
artifacts:
  - docs/development/coding-conventions.md
  - docs/development/conventions/dotnet.md
  - docs/development/conventions/documentation.md
  - docs/development/conventions/schemas.md
  - docs/development/conventions/specifications.md
  - .github/instructions/dotnet.instructions.md
  - .github/instructions/documentation.instructions.md
  - .github/instructions/schemas.instructions.md
  - .github/instructions/specifications.instructions.md
---

# I-0008-001: Separate Common and Specialized Engineering Policy

## Objective and coverage

Deliver the common, language-specific, and artifact-specific policy structure
defined by R-0008-004 and applicable instruction links, including explicit
language-native reference, waiver, invariant, whole-member, and test
placements. Policy may be delivered before a matching checker, but does not
register an extractor or claim language traceability support. This milestone
does not implement or register the checker. It is an aggregate gate, not an
executable slice; its policy outcome depends on both child slices:
[I-0008-010](I-0008-010-dotnet-policy-extraction.md) and
[I-0008-011](I-0008-011-artifact-policy-routing.md).

## Entry gates

D-0008-002, D-0008-003, D-0008-008, and D-0008-014 are complete; affected
specification and ADR amendments are approved; scope readiness is approved.

## File and ownership manifest

The common source remains `docs/development/coding-conventions.md`.
Specialized guides, if required by real consumers, belong beneath
`docs/development/conventions/`, and path routing remains under
`.github/instructions/`. The child slices name the .NET and maintained
artifact-authoring guides and their exact routing files. No guide for an
unselected language or other speculative consumer is delivered.

## Design and integration

Apply common and specialized policies cumulatively. A specialized guide may
explicitly replace a common Default or Recommendation within its declared
scope, but it cannot weaken a common Required rule or override a specification
or ADR. Policy owns each maintained implementation language's unambiguous
native placements; I-0008-007 owns extractor registration and evidence that
the registered extractor matches the approved policy. Policy delivery alone
does not make a language supported for traceability. Link portable
requirements instead of copying them, and keep path-specific instructions as
routing and tool-execution guidance rather than a competing policy source.

## Tests and validation

Validate links, applicability patterns, absence of contradictory duplicate
rules, traceability checks, and any documented policy validation command.

## Exit criteria

- [x] Approved policy sources and instruction links exist.
- [x] Native placements and attachment rules are explicit, without claiming
  traceability support before a matching extractor is registered.
- [x] No portable behavior is duplicated as language policy.
- [x] Both child slices are complete and their exact output snapshots have
  passed the required validation and explicit delivery review.
- [x] Required validation passes.
- [x] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

### Validation and review

The completed child slices [I-0008-010](I-0008-010-dotnet-policy-extraction.md)
and [I-0008-011](I-0008-011-artifact-policy-routing.md) each record passing
slice validation and explicit user approval of their exact output snapshots.
Every file in this milestone's manifest is present, and its current full-byte
hash matches the corresponding child-approved output hash below.

- The .NET policy transfer and its routing instruction passed the 21 focused
  transfer checks, relative-link checks, `git diff --check`, and the
  specification trace check as `maintenance`.
- The documentation, schema, and specification policy transfers passed their
  rule-mapping, routing/applicability, relative-link, and `git diff --check`
  checks; the specification trace check passed as `maintenance`.
- Together, these reviews verify the native C# placement guidance and the
  routing-only instruction boundaries. The policy explicitly does not claim
  traceability support before a matching extractor is registered.
- No documented build, format, lint, or test command applies to these
  documentation-only outputs; none was run. No deviation or additional
  artifact was reported.

The aggregate outputs have passed explicit delivery review and approval. This
approval does not publish a contract or claim trace-checker support.

Material inputs reviewed:

| Input | Snapshot |
| --- | --- |
| SPEC-0008 requirement source | SHA-256 `1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a` |
| Approved Phase 2 plan | Full-byte SHA-256 `b58de6089af182bca9aefe9fd1df2953a88b31801b59ecd11c0b8e135d2c9d25` |
| Approved engineering-policy readiness assessment | Snapshot SHA-256 `d7336321c16c11706defc78feb234168f0c4b1080438dfa0790993a2f37c6889`; current record full-byte SHA-256 `3575caac9ae9a0d98f2fedf4ff0f982cb1ba4cb8fee895435469f3d1d9aaf290` |
| I-0008-010 delivery evidence | Full-byte SHA-256 `087441e531f8b82b13b8d945367fa2442c8ca684c405c830d5befd313a831f43` |
| I-0008-011 delivery evidence | Full-byte SHA-256 `d73f1ddf80ef6a351443a0b6defc892e5301dd6bb279465c24c4ba234a22f43b` |

Current aggregate material SHA-256: `cd5630e41a99115709bb1a90d6048d4d2fbb8a285259199d92e272c175537a62`.

Output snapshot:

| Path | SHA-256 |
| --- | --- |
| `docs/development/coding-conventions.md` | `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b` |
| `docs/development/conventions/dotnet.md` | `712c0ed6d05c230f28146b0f4447622c5c62214e4b85c4c2d53d83bac1879c24` |
| `.github/instructions/dotnet.instructions.md` | `287898a2f49f45070fc7000bb977a04525b3e7bc49ea84b8a9bf8f12bf1f6ff645` |
| `docs/development/conventions/documentation.md` | `ac934e59fe3f4349f2c5302a85c694160829d1f54df5f18ab85f76a79e61c4ce` |
| `docs/development/conventions/schemas.md` | `a9a44c96d0ab48af49d3b7ea8ade8b13f3343814c36842519571f03046f0c33a` |
| `docs/development/conventions/specifications.md` | `8379c469032f87ba8f672b6ac614dd7c53cd0b4e0d4c72140802e61012469297` |
| `.github/instructions/documentation.instructions.md` | `4e84a7e492ea2f86e1e120030882fe7778241b26b107efe703670a38ba0f5b4b` |
| `.github/instructions/schemas.instructions.md` | `bee18c9090b555d6ad1e79105797b77da412fd9135315e290d44824901bcc8c7` |
| `.github/instructions/specifications.instructions.md` | `693dd3fe6360afd6af56250260b4bbf97450e6127d7db9c1beb4805c7904438c` |

The user explicitly approved the exact output snapshot listed above and
material SHA-256
`7351d3870d779bc49fa50b7663bc623063aad584ee4cea2f014bb47dd4924e1a` on
2026-10-11. After recording the satisfied delivery-review criterion, the user
explicitly approved the resulting current material SHA-256
`cd5630e41a99115709bb1a90d6048d4d2fbb8a285259199d92e272c175537a62` on
2026-10-11. This completes only the aggregate policy deliverable; it does not
approve contract publication or claim trace-checker support.
