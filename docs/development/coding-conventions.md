# Coding Conventions

> **Status:** Initial defaults
> **Applies to:** Qhapaq repository

These conventions define repository engineering defaults that are not fully
expressible through formatters, analyzers, compilers, schemas, or tests.
Objective rules should be automated as the toolchain is introduced.

Normative product behavior remains in [SPEC.md](../../SPEC.md) and numbered
[specifications](../../specs/). When these conventions conflict with a product
specification, the specification wins.

## Policy ownership and applicability

This file is the common engineering-policy baseline for every maintained
artifact and contributor workflow in the repository. It owns cross-cutting
requirements and defaults; it does not restate normative product behavior or
replace architectural decisions.

Add a specialized policy beneath `docs/development/conventions/` only when a
maintained language or artifact needs rules that do not apply repository-wide.
The specialized guide must declare its scope and link this file plus the
applicable specifications and ADRs. Applicable common and specialized policies
are cumulative. A specialized guide may explicitly replace a common Default or
Recommendation within its scope, but it cannot weaken a common Required rule
or override a specification or ADR. Resolve such a conflict in the
higher-authority source before proceeding.

Path-specific files under `.github/instructions/` route agents to the applicable
policy and may contain path or tool-execution guidance. They do not own
repository engineering policy or duplicate normative product behavior.

Existing specialized content remains here until approved delivery work moves
it without changing meaning. Do not create empty specialization documents or
directories in anticipation of future consumers.

## 1. Requirement levels

- **Required:** the rule must be followed.
- **Default:** follow the rule unless a change documents a justified exception.
- **Recommendation:** preferred when practical.
- **Decision required:** record the choice in a specification or ADR before
  implementation.

Exceptions should be narrow, reviewable, and recorded close to the decision
without weakening unrelated rules.

## 2. General engineering

### Required

- Prefer clarity, correctness, and explicit behavior over cleverness.
- Keep changes focused and preserve existing behavior outside their stated
  scope.
- Validate invalid input at the boundary that has enough context to explain the
  error.
- Surface failures explicitly; do not silently substitute default output.
- Keep public contracts intentional, documented, and covered by compatibility
  tests.
- Use deterministic behavior for canonicalization, generated views, hashes,
  manifests, and conformance data.
- Keep implementation-specific details out of portable contracts.

### Default

- Prefer small types and functions with one clear responsibility.
- Prefer immutable values and read-only views across boundaries.
- Model meaningful states explicitly rather than with unrelated Boolean flags.
- Reuse a shared abstraction only when its callers have the same semantics, not
  merely similar syntax.
- Delete superseded code instead of retaining speculative compatibility layers
  before a public contract exists.

## 3. Specification traceability

Product behavior is specification-driven, as decided by
[ADR-0003](../architecture/decisions/0003-enforce-specification-traceability.md)
and amended by
[ADR-0004](../architecture/decisions/0004-classify-changes-and-trace-through-commits.md).
Specifications are written first and are the source of truth; implementations
conform to them.

### Required

- Classify every change as one kind of change: `requirement`, `amendment`,
  `extension`, `bug`, `editorial`, `refactor`, or `maintenance`, as defined in
  [specs/README.md](../../specs/README.md#kinds-of-change).
- Do not add or alter product behavior unless a requirement describes it. If
  no requirement exists, add or revise one in the governing platform or
  [component specification](../../specs/components/README.md) in the same or
  an earlier change.
- Record the change kind and the requirements a change implements in commit
  trailers:

  ```text
  Change-Kind: <kind>
  Spec: R-0001-012@44aa01, R-0001-013@9c2e10
  ```

  `Spec:` is required for `requirement`, `amendment`, `extension`, `bug`, and
  `editorial` changes and is omitted for `refactor`. A `requirement` or
  `extension` change may name a whole document, such as `SPEC-0007` or
  `COMP-0001`. Integration into the default branch must preserve the required
  traceability of every included commit. Rebase merges retain each validated
  commit and its trailers. If an explicitly selected squash merge combines
  commits, its resulting commit must retain their complete required `Spec:`
  coverage.
  `Change-Kind:` is required even for intermediate commits. Enable the local
  [commit-message hook](git-hooks.md); it complements the commit skills but
  does not replace semantic review or future CI enforcement.
- Mark code that enforces a requirement with the language-neutral payload
  `spec: <requirement-id>@<fingerprint>`, for example
  `spec: R-0001-012@44aa01`. Separate multiple references with commas. Use only
  native comment or documentation constructs registered by the applicable
  language policy and deterministic checker extractor.
- Tests that verify a requirement use the applicable language's registered test
  placement. A `bug` fix adds a regression test that references the requirement
  it restores.
- When any text in a requirement block changes, review every code and test
  location that references it and update the fingerprint in the same change.
  Do not update a fingerprint without confirming that the referencing code
  still conforms.
- Never reference a section number or heading instead of a requirement
  identifier.

### Placement

Commit trailers record which requirements a change implements. An inline
reference marks only an *invariant*: code that enforces a requirement, where
the test is *would deleting or rewriting this code violate a specification?*
Invariants include:

- validation and policy checks and their ordering;
- permission, credential, and disclosure decisions;
- limits and bounds;
- cancellation, failure, and error-mapping semantics;
- exact-version resolution and determinism rules; and
- security and trust boundaries.

Each maintained implementation language must define unambiguous native
placements for an enforcing statement or block, whole-member enforcement, and
a verifying test. Its language-aware checker extractor must be registered
before that language is supported for traceability. Marker-like text in a
string, generated output, example, unsupported file, or unregistered construct
does not satisfy a traceability obligation.

Do not add references to types, entry points, members that merely implement a
feature, dependency-injection registration, or plumbing. The commit trailers
already trace them.

### Waivers

The AI-led semantic review is not deterministic. When a reviewer
confirms that a judgment finding is wrong or accepted, waive it explicitly in
the code instead of rewording the code to satisfy the reviewer:

```text
spec-waive: <rule>[, <rule>...] — <justification>
```

Waivable rules are the judgment findings of the semantic review:

| Rule | Finding waived |
| --- | --- |
| `untraced-behavior` | The code implements behavior that no requirement describes. |
| `conformance` | The code appears to contradict a requirement in scope. |
| `unsupported-reference` | A reference appears not to support the code it annotates. |
| `invariant-marker` | Code that enforces a requirement lacks an inline reference. |
| `test-reference` | A test of a specified rule, an implemented requirement, or a bug fix lacks a test reference. |

- Place the waiver in a registered native construct where a reference could
  appear. It covers only that placement's attachment target.
- The justification is required and must explain why the finding does not
  apply or why it is accepted, for example by citing the requirement text or a
  tracking issue.
- Mechanical rules cannot be waived. These are reference grammar, resolution,
  fingerprints, identifier integrity, and a missing `Spec:` trailer. Fix the
  code, the trailers, or the specification instead.
- AI agents must not add, broaden, or move a waiver unless the user explicitly
  directs it for that finding.

### Enforcement

A deterministic trace checker will use registered language-aware extractors to
read permitted native constructs and one shared rules engine to verify payload
grammar, requirement resolution, current fingerprints, placement, changed-
requirement reverse impact, waiver scope, and commit trailers. Each diagnostic
will identify the file, source span, stable rule, and offending marker or
requirement identity. Malformed markers, unsupported placements, missing
required references, and extractor failures will fail explicitly. The checker
is planned and not yet available. Until it exists, the AI-led
[`spec-trace-check` skill](../../.agents/skills/spec-trace-check/SKILL.md)
inspects files changed since `HEAD`, classifies the change, proposes its
trailers, and reviews changed code against the requirements in scope. It runs
as the first step of `build-and-test`, which `commit-and-push` runs by default.
The [`fix-bug` skill](../../.agents/skills/fix-bug/SKILL.md) applies the bug
workflow. Reviewers remain responsible for anything the skills miss.

## 4. Repository and project organization

- Language-neutral specifications, schemas, conformance data, and examples stay
  at the repository root.
- Project-specific .NET organization, layering, namespaces, and operation file
  naming are defined in the [.NET conventions](conventions/dotnet.md).
- Adding or reversing a project dependency is a design change that requires
  review against [SPEC-0001](../../specs/0001-core-pipeline-model.md).

## 6. Portable JSON and schemas

- Portable property names use a documented, consistent casing policy.
- Do not serialize CLR assembly names, type names, exception objects, delegates,
  credentials, or implementation-only state.
- Reject unknown document versions.
- Reject unknown fields when accepting them could create ambiguous execution or
  security behavior.
- Keep semantic ordering explicit. Canonicalization must not depend on hash-map
  enumeration, current culture, local time zone, or platform-specific paths.
- Schema references must resolve from versioned repository or package content
  without ambient network access.
- Breaking portable-contract changes require a new document, schema, or
  protocol version and updated conformance vectors.

## 7. Security and privacy

- Treat pipeline documents, imported OpenAPI documents, operation metadata,
  external responses, paths, URLs, and generated prose as untrusted input.
- Never write secrets, tokens, authorization codes, credential references that
  reveal sensitive state, or operation payloads to logs by default.
- Keep execution permission, network permission, and payload disclosure as
  separate policy decisions.
- Validate structure, schemas, configuration, types, capabilities, budgets, and
  policy before starting any operation.
- Bound loops, retries, concurrency, duration, memory-sensitive buffering, and
  output size.
- Normalize and validate archive and bundle paths before file creation; reject
  traversal outside the intended root.
- Use allowlists for implementation activation, connector operations, network
  destinations, and disclosed fields where applicable.
- Do not add cryptography, secret storage, or authentication mechanisms without
  specialist review and an explicit design decision.

## 8. Logging, diagnostics, and observability

- Use structured logging fields rather than interpolating machine-readable
  values into message text.
- Identify pipeline, plan, run, expression, operation, implementation version,
  attempt, branch, and duration where applicable.
- Avoid payload contents in logs, traces, metrics, exception messages, and test
  snapshots unless a test uses synthetic non-sensitive values and the behavior
  is intentional.
- Use stable event names and dimensions with bounded cardinality.
- Diagnostics must be actionable and distinguish validation, binding, policy,
  configuration, cancellation, timeout, and operation failures.
- Human CLI diagnostics go to standard error; machine-readable output remains
  valid on standard output.

## 9. Testing

### Required

- Add tests for changed behavior and for every corrected defect.
- Test observable contracts rather than private implementation details.
- Keep tests deterministic and independent of execution order.
- Use synthetic credentials, endpoints, and payloads.
- Prove rejection paths as well as successful paths.
- Verify cancellation, timeout, concurrency, and multiple-failure behavior when
  the changed code can exercise them.
- Consume shared conformance vectors instead of copying language-neutral cases
  into implementation-specific fixtures.

### Organization

- Unit tests cover isolated algorithms, type compatibility, composition,
  canonicalization, binding, and policy decisions.
- Integration tests cover process, package, hosting, transport, connector, and
  external-boundary behavior.
- Golden files are appropriate for canonical JSON, Mermaid, schemas, manifests,
  and protocol envelopes when diffs are reviewable and regeneration is
  documented.
- Test names describe the condition and expected outcome without encoding
  incidental implementation steps.

## 10. Dependencies and tools

- Prefer the platform and existing dependencies before adding a package.
- Pin SDKs and tools; use lock files where the ecosystem supports them.
- Review license, maintenance, provenance, transitive dependency, trimming, and
  security implications before adoption.
- Keep runtime dependencies out of abstraction packages unless they are part of
  that package's public purpose.
- Do not add a dependency solely to avoid a small, well-understood use of the
  standard library.
- Dependency updates must pass the same tests and package-consumer checks as
  source changes.

## 11. Documentation

- Update documentation and examples in the same change as the behavior they
  describe.
- Use repository-relative links in Markdown source.
- Link to the authoritative specification instead of duplicating normative
  rules across guides.
- Label planned behavior clearly; do not present unimplemented functionality as
  available.
- Include language identifiers on fenced code blocks.
- Keep generated reference output separate from curated source and document its
  generation command.
- Use accessible headings, descriptive link text, alt text, and table structure.

## 12. Generated code and artifacts

- Generated files identify their source and generation process when the format
  permits it.
- Never hand-edit generated output when the source can be changed and
  regenerated.
- Generation must be deterministic or clearly identify unavoidable variance.
- Do not commit build output, caches, local profiles, test result directories,
  deployment credentials, or machine-specific IDE state.
- Published packages, manifests, checksums, SBOMs, and provenance must refer to
  the exact same built bytes.

## 13. Decision triggers

Record a specification or ADR before implementing a choice that affects:

- Public API or portable document compatibility.
- Trust boundaries, authentication, authorization, or disclosure.
- Project dependency direction or package boundaries.
- Persistence, remote protocols, deployment topology, or durability.
- Canonicalization, schema draft, error envelope, version derivation, or
  supported platform matrix.
- Build system, test framework, documentation generator, signing, or provenance
  standards when more than a local implementation detail is involved.

Minor refactoring and application of an existing convention do not require a
new decision record.
