---
spec: "<SPEC-NNNN or COMP-NNNN>"
scope: "<stable scope name>"
assessment: not-assessed
process_version: 1
sources:
  - path: "<repository-relative assessed input>"
    revision: null
    content_sha256: "<SHA-256 of exact assessed file bytes>"
  - path: "<work item, for example work/NNNN/implementation/I-NNNN-NNN-name.md>"
    revision: null
    content_sha256: "<SHA-256 of exact assessed file bytes>"
    material_sha256: "<material SHA-256; governs currency of work-item sources>"
  - path: "<another plan or readiness record, for example work/NNNN/plan.md>"
    revision: null
    content_sha256: "<SHA-256 of exact assessed file bytes>"
    material_sha256: "<plan or readiness material SHA-256; governs currency>"
---

# <Specification ID>: <Scope> Readiness

Template only. Replace placeholders and remove this sentence when instantiated.

## Assessed scope

List requirement IDs, capabilities, and related decisions included in assessment.

## Exclusions

State what is not assessed; do not imply whole-release conformance.

## Completeness and consistency

Review semantics, contracts, failure behavior, limits, security/privacy,
compatibility, and cross-specification consistency. Check for unknown decisions,
not merely unchecked known items.

## Conformance and prerequisite artifacts

Link required cases, schemas, vectors, and normative delivery gates. Distinguish
specified expectations from published artifacts.

## Blockers

List missing decisions, contradictions, artifacts, or validation evidence.

## Validation and approval

Record actual checks and results, exact source snapshot, and explicit human
approval evidence. Initially absent. New material source changes require impact
review and reassessment; approval does not publish a contract.
