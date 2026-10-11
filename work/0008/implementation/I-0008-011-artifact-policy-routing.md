---
id: I-0008-011
kind: implementation
granularity: slice
change_kind: maintenance
title: Separate artifact-authoring policy from path instructions
status: open
spec: SPEC-0008
requirements:
  - R-0008-004
depends_on:
  - D-0008-002
artifacts:
  - docs/development/conventions/documentation.md
  - docs/development/conventions/schemas.md
  - docs/development/conventions/specifications.md
  - .github/instructions/documentation.instructions.md
  - .github/instructions/schemas.instructions.md
  - .github/instructions/specifications.instructions.md
---

# I-0008-011: Separate Artifact-Authoring Policy from Path Instructions

## Objective and coverage

Move the substantive authoring rules from the documentation, schema, and
specification path instructions into scoped policy guides under
`docs/development/conventions/`. Leave each path instruction as a concise
route to the common and applicable specialized policies, plus any path or
tool-execution guidance permitted by R-0008-004.

This slice reorganizes engineering policy only. It does not change normative
product requirements, schema contracts, or specification-authoring decisions.

## Entry gates

- D-0008-002 remains complete.
- The `engineering-policy` readiness record has been reassessed for the
  decomposed I-0008-001 scope and is approved/current for this slice.
- The exact revised plan and this slice are explicitly approved before
  execution. The existing readiness approval predates the aggregate split and
  is not sufficient without impact review.
- Any proposed change to an authoring rule's meaning is excluded and must be
  resolved in its authoritative policy or specification before this slice
  proceeds.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Add | `docs/development/conventions/documentation.md` | Own the maintained documentation authoring rules currently in the documentation path instruction. | Not applicable | Repository documentation |
| Add | `docs/development/conventions/schemas.md` | Own schema and conformance-artifact authoring rules currently in the schema path instruction. | Not applicable | Repository documentation |
| Add | `docs/development/conventions/specifications.md` | Own specification-authoring rules currently in the specification path instruction, linking authoritative specification policy rather than restating product behavior. | Not applicable | Repository documentation |
| Modify | `.github/instructions/documentation.instructions.md` | Preserve `applyTo` and route to common and documentation-specific policy. | Not applicable | Agent instruction |
| Modify | `.github/instructions/schemas.instructions.md` | Preserve `applyTo` and route to common, schema-specific, and applicable product policy. | Not applicable | Agent instruction |
| Modify | `.github/instructions/specifications.instructions.md` | Preserve `applyTo` and route to common and specification-specific policy. | Not applicable | Agent instruction |

## Design and integration

Each specialized guide declares its maintained artifact scope, links the
common conventions and applicable authoritative sources, and owns only
artifact-specific authoring concerns. Preserve the current rules' meaning
while transferring them; avoid duplicating common rules or copying normative
product behavior into the guides. The three instructions retain their current
path matching patterns and link to the policy that applies to those paths.

## Tests and validation

- Map every substantive rule in the three current instructions to one
  specialized guide or an existing common rule; document any omitted line as
  routing/tool-execution material rather than silently dropping it.
- Verify the guides declare scope, link common and relevant authoritative
  sources, and do not create conflicting policy.
- Verify each `.github` instruction preserves its existing `applyTo` pattern
  and contains only routing or permitted tool-execution guidance.
- Verify all relative links resolve and run `git diff --check`.
- No repository build, format, lint, or test command is documented for this
  documentation-only slice. Record that absence; do not invent one.

## Exit criteria

- [ ] All authoring rules remain present with unchanged meaning in exactly one
      policy source.
- [ ] All three path instructions retain their applicability and route to the
      correct common and specialized guides.
- [ ] No path instruction remains a competing engineering-policy source.
- [ ] All links and whitespace checks pass; no undocumented build or test
      command is claimed.
- [ ] Explicit delivery review covers the exact output snapshot.

## Plan approval

Absent. Record explicit approval of the exact material plan and full-byte
hashes of governing inputs before execution. Any material change requires
renewed approval.

## Delivery evidence and review

No implementation, delivery evidence, or approval recorded.
