---
id: "I-<owner>-<sequence>"
kind: implementation
granularity: milestone
change_kind: "<ADR-0004 change kind>"
title: "<outcome>"
status: open
spec: "<SPEC-NNNN or COMP-NNNN>"
requirements: []
depends_on: []
artifacts: []
---

# <ID>: <Title>

Template only. Replace placeholders and remove this sentence when instantiated.

## Objective and coverage

State the demonstrable outcome, requirements covered, incomplete behavior,
exclusions, and any child slices. A milestone is not executable.

## Entry gates

Link approved scope readiness, prerequisite items, schemas/vectors, and normative
gates. State which evidence is still missing.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| <add/modify/delete> | <exact path> | <responsibility> | <owner or not applicable> | <visibility or not applicable> |

Milestones may state that detail is pending. A slice must replace that statement
and populate an exact manifest before approval and execution.

## Design and integration

Describe contracts, collaborators, existing helpers, dependency direction,
registration, and compatibility implications. Do not invent product behavior.

## Tests and validation

Identify conformance groups, regression cases, architecture and integration
tests, existing commands, and expected results. Record missing tooling as a
blocker where required.

## Exit criteria

- [ ] Specified outcome and persistent artifacts exist.
- [ ] Required tests and validation pass.
- [ ] Material deviations have been reviewed and approved.
- [ ] Explicit delivery review covers the exact implemented snapshot.

Add measurable slice-specific criteria.

## Plan approval

Initially absent. Record explicit approval of scope, manifest, dependencies,
and gates using a reviewed revision or the item's material SHA-256 defined in
the workflow guide, plus full-byte hashes of its governing inputs. Do not create
a separate review file solely for hashing. Require reapproval when material
plan content changes.

## Delivery evidence and review

Record actual files, tests/results, deviations, remaining blockers, exact
reviewed input/output snapshot, and explicit approval. Plan approval is not
delivery approval or publication.
