# ADR-0004: Classify Changes and Trace Them Through Commits

> **Status:** Accepted
> **Date:** 2026-10-07
> **Amends:** [ADR-0003](0003-enforce-specification-traceability.md)

## Context

[ADR-0003](0003-enforce-specification-traceability.md) made specifications
the source of truth, gave requirements stable identifiers and fingerprints,
and required every non-private product type and member to carry a `spec:`
reference. Two kinds of change that will be common once the base system exists
expose problems with that design:

1. **Adding a component**, such as a new operation that touches several files
   to connect to a new data source or integrate with permissions differently.
   Its behavior needs a source of truth, but it does not change the platform
   specifications. A `spec:` reference on every type and member it touches
   would repeat what version control already records and would accumulate
   references that explain nothing.
2. **Fixing a bug.** Bug fixes should be lightweight and AI-driven, not
   specification-led. They must still not violate an earlier specification
   decision, and comparing code with the requirements it depends on is the
   most valuable check available.

The specifications must also be complete enough that the entire system could
be reproduced in a new implementation from the specifications alone. They are
implementation-neutral descriptions of behavior; code is an
implementation-specific derivation of them. The two must not be mixed.

## Decision

### Kinds of change

Every change is classified as exactly one kind. The kind determines what must
change in the specifications and what the commit must record.

| Kind | Meaning | Specification change | `Spec:` trailer |
| --- | --- | --- | --- |
| `requirement` | Adds a platform capability, contract, or trust boundary. | New requirement blocks in `SPEC.md` or a numbered specification, and an ADR when the choice is architectural. | Required |
| `amendment` | Changes the meaning of an existing requirement. | The block is edited in place, keeping its identifier; a component's published contract instead gains a new version. | Required |
| `extension` | Adds or changes a component within existing platform contracts. | A new or changed component specification. | Required |
| `bug` | Restores conformance to a requirement the code violates. | None. | Required: the violated requirements |
| `editorial` | Rewords requirements without changing their meaning. | Blocks are reworded; fingerprints change. | Required: the reworded blocks |
| `refactor` | Changes structure without changing behavior. | None. | None |
| `maintenance` | Changes no product behavior: build, tooling, skills, documentation, or tests of existing behavior. | None. | Optional |

Two tests resolve ambiguous cases:

- **Bug or amendment.** If the specification is right and the code is wrong,
  the change is a `bug`. If the specification is wrong, ambiguous, or silent
  about the behavior, the change is an `amendment`, even when a bug report
  prompted it. A fix that changes specified behavior, or that decides behavior
  the specification does not describe, is never a `bug`.
- **Requirement or extension.** If adding the component requires a platform
  specification to change, such as a new permission kind or a new class of
  data source, that platform change is a `requirement` or `amendment` and
  lands first. The component is then an `extension` that uses it.

A change should be one kind. When a change mixes kinds, prefer splitting it.
Otherwise use the first applicable kind in this order: `requirement`,
`amendment`, `extension`, `bug`, `editorial`, `refactor`, `maintenance`, and
record every `Spec:` reference that any part of the change needs.

### Component specifications

The behavior of an individual product component (an operation, declarative
connector, decorator, credential provider, or similar unit that instantiates
platform contracts without changing them) is specified in a component
specification under [specs/components/](../../../specs/components/).

- Component specifications form a separate library from the platform
  specifications and are equally authoritative. Together, `SPEC.md`, the
  numbered specifications, and the component specifications must be
  sufficient to reproduce the system in a new implementation.
- They are implementation-neutral. They never name implementation types,
  source files, packages, or languages, and they never reference code.
- A component specification is numbered `COMP-<number>`, for example
  `COMP-0001`, and its file is `specs/components/<number>-<slug>.md`. Its
  requirement blocks follow ADR-0003 with the specification number `C<number>`,
  for example `R-C0001-003`.
- A component specification states the platform requirements it relies on by
  identifier.
- Runtime operation descriptors and catalogs defined by
  [SPEC-0002](../../../specs/0002-operation-catalogs-and-host-configuration.md)
  are product artifacts derived from component specifications and must agree
  with them. A component specification is not a catalog and is not loaded at
  runtime.
- Contract versions are immutable once published, as SPEC-0002 requires of
  operation contracts. Changing a published contract adds a new version with
  new requirement blocks; the earlier version's blocks remain until that
  version is no longer supported and are then retired as tombstones.

#### Contract publication lifecycle

Each contract version has its own status: `Incomplete` or `Published`. New
versions start `Incomplete` and may be revised across intermediate commits
and pushes. Git commit or push success never means the contract is published.
An incomplete specification can guide implementation but is not a finalized,
reviewed contract.

Promotion to `Published` requires explicit human approval after documented
review and validation of the exact revision being promoted. Record approval
and validation evidence in version history; keep lifecycle metadata outside
requirement blocks so promotion does not change their fingerprints. Once
published, a version cannot return to `Incomplete` to evade immutability.
Editorial corrections remain possible without changing contract meaning.

Future CI should promote a reviewed revision after its required gates pass.
Promotion must change only lifecycle metadata and must not publish unvalidated
concurrent edits. The CI gates and promotion mechanism remain future work;
until then, use the explicit human approval process above.

### Commit trailers record provenance

The relationship between a change and the specifications that motivated it is
recorded in commit trailers, not in code comments. Version control already
records which files a change touched, so the trailers make every touched file
traceable without adding references to plumbing, registration, or wiring.

```text
Change-Kind: <kind>
Spec: <reference>[, <reference>...]
```

- `Change-Kind` is required on every commit.
- The commit skills write it, and the repository-managed `commit-msg` hook
  rejects a missing, duplicate, or invalid trailer. Enable the hook in each
  clone using the [hook setup guide](../../development/git-hooks.md). The hook
  checks syntax only, not whether the declared kind matches the change.
- Each `Spec:` reference is either a requirement reference
  `R-<spec>-<sequence>@<fingerprint>`, which records the exact text the change
  implemented, or a whole-document identifier `SPEC-<number>` or
  `COMP-<number>`, allowed only for `requirement` and `extension` changes. A
  commit may contain several `Spec:` lines.
- The `Spec:` trailers of a commit are its provenance: the reason the change
  exists. They answer questions such as "which files implemented `COMP-0003`?"
  through `git log --grep`, and "which requirements does this code depend
  on?" through `git log -L` over its lines.

### Inline references mark enforced invariants only

This decision replaces the reference placement rules and the untraced product
surface check of ADR-0003.

A `spec:` reference in code, using the ADR-0003 grammar, marks an *invariant*:
code that enforces a requirement, so that removing or rewriting it would
violate the requirement without a compile failure or an obvious test failure.
Invariants include:

- validation and policy checks and their ordering;
- permission, credential, and disclosure decisions;
- limits and bounds;
- cancellation, failure, and error-mapping semantics;
- exact-version resolution and determinism rules; and
- security and trust boundaries.

The test for placing a reference is: *would deleting or rewriting this code
violate a specification?* If so, mark it. If not, the commit trailers are
sufficient.

- Place the reference in a `//` comment immediately before the enforcing
  statement or block, or in a member's `<remarks>` when the whole member is
  the enforcement, such as a dedicated validator.
- Do not place references on types, entry points, members that merely
  implement a feature, dependency-injection registration, or plumbing.
- Tests that verify a requirement reference it, as ADR-0003 requires. A bug
  fix adds a regression test that references the requirement it restores.

Inline references remain because version history is weakest where invariants
matter most: a refactor or squash can move enforcing code into a commit whose
trailers do not mention the requirement it enforces. The reference keeps that
requirement attached to the code.

### Reverse-impact review

Before any change to existing product code is accepted, the trace check
collects the requirements in scope of each changed region:

1. `spec:` references in or enclosing the changed lines;
2. `spec:` references in tests that exercise the changed members; and
3. `Spec:` trailers of recent commits that touched the changed lines,
   found with `git log -L`.

It then asks one narrow question: does this change contradict any of these
requirements? Because the review is limited to the requirements the code
depends on, it stays focused enough to be reliable, and it protects
lightweight bug fixes from undoing earlier specification decisions without
requiring the fix to be specification-led.

### Enforcement

The interim AI-led `spec-trace-check` skill and the planned deterministic
checker apply these rules in addition to the ADR-0003 rules that remain in
force.

| Rule | Severity | Waivable |
| --- | --- | --- |
| A change classified as `requirement`, `amendment`, `extension`, `bug`, or `editorial` has at least one resolvable `Spec:` reference. | Error | No |
| An `extension` has a component specification in the repository or the same change. | Error | No |
| Product behavior changed by the diff is described by a requirement or component specification (`untraced-behavior`). | Error | Yes |
| The change contradicts a requirement in scope, including those found by the reverse-impact review (`conformance`). | Error | Yes |
| New or changed code that enforces a requirement carries an inline reference (`invariant-marker`). | Error | Yes |
| A `bug` change adds a regression test that references the restored requirement (`test-reference`). | Error | Yes |
| An inline reference annotates a type, entry point, registration, or plumbing (reference sprawl). | Warning | Not needed |
| A change mixes kinds. | Warning | Not needed |

The trace check reports the change kind and the `Spec:` trailers it derived,
and the `commit-and-push` skill writes them into the commit message.

### Amendments to ADR-0003

- **Source references** placement is replaced by *Inline references mark
  enforced invariants only*.
- The **untraced product surface** check, its baseline, and ADR-0003 rollout
  steps 5 and 6 for that check are withdrawn. The untraced-change rules above
  replace them.
- **Specification-first changes** step 2 now means implementing with `Spec:`
  trailers and invariant references rather than references on every member.
- The **coverage** check counts test references and commit trailers rather
  than code references.

All other ADR-0003 rules, including identifiers, fingerprints, stale-reference
detection, waivers, and the semantic review, remain in force.

## Consequences and Tradeoffs

- Code stays readable: references appear only where they protect an
  invariant, and they become a precise lookup table for reviewing changes.
- Provenance lives in version history, where it does not repeat in the code
  and does not rot as code is reorganized.
- Trailers are self-reported. The trace check validates their grammar and
  resolution and derives them from the diff, but it cannot prove the
  classification is right; review remains responsible for that.
- Squash merges must preserve every `Spec:` trailer of the squashed commits,
  or provenance is lost.
- `git log -L` follows lines through refactors only approximately. Inline
  invariant references and regression tests cover the cases where that matters
  most.
- Removing the untraced-surface check removes a deterministic, structural
  rule. Untraced behavior is now detected by classification and semantic
  review, which is less mechanical but no longer requires a reference on
  every member.
- A bug fix stays lightweight but must still name the requirement it restores;
  a defect with no governing requirement is an amendment.

## Alternatives

### Version history only, with no inline references

Rejected for invariants. A refactor or squash can disconnect enforcing code
from the commit that introduced it, and the reverse-impact review would then
miss the requirement.

### Explicit file references in component specifications

Rejected because it couples implementation-neutral specifications to one
implementation's file layout and violates the reproducibility goal.

### Component behavior in the runtime catalogs or operation descriptors

Rejected because descriptors are product artifacts of one implementation and
do not carry the full behavioral contract. Keeping component specifications
separate keeps the specification library complete and implementation-neutral.

### Unit tests as the only protection against bug-fix regressions

Rejected as insufficient alone. Tests catch only anticipated violations; the
reverse-impact review catches contradictions with requirements no test
covers. Regression tests remain required.

## Rollout

1. Adopt this decision, the component specification format, and the updated
   conventions and skills.
2. Write component specifications for new components as they are added.
3. Backfill existing code's provenance and invariant/test references against
   the requirements once the remaining architectural decisions are settled.
   This is deferred work, not part of adopting this ADR. Do not require a new
   component specification for every existing built-in operation as an
   adoption prerequisite; add one when component-specific behavior needs it.
4. Enable the local commit-message hook and use the commit skills to record
   `Change-Kind` now.
5. Add the change-kind, trailer, and reverse-impact rules to the deterministic
   trace checker when it is implemented.
6. Automate per-version publication after review and CI gates exist.

## Open Questions

- Which review and validation gates will future CI require before promoting a
  component contract version, and how will it record promotion atomically?

## Related Specifications

- [SPEC.md](../../../SPEC.md)
- [SPEC-0002: Operation Catalogs and Host Configuration](../../../specs/0002-operation-catalogs-and-host-configuration.md)
- [Component specifications](../../../specs/components/README.md)
