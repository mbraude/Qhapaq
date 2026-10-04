# Architecture Diagrams

Store maintainable diagram source files here. Prefer text-based source that can
be reviewed in diffs and regenerated deterministically. Exported images should
be committed only when documentation consumers require them and the generating
source remains beside them.

Generated pipeline Mermaid diagrams are runtime or documentation outputs and do
not define executable pipeline behavior.

Current maintained diagram sources:

- [Initial .NET layered components](dotnet-layered-components.mmd) illustrates
  the accepted dependency direction and composition-only registrations from
  [SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md).
