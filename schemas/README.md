# Schemas

This directory will contain normative, versioned, language-neutral schemas for
Qhapaq documents and protocol envelopes.

Initial schema families are expected to cover:

- Pipeline definitions.
- Operation descriptors, catalogs, and extension manifests.
- Host-visible connection plans and sanitized status.
- Structured errors and execution results.
- Portable invocation-skill manifests.

The initial operation-descriptor schema is
[`operation-descriptor-v1alpha1.schema.json`](operation-descriptor-v1alpha1.schema.json).
It defines the basic structural envelope while the descriptor vocabularies and
nested Qhapaq JSON Schema profile continue to evolve toward immutable `v1`.

Schema identifiers and references must be stable, resolvable without ambient
network access during validation, and tested through
[conformance/](../conformance/). Breaking changes require a new schema or
document-format version.
