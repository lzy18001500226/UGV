# Track1 Candidate Review - v22 Lateral Init Dwell 1.5s

timestamp: 2026-07-09 CST
scope: targeted Track1 follow-up after v20/v21 rejection
accepted_controller_after_review: v13_side_trigger045

## Hypothesis

v13 Track1 road collisions occurred while `avoid_lateral` was still in its
initial fixed-steer window. v7 had already shown that `0.5s` is too aggressive
on Track3, so v22 tested a smaller midpoint change:

```text
avoid_lateral initialization dwell: 2s -> 1.5s
```

No official no-edit zone was modified. The only source change was in:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

## Static Check

```text
Results/evidence/controller_deployability_static_check_v22_lateral_init_dwell15_20260709_1805.md
ready_for_physical_claim=true, high=0, medium=0
```

## Track1 Runtime Evidence

```text
Results/simulations/controller_v22_lateral_init_dwell15_saidao1_120s_20260709_1808/
T=120.0, cR=15, cO=1, P=3.6
```

Decision: reject v22. Shortening the lateral initialization dwell from 2s to
1.5s badly increases road collisions. This confirms that v7 was not just an
extreme outlier; the current lateral state handoff is fragile and should not be
tuned by reducing this dwell.

## Source Restoration

The controller source was restored to v13 semantics after v22:

```text
avoid_lateral initialization dwell: 2s
```

Restoration static check:

```text
Results/evidence/controller_deployability_static_check_v13_restored_after_v22_20260709_1815.md
ready_for_physical_claim=true, high=0, medium=0
```

## Next Direction

Do not retry shorter `avoid_lateral` initialization dwell values. If further
controller tuning is attempted, prefer analysis of path-planner and
ControlAllocate interaction, or a separate conservative rule that does not
destabilize the current lateral handoff.
