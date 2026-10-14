---
spec: SPEC-0008
scope: requirement-example-audit
assessment: approved
process_version: 1
sources:
  - path: AGENTS.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: specs/0001-core-pipeline-model.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca
  - path: specs/0005-build-release-and-website-delivery.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 8259be3d7e256d77ab18e96c35906ce64c01d25eb7a22f45a911c0727d1a1679
  - path: specs/0006-dotnet-layered-architecture.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 399e0083473b9adb30375c6572e53c1c04249606e46f7aab3fd4eb8ed289232e
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/documentation.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: ee1ab8d0f2237adb5a1fd986ce5c925eb1b0d6bafa51bd5c700bfd3436e7f657
  - path: docs/development/conventions/specifications.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: .github/instructions/documentation.instructions.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 9ff5086829552eca77b740e59fc500bf5d5c2509bb6a2d0114bded5345ef2d03
  - path: .github/instructions/specifications.instructions.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: work/0008/plan.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 6a470ba804c17376b75db39598f5a7f6fd56121d60805e24f0508339e67b12bc
    material_sha256: e8fc4e833f454d2fb435b30d5e46f4256164541107dc42de2045cde297f9eed3
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: b78b184d3024ad6fd8d5857b49b59b02bd276318
    content_sha256: 0af546f80a3aa791db86d64f72c379d237df94f525a8df9c1f12feef5076a2a7
---

# SPEC-0008: Requirement and Example Audit Readiness

## Assessed scope

Assess readiness to create concrete delivery slices for
[I-0008-002](../implementation/I-0008-002-requirement-example-audit.md), which
will audit portable requirements, language-specific contracts, and examples
against R-0008-005. R-0000-007 remains the governing portability boundary.
Representative examples requiring explicit classification include the
illustration in R-0001-011, exported examples under R-0001-052, and the
Windows-path example referenced by R-0002-017. These are audit candidates, not
findings or pre-approved edits; the complete target inventory belongs in the
implementation plan.

## Exclusions

This assessment does not perform the content audit, change requirements or
fingerprints, approve implementation slices, or authorize edits. It does not
assess whole-v1 conformance. Language-native traceability placement and checker
behavior remain governed by D-0008-008 and its own delivery scope.

## Completeness and consistency

D-0008-003 is complete and accepted R-0008-005. The rule distinguishes
implementation-neutral portable requirements, explicitly scoped language
contracts, non-normative rationale, illustrative examples outside requirement
blocks, and normative examples inside them. ADR-0003 defines block and
fingerprint boundaries; the specifications convention preserves stable IDs and
requires reverse-impact review for edits within requirement blocks. SPEC-0006
is explicitly the current .NET implementation specification, not the
authority for portable semantics.

The item is a planning milestone, and its missing exact audit inventory is
intentional input to concrete planning rather than an unknown product decision.
The plan can enumerate documents and affected blocks, separate editorial
classification from requirement changes, and add per-slice fingerprints,
review impact, and validation gates. If the audit discovers behavior that is
not governed by accepted requirements, it must stop for the appropriate
specification decision rather than inventing semantics.

The examples noted above show why exact inventory and classification matter.
R-0001-011 includes an explanatory example within a requirement block, and
R-0002-017 describes a Windows-path example as illustrative while stating a
portable-path requirement in the same block. The audit plan must assess these
against R-0008-005 without presuming that moving or relabeling them is
semantics-preserving; any material requirement change needs its own review and
fingerprint impact analysis.

## Conformance and prerequisite artifacts

The planning work must preserve R-0008-005's categories and R-0000-007's
language-neutral contract boundary, identify normative and illustrative
examples, preserve requirement identities, and trace every proposed block
change to references and reverse-impact review. D-0008-008 owns native marker
placement and checker architecture; I-0008-002 must not duplicate that work.
No schemas, vectors, or other conformance artifacts are entry prerequisites
for planning this documentation audit.

## Blockers

No blocker prevents concrete planning of I-0008-002. The exact audit inventory,
slice boundaries, fingerprints, and validation matrix remain to be specified
in that plan. Implementation remains gated on approved concrete slices and
readiness of the exact specifications each slice would edit.

## Validation and approval

Validated 2026-10-12 against the exact source bytes listed above. Confirmed all
19 SPEC-0008 and 21 SPEC-0007 plan source hashes are current, D-0008-003 and
D-0008-008 are complete, the selected milestone depends on completed
D-0008-003, and the cross-specification boundaries and examples are recorded
without treating audit candidates as approved changes.

The assessment was explicitly approved in this session on 2026-10-12 for
planning I-0008-002 only. The exact readiness-record bytes reviewed before
recording approval had SHA-256
`8327c825126af9027848ab17a547db7e6ea1703f89c821d1dc376d326f9f2080`; all 21
assessed source hashes above matched at HEAD
`b78b184d3024ad6fd8d5857b49b59b02bd276318`. Approval permits concrete
implementation planning only. It does not approve the resulting plan or any
implementation, authorize specification edits, publish a contract, or
establish full v1 conformance.
