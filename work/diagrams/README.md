# Generated Work-Plan Diagrams

This directory stores standalone `.mmd` Mermaid exports of repository
work-plan dependencies. Open them directly in Mermaid viewers to zoom and pan.
Each diagram is a generated view, not a second status or dependency authority;
the selected plans own phase membership and preferred order, and their item
files own status and prerequisite edges.

Regenerate a diagram from the repository root with the
[work-plan-diagram skill](../../.agents/skills/work-plan-diagram/SKILL.md) and
its standard-library [renderer](../../.agents/skills/work-plan-diagram/scripts/render.py).
For example:

```powershell
python .agents/skills/work-plan-diagram/scripts/render.py 0007 0008
```

The renderer validates item metadata, unique IDs, prerequisites, and graph
acyclicity before writing. Each export records UTC generation time, branch,
repository `HEAD`, source file count, source-set SHA-256, plan hashes, and
graph counts in Mermaid comments. A visible snapshot panel puts the time,
branch, abbreviated hashes, and counts inside the chart itself. Recorded
artifact paths are displayed on their owning item nodes.

Open items are blue with white text; complete items are green with white text.
Cancelled items are gray with dashed borders. Every item also includes its
persisted status in text, independently of color.

A source-set
digest identifies the exact plan and item bytes used, including working-copy
changes; `HEAD` alone does not describe uncommitted inputs. Use `--check` to
verify that a saved export is current without rewriting it. It reuses the
saved generation time, so passage of time does not make an export stale.
Filenames stay stable (for example `spec-0007-0008.mmd`) for versioning through
Git; regenerating refreshes the time in the chart.

Do not edit generated `.mmd` files by hand. Fix source records or the renderer,
then regenerate and review the resulting diff.
