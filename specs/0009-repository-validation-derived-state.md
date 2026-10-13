# SPEC-0009: Repository Validation Derived State

> **Status:** Draft
> **Version:** 0.2
> **Scope:** Incremental repository validation, derived indexes, and local caches
> **Last updated:** 2026-10-12

## 1. Purpose and Status

Repository validation currently derives requirement fingerprints, source
digests, reverse-reference indexes, and workflow snapshots from authoritative
repository files. Repeated skills and commands may independently read, parse,
and hash the same unchanged inputs. This specification defines a separate,
optional line of work for reusing validated derived state without weakening
the authority, determinism, or failure semantics of those checks.

This specification extends repository development tooling. It does not change
requirement fingerprint meaning, traceability marker syntax, source-snapshot
meaning, approval evidence, or conformance claims. The deterministic trace
checker remains governed by
[SPEC-0008](0008-multi-language-conformance-and-repository-organization.md),
particularly R-0008-016 through R-0008-018. Incremental state may be delivered
after that checker and must not become a prerequisite for completing
SPEC-0007 or SPEC-0008.

The [SPEC-0009 work plan](../work/0009/plan.md) tracks unresolved architecture
and future delivery. This draft does not select an implementation technology,
approve a cache format, implement tooling, or authorize CI integration.

## 2. Goals and Non-goals

### Goals

- Avoid repeated parsing and per-requirement fingerprint computation for
  authoritative content that is proven unchanged.
- Reuse exact-byte source digests across planning, readiness, runbook,
  approval, and traceability workflows.
- Preserve identical validation meaning and results with or without derived
  state.
- Make stale, incompatible, malformed, and incomplete state explicit and
  safely recoverable.
- Keep local iteration fast while retaining independently reproducible
  required validation.
- Centralize derived-state behavior so skills orchestrate one maintained
  contract rather than duplicating cache logic.

### Non-goals

- Change SHA-256 fingerprint or source-snapshot semantics.
- Replace stable requirement identifiers with author-maintained versions.
- Make a cache, index, timestamp, or file-system attribute authoritative.
- Add incremental-state delivery to the completion gates of SPEC-0007 or
  SPEC-0008.
- Select a programming language, storage format, package boundary, exact path,
  or command-line syntax.
- Persist credentials, resolved secrets, operation payloads, private user data,
  or imported untrusted source text for convenience.
- Treat improved local performance as evidence that validation, readiness,
  approval, conformance, or publication succeeded.

## 3. Authority and Dependency Boundary

Authoritative specifications, policies, source files, work artifacts, and
review evidence remain the inputs from which derived state is reproduced.
Incremental tooling consumes the deterministic validation contracts already
defined by SPEC-0008 and the exact snapshot contracts defined by
[the specification-driven workflow](../docs/development/spec-driven-workflow.md).

**[R-0009-001]** A repository validation index or cache is local,
non-authoritative derived state. Its presence, absence, contents, or successful
creation must not change the meaning of an authoritative source, satisfy a
validation or workflow gate, establish readiness or approval, support a
conformance claim, or authorize publication. Incremental-state delivery
depends on the validation behavior it accelerates; existing specifications and
their delivery plans must not depend on incremental-state availability.

## 4. Content Identity and Reuse

**[R-0009-002]** A derived entry may be reused only when it is bound to the
exact authoritative input bytes and every versioned rule that can affect the
derived result, including the cache format, source parser, normalization,
fingerprint or digest algorithm, and applicable validation rules. File names,
timestamps, sizes, branch names, commit identities that do not uniquely bind
the consumed bytes, and prior success alone are insufficient reuse keys.

**[R-0009-003]** An incremental invocation must reuse a complete compatible
entry for unchanged exact content without reparsing that content or
recomputing its per-requirement fingerprints. It must recompute affected
derived results when the exact content identity or any result-affecting rule
version changes. Implementations may conservatively recompute additional
results, but they must not reuse an entry whose complete identity has not been
established.

## 5. Behavioral Equivalence and Diagnostics

**[R-0009-004]** Cached and uncached execution over the same authoritative
inputs and validation configuration must produce equivalent requirement
resolution, fingerprints, exact-byte digests, diagnostics, pass-or-fail
outcomes, and machine-readable result semantics. Cache metadata such as hits,
misses, invalidations, and rebuild timing may be additional diagnostics but
must not alter the validation result.

**[R-0009-005]** Missing state is a cache miss, not a validation failure.
Unsupported, stale, malformed, incomplete, or internally inconsistent state
must be reported explicitly, excluded from reuse, and either rebuilt from
authoritative inputs or fail with a non-success result when safe rebuilding is
not possible. Writers must not expose a partial entry as reusable complete
state, and concurrent readers and writers must not cause incorrect reuse or a
false successful result.

## 6. Required Validation and Trust

**[R-0009-006]** A required validation gate must remain independently
reproducible from authoritative inputs without preexisting local state. CI and
release validation must either recompute derived results or verify every reused
entry against the authoritative content and result-affecting rule versions
before accepting it. Deleting all incremental state and rerunning validation
must preserve the result semantics required by R-0009-004.

## 7. Shared Exact-byte Digests

**[R-0009-007]** Repository workflows may reuse a validated exact-byte digest
for an input with matching exact content identity. Reuse must preserve the
digest algorithm, byte boundaries, path ordering, inclusion and exclusion
rules, and composition rules of the consuming workflow. A cached digest must
not replace the recorded revision, SHA-256 value, material-input selection,
or explicit review evidence required by planning, readiness, runbook,
approval, traceability, conformance, or publication procedures.

## 8. Security, Privacy, and Lifecycle

**[R-0009-008]** Incremental state must be excluded from version control,
bounded to derived validation metadata, and safe to delete at any time. It
must not persist credentials, resolved secrets, operation payloads, private
user data, or complete copies of imported untrusted content. Diagnostics must
identify invalidation and recovery without disclosing excluded content.
Cleanup, format replacement, and recovery must be scoped to the owned
incremental-state location and must not modify authoritative inputs or
unrelated user files.

## 9. Compatibility and Recovery

**[R-0009-009]** Incremental state has no compatibility authority over
repository sources or public Qhapaq contracts. A tool may replace an obsolete
local format rather than migrate it when deletion and deterministic
regeneration are safe, but persistent formats must carry explicit identity so
an older tool cannot misinterpret newer state. Recovery must first exclude the
suspect entry from reuse and may rebuild only from resolved authoritative
inputs. A rebuild failure remains a failure; tooling must not substitute
empty, partial, or previous results and report success.

## 10. Verification Expectations

**[R-0009-010]** Delivery must include deterministic cases for:

- unchanged exact content and matching rule versions;
- changed bytes with unchanged path, size, or timestamp;
- parser, normalization, fingerprint, digest, validation-rule, and format
  version changes;
- missing, malformed, truncated, inconsistent, and unknown state;
- concurrent readers and writers and interrupted writes;
- cached and uncached result equivalence;
- clean-state CI or equivalent independent verification;
- exact-byte digest reuse with differing composition rules;
- deletion and safe regeneration; and
- excluded sensitive or untrusted content.

Performance validation must distinguish hashing, parsing, reference indexing,
repository search, process startup, and semantic review. A faster aggregate
command alone is insufficient evidence that derived-state reuse works.

## 11. Runbook and Workflow Reuse

**[R-0009-011]** A persisted runbook freshness decision must bind the complete
resolved input manifest, dependency closure, branch-sensitive inputs, and the
versions of the resolver and eligibility-selection rules that produced it.
An aggregate digest, generation time, branch name, `HEAD`, source count, file
size, or timestamp alone is insufficient to prove freshness. A workflow may
skip full runbook regeneration only after establishing that the complete
recorded identity matches the current authoritative inputs and applicable
rules.

**[R-0009-012]** A runbook's stored `Next command` may be reused as the cached
result of global eligibility selection only when R-0009-011 freshness has been
established. Immediately before plan approval or implementation, the workflow
must still verify the selected target's mutation-specific readiness, approval,
manifest, and prerequisite identities. If freshness or targeted preflight
cannot be established, the stored command must not be executed as trusted
eligibility evidence.

**[R-0009-013]** Incremental workflow resolution must identify changed
authoritative paths, map them through a maintained dependency graph, invalidate
every transitively affected derived result, and preserve unaffected results
only when their complete identities remain valid. A composed workflow may
defer intermediate runbook rendering and perform one final refresh after its
last repository mutation, but it must refresh before reporting persisted
status or a newly unlocked command and must not use deferred rendering to
bypass a review or eligibility gate.

**[R-0009-014]** A validation receipt may be reused only when it binds the exact
reviewed or staged material, validator and rule versions, applicable
configuration, and every environment input required by that validation class.
The consuming workflow must verify those identities before reuse and preserve
the original result and diagnostics. A repository mutation or unbound
environment change invalidates the affected receipt. Nondeterministic build,
test, external-service, and time-sensitive results must not be treated as
reusable merely because source bytes are unchanged.

## 12. Rollout

Rollout is independent of SPEC-0007 and SPEC-0008 completion:

1. Resolve repository-tool ownership, implementation boundary, storage
   representation, concurrency, and command integration through an approved
   architectural decision.
2. Establish deterministic baseline measurements and machine-readable
   validation results.
3. Add the derived index and local cache behind uncached-equivalence tests.
4. Add complete runbook freshness manifests and incremental dependency
   invalidation before trusting stored commands or skipping regeneration.
5. Migrate direct fingerprint, exact-byte digest, runbook, and workflow
   consumers to the central interface without changing their authority or
   review semantics.
6. Add validation receipts first for deterministic checks, then for other
   validation classes only when their complete environment identity and
   invalidation rules are defined.
7. Add clean-state or fully verified CI use only after equivalence, corruption,
   recovery, and receipt-verification tests pass.

Each step remains separately reviewable and recoverable. The rollout must not
add a reverse dependency from SPEC-0007 or SPEC-0008 work.

## 13. Alternatives

### Sequential requirement versions

Rejected for this scope because a manually incremented version does not by
itself prove that changed requirement text received a new identity. It also
changes the meaning of existing traceability references rather than optimizing
their computation.

### Embedded fingerprints as authoritative metadata

Rejected because embedded metadata can become stale with the text it
describes. Such metadata would still require independent validation and would
duplicate the authoritative derivation.

### Timestamp and size validation

Rejected as a trust key because different content can retain the same size or
timestamp and file-system timestamp behavior is not uniform.

### Unconditionally recompute all derived state

Retained as the correctness baseline and recovery path. It is insufficient as
the only local workflow when repeated derivation materially slows development.

## 14. Open Questions

These questions require architectural decisions before implementation:

- Which repository-owned tool or shared library owns parsing, fingerprinting,
  exact-byte digests, indexing, cache validation, and machine-readable output?
- Which implementation technology and package boundary preserve dependency
  direction without coupling portable contracts to one runtime?
- What local storage representation and owned location provide atomic writes,
  bounded cleanup, and practical inspection?
- Which commands expose uncached, incremental, and full-verification modes?
- How are concurrent processes coordinated without treating process-local
  state as repository authority?
- Which authoritative paths and rule versions form the complete runbook input
  manifest, and how is its dependency closure versioned?
- Which validation classes are sufficiently deterministic for receipts, and
  which environment inputs invalidate each class?
- Which phase measurements and thresholds demonstrate a worthwhile
  improvement without creating machine-specific pass/fail gates?

## 15. Revision History

| Version | Date | Changes |
| --- | --- | --- |
| 0.2 | 2026-10-12 | Defined complete runbook freshness, conditional reuse of stored next commands, incremental dependency invalidation and refresh collapsing, and exact-identity validation receipts. |
| 0.1 | 2026-10-12 | Initial draft defining non-authoritative content-addressed validation state, equivalence, invalidation, trust, digest reuse, security, verification, and independent rollout. |
