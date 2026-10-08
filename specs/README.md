# Specifications

Specifications define accepted or proposed Qhapaq behavior before or alongside
implementation.

| Specification | Scope |
| --- | --- |
| [SPEC-0001](0001-core-pipeline-model.md) | Core pipeline model, execution, CLI/MCP boundaries, and invocation skills. |
| [SPEC-0002](0002-operation-catalogs-and-host-configuration.md) | Operation catalogs, extensions, host configuration, and authentication. |
| [SPEC-0003](0003-product-evolution-roadmap.md) | Deferred remote providers, hosting, identity, and durability directions. |
| [SPEC-0004](0004-ai-assisted-connections.md) | AI-assisted connection planning, consent, execution, and disclosure. |
| [SPEC-0005](0005-build-release-and-website-delivery.md) | CI, edge builds, releases, provenance, and website delivery. |
| [SPEC-0006](0006-dotnet-layered-architecture.md) | .NET layers, dependency direction, visibility, service versioning, and initial component plan. |
| [SPEC-0007](0007-portable-pipeline-definitions-and-binding.md) | Canonical pipeline JSON, execution-frame dataflow, transforms, operation contracts, validation, and plan binding. |

New substantial features use the next stable numeric identifier and include
status, goals, non-goals, design, security, testing, rollout, alternatives, and
open questions as applicable. Cross-cutting implementation choices may also
require an ADR under [docs/architecture/decisions/](../docs/architecture/decisions/).

## Requirement identifiers and traceability

Specifications are the source of truth for product behavior. Product behavior
is specified before it is implemented, and implementations reference the
requirements they satisfy, as decided by
[ADR-0003](../docs/architecture/decisions/0003-enforce-specification-traceability.md).

Normative content that an implementation or test can satisfy is grouped into
requirement blocks, each starting with a stable identifier. A block is one
cohesive rule and runs to the next identifier or heading:

```markdown
**[R-0001-012]** If either branch fails, the composed operation must signal
cancellation to the other branch and must not lose the secondary failure.
```

Identifiers are never renumbered or reused. Retired requirements remain as
tombstones. Code and tests reference requirements as
`spec: R-0001-012@<fingerprint>`, where the fingerprint changes whenever any
text in the block changes, so dependent code must be reviewed with every
requirement edit.

`SPEC.md` and every numbered specification carry requirement identifiers. New
requirements take the next unused sequence number in their specification.
