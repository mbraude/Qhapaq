---
spec: "<SPEC-NNNN or COMP-NNNN>"
sources:
  - path: "<repository-relative authoritative input>"
    revision: null
    content_sha256: "<SHA-256 of exact reconciled file bytes>"
---

# <Specification ID>: Work Plan

Template only. Replace placeholders and remove this sentence when instantiated.

## Scope and authority

Link the governing specification, relevant ADRs, and related plans. State the
scope and exclusions. The plan cannot define product behavior.

## Phase <identity>: <title>

### Entry gates

Name normative gates by requirement ID and existing prerequisites.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | <relative item link and stable ID> | <persistent outcome> |

### Exit gates

State measurable completion criteria. Status and dependencies live in items.

## External prerequisites

Link cross-plan prerequisite items without copying or owning them.

## Reconciliation evidence

Record baseline revision, source snapshots, affected work, readiness impact,
unresolved blockers, and whether reconciliation is complete. Explain null
revisions for new inputs. Do not advance snapshots after incomplete review.
