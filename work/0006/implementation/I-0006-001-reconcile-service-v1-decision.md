---
id: I-0006-001
kind: implementation
granularity: slice
change_kind: editorial
title: Reconcile SPEC-0006's first Service V1 use-case references
status: open
spec: SPEC-0006
requirements:
  - R-0006-004
  - R-0006-005
  - R-0006-033
depends_on:
  - D-0007-004
artifacts:
  - specs/0006-dotnet-layered-architecture.md
---

# I-0006-001: Reconcile the First Service V1 Use-Case References

## Objective and coverage

Update SPEC-0006's remaining open-question and rollout references to reflect the
first Service V1 use case and public contracts already accepted by SPEC-0007
D-0007-004 and R-0007-404 through R-0007-410. This is a documentation alignment
change only; it does not select or change product behavior, APIs, or rollout
requirements.

## Entry gates

SPEC-0007 D-0007-004 remains complete and its exact descriptor-retrieval
contracts remain in force. Review SPEC-0006 and the referenced SPEC-0007
requirements together before editing.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| modify | `specs/0006-dotnet-layered-architecture.md` | Replace the resolved first-use-case questions with cross-references and align rollout text with the existing work owners | Not applicable | Normative specification |

## Design and integration

Keep SPEC-0007 authoritative for the exact descriptor-retrieval Service V1 and
CLI contracts. Preserve SPEC-0006's layer responsibilities and R-0006-033
rollout gate. Do not duplicate R-0007 contract semantics or alter requirement
identifiers; record any discovered inconsistency as a blocker for review rather
than silently changing behavior.

## Tests and validation

- Confirm the linked D-0007-004 and R-0007-404 through R-0007-410 requirements
  still exist and support the exact references added.
- Run the documented specification traceability check and review reverse
  references for any changed requirement block.
- Check local Markdown links, requirement IDs, and formatting with the
  repository-documented checks. No product build or unit test is implied.

## Exit criteria

- [ ] Resolved first-Service choices are no longer presented as unresolved in SPEC-0006.
- [ ] Cross-specification ownership and links are accurate.
- [ ] No requirement semantics, IDs, or implementation ownership are changed.
- [ ] Required traceability, link, and formatting checks pass.
- [ ] Explicit review covers the exact resulting specification snapshot.

## Plan approval

Approved in this session on 2026-10-12 for the exact execution scope below.

Approved material snapshot SHA-256:
`2a3dd7e53335e09beb9525bf45ea6f70faa37b1793c61f07518ef8758d8da4f7`.

Approved scope: this documentation-only slice modifies
`specs/0006-dotnet-layered-architecture.md` to reconcile its first Service V1
use-case and rollout wording with completed SPEC-0007 decision D-0007-004 and
R-0007-404 through R-0007-410. It preserves requirement identifiers,
semantics, layer responsibilities, and implementation ownership.

Exclusions: Service runtime or CLI implementation, architecture scaffolding,
migrations, schemas or vectors, I-0006-002, full SPEC-0006 conformance, and
contract publication. This plan approval authorizes execution of this slice
only; delivery review remains separate.

Readiness gate: approved `service-v1-reconciliation`, covering R-0006-004,
R-0006-005, and R-0006-033. Its assessed material SHA-256 is
`606ed20364be5a7ec1c8f88528a2756815ab9108277dd015e3c39ebb65d235e5`.
The completed direct prerequisite D-0007-004 depends on completed D-0007-006;
both prerequisite items and all listed inputs were verified current at
approval.

Full-byte SHA-256 values of material approval inputs:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `docs/development/spec-driven-workflow.md` | `c1045d2891c7ccbe00c833e247d7254c7e4161857dfe6884b47a644cb3e1c11e` |
| `docs/development/coding-conventions.md` | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/conventions/specifications.md` | `9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a` |
| `.github/instructions/specifications.instructions.md` | `7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2` |
| `work/0006/plan.md` | `b74bb5a11087fb1c92950b29246d3ccbf2a446812c8b1168a7c6ccb6e3709a5d` |
| `specs/0006-dotnet-layered-architecture.md` | `785bc5aba6b82f1aa3e73a84d86d91fcf4c7d0a3bb0425f2a389d1d874940732` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `work/0006/readiness/service-v1-reconciliation.md` | `642103b9ee6bc580561437cf6e7d9ab3cf6e05611a633f4a77f01b423998b2b8` |
| `work/0007/plan.md` | `4c1cb8bd2aefb2e2cbfa1d17d77942ff926c94c4bbba147d71dfe1cfe05775f2` |
| `work/0007/decisions/D-0007-004-exact-descriptor-service.md` | `86b5676dae2c007e280228294cba24d0632825cb2bdaeba656d6cb97ff194a4e` |
| `work/0007/decisions/D-0007-006-non-executing-conclusions.md` | `70543687f3ed0bdfc445a5eb7aafe774da5224dbf4d26f09503122e7e2c040ac` |

## Delivery evidence and review

No specification edit or validation has been performed by this work item.
