---
applyTo: "SPEC.md,specs/**/*.md"
---

# Specification Instructions

Follow [AGENTS.md](../../AGENTS.md).

- Write normative behavior independently of the .NET reference implementation
  unless a section is explicitly implementation-specific.
- Distinguish goals, required behavior, defaults, non-goals, alternatives, and
  open questions.
- Cover security, privacy, compatibility, testing, rollout, and recovery where
  applicable.
- Do not present an unresolved question as an accepted decision.
- Update cross-references, decision tables, artifact plans, and revision history
  when a change affects them.
- Preserve exact-version, canonical-definition, policy, and disclosure
  invariants unless the change explicitly revises the governing decision.
- Use relative links within repository Markdown.
- Do not mark an artifact-plan item complete until the persistent artifact and
  required validation exist.
- Group normative content that an implementation or test can satisfy into
  requirement blocks with stable identifiers, as defined by
  [ADR-0003](../../docs/architecture/decisions/0003-enforce-specification-traceability.md).
  A block is one cohesive rule that a single code unit would implement and
  cite: keep a small section as one block, and split a large section only where
  its parts would be implemented by different code or change independently.
  Start the block's first top-level paragraph with `**[R-<spec>-<sequence>]**`,
  for example `**[R-0001-012]**`; never tag inside a list, table, block quote,
  or code block. A block runs to the next identifier or heading.
  `SPEC.md` uses `0000` as its specification number. Assign the next unused
  sequence number within the specification; never encode section numbers.
  Identify requirements by meaning, including present-tense and "should"
  statements, not only by the word "must".
- Never renumber, reuse, or delete a requirement identifier. Retire a
  requirement by replacing its text with
  `*Retired; superseded by R-<spec>-<sequence>.*` or `*Retired.*`.
- Do not assign identifiers to goals, non-goals, summaries, terminology,
  rationale, alternatives, open questions, future-only direction, or revision
  history. Place examples and rationale before a block's identifier or under a
  separate heading if edits to them should not affect references.
- When changing any text inside a requirement block, find every `spec:`
  reference to its identifier, confirm the referencing code and tests still
  conform or update them, and update their fingerprints in the same change.
