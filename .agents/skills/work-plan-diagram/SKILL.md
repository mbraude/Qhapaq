---
name: work-plan-diagram
description: "Generate and refresh snapshot-stamped Mermaid dependency diagrams from Qhapaq work plans. Use when visualizing specification decisions, implementation milestones, statuses, or cross-spec prerequisites."
argument-hint: "<spec-id> [spec-id ...]"
---

# Generate a Work-Plan Diagram

## Contract

Read the [specification-driven workflow](../../../docs/development/spec-driven-workflow.md)
and [work directory guidance](../../../work/README.md). This skill explicitly
exports a derived view; it never edits plans, items, statuses, dependencies,
approvals, readiness records, or product specifications. Work-item files remain
the only authority for item status and dependency edges.

## Procedure

1. Resolve each supplied four-digit specification ID to `work/<id>/plan.md`
   and its `decisions/` and `implementation/` item files. Include every item
   in the selected plans. Ask the user which scope to include if the request
   does not identify it.
2. Review the selected plans and item records. Check that each item's ID,
   owner, kind, title, status, and prerequisites are usable; IDs are unique;
   every prerequisite is present in the selected scope; and the combined
   dependency graph is acyclic. Stop and report any inconsistency instead of
   drawing a misleading graph.
3. Run the bundled standard-library-only
   [renderer](./scripts/render.py) from the repository root:

   ```powershell
   python .agents/skills/work-plan-diagram/scripts/render.py 0007 0008
   ```

   It writes `work/diagrams/spec-0007-0008.mmd`. With one ID it writes
   `work/diagrams/spec-<id>.mmd`. This standalone Mermaid file can be opened
   directly in viewers supporting zoom and pan. The graph is grouped by
   specification, with item kind, persisted status, recorded artifact paths,
   and prerequisite-to-dependent arrows. Open items are blue, complete items
   are green, and cancelled items are gray with dashed borders; status text
   remains visible so color is not the only distinction.
4. Review the rendered diff and confirm its snapshot metadata, item count,
   dependency count, cross-spec edges, and status labels agree with the input
   files. Do not manually edit generated diagrams; correct the source records
   or renderer and regenerate.
5. For a read-only freshness check, add `--check` to the command. A stale or
   missing export fails the check; it is not silently rewritten.

## Output and stop

The generated Mermaid file records UTC generation time, branch, `HEAD`, the
exact source-file count and SHA-256 digest, each plan's SHA-256 digest, and
graph counts in Mermaid comments. A visible snapshot panel repeats the time,
branch, shortened hashes, and counts inside the chart. Recorded artifact paths
appear on their owning item nodes; they are not proof of publication.
It is a working-copy snapshot when its plan or item files have uncommitted changes.
The filename is stable for reviewable Git diffs. Regeneration updates the
timestamp; `--check` reuses the saved timestamp and checks all other content
without writing, so passage of time alone does not make a chart stale.
Generated graphs are not editable status authorities and do not approve,
complete, or authorize any work.

Evaluation: duplicate IDs, missing prerequisites, unsupported metadata, and
cycles stop generation; each item is rendered once; every dependency points
from prerequisite to dependent; `--check` detects a stale export.
