---
id: D-0007-006
kind: decision
title: Stage-aware non-executing validation conclusions
status: complete
spec: SPEC-0007
requirements: [R-0007-299, R-0007-300, R-0007-301, R-0007-344, R-0007-352, R-0007-353, R-0007-400, R-0007-401, R-0007-402, R-0007-403]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-006: Non-Executing Conclusions

## Objective

Specify how early responses distinguish document validity, host bindability,
policy eligibility, and invocation-specific execution permission.

## Scope and exclusions

Stage-aware conclusions and unavailable/unknown results for non-executing slices.
Existing four-conclusion semantics remain authoritative. No execution grant,
canonical pre-normalization identity, or success-shaped unavailable conclusion.

## Questions to resolve

Which conclusions can retrieval, inert parsing, full validation, and explanation
actually establish? How are unavailable conclusions represented and mapped?
How are bind-time and invocation-time results distinguished?

## Acceptance criteria

- [x] Each early slice has explicit supported and unavailable conclusions.
- [x] Results cannot imply execution or payload-disclosure authority.
- [x] Document validity is not confused with normalized identity or bindability.
- [x] Service/CLI/MCP mappings and negative conformance cases are defined.
- [x] Related diagnostics and first-slice contracts agree; required checks pass.

## Resolution

Resolved in
[SPEC-0007 Section 14.1](../../../specs/0007-portable-pipeline-definitions-and-binding.md#141-stage-aware-conclusions):

- R-0007-400 defines the closed four-conclusion, three-state result model and
  stable unavailability reasons.
- R-0007-401 defines exact retrieval, inert-parsing, full-validation, and
  explanation outcomes. Early negative evidence can establish
  `notSatisfied`, while partial success remains `unavailable`.
- R-0007-402 separates normal unavailable or negative conclusions from
  structured operation errors when a promised evaluation cannot be performed.
- R-0007-403 requires Service-authoritative CLI/MCP preservation and the
  language-neutral negative conformance matrix.

The resolution does not name .NET APIs, CLI commands, MCP tools, or execution
contracts. Those remain with D-0007-004 and D-0007-005.

## Validation and review

Decision input: on 2026-10-09 the user explicitly selected:

- three conclusion states plus stable unavailability reasons;
- early negative evidence establishing `notSatisfied` while partial success
  remains `unavailable`; and
- normal `unavailable` results only for deliberately unevaluated,
  context-absent, or prerequisite-blocked conclusions, with structured errors
  when a promised conclusion cannot be evaluated.

Validation performed on 2026-10-09:

- Work-artifact structure: PASS. Checked 50 unique item identities, required
  sections, 97 dependency edges, acyclic ordering, no unknown or cancelled
  prerequisite, one phase membership per 0007 item, and 187 existing
  requirement references.
- Specification structure: PASS. All 403 R-0007 identifiers are unique;
  R-0007-400 through R-0007-403 are the next unused sequence, and no prior
  identifier was removed or retired.
- Specification trace check: PASS. Classified as `requirement` because the
  change adds four platform requirement blocks. Repository-wide reverse-impact
  search found no stale code or test fingerprint, no changed implementation,
  and no new waiver. Semantic review checked R-0007-299 through R-0007-301,
  R-0007-344, R-0007-352, R-0007-353, R-0007-368, and new R-0007-400 through
  R-0007-403 against the four-conclusion, permission/disclosure, inert-parsing,
  Service-authority, and no-success-fallback invariants.
- Contract consistency: PASS. Retrieval establishes no pipeline conclusion;
  structural failures can disprove document validity without a successful parse
  claiming complete validity; full validation establishes conclusions only in
  dependency order; explanation cannot upgrade them; and unexpected inability
  to evaluate a promised conclusion is not returned as success.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  all 74 local links in changed Markdown resolve, and all 11 plan source hashes
  match exact current bytes.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `9729e685b998e39083ddc15ed52a0df4bff2a6cf4fb00c8ca44ed1dc32258397` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `73cfabd8e5fcc8d010ad8036ab53324dd1947bd7e8c485c8098ed99b29b12b3d` |
| `work/0007/plan.md` | SHA-256 `c5e5bbbaae9d2ceca68b1f96910c89f15916513da6396dbf059dc6e3b7600a6b` |
| `work/0007/decisions/D-0007-004-exact-descriptor-service.md` | SHA-256 `84cb7f7a3c6b2ede76c6cc3027570e259c13a438f6ac401a7cff79ed8af51dca` |
| `work/0007/decisions/D-0007-005-subsequent-surface-contracts.md` | SHA-256 `c33101894930f2a52e05ee7a223218bd9e2ae586a67f591ae1c51266a772a276` |
| `work/0007/implementation/I-0007-011-first-service-cli-slice.md` | SHA-256 `2713fa4f9f49f587008f28f222c6192f6c397ea63818e3feff4d59ae7bf67e80` |
| `work/0007/implementation/I-0007-012-inert-parsing.md` | SHA-256 `7b9e685bff0d734986b489e6a39bd643e3ee38d110c2ec25a877fec836aaaf48` |
| `work/0007/implementation/I-0007-024-authoring-projections.md` | SHA-256 `acd23cc1309d9814dccc7d63636843d877cf2efe8842bef740fc68f5d233f06e` |

Approval is absent. Ready-for-review does not authorize implementation,
publication, execution, payload disclosure, or a specification-readiness claim.

Approval recorded on 2026-10-09: the user explicitly approved this exact
snapshot in this session.

Approved scope: D-0007-006 and its stage-aware non-executing conclusion outcome,
including the bounded SPEC-0007 plan reconciliation and directly affected
downstream requirements, decisions, and milestones. Commit scope is exactly
this decision, SPEC-0007, `work/0007/plan.md`, D-0007-004, D-0007-005,
I-0007-011, I-0007-012, and I-0007-024. Exclusions: implementation, schemas,
conformance vectors, contract publication, execution, payload-disclosure
authority, and specification-readiness approval.

Approval covers unchanged material content with SHA-256
`9729e685b998e39083ddc15ed52a0df4bff2a6cf4fb00c8ca44ed1dc32258397` and
these exact full-byte snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `73cfabd8e5fcc8d010ad8036ab53324dd1947bd7e8c485c8098ed99b29b12b3d` |
| `work/0007/plan.md` | `c5e5bbbaae9d2ceca68b1f96910c89f15916513da6396dbf059dc6e3b7600a6b` |
| `work/0007/decisions/D-0007-004-exact-descriptor-service.md` | `84cb7f7a3c6b2ede76c6cc3027570e259c13a438f6ac401a7cff79ed8af51dca` |
| `work/0007/decisions/D-0007-005-subsequent-surface-contracts.md` | `c33101894930f2a52e05ee7a223218bd9e2ae586a67f591ae1c51266a772a276` |
| `work/0007/implementation/I-0007-011-first-service-cli-slice.md` | `2713fa4f9f49f587008f28f222c6192f6c397ea63818e3feff4d59ae7bf67e80` |
| `work/0007/implementation/I-0007-012-inert-parsing.md` | `7b9e685bff0d734986b489e6a39bd643e3ee38d110c2ec25a877fec836aaaf48` |
| `work/0007/implementation/I-0007-024-authoring-projections.md` | `acd23cc1309d9814dccc7d63636843d877cf2efe8842bef740fc68f5d233f06e` |

Approval and completion do not authorize implementation, contract publication,
execution, payload disclosure, or specification readiness.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-400@d64d22, R-0007-401@031d0f, R-0007-402@cd904b, R-0007-403@7d17ca
```
