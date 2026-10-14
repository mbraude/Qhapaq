import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(
    0,
    str(
        Path(__file__).resolve().parents[2]
        / "skills"
        / "work-runbook-sync"
        / "scripts"
    ),
)

import qhapaq_work as q
import runbook_facts
import work_hashes


ITEM_PATH = "work/0008/implementation/I-0008-999-test.md"
REVISION = "a" * 40
RECORD_PATH = "work/0008/implementation/I-0008-999-record.md"
TARGET_PATH = "work/0008/implementation/I-0008-998-target.md"


def item(status: str, plan_evidence: str, scope: str = "same scope") -> bytes:
    return (
        "---\n"
        f"status: {status}\n"
        "id: I-0008-999\n"
        "---\n"
        "## Objective\n"
        f"{scope}\n"
        "\n"
        "## Plan approval\n"
        f"{plan_evidence}\n"
    ).encode()


class LegacyWorkItemSourceTests(unittest.TestCase):
    def snapshot(self, data: bytes) -> q.Snapshot:
        snap = q.Snapshot()
        snap._bytes[ITEM_PATH] = data
        return snap

    def test_approval_evidence_only_change_is_current(self) -> None:
        recorded = item("open", "approval pending")
        current = item("open", "approved with evidence")
        snap = self.snapshot(current)

        with patch.object(q, "recover_bytes", return_value=recorded):
            state = q.source_state(snap, ITEM_PATH, q.sha256_bytes(recorded), REVISION)

        self.assertEqual("current", state)

    def test_material_change_remains_stale(self) -> None:
        recorded = item("open", "approval pending")
        current = item("open", "approval pending", scope="changed scope")
        snap = self.snapshot(current)

        with patch.object(q, "recover_bytes", return_value=recorded):
            state = q.source_state(snap, ITEM_PATH, q.sha256_bytes(recorded), REVISION)

        self.assertEqual("stale", state)

    def test_unrecoverable_legacy_bytes_fall_back_to_recorded_revision(self) -> None:
        recorded = item("open", "approval pending")
        current = item("open", "approved with evidence")
        snap = self.snapshot(current)

        with patch.object(q, "recover_bytes", return_value=None), patch.object(
            q, "git_bytes", return_value=recorded
        ):
            state = q.source_state(snap, ITEM_PATH, q.sha256_bytes(recorded), REVISION)

        self.assertEqual("current", state)

    def test_verifier_labels_legacy_material_fallback(self) -> None:
        recorded = item("open", "approval pending")
        current = item("open", "approved with evidence")
        source_record = (
            "---\n"
            "id: I-0008-997\n"
            "sources:\n"
            f"  - path: {ITEM_PATH}\n"
            f"    revision: {REVISION}\n"
            f"    content_sha256: {q.sha256_bytes(recorded)}\n"
            "---\n"
        )
        snap = q.Snapshot()
        snap._bytes[RECORD_PATH] = source_record.encode()
        snap._bytes[ITEM_PATH] = current

        with patch.object(q, "recover_bytes", return_value=recorded):
            rows, ok = work_hashes.cmd_verify(snap, [RECORD_PATH])

        self.assertTrue(ok)
        self.assertEqual("material (legacy fallback)", rows[0]["basis"])
        self.assertEqual("current", rows[0]["state"])

    def test_recorded_material_hash_controls_source_currentness(self) -> None:
        current = item("open", "approved with evidence")
        snap = self.snapshot(current)

        matching = q.source_state(
            snap,
            ITEM_PATH,
            "b" * 64,
            REVISION,
            material=q.material_sha256(current),
        )
        stale = q.source_state(snap, ITEM_PATH, "b" * 64, REVISION, material="c" * 64)

        self.assertEqual("current", matching)
        self.assertEqual("stale", stale)

    def test_evidence_rows_support_legacy_bytes_and_material_basis(self) -> None:
        target = item("open", "approval pending")
        material_hash = q.source_material_sha256(TARGET_PATH, target)
        evidence = (
            "## Plan approval\n"
            f"| `{TARGET_PATH}` | `{q.sha256_bytes(target)}` |\n"
            f"| `{TARGET_PATH}` | bytes | `{q.sha256_bytes(target)}` |\n"
            f"| `{TARGET_PATH}` | material | `{material_hash}` |\n"
        )
        snap = q.Snapshot()
        snap._bytes[TARGET_PATH] = target
        snap._bytes[RECORD_PATH] = evidence.encode()

        rows, ok = work_hashes.cmd_evidence(snap, [RECORD_PATH], ["Plan approval"])

        self.assertTrue(ok)
        self.assertEqual(["bytes", "bytes", "material"], [row["basis"] for row in rows])
        self.assertEqual(["current", "current", "current"], [row["state"] for row in rows])

    def test_runbook_plan_approval_parser_accepts_both_hash_bases(self) -> None:
        target = item("open", "approval pending")
        material_hash = q.source_material_sha256(TARGET_PATH, target)
        item_record = (
            "---\n"
            "id: I-0008-999\n"
            "kind: implementation\n"
            "granularity: slice\n"
            "status: open\n"
            "spec: SPEC-0008\n"
            "title: fixture\n"
            "---\n"
            "## Plan approval\n"
            "Approved explicitly 2025-01-01.\n"
            f"| `{TARGET_PATH}` | `{q.sha256_bytes(target)}` |\n"
            f"| `{TARGET_PATH}` | bytes | `{q.sha256_bytes(target)}` |\n"
            f"| `{TARGET_PATH}` | material | `{material_hash}` |\n"
        )
        facts = runbook_facts.Facts("SPEC-0008", [])
        facts.snap._bytes[ITEM_PATH] = item_record.encode()
        facts.snap._bytes[TARGET_PATH] = target

        result = facts.load_item(ITEM_PATH)

        self.assertEqual("recorded", result["plan_approval"]["state"])
        self.assertEqual([], result["plan_approval"]["reviewed_hash_mismatches"])


if __name__ == "__main__":
    unittest.main()
