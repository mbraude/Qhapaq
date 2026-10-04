# .NET Source Projects

Production .NET projects will live here once the solution is scaffolded.
Projects must preserve the package boundaries defined in
[SPEC-0001](../../../specs/0001-core-pipeline-model.md) and keep hosting, CLI,
and MCP dependencies out of lower-level abstractions.

The planned project and folder structure is defined in
[SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md). Production
calls follow Service Implementations -> versioned Service -> Business -> DAL,
cross only adjacent boundaries through dependency-injected abstractions, and
keep concrete lower-layer types internal. Each production project's assembly
name and root namespace match its layer, including `Qhapaq.Service.V1`,
`Qhapaq.Business`, `Qhapaq.DAL`, and `Qhapaq.Implementations.*`.

Shared portable contracts must be expressed through the root schemas and
specifications rather than inferred solely from CLR types.
