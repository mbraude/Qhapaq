import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import runbook_facts


def milestone(readiness_candidates: list[dict]) -> dict:
    return {
        "id": "I-0099-001",
        "spec": "SPEC-0099",
        "slug": "trace-checker",
        "kind": "implementation",
        "granularity": "milestone",
        "status": "open",
        "deps_ready": True,
        "child_items": [],
        "planning_readiness_scope": "trace-checker",
        "requirements": ["R-0010-001"],
        "manifest_spec_docs": [],
        "plan_approval": {"state": "absent"},
        "readiness_candidates": readiness_candidates,
    }


def readiness(
    *,
    assessment: str,
    current: bool = True,
    planning_only_language: bool = False,
) -> dict:
    return {
        "path": "work/0099/readiness/trace-checker.md",
        "scope": "trace-checker",
        "match": "scope",
        "assessment": assessment,
        "current": current,
        "stale_sources": ["SPEC.md(stale)"] if not current else [],
        "uncovered_manifest_spec_docs": [],
        "unmentioned_requirements": [],
        "planning_only_language": planning_only_language,
        "planning_only_excerpt": None,
    }


class MilestoneReadinessGateTests(unittest.TestCase):
    # spec: R-0010-001@7f4c61
    def test_milestone_with_missing_planning_readiness_gets_assessment_gate(self) -> None:
        entry, gates = runbook_facts.suggest(milestone([]), {})

        self.assertEqual("", entry["command"])
        self.assertEqual(
            "/spec-readiness 0099 scope=trace-checker",
            gates[0]["command"],
        )
        self.assertEqual("Gate - assessment required", gates[0]["status"])

    # spec: R-0010-001@7f4c61
    def test_milestone_waits_for_current_approved_readiness_before_planning(self) -> None:
        entry, gates = runbook_facts.suggest(
            milestone([readiness(assessment="blocked", current=False)]),
            {},
        )

        self.assertEqual("Open - blocked", entry["status"])
        self.assertEqual("", entry["command"])
        self.assertEqual(
            "/spec-readiness 0099 scope=trace-checker",
            gates[0]["command"],
        )
        self.assertIn("READINESS SPEC-0099 trace-checker", entry["blockers"])

    # spec: R-0010-001@7f4c61
    def test_milestone_requires_readiness_approval_before_planning(self) -> None:
        entry, gates = runbook_facts.suggest(
            milestone([readiness(assessment="ready-for-review")]),
            {},
        )

        self.assertEqual("", entry["command"])
        self.assertEqual(
            "/approve work/0099/readiness/trace-checker.md",
            gates[0]["command"],
        )

    # spec: R-0010-001@7f4c61
    def test_milestone_planning_is_eligible_after_current_approved_readiness(self) -> None:
        entry, gates = runbook_facts.suggest(
            milestone([readiness(assessment="approved")]),
            {},
        )

        self.assertEqual(
            "/implementation-plan 0099 item=I-0099-001",
            entry["command"],
        )
        self.assertEqual([], gates)

    # spec: R-0010-001@7f4c61
    def test_milestone_does_not_accept_planning_only_readiness(self) -> None:
        entry, _ = runbook_facts.suggest(
            milestone([
                readiness(assessment="approved", planning_only_language=True),
            ]),
            {},
        )

        self.assertEqual("<judge>", entry["command"])
