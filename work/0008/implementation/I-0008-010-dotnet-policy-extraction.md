---
id: I-0008-010
kind: implementation
granularity: slice
change_kind: maintenance
title: Extract .NET policy and route its path instructions
status: open
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

- [ ] Every in-scope .NET rule has one owning location in the .NET guide or
      common policy, with the common/specialized precedence intact.
- [ ] The C# reference and waiver placements match D-0008-008 and R-0008-016
      through R-0008-018 exactly.
- [ ] The path instruction preserves its applicability pattern and contains
      no conflicting traceability placement or competing engineering policy.
- [ ] All links and whitespace checks pass; no undocumented build or test
      command is claimed.
- [ ] Explicit delivery review covers the exact output snapshot.

## Plan approval

Absent. Record explicit approval of the exact material plan and full-byte
hashes of governing inputs before execution. Any material change requires
renewed approval.

## Delivery evidence and review

No implementation, delivery evidence, or approval recorded.
