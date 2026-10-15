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

    def test_work_item_source_checkbox_progress_does_not_stale_readiness(self) -> None:
        approved = (
            "---\n"
            "status: open\n"
            "id: I-0008-999\n"
            "---\n"
            "## Exit criteria\n"
            "- [ ] Required validation passes.\n"
        ).encode()
        current = approved.replace(b"- [ ]", b"- [x]")
        snap = self.snapshot(current)

        with patch.object(q, "recover_material_bytes", return_value=approved):
            state = q.source_state(
                snap,
                ITEM_PATH,
                "b" * 64,
                REVISION,
                material=q.material_sha256(approved),
            )

        self.assertEqual("current", state)

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

    def test_plan_approval_material_ignores_checklist_progress_only(self) -> None:
        approved = (
            "---\n"
            "status: open\n"
            "id: I-0008-999\n"
            "---\n"
            "## Exit criteria\n"
            "- [ ] Required validation passes.\n"
            "\n"
            "## Plan approval\n"
            "Approved material SHA-256: `PLACEHOLDER`.\n"
        ).encode()
        recorded_hash = q.material_sha256(approved)
        current = approved.replace(b"status: open", b"status: ready-for-review")
        current = current.replace(b"- [ ]", b"- [x]").replace(b"PLACEHOLDER", recorded_hash.encode())
        snap = self.snapshot(current)

        with patch.object(q, "recover_material_bytes", return_value=approved):
            rows, ok = work_hashes.cmd_evidence(snap, [ITEM_PATH], ["Plan approval"])

        self.assertTrue(ok)
        self.assertEqual("current", rows[0]["state"])
        self.assertEqual("progress-only", rows[0]["basis"])

    def test_plan_approval_manifest_output_hash_is_a_delivery_target(self) -> None:
        old_output = b"before\n"
        current_output = b"after\n"
        item_record = (
            "---\n"
            "id: I-0008-999\n"
            "---\n"
            "## File and ownership manifest\n"
            "| Action | Repository-relative path | Purpose | Project / namespace | Visibility |\n"
            "| --- | --- | --- | --- | --- |\n"
            f"| Modify | `{TARGET_PATH}` | Output | N/A | N/A |\n"
            "\n"
            "## Plan approval\n"
            f"| `{TARGET_PATH}` | baseline | `{q.sha256_bytes(old_output)}` |\n"
        )
        snap = self.snapshot(item_record.encode())
        snap._bytes[TARGET_PATH] = current_output

        rows, ok = work_hashes.cmd_evidence(snap, [ITEM_PATH], ["Plan approval"])

        self.assertTrue(ok)
        self.assertEqual("planned-output", rows[0]["state"])
        self.assertEqual("manifest", rows[0]["basis"])

    def test_plan_approval_non_manifest_input_change_remains_stale(self) -> None:
        old_input = b"before\n"
        current_input = b"after\n"
        item_record = (
            "---\n"
            "id: I-0008-999\n"
            "---\n"
            "## File and ownership manifest\n"
            "| Action | Repository-relative path | Purpose | Project / namespace | Visibility |\n"
            "| --- | --- | --- | --- | --- |\n"
            f"| Modify | `{TARGET_PATH}` | Output | N/A | N/A |\n"
            "\n"
            "## Plan approval\n"
            f"| `{RECORD_PATH}` | `{q.sha256_bytes(old_input)}` |\n"
        )
        snap = self.snapshot(item_record.encode())
        snap._bytes[RECORD_PATH] = current_input

        rows, ok = work_hashes.cmd_evidence(snap, [ITEM_PATH], ["Plan approval"])

        self.assertFalse(ok)
        self.assertEqual("stale", rows[0]["state"])

    def test_plan_approval_rejects_changed_criterion_text(self) -> None:
        approved = (
            "---\n"
            "status: open\n"
            "id: I-0008-999\n"
            "---\n"
            "## Exit criteria\n"
            "- [ ] Required validation passes.\n"
            "\n"
            "## Plan approval\n"
            "Approved material SHA-256: `PLACEHOLDER`.\n"
        ).encode()
        recorded_hash = q.material_sha256(approved)
        current = approved.replace(b"PLACEHOLDER", recorded_hash.encode())
        current = current.replace(b"Required validation", b"Required security validation")
        snap = self.snapshot(current)

        with patch.object(q, "recover_material_bytes", return_value=approved):
            rows, ok = work_hashes.cmd_evidence(snap, [ITEM_PATH], ["Plan approval"])

        self.assertFalse(ok)
        self.assertEqual("stale", rows[0]["state"])

    def test_plan_approval_accepts_plan_byte_change_when_material_is_same(self) -> None:
        path = "work/0008/plan.md"
        old_plan = b"---\nsources: [old]\n---\n\n## Phase 0\n- item\n"
        current_plan = b"---\nsources: [new]\n---\n\n## Phase 0\n- item\n"
        item_record = (
            "---\n"
            "id: I-0008-999\n"
            "---\n"
            "## Plan approval\n"
            f"| `{path}` | `{q.sha256_bytes(old_plan)}` |\n"
        )
        snap = self.snapshot(item_record.encode())
        snap._bytes[path] = current_plan

        with patch.object(q, "recover_bytes", return_value=old_plan):
            rows, ok = work_hashes.cmd_evidence(snap, [ITEM_PATH], ["Plan approval"])

        self.assertTrue(ok)
        self.assertEqual("current", rows[0]["state"])
        self.assertEqual("material fallback", rows[0]["basis"])


if __name__ == "__main__":
    unittest.main()
