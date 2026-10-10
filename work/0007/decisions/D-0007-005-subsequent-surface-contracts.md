---
id: D-0007-005
kind: decision
title: Minimal subsequent Service, CLI and MCP contracts
status: complete
spec: SPEC-0007
requirements: [R-0007-344, R-0007-368, R-0007-369, R-0007-399, R-0007-400, R-0007-401, R-0007-402, R-0007-403, R-0007-411, R-0007-412, R-0007-413, R-0007-414, R-0007-415, R-0007-416, R-0007-417, R-0007-418, R-0007-419, R-0007-420, R-0007-421, R-0007-422, R-0007-423]
depends_on: [D-0007-004, D-0007-006]
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-005: Subsequent Surface Contracts

## Objective

Resolve the subsequent-surface contracts in R-0007-344 and the remainder of
Section 23 question 2, building on the first retrieval slice and conclusions.

## Scope and exclusions

Smallest versioned authoring/validation/explanation and execution surfaces needed
by later slices. Do not front-load unrelated authentication or release detail.
Invocation-skill and companion-specific protocols remain under their own owners.
Versioned catalog membership is host/Service configuration over exact operation
references, not operation declaration or manifest metadata.

## Questions to resolve

Which public use cases, exact CLI commands, MCP tool requests/results, structured
errors, and execution mappings are required next? Which surfaces are explicitly
deferred, and what capability advertisements distinguish unavailable behavior?
How do Service/catalog versions include, omit, or replace exact operation
contracts without changing their declarations?

## Acceptance criteria

- [x] Exact minimal contracts and version identities are recorded.
- [x] Authoring and execution operations remain separate.
- [x] All four conclusions and independent disclosure/permission decisions survive
  Service and transport mappings.
- [x] Deferred contracts are explicit; no placeholder protocol is advertised.
- [x] Required adapter, compatibility, failure, cancellation, and conformance
  cases are specified.
- [x] Catalog-version membership and policy-filtered projection satisfy
  R-0007-399 without duplicating operation implementations.
- [x] Checks pass and the exact ready-for-review snapshot is recorded.

## Resolution

Resolved in
[SPEC-0007 Section 14.3](../../../specs/0007-portable-pipeline-definitions-and-binding.md#143-subsequent-service-cli-and-mcp-surfaces):

- R-0007-411 and R-0007-412 define distinct typed Service V1 operations,
  versioned envelopes, bounded raw UTF-8 JSON input, and exact catalog
  selection.
- R-0007-413 through R-0007-415 define immutable catalog identity and membership,
  separate implementation provenance, policy-filtered pagination, and
  capability introspection.
- R-0007-416 and R-0007-417 keep authoring and execution separate and preserve
  the four conclusions plus independent execution and result-disclosure
  decisions.
- R-0007-418 through R-0007-421 define exact CLI grammar, shared exit statuses,
  distinct MCP tools, omission of disabled tools, and closed structured errors.
- R-0007-422 and R-0007-423 define explicit deferrals, adapter boundaries,
  cancellation, security, and language-neutral conformance coverage.

The accepted topology uses one typed operation per use case with shared
versioned primitives. Catalog membership changes require a new exact catalog
version and digest, while implementation-only fixes retain portable contract
identity and change separate implementation provenance. No additional decision
item is required.

## Validation and review

Decision input: on 2026-10-10 the user explicitly selected:

- distinct typed operations per use case;
- bounded raw UTF-8 JSON document input, loaded by CLI from a file or standard
  input and passed by MCP as JSON text;
- immutable catalog ID, exact Semantic Versioning version, and canonical
  contract-membership digest, separate from implementation artifact identity;
- versioned capability introspection with disabled reasons and MCP registration
  of enabled tools only;
- exact catalog ID/version selection with an optional digest precondition;
- separate inline-definition and exact-reference execution operations;
- completed execution with output withheld when result disclosure is denied;
- shared CLI statuses `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, and `130`;
- descriptor-list pages defaulting to `100`, limited to `1000`, with opaque
  snapshot-bound continuation; and
- the `capabilities`, `operation list`, and
  `pipeline parse|validate|explain|mermaid|compare|run` CLI family with distinct
  corresponding MCP tools.

No implementation, schema, conformance vector, catalog, registry, policy,
execution capability, publication, or payload-disclosure authority is approved
by this decision.

Validation performed on 2026-10-10:

- Work-artifact structure: PASS. Checked 48 unique item identities, all
  dependency targets, no cancelled prerequisites, acyclic ordering, one phase
  membership for each affected milestone, and all 12 exact plan source
  snapshots.
- Specification structure: PASS. All 423 R-0007 identifiers are unique;
  R-0007-411 through R-0007-423 are the next unused sequence, and no prior
  identifier was removed or retired.
- Specification trace check: PASS with one warning. Classified as
  `requirement` because the change adds 13 platform requirement blocks.
  Repository-wide reverse-impact review found no changed code or tests, stale
  fingerprint, removed requirement, or waiver. The warning is expected because
  the explicitly .NET-specific Service subsection names public CLR contracts.
- Semantic review: PASS. Checked the new requirements against R-0007-268,
  R-0007-297 through R-0007-301, R-0007-344, R-0007-368, R-0007-369,
  R-0007-399 through R-0007-410, R-0002-028 through R-0002-035,
  R-0001-043 through R-0001-047, and R-0001-048 through R-0001-063.
  Exact selection, immutable catalog membership, capability advertisement,
  stage-aware conclusions, adapter authority, permission/disclosure
  independence, filesystem boundaries, and non-durable execution remain
  consistent.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  local links in all seven changed Markdown files resolve, all changed
  work-item requirement references resolve, and all plan source hashes match
  exact current bytes.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `8098aa39e4c4a26a1fb5da462cd74188cb068ed526ed5e20c69ae558b467b5d6` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `7b3c946a9fd554e9b7129bc391dc68957633716f6a3264cdd659954704413249` |
| `work/0007/plan.md` | SHA-256 `27a91433a0d523b20f4080ad6e230ac3f602da57c1ca8f9e9baba17b578debcc` |
| `work/0007/implementation/I-0007-009-registry-native-bindings.md` | SHA-256 `0cd5010995310b6d62401fc4fb8906ae332178667bdedaa023aaf43d1593193e` |
| `work/0007/implementation/I-0007-010-trusted-host-policy.md` | SHA-256 `8da47f34c14b8a781784bcd3350a3ea7fc1d98000376e300f61a3305dc0f0679` |
| `work/0007/implementation/I-0007-024-authoring-projections.md` | SHA-256 `ed6cdbab4d73eca1af50a5686c905c605294cb06cd7405db2435aa8d25518741` |
| `work/0007/implementation/I-0007-025-enable-execution.md` | SHA-256 `1d5e0029a7e4b9ac448898f1fe61d72a3bb62d5abcc59f0b99042c8547f4a9a9` |

Approval recorded on 2026-10-10: the user explicitly approved this exact
snapshot in this session.

Approved scope: D-0007-005 and its subsequent versioned Service, CLI, and MCP
contract outcome, including the bounded SPEC-0007 plan reconciliation and the
requirement/dependency updates to I-0007-009, I-0007-010, I-0007-024, and
I-0007-025. Commit scope is exactly this decision, SPEC-0007,
`work/0007/plan.md`, and those four implementation milestones.

Exclusions: implementation, schemas, conformance vectors, catalog, registry,
policy, execution capability, payload-disclosure authority, contract
publication, and specification readiness.

Approval covers unchanged material content with SHA-256
`8098aa39e4c4a26a1fb5da462cd74188cb068ed526ed5e20c69ae558b467b5d6`
and these exact full-byte snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `7b3c946a9fd554e9b7129bc391dc68957633716f6a3264cdd659954704413249` |
| `work/0007/plan.md` | `27a91433a0d523b20f4080ad6e230ac3f602da57c1ca8f9e9baba17b578debcc` |
| `work/0007/implementation/I-0007-009-registry-native-bindings.md` | `0cd5010995310b6d62401fc4fb8906ae332178667bdedaa023aaf43d1593193e` |
| `work/0007/implementation/I-0007-010-trusted-host-policy.md` | `8da47f34c14b8a781784bcd3350a3ea7fc1d98000376e300f61a3305dc0f0679` |
| `work/0007/implementation/I-0007-024-authoring-projections.md` | `ed6cdbab4d73eca1af50a5686c905c605294cb06cd7405db2435aa8d25518741` |
| `work/0007/implementation/I-0007-025-enable-execution.md` | `1d5e0029a7e4b9ac448898f1fe61d72a3bb62d5abcc59f0b99042c8547f4a9a9` |

Approval and completion do not authorize implementation, contract publication,
execution, payload disclosure, or specification readiness.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-411@212053, R-0007-412@001686, R-0007-413@6cc3ff
Spec: R-0007-414@91add2, R-0007-415@1a6d47, R-0007-416@f5fbea
Spec: R-0007-417@3d8c63, R-0007-418@e5c803, R-0007-419@d0989c
Spec: R-0007-420@01e9f0, R-0007-421@6159da, R-0007-422@610e33
Spec: R-0007-423@e4363d
```
