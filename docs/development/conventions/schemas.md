# Schema and Conformance Conventions

**Applies to:** JSON schemas and conformance artifacts under `schemas/` and
`conformance/`.

These rules specialize the [common coding conventions](../coding-conventions.md)
for maintained schemas and conformance artifacts. Follow [AGENTS.md](../../../AGENTS.md),
[SPEC.md](../../../SPEC.md), and the applicable
[numbered specifications](../../../specs/README.md), including
[SPEC-0007](../../../specs/0007-portable-pipeline-definitions-and-binding.md)
where it governs pipeline definitions and binding.
[SPEC-0008 R-0008-004](../../../specs/0008-multi-language-conformance-and-repository-organization.md#5-engineering-policy-ownership-and-applicability)
defines this guide's policy ownership; it does not replace artifact-specific
product requirements.

## Authoring

- Keep schemas and vectors language-neutral and versioned.
- Use stable identifiers and offline-resolvable references.
- Reject unknown versions and ambiguous fields.
- Do not include CLR type names, executable source, credentials, secrets, or
  machine-specific paths.
- Make semantically relevant ordering and canonicalization expectations
  explicit.
- Pair schema behavior with valid, invalid, and boundary conformance cases.
- Treat a breaking contract change as a new version with documented migration
  and compatibility consequences.
- Keep expected outputs deterministic across operating systems, architectures,
  cultures, and time zones.
