import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import plan_reconciliations as reconciliations
import qhapaq_work as q


PLAN_PATH = "work/0099/plan.md"


def plan() -> str:
    return (
        "---\n"
        "spec: SPEC-0099\n"
        "process_version: 1\n"
        "sources: []\n"
        "---\n"
        "\n"
        "# SPEC-0099: Work Plan\n"
        "\n"
        "## Source reconciliation\n"
        "\n"
        "- Date: 2026-10-13. First review.\n"
        "- Preserved evidence.\n"
        "- Date: 2026-10-14. Second review.\n"
        "- More evidence.\n"
        "\n"
        "## Scope and authority\n"
        "\n"
        "Current scope.\n"
        "\n"
        "## Reconciliation evidence\n"
        "\n"
        "Undated extraction evidence.\n"
    )


class PlanReconciliationTests(unittest.TestCase):
    def test_transform_preserves_material_hash_and_splits_dated_records(self) -> None:
        original = plan()

        migration = reconciliations.transform(PLAN_PATH, original)

        self.assertEqual(
            q.source_material_sha256(PLAN_PATH, original.encode()),
            q.source_material_sha256(PLAN_PATH, migration.plan_text.encode()),
        )
        self.assertEqual(3, len(migration.records))
        self.assertIn("## Reconciliation index", migration.plan_text)
        self.assertNotIn("## Source reconciliation", migration.plan_text)
        self.assertNotIn("## Reconciliation evidence", migration.plan_text)
        self.assertIn("## Scope and authority", migration.plan_text)
        self.assertTrue(migration.plan_text.endswith(
            "The linked records are non-material and do not own current plan state.\n"
        ))

    def test_transform_creates_unique_names_for_same_date_and_section(self) -> None:
        original = plan().replace(
            "- Date: 2026-10-14. Second review.",
            "- Date: 2026-10-13. Second review.",
        )

        migration = reconciliations.transform(PLAN_PATH, original)

        names = [Path(record.path).name for record in migration.records]
        self.assertIn("2026-10-13-source-reconciliation.md", names)
        self.assertIn("2026-10-13-source-reconciliation-02.md", names)

    def test_transform_rejects_an_already_migrated_plan(self) -> None:
        migrated = plan().replace(
            "## Source reconciliation\n\n- Date: 2026-10-13. First review.\n"
            "- Preserved evidence.\n- Date: 2026-10-14. Second review.\n"
            "- More evidence.\n\n",
            "## Reconciliation index\n\n"
            "See [index](reconciliations/index.md).\n\n",
        ).replace(
            "## Reconciliation evidence\n\nUndated extraction evidence.\n",
            "",
        )

        with self.assertRaisesRegex(ValueError, "no extractable"):
            reconciliations.transform(PLAN_PATH, migrated)

    def test_move_index_to_end_preserves_material_hash(self) -> None:
        original = plan()
        migration = reconciliations.transform(PLAN_PATH, original)
        lines = migration.plan_text.splitlines(keepends=True)
        sections = reconciliations.level_two_sections(lines)
        scope_start = next(start for start, _, title in sections if title == "Scope and authority")
        index_start = next(start for start, _, title in sections if title == "Reconciliation index")
        early = "".join(lines[:scope_start] + lines[index_start:] + lines[scope_start:index_start])

        normalized = reconciliations.move_index_to_end(PLAN_PATH, early)

        self.assertEqual(
            q.source_material_sha256(PLAN_PATH, early.encode()),
            q.source_material_sha256(PLAN_PATH, normalized.encode()),
        )
        self.assertTrue(normalized.endswith(
            "The linked records are non-material and do not own current plan state.\n"
        ))

    def test_reconciliation_records_are_not_authoritative_sources(self) -> None:
        path = "work/0099/reconciliations/2026-10-14-review.md"

        self.assertEqual("reconciliation-record", q.source_kind(path))


if __name__ == "__main__":
    unittest.main()
