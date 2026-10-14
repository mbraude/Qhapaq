---
id: I-0010-003
kind: implementation
granularity: milestone
change_kind: requirement
title: Deliver the selected work-run management interface
status: open
spec: SPEC-0010
requirements:
  - R-0010-002
  - R-0010-006
  - R-0010-008
depends_on: [D-0010-001, I-0010-001]
artifacts: []
---

# I-0010-003: Deliver the Selected Work-Run Management Interface

## Objective and coverage

Deliver the command-based or graphical interface selected by D-0010-001 for
creating and inspecting runs, pausing, resuming, cancelling, and reviewing
exact-snapshot gates.

The milestone may be explicitly deferred or cancelled if the architecture
decision selects a command-based initial experience. It is not executable as
written.

## Entry gates

D-0010-001 selects the interface for delivery. I-0010-001 is complete, and
current scoped readiness and concrete slices define the supported controls
and interaction behavior.

## File and ownership manifest

Pending the architecture decision, scoped readiness, and concrete slice
planning. This milestone is not executable.

## Design and integration

Present authoritative work status distinctly from orchestrator progress.
Show the exact scope, snapshot, and authorization target before accepting a
review or approval action. Keep the interface as a projection and control
surface, not another authority for work-item status.

## Tests and validation

Cover run creation and status, pause/resume/cancellation controls, interrupted
and stale runs, exact-snapshot review, authorization boundaries, and
accessibility/usability expectations appropriate to the selected interface.

## Exit criteria

- [ ] The selected interface exposes only authorized run controls.
- [ ] Run progress and authoritative work-item status are clearly distinct.
- [ ] Review actions identify the exact target snapshot before confirmation.
- [ ] Required tests and validation pass.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition into approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
