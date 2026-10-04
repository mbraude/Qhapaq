# Architecture Decision Records

Use this directory for cross-cutting technical decisions whose rationale should
remain visible after implementation.

Files use the form `NNNN-short-title.md` and record:

1. Status and date.
2. Context and constraints.
3. Decision.
4. Consequences and tradeoffs.
5. Superseded decisions or related specifications.

ADRs do not replace feature specifications. They capture implementation choices
made within the behavior required by those specifications.

## Accepted Decisions

| Decision | Summary |
| --- | --- |
| [ADR-0001](0001-use-microsoft-dependency-injection.md) | Use Microsoft dependency injection with adjacent-layer, layer-owned composition. |
| [ADR-0002](0002-use-xunit-v3-for-dotnet-tests.md) | Use xUnit v3 for .NET architecture, unit, and integration tests. |
