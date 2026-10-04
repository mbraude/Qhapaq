# ADR-0002: Use xUnit v3 for .NET Tests

> **Status:** Accepted
> **Date:** 2026-10-04

## Context

The initial .NET scaffold requires architecture, unit, integration, and
package-consumer tests. The repository needs one test framework before those
projects can provide executable checks. The framework must support the pinned
.NET 10 SDK, deterministic parallel-safe tests, command-line execution through
`dotnet test`, and common editor and CI integrations.

The options considered were xUnit v3, MSTest, and NUnit.

## Decision

Qhapaq .NET test projects use xUnit v3.

- Test dependencies are centrally versioned in
  `implementations/dotnet/Directory.Packages.props`.
- Test projects use `Microsoft.NET.Test.Sdk` and the `xunit.v3` package.
- Tests remain deterministic, parallel-safe, and independent of execution
  order as required by the coding conventions.
- Architecture rules are tested with platform reflection and project-file
  inspection initially. A dedicated architecture-testing package may be added
  only when its value justifies another dependency.

## Consequences and Tradeoffs

- Contributors use one test model across unit, integration, architecture, and
  package-consumer projects.
- xUnit v3 provides current .NET support and can run through standard .NET test
  tooling.
- The repository takes a development dependency on xUnit v3 and its transitive
  packages.
- Contributors familiar with MSTest or NUnit must use xUnit conventions in
  this repository.
- A future framework migration would affect the full .NET test suite and
  requires a superseding ADR.

## Alternatives

### MSTest

Not selected. Its first-party integration is strong, but Qhapaq does not
currently need framework-specific Microsoft test features.

### NUnit

Not selected. It is capable and mature, but does not provide a compelling
advantage for the initial Qhapaq test model.

## Related Specifications

- [SPEC-0005: Build, Release, and Website Delivery](../../../specs/0005-build-release-and-website-delivery.md)
- [SPEC-0006: .NET Layered Architecture](../../../specs/0006-dotnet-layered-architecture.md)
