# ADR-0003: Enforce Specification Traceability

> **Status:** Accepted; amended by
> [ADR-0004](0004-classify-changes-and-trace-through-commits.md)
> **Date:** 2026-10-07

> [!NOTE]
> ADR-0004 replaces the source-reference placement rules and the untraced
> product surface check below. Code now carries `spec:` references only where
> it enforces a requirement, and commit trailers record which requirements a
> change implements. The identifier, fingerprint, stale-reference, waiver, and
> semantic-review rules remain in force.

## Context

Qhapaq uses a specification-driven development model.
[SPEC.md](../../../SPEC.md) and the numbered [specifications](../../../specs/)
are the source of truth for product behavior. Implementations are expected to
be authored, primarily by AI agents, only after the behavior they realize has
been specified. Reviewers and agents must be able to reason from a line of code
back to the requirement that justifies it, derive expected behavior from the
specification, and validate or invalidate observed behavior against it.

Three problems block that model today:

1. Specifications are addressable only by section number and heading. Both
   change during editing, so references to them silently rot.
2. Nothing connects product code to the requirement it implements, so a change
   that introduces unspecified behavior looks the same as one that implements a
   specified requirement.
3. When a requirement changes, nothing identifies the code and tests that
   depended on the old wording.

Instruction files such as [AGENTS.md](../../../AGENTS.md) are advisory: an AI
agent may ignore or misapply them. Rules intended to stop a change must
therefore be enforced mechanically at a point the agent cannot bypass. The
authorship of a change (human or AI) cannot be verified reliably; commit
trailers are self-reported. Enforcement must apply to every change regardless
of author.

## Decision

### Stable requirement identifiers

Normative content in a specification that implementations or tests can satisfy
is grouped into requirement blocks. Each block receives a stable requirement
identifier of the form `R-<spec>-<sequence>`, for example `R-0001-012`.

- `<spec>` is the four-digit specification number. The top-level
  [SPEC.md](../../../SPEC.md) uses `0000`. `<sequence>` is a three-digit (or
  longer) number assigned sequentially within that specification.
- Identifiers never encode section numbers and are never renumbered or reused.
- A requirement block is one cohesive rule: content that a single code unit,
  such as a type, member, or group of tests, would implement and cite. A
  section whose normative content is one rule is one block. A larger section
  is split into several blocks when its parts would be implemented by
  different code or would change independently. A lead-in sentence stays in
  the same block as the list or table it introduces.
- The identifier appears in bold brackets at the start of a top-level
  paragraph, never inside a list item, table, block quote, or code block. The
  block extends from the identifier to the next identifier or the next heading
  of any level, whichever comes first, and includes any lists, tables, and code
  blocks in that range:

  ```markdown
  ### 6.1 Required top-level members

  **[R-0007-004]** Every definition contains:

  - `format`, with the exact value `qhapaq.pipeline/v1`;
  - a stable pipeline `id`;
  - ...

  Unknown properties are rejected unless the normative pipeline JSON Schema
  explicitly permits them.
  ```

  When a block begins with a list, table, or code block rather than prose, the
  identifier stands alone as a one-line paragraph immediately before it.
- Normative content is identified by meaning, not keywords. Present-tense
  descriptions of required behavior ("The second operation starts only after
  the first completes successfully.") are requirements; "should" statements
  are Default-level requirements and are also tagged.
- A removed requirement keeps its identifier as a tombstone that names its
  replacement, if any:

  ```markdown
  **[R-0001-007]** *Retired; superseded by R-0001-031.*
  ```

- Goals, non-goals, summaries, terminology, rationale, alternatives, open
  questions, future-only direction, and revision history do not receive
  requirement identifiers. Content that precedes the first identifier in a
  section is outside every block. Examples and rationale that appear inside a
  block's range are part of that block; place them before the block's
  identifier or under a separate heading if edits to them should not affect
  references.

### Requirement fingerprints

Each requirement block has a fingerprint: the first six lowercase hexadecimal
characters of the SHA-256 hash of its block text encoded as UTF-8. The block
text is everything after the identifier tag up to the end of the block, with
task-list checkboxes (`[ ]`, `[x]`, `[X]` following a list marker) removed,
every run of whitespace collapsed to one space, and the result trimmed.
Checking off a task therefore does not change a fingerprint, but any change to
the wording, examples, or tables inside the block does.

### Source references

Product code and tests reference requirements with one grammar:

```text
spec: <requirement-id>@<fingerprint>[, <requirement-id>@<fingerprint>...]
```

The `spec:` token may appear in an XML documentation `<remarks>` element or in
a `//` line comment, followed optionally by a short explanation after an em
dash. References are placed at the narrowest level that explains the code:

| Level | Use when |
| --- | --- |
| Type `<remarks>` | The type as a whole realizes a specified concept, such as a composition form, binder, or policy evaluator. |
| Member `<remarks>` | The member implements a specific rule or contract. This is the default level. |
| Line comment before a block | The block encodes a non-obvious specified decision: validation or policy ordering, cancellation or failure semantics, limits, disclosure, or error mapping. |
| Test line comment | The test verifies the requirement. |

References are not required on dependency-injection registration, plumbing,
private helpers whose containing member is already traced, or trivial members.

```csharp
/// <summary>Runs two operations concurrently.</summary>
/// <remarks>spec: R-0001-010@3fa2c1</remarks>
internal sealed class ParallelOperation : IOperation
{
    /// <summary>Invokes both branches and combines their results.</summary>
    /// <remarks>spec: R-0001-012@44aa01</remarks>
    public async Task<Document> InvokeAsync(Document input, CancellationToken cancellationToken)
    {
        // spec: R-0001-012@44aa01 — cancel the sibling before awaiting it so no failure is lost.
        ...
    }
}
```

The fingerprint values above are illustrative.

### Specification-first changes

Product behavior must trace to a specified requirement. A change that adds or
alters product behavior without a requirement that describes it is
nonconforming. The required order is:

1. Add or revise the requirement in the governing specification.
2. Implement it with references to the new or revised identifiers.
3. Add or update tests that reference the same identifiers.

Steps may land in one change, but the specification text is authoritative; the
implementation conforms to it, not the reverse. When a requirement's wording
changes, every reference to it must be reviewed and its fingerprint updated in
the same change.

### Mechanical enforcement

A repository trace checker will enforce the following rules in local builds
and as required CI status checks protecting the default branch. Until the
checker and CI exist, the interim enforcement described below applies.

| Check | Rule | Severity |
| --- | --- | --- |
| Resolution | Every reference names an existing, non-retired requirement. | Error |
| Fingerprint | Every reference fingerprint matches the requirement's current fingerprint. | Error |
| Identifier integrity | Identifiers are unique, well-formed, and never removed or reused; retired identifiers remain as tombstones. | Error |
| Untraced product surface | In `Qhapaq.Service.V*`, `Qhapaq.Business`, `Qhapaq.DAL`, and `Qhapaq.Implementations.*`, every non-private type and member has a reference on itself or its containing type. | Error, ratcheted by a baseline that may only shrink |
| Coverage | Requirements applicable to the .NET implementation have at least one code reference and one test reference. | Warning initially |

A semantic conformance review supplements these checks. On each pull request,
an AI reviewer receives each changed code region together with the text of the
requirements it references and reports inconsistencies, untraced behavior, and
references that do not support the code. Because this review is not
deterministic, its findings are advisory and require human disposition; it does
not by itself block merging.

AI agents must run the trace checker before reporting a change as complete.
Where the agent host supports completion hooks, the repository should configure
them to run the checker so that an agent session fails visibly rather than
relying on instructions alone.

### Interim enforcement

Until the deterministic checker and CI exist, the repository's
[`spec-trace-check` skill](../../../.agents/skills/spec-trace-check/SKILL.md)
enforces the table above through AI-led inspection, together with the semantic
conformance review. The `build-and-test` skill runs it first, and
`commit-and-push` runs `build-and-test` by default, so a `FAIL` verdict stops
the commit. To stay efficient, the skill inspects only files changed since
`HEAD` (staged, unstaged, and untracked). The one exception is a
repository-wide search for references to requirement blocks whose text
changed.

Because the semantic review is not deterministic, its judgment findings
(untraced behavior, conformance, unsupported references, and missing line or
test references) can be overridden in two ways:

- **Waiver comment.** A `spec-waive: <rule> — <justification>` comment in the
  code, defined in the
  [coding conventions](../../development/coding-conventions.md#waivers),
  overrides one finding. Waivers are scoped like references, require a
  justification, stay visible in the code and the diff, and are listed in
  every trace-check report. Agents may add one only at a user's explicit
  direction.
- **Run argument.** A user-supplied `skip-semantic-review` argument skips the
  semantic review for one run. The skip is recorded in the report.

Mechanical rules cannot be waived or skipped: reference grammar, resolution,
fingerprints, identifier integrity, and missing references on product
surface. Without that limit, a waiver could admit unspecified product
surface, which this decision exists to prevent.

This interim enforcement is weaker than the target design:

- AI inspection is not deterministic and can miss or misjudge findings.
- It runs only when an agent invokes the skill. Skipping `build-and-test`
  also skips the trace check.
- It cannot prevent a push that bypasses the skills.
- Before the untraced-surface baseline exists, it reports untraced surface
  only for changed code.

Fingerprints are computed with a small hashing helper embedded in the skill,
never estimated. The helper is the reference implementation of the fingerprint
rule above until the checker replaces it.

## Consequences and Tradeoffs

- Code is navigable back to authoritative requirement text, and requirement
  changes mechanically identify every dependent code and test location.
- Untraced public or internal product surface cannot merge, which makes adding
  unspecified behavior require a specification change first.
- Fingerprints add churn: editorial changes to a requirement require updating
  every reference. This is intentional, because it forces review of dependent
  code, but editorial cleanups should be batched.
- An agent can update fingerprints without genuinely reviewing the code. The
  fingerprint update is visible in the diff, and the semantic conformance
  review and human review are the controls for that risk.
- The untraced-surface check is a structural proxy. It cannot prove that the
  behavior inside a traced member matches the requirement; tests and review
  remain responsible for that.
- Existing specifications need an editorial pass to add identifiers, and
  existing code needs references or a recorded baseline before enforcement.
- The checker is repository tooling; its implementation language and packaging
  are local implementation details unless they affect contributors or CI
  contracts in [SPEC-0005](../../../specs/0005-build-release-and-website-delivery.md).

## Alternatives

### Reference sections by number or heading anchor

Rejected because section numbers and generated heading anchors change when
specifications are reorganized, silently invalidating references.

### One identifier per statement, list item, or table row

Rejected after a trial pass produced more than 1,800 identifiers, including
more than 1,000 in SPEC-0007, many on list fragments such as a single property
name. That granularity made specifications harder to read and references harder
to choose without improving the precision of staleness detection in practice.

### One identifier per section

Rejected because several sections are hundreds of lines long and contain rules
implemented by unrelated code. A single section fingerprint would mark every
reference to the section stale whenever any rule in it changed. Requirement
blocks keep small sections as one identifier while splitting large ones by
rule.

### Custom attributes such as `[SpecRequirement("R-0001-012")]`

Deferred. Attributes are reflectable and analyzer-friendly, but they cannot
annotate individual statements or blocks, they add metadata to compiled
assemblies, and they are .NET-specific. A comment grammar works for every language and file
type. An analyzer may later validate the comment grammar directly.

### Instruction-only enforcement

Rejected because agents can ignore or misapply instructions. Instructions
explain the model; required checks enforce it.

### Verify that implementation changes were authored by AI

Rejected because authorship markers are self-reported and cannot be verified.
The same checks apply to every change.

## Rollout

1. Adopt this decision and the related convention and specification-authoring
   rules.
2. Add requirement identifiers to existing specifications.
3. Add the interim AI-led `spec-trace-check` skill over changed files and run
   it from `build-and-test`.
4. Implement the deterministic trace checker with resolution, fingerprint, and
   identifier integrity checks.
5. Add references to existing code and record the untraced-surface baseline.
6. Enable the untraced-surface check and required CI status checks.
7. Add the semantic conformance review to CI and agent completion hooks.

## Open Questions

- Should a referenced requirement be required to belong to a specification
  whose status is Accepted, and to be accepted on the base branch before code
  that references it merges? This would enforce specification-first ordering
  strictly but would block implementation while every current specification is
  Draft.
- Should the coverage check become an error, and for which specification
  statuses?

## Related Specifications

- [SPEC.md](../../../SPEC.md)
- [SPEC-0005: Build, Release, and Website Delivery](../../../specs/0005-build-release-and-website-delivery.md)
- [SPEC-0006: .NET Layered Architecture](../../../specs/0006-dotnet-layered-architecture.md)
