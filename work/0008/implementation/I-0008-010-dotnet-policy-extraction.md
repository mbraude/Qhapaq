---
id: I-0008-010
kind: implementation
granularity: slice
change_kind: maintenance
title: Extract .NET policy and route its path instructions
status: complete
spec: SPEC-0008
requirements:
  - R-0008-004
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on:
  - D-0008-002
  - D-0008-008
  - D-0008-014
artifacts:
  - docs/development/coding-conventions.md
  - docs/development/conventions/dotnet.md
  - .github/instructions/dotnet.instructions.md
---

# I-0008-010: Extract .NET Policy and Route Its Path Instructions

## Objective and coverage

Move the maintained .NET-specific conventions and C# traceability placements
from the common conventions into a scoped .NET guide. Reduce the .NET path
instruction to policy links and any remaining path or tool-execution guidance.
Keep the portable payload, waiver, and checker rules in the common policy;
document the approved C# constructs and exact attachment rules in the .NET
guide without claiming that a C# extractor or checker is registered.

This slice covers the policy-placement portion of R-0008-017 only. It does not
implement or register an extractor, change product behavior, or claim
traceability support.

## Entry gates

- D-0008-002, D-0008-008, and D-0008-014 remain complete.
- The `engineering-policy` readiness record has been reassessed for the
  decomposed I-0008-001 scope and is approved/current for this slice.
- The exact revised plan and this slice are explicitly approved before
  execution. The existing readiness approval predates the aggregate split and
  is not sufficient without impact review.
- No SPEC-0006 or ADR amendment is required for the planned content-only move;
  any discovered semantic change is returned to the governing source.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify | `docs/development/coding-conventions.md` | Retain common policy and portable traceability rules; remove C#-specific convention and placement details and link the specialization. | Not applicable | Repository documentation |
| Add | `docs/development/conventions/dotnet.md` | Own the moved .NET conventions, .NET JSON implementation guidance, and approved C# reference and waiver placements. | Not applicable | Repository documentation |
| Modify | `.github/instructions/dotnet.instructions.md` | Preserve `applyTo`; route contributors to common and .NET policies and retain only path/tool-execution guidance. | Not applicable | Agent instruction |

## Design and integration

The .NET guide declares its scope, links the common conventions and relevant
SPEC-0006 and ADR sources, and accumulates with the common Required rules.
Transfer rather than duplicate the existing .NET-specific rules, including
the C# placement requirements now in the common traceability section and
the .NET-specific JSON implementation rule. Preserve the approved placements:
an immediately preceding `//` comment for a statement or block and test
method, and XML `<remarks>` for whole-member enforcement. Place waivers only
in those permitted constructs with the same attachment scope.

The common guide continues to own portable payload grammar, shared checker
responsibilities, and portable waiver limits. The path instruction must not
broaden marker placement or describe C# as supported for deterministic
traceability until I-0008-007 registers a matching extractor.

## Tests and validation

- Compare the transferred .NET rules against the source sections and confirm
  no rule is lost, broadened, duplicated as a competing authority, or changed
  in meaning.
- Verify the common guide retains the portable traceability and waiver rules
  and no longer prescribes C#-specific syntax or attachment.
- Verify the .NET guide states the exact statement/block, whole-member, test,
  and waiver placements, and does not claim checker support.
- Verify all relative links resolve and the `.NET` instruction `applyTo`
  pattern is unchanged and links to both policy layers.
- No repository build, format, lint, or test command is documented for this
  documentation-only slice. Record that absence; do not invent one. Run
  `git diff --check` and manual link/content checks.

## Exit criteria

- [x] Every in-scope .NET rule has one owning location in the .NET guide or
      common policy, with the common/specialized precedence intact.
- [x] The C# reference and waiver placements match D-0008-008 and R-0008-016
      through R-0008-018 exactly.
- [x] The path instruction preserves its applicability pattern and contains
      no conflicting traceability placement or competing engineering policy.
- [x] All links and whitespace checks pass; no undocumented build or test
      command is claimed.
- [x] Explicit delivery review covers the exact output snapshot.

## Plan approval

Approved explicitly by the user on 2026-10-11 for:

- Revised Phase 2 plan full-byte SHA-256:
  `8559b6347e3163b332bb1bcd1e213f191bf961b66e1e4400476ceb47a326293d`.
- This slice material SHA-256:
  `c3be1c88bc4acaa9f971d0b452abd5a0f9e0ac1957d2eefecffc3c85873c20c0`.
- This slice full-byte SHA-256 at approval:
  `b4f76c606812bfa48fae385e4c673ea8a599b861965297c5f9415f5bc89d2406`.

Full-byte SHA-256 of governing inputs reviewed:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| SPEC-0008 | `1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a` |
| SPEC-0006 | `62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653` |
| ADR-0003 | `1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83` |
| ADR-0004 | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| Common coding conventions | `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` |
| Spec-driven workflow | `574d0e18efb42b5701b148a68a62fbd4be7b748e3f276bb6424a056c152507f4` |
| D-0008-002 | `6cd4c9a0740873953903e81617c7ad9e493f2321314dcca122465f8e32920afd` |
| D-0008-008 | `e9e6f9fb099ee08b82ddcf6ca491f178ef2099d6aab2109802223619212a89ae` |
| D-0008-011 | `3f0fd4bb00e527cd3ed4f3325472edd9c75a82abbc80ed5de95ff743557a9639` |
| D-0008-012 | `e0127638451b6afa9fcb493b786b5712b2e9c86a41d4a5fdb61e76eb3fbccf08` |
| D-0008-014 | `ec527cd25f0550c436ee5276400344dfcb66982623fd71c787ad894a60ea2b35` |
| I-0008-001 aggregate | `9b17dc3774ea64c3c15b20b7f18f15a8b37b128ed791f45e2dbedbd83d0d71f4` |
| Approved readiness assessment snapshot | `007ac35cc15a8a70ea74c97bee5b436f6a4071ebecd3a981d6d3a92a7c6f4218` |
| .NET path instruction | `18eb5accd0bd3f627f35d719ca43c66ac520c2765d27e18ead4a9195148acf7f` |

Approval covers this slice and the exact revised plan only. Any material
change to scope, manifest, dependencies, or gates requires renewed approval.
Approval does not authorize contract publication or imply C# traceability
support.

## Delivery evidence and review

The approved policy move is implemented in the manifest:

| Path | SHA-256 |
| --- | --- |
| `docs/development/coding-conventions.md` | `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b` |
| `docs/development/conventions/dotnet.md` | `712c0ed6d05c230f28146b0f4447622c5c62214e4b85c4c2d53d83bac1879c24` |
| `.github/instructions/dotnet.instructions.md` | `287898a2f49f45070fc700b977a04525b3e7bc49ea84b8a9bf8f12bf1f6ff645` |

Content comparison confirmed that the .NET project organization and layering,
C# namespace rules, C# and .NET conventions, C# traceability and waiver
placements, .NET JSON implementation choice, and .NET package-version rule
have one owner in the .NET guide. Portable traceability payload and waiver
rules and portable JSON/schema rules remain in the common guide. The path
instruction's `applyTo` pattern is unchanged and it now routes to both policy
layers without repeating engineering rules.

Validation results:

- All 21 focused transfer checks passed; manual comparison against the source
  sections found no lost or broadened rule.
- Relative link targets resolve in all three policy files.
- `git diff --check` passed. Git emitted existing CRLF-to-LF normalization
  warnings.
- Build, format, lint, and test commands are not documented for this
  documentation-only slice; none were run.
- Specification trace check: `PASS`. All five in-scope files are policy,
  instruction, readiness, or work-plan documentation (`Other`); the change is
  `maintenance`, so the proposed trailer is `Change-Kind: maintenance` with no
  `Spec:` trailer. No product or test code changed, so semantic code review is
  not applicable. No operational waiver was added; the existing illustrative
  `spec-waive` example was transferred unchanged to the .NET guide.

No scope deviation or incidental manifest discovery occurred.

The user explicitly approved this exact output snapshot on 2026-10-11:

| Output | Approved SHA-256 |
| --- | --- |
| `docs/development/coding-conventions.md` | `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b` |
| `docs/development/conventions/dotnet.md` | `712c0ed6d05c230f28146b0f4447622c5c62214e4b85c4c2d53d83bac1879c24` |
| `.github/instructions/dotnet.instructions.md` | `287898a2f49f45070fc700b977a04525b3e7bc49ea84b8a9bf8f12bf1f6ff645` |

This completes I-0008-010 only. I-0008-011 and the I-0008-001 aggregate remain
open.
