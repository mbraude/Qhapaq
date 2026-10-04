# .NET Reference Implementation

This directory will contain the .NET 10 reference implementation, its solution
and pinned toolchain configuration, source projects, and tests.

The planned package boundaries are:

- `Qhapaq.Abstractions`
- `Qhapaq`
- `Qhapaq.Hosting`
- `Qhapaq.Mcp`

The self-contained `qhapaq` CLI is a separately distributed executable rather
than another reusable package. Source layout is described in [src/](src/), and
test layout is described in [tests/](tests/).

The language-neutral specifications, schemas, and conformance vectors remain at
the repository root.
