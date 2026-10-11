---
spec: SPEC-0008
scope: engineering-policy
assessment: blocked
sources:
  - path: work/0008/plan.md
    revision: null
    content_sha256: da3dcba5de8f6d65769ab5785d5dfe19af37a6cb3817eafcec11dd0efac9ed76
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a
  - path: SPEC.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908
  - path: specs/0006-dotnet-layered-architecture.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834
  - path: docs/development/spec-driven-workflow.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 574d0e18efb42b5701b148a68a62fbd4be7b748e3f276bb6424a056c152507f4
  - path: work/templates/readiness.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 707d334f40feb8e3462f8ee814c55ce3a8f66c32a860a4b8557d5eaa2f672bf2
  - path: work/0008/implementation/I-0008-001-engineering-policy-separation.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: fc3128316dc5e0982d1931bcd74d4d139c3ee0d5333796934c211e2431d125a3
  - path: work/0008/decisions/D-0008-002-convention-ownership.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 6cd4c9a0740873953903e81617c7ad9e493f2321314dcca122465f8e32920afd
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 65a80afc49a365290ae9c366677e70bb7a46f7c770ab89961285b1b96ad531f5
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: e9e6f9fb099ee08b82ddcf6ca491f178ef2099d6aab2109802223619212a89ae
  - path: work/0008/decisions/D-0008-011-build-ci-release-orchestration.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 3f0fd4bb00e527cd3ed4f3325472edd9c75a82abbc80ed5de95ff743557a9639
  - path: work/0008/implementation/I-0008-007-trace-checker.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: dd0b4bb92f39a6c2b957747c68a92f47a21364bdd8fd12b7f0894c9a99fd66e4
  - path: .github/instructions/dotnet.instructions.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 18eb5accd0bd3f627f35d719ca43c66ac520c2765d27e18aad4a9195148acf7f
  - path: .github/instructions/documentation.instructions.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: ab813b9414defa53852f6137383b2d0f36897e74903f231b86ef185c6999a477
  - path: .github/instructions/schemas.instructions.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: 14a8d2de3283bfde7d94053f45e06bd53943d17ece2130f3ac85842520609b85
  - path: .github/instructions/specifications.instructions.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: fd113cfea6cc774e500ddac0baf21de8d0be2684931faa96e22c7fa55bfcc03a
  - path: .agents/skills/spec-trace-check/SKILL.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: e0b7bc16c1cad5da3332293086c83a66421b0ffd8b29adac6347fec1a7eac486
---

# SPEC-0008: Engineering Policy Readiness

## Assessed scope

Assess the engineering-policy delivery scope represented by
[I-0008-001](../implementation/I-0008-001-engineering-policy-separation.md):

- [R-0008-004](../../../specs/0008-multi-language-conformance-and-repository-organization.md#common-and-specialized-conventions):
  ownership and applicability of common and specialized policy, including
  precedence and the routing-only role of path-specific instructions.
- [R-0008-016](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability):
  portable marker payloads, native placement rules, and language-support gate.
- [R-0008-017](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability):
  registered language-aware extractors and one shared validation engine.
- [R-0008-018](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability):
  portable, scoped waivers and non-waivable mechanical checks.

Related completed decisions: D-0008-002, D-0008-003, and D-0008-008.
I-0008-001 explicitly excludes implementing the checker.

## Exclusions

This assessment does not cover requirement/example migration under I-0008-002,
the trace checker implementation under I-0008-007, CI/root orchestration,
conformance profiles or publication, new implementation languages, source
relocation, or the Entry Point identity migration. It grants no implementation
plan approval and does not authorize executing I-0008-001.

## Completeness and consistency

The policy authority model is sufficiently explicit: common rules belong in
`docs/development/coding-conventions.md`; real specializations belong under
`docs/development/conventions/`; applicable policies accumulate; and
specifications and ADRs remain authoritative. D-0008-002 and D-0008-003 record
explicit approval for their exact assessed decision snapshots. The C# placement
model in the common conventions distinguishes member-wide enforcement,
statement/block invariants, and test references; the portable waiver syntax and
scope are also stated.

Current policy surfaces are not yet consistent with those requirements:

- `.github/instructions/dotnet.instructions.md` permits references at the
  type, member, or block level, broader than the common policy and ADR-0003.
- The documentation, schema, and specification path instructions contain
  substantive authoring policy rather than only routing or tool-execution
  guidance.
- .NET-specific rules remain in the common conventions, and no specialized
  guide exists. These are identifiable extraction and routing tasks, not
  unresolved product semantics.
- No C# `spec:` or `spec-waive:` references were found under
  `implementations/dotnet/`; the AI-led review procedure is not a registered
  deterministic language extractor.

No additional decision about payload grammar, attachment categories, waiver
limits, or common-versus-specialized precedence was identified. The target
exact file manifest and delivery slices remain to be planned.

## Conformance and prerequisite artifacts

- The portable payload, placement categories, checker responsibility,
  diagnostic fields, and failure cases are specified in R-0008-016 through
  R-0008-018. These are specified expectations, not evidence that an extractor
  or checker exists.
- Current C# reference and waiver placements are described in
  `docs/development/coding-conventions.md`; path routing is in
  `.github/instructions/dotnet.instructions.md`. Their disagreement is listed
  above.
- No traceability extractor registration, deterministic shared checker, or
  checker test/conformance group was found. I-0008-007 remains an open,
  non-executable milestone with no approved exact manifest. The AI-led
  `spec-trace-check` skill is explicitly an interim review, not that artifact.
- No schema or published vector is normatively required for the policy
  documents themselves. I-0008-007 specifies the cases its future checker must
  cover; those tests cannot be treated as already delivered.
- `docs/development/conventions/` does not exist. Creating a guide is
  appropriate only for maintained consumers whose specialized rules are
  actually separated; no empty guide should be created speculatively.

## Blockers

1. **R-0008-016 language-support gate is unmet for C#.** No matching registered
   deterministic extractor is available. I-0008-001 excludes checker
   implementation, while its objective requires placements to match the
   registered extractor. New decision
   [D-0008-014](../decisions/D-0008-014-policy-checker-delivery-boundary.md)
   will resolve sequencing and acceptance boundaries without allowing policy
   preparation to claim C# traceability support before the extractor exists.
2. **Policy-routing surfaces need an exact migration manifest.** Existing
   path-specific instruction content conflicts with R-0008-004 and the .NET
   placement summary contradicts the common rule. Identify which content moves
   to specialized policy and which instructions become links/routing before
   authorizing execution.
3. **No approved executable plan exists.** I-0008-001 is a milestone; its
   manifest and plan approval are absent, and no readiness record was
   previously present. D-0008-014 is now an additional prerequisite.
   Readiness cannot substitute for concrete slices or their separate plan
   approval.

## Validation and approval

Assessed 2026-10-10 on branch `spec/0008-repository-organization`, commit
`4e24e1b0e293691eb731bbc8429671aaf20cbb43`. The worktree already contained an
uncommitted, bounded SPEC-0008 plan synchronization; its exact bytes are
fingerprinted in the source list with `revision: null`. All other listed
inputs match their recorded hashes at the assessed commit.

Checks performed:

- Reviewed R-0008-004 and R-0008-016 through R-0008-018 against SPEC-0006,
  ADR-0003, ADR-0004, the common conventions, path instructions, and the
  linked 0008 decisions and milestones.
- Confirmed the three prerequisite decisions are complete and contain explicit
  approval evidence for their exact decision snapshots. This does not approve
  this readiness record or I-0008-001's plan.
- Checked for existing readiness records, specialized convention files,
  traceability references in .NET source, and an implemented registered
  extractor/checker.
- No build or unit-test command was run: this assessment changes planning
  documentation only, and the checker implementation is absent.
- Specification trace check classified the changed plan and readiness
  artifacts as documentation (`maintenance`) and passed with no requirement
  or code changes in scope; no `Spec:` trailer applies. The semantic code
  review is not applicable to these documentation-only files.
- Verified all 20 source hashes, all five relative links, readiness frontmatter
  and scope references, and `git diff --check`. Git emitted its existing
  CRLF-to-LF normalization warning for the plan.

No human approval of this exact readiness snapshot is recorded. This scoped
assessment is **not** publication, a full v1 conformance claim, approval of an
implementation plan, or authorization to execute a work item.

## Snapshot invalidation

After this assessment, D-0008-014 was added and I-0008-001 and I-0008-007 were
made dependent on it. The plan and those item snapshots therefore differ from
the inputs assessed above. The assessed plan hash was
`da3dcba5de8f6d65769ab5785d5dfe19af37a6cb3817eafcec11dd0efac9ed76`; the
updated plan hash is
`0cb0ef261b14915fa77ff3b5a852ec57f20b9e229aab919539a6931f0149d322`. This
record preserves the earlier blocked result for its recorded snapshots; it is
not current readiness evidence. Reassess after D-0008-014 is resolved.
