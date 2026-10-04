# .NET Source Projects

Production .NET projects will live here once the solution is scaffolded.
Projects must preserve the package boundaries defined in
[SPEC-0001](../../../specs/0001-core-pipeline-model.md) and keep hosting, CLI,
and MCP dependencies out of lower-level abstractions.

Shared portable contracts must be expressed through the root schemas and
specifications rather than inferred solely from CLR types.
