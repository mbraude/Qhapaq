---
applyTo: "implementations/dotnet/**/*.cs,implementations/dotnet/**/*.csproj,implementations/dotnet/**/*.props,implementations/dotnet/**/*.targets"
---

# .NET Instructions

Follow [AGENTS.md](../../AGENTS.md) and the
[coding conventions](../../docs/development/coding-conventions.md).

- Target the pinned .NET 10 SDK and do not use unpinned preview features.
- Preserve the package dependency direction defined by SPEC-0001.
- Enable nullable reference types and maintain type safety without broad
  suppressions or unnecessary casts.
- Propagate cancellation through asynchronous code. Do not block on tasks or
  create unowned background work.
- Keep portable contracts independent of CLR type names and implementation-only
  serialization details.
- Validate complete input and policy before side effects.
- Keep secrets and operation payloads out of logs and diagnostics by default.
- Add focused unit or integration tests with every behavioral change.
- Update public API documentation and compatibility expectations when changing
  a public surface.
- Implement only behavior described by a specification requirement. Add
  `spec: <requirement-id>@<fingerprint>` references at the type, member, or
  block level and in verifying tests, following the
  [specification traceability conventions](../../docs/development/coding-conventions.md#3-specification-traceability).
