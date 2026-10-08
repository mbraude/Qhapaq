# Component Specifications

Component specifications define the behavior of individual Qhapaq components
that work within the platform contracts in [SPEC.md](../../SPEC.md) and the
[numbered specifications](../README.md) without changing them. Examples are a
built-in operation, a declarative connector, a decorator, and a credential
provider. Adding or changing a component is an `extension` change, as defined
by
[ADR-0004](../../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md).

A component specification is not an operation catalog. Catalogs and operation
descriptors, defined by
[SPEC-0002](../0002-operation-catalogs-and-host-configuration.md), are runtime
artifacts that an implementation derives from component specifications and
must keep consistent with them.

## Rules

- Write component specifications so that the component can be reimplemented
  in any language from the specification library alone. Never name
  implementation types, source files, packages, or languages, and never
  reference implementation code.
- Number each specification `COMP-<number>` with the next unused four-digit
  number, and name its file `<number>-<slug>.md`, for example
  `0001-http-request.md`.
- Use requirement blocks as defined by
  [ADR-0003](../../docs/architecture/decisions/0003-enforce-specification-traceability.md),
  with the specification number `C<number>`. For example, the third block of
  `COMP-0001` is `**[R-C0001-003]**`, and code references it as
  `spec: R-C0001-003@<fingerprint>`.
- State the platform requirements the component relies on by identifier.
- If the component needs a platform behavior that no platform requirement
  provides, change the platform specification first as a `requirement` or
  `amendment`.
- Never change the meaning of a published contract version. Add a new version
  section with new requirement blocks instead. Retire the earlier version's
  blocks as tombstones only when that version is no longer supported.

## Publication lifecycle

Each contract version starts with status `Incomplete`. Intermediate commits
and pushes may revise it; neither action publishes it. Mark a version
`Published` only after explicit human approval following documented review
and validation of that exact revision. Record approval and validation evidence
in version history, not implementation references in the specification.

Keep the per-version status outside requirement blocks, so publication alone
does not change fingerprints. A `Published` version cannot be reset to
`Incomplete`; behavioral changes require a new version. Editorial corrections
must preserve meaning.

Future CI is intended to promote reviewed versions after its required gates
pass, without including unvalidated concurrent edits. That automation and its
gates are not implemented yet; explicit human approval is the current process.

Existing code will be backfilled against governing requirements after the
remaining ADRs are settled. This does not require writing component
specifications for every existing built-in operation now.

## Template

Include the following sections as applicable.

1. **Header:** `COMP-<number>: <title>`, status, component kind, stable
   identifier (for an operation, its operation stable ID as defined by
   SPEC-0002), supported contract versions, and the platform requirements it
   relies on.
2. **Purpose and non-goals.**
3. **Contract**, with one subsection per contract version and a status
   (`Incomplete` or `Published`) before its requirement blocks:
   - inputs and outputs, which may use embedded JSON Schema;
   - capabilities and side effects;
   - permissions and credentials;
   - payload disclosure;
   - failure modes and error mapping; and
   - limits, timeouts, and cancellation.
4. **Security and privacy.**
5. **Testing and conformance:** the cases an implementation must pass.
6. **Open questions.**

## Index

| Specification | Kind | Scope |
| --- | --- | --- |
| *None yet.* | | |
