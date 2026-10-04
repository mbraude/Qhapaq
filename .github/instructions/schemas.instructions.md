---
applyTo: "schemas/**/*.json,conformance/**/*.json"
---

# Schema and Conformance Instructions

Follow [AGENTS.md](../../AGENTS.md), the
[coding conventions](../../docs/development/coding-conventions.md), and the
applicable product specification.

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
