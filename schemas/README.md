# Schemas

This directory will contain normative, versioned, language-neutral schemas for
Qhapaq documents and protocol envelopes.

Initial schema families are expected to cover:

- Pipeline definitions.
- Operation catalogs and extension manifests.
- Host-visible connection plans and sanitized status.
- Structured errors and execution results.
- Portable invocation-skill manifests.

Schema identifiers and references must be stable, resolvable without ambient
network access during validation, and tested through
[conformance/](../conformance/). Breaking changes require a new schema or
document-format version.
