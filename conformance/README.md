# Conformance

This directory will contain language-neutral vectors used to verify compatible
Qhapaq implementations and hosts.

Conformance data is organized by declared capability:

- Definition parsing, validation, and canonicalization.
- Deterministic Mermaid visualization.
- Composition and execution behavior.
- CLI and MCP host contracts.
- Portable invocation-skill bundles.

Each suite must contain valid, invalid, and behavioral cases with versioned
expected results. Tests must not depend on .NET implementation details or
network access unless a suite explicitly defines that boundary.

The normative conformance model is described in
[SPEC-0001](../specs/0001-core-pipeline-model.md).
