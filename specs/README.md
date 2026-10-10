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
| [SPEC-0008](0008-multi-language-conformance-and-repository-organization.md) | Draft discussion of multi-language conformance profiles, source organization, and language/artifact conventions; requirements remain unresolved. |

Platform specifications define the platform. Individual components that work
within platform contracts, such as operations, connectors, decorators, and
credential providers, are specified separately in
[component specifications](components/README.md).

New substantial features use the next stable numeric identifier and include
status, goals, non-goals, design, security, testing, rollout, alternatives, and
open questions as applicable. Cross-cutting implementation choices may also
require an ADR under [docs/architecture/decisions/](../docs/architecture/decisions/).

## Requirement identifiers and traceability

Specifications are the source of truth for product behavior. Product behavior
is specified before it is implemented, as decided by
[ADR-0003](../docs/architecture/decisions/0003-enforce-specification-traceability.md)
and amended by
[ADR-0004](../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md).
The specification library, which is `SPEC.md`, the numbered specifications,
and the [component specifications](components/README.md), must be sufficient
to reproduce the system in a new implementation. Specifications never
reference implementation code.

Normative content that an implementation or test can satisfy is grouped into
requirement blocks, each starting with a stable identifier. A block is one
cohesive rule and runs to the next identifier or heading:

```markdown
**[R-0001-012]** If either branch fails, the composed operation must signal
cancellation to the other branch and must not lose the secondary failure.
```

Identifiers are never renumbered or reused. Retired requirements remain as
tombstones. A reference has the form `spec: R-0001-012@<fingerprint>`, where
the fingerprint changes whenever any text in the block changes, so dependent
code must be reviewed with every requirement edit.

Each commit records the requirements it implements in `Spec:` trailers. Code
carries an inline reference only where it enforces a requirement, and tests
reference the requirements they verify.

`SPEC.md` and every numbered specification carry requirement identifiers. New
requirements take the next unused sequence number in their specification.

## Kinds of change

Every change is one of the following kinds, as defined by ADR-0004.

| Kind | When to use it | Specification change |
| --- | --- | --- |
| `requirement` | Add a platform capability, contract, or trust boundary. | New blocks in `SPEC.md` or a numbered specification. |
| `amendment` | Change the meaning of an existing requirement. | Edit the block in place and update the code that references it. |
| `extension` | Add or change a component, such as an operation, within existing platform contracts. | A new or changed [component specification](components/README.md). |
| `bug` | Make code conform to a requirement it violates. | None; add a regression test that references the requirement. |
| `editorial` | Reword without changing meaning. | Reworded blocks; review and update references. |
| `refactor` | Restructure without changing behavior. | None. |
| `maintenance` | Change build, tooling, skills, documentation, or tests of existing behavior. | None. |

If the specification is wrong, ambiguous, or silent about a defect, the fix is
an `amendment`, not a `bug`. If a new component needs a platform change, that
change is a `requirement` or `amendment` made first.
