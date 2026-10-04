# .NET Reference Implementation

This directory will contain the .NET 10 reference implementation, its solution
and pinned toolchain configuration, source projects, and tests.

The planned public package boundaries are:

- `Qhapaq.Abstractions`, containing the supported public Service and
  operation-authoring contracts plus internal cross-layer contracts
- `Qhapaq`, containing `Qhapaq.Service.V1`, `Qhapaq.Business`, and
  `Qhapaq.DAL`
- `Qhapaq.Hosting`, containing `Qhapaq.Implementations.Hosting`
- `Qhapaq.Mcp`, containing `Qhapaq.Implementations.MCP`

The self-contained `qhapaq` CLI is a separately distributed executable rather
than another reusable package. Its assembly and root namespace are
`Qhapaq.Implementations.CLI`. Source layout is described in [src/](src/), and
test layout is described in [tests/](tests/).

The implementation follows the Service Implementations -> versioned Service ->
Business -> DAL dependency direction. The authoritative layer responsibilities,
visibility rules, initial file plan, and component diagram are in
[SPEC-0006](../../specs/0006-dotnet-layered-architecture.md).

The language-neutral specifications, schemas, and conformance vectors remain at
the repository root.
