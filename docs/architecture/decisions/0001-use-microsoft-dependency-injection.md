# ADR-0001: Use Microsoft Dependency Injection

> **Status:** Accepted
> **Date:** 2026-10-04

## Context

The .NET reference implementation requires dependency injection to connect its
Service Implementations, versioned Service, Business, and DAL assemblies. The
selected framework must support the .NET Generic Host used by the CLI, MCP, and
future hosted entry points without exposing the container to behavioral code or
weakening the adjacent-layer dependency rules in
[SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md).

Options considered included Microsoft dependency injection, Autofac, Lamar,
Simple Injector, DryIoc, Grace, and compile-time dependency-injection
generators. The initial implementation does not require container-specific
features such as child containers, interception, convention-based assembly
scanning, or dynamic modules.

## Decision

Qhapaq will use `Microsoft.Extensions.DependencyInjection` as the dependency
injection framework for the initial .NET implementation.

- Composition APIs use `IServiceCollection`.
- Only an executable or hosting boundary may build or directly access the root
  `IServiceProvider`.
- Behavioral Service, Business, and DAL components use constructor injection
  and must not depend on `IServiceCollection`, `IServiceProvider`, or
  `IServiceScopeFactory`.
- `Qhapaq.Abstractions` remains independent of Microsoft dependency-injection
  types. Portable and cross-layer behavioral contracts do not expose container
  concepts.
- Each layer owns registration of its internal concrete implementations and
  delegates composition only to the immediately lower layer:

  ```text
  Qhapaq.Implementations.Hosting
      -> Qhapaq.Service.V1
      -> Qhapaq.Business
      -> Qhapaq.DAL
  ```

- `Qhapaq.Implementations.Hosting` invokes the public Service V1 composition
  entry point. It does not reference Business or DAL.
- Service V1 invokes only the Business composition entry point, and Business
  invokes only the DAL composition entry point. Lower-layer composition entry
  points remain internal and are visible only to their named adjacent Qhapaq
  assembly and tests.
- Registration is explicit. The initial implementation does not use
  reflection-based assembly scanning for Qhapaq services.
- Registration methods must not call `BuildServiceProvider`, resolve services,
  or run product behavior.
- Hosts enable build and scope validation in development and automated tests.

Operation identity and exact-version resolution remain responsibilities of the
Qhapaq operation registry. They must not be implemented as implicit keyed or
named container lookup.

## Consequences and Tradeoffs

- Qhapaq aligns with the .NET Generic Host and common CLI, MCP, and future gRPC
  hosting patterns without introducing a third-party container dependency.
- Explicit, layer-owned registration preserves assembly boundaries and keeps
  internal concrete types hidden from entry points.
- Most components can be tested without a container by constructing them with
  test collaborators.
- Integration and architecture tests must verify the complete object graph,
  service lifetimes, scope validation, and prohibited cross-layer references.
- Advanced features from third-party containers are unavailable unless a later
  accepted decision introduces them.
- Composition assemblies depend on Microsoft DI abstractions, but behavioral
  contracts and portable semantics remain container-independent.

## Alternatives

### One top-level composition root referencing every layer

Rejected because it would let Hosting reference Business and DAL directly,
contradicting the adjacent-layer architecture and exposing lower-layer
implementation details to the top layer.

### Autofac or another third-party container

Deferred. The initial implementation has no requirement that justifies the
additional dependency or container-specific programming model.

### Reflection-based registration

Rejected for the initial implementation because explicit registrations are
easier to review, trim, test, and constrain by layer.

### Compile-time dependency injection

Deferred until the implementation has measured startup, trimming, Native AOT,
or graph-validation requirements that Microsoft dependency injection cannot
meet adequately.

## Related Specifications

- [SPEC-0001: Core Pipeline Model](../../../specs/0001-core-pipeline-model.md)
- [SPEC-0006: .NET Layered Architecture](../../../specs/0006-dotnet-layered-architecture.md)
