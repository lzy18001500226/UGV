# Track2 Candidate Review: v141 Clearance-Based Avoidance Speed Governor

## Decision

Rejected after the Track2 120 s comparable gate. The controller source was
restored to the exact v80 semantic assignment. No 700 s run or cross-track
expansion was run.

## Candidate

- Design: `Docs/Design/unified_obstacle_avoidance_v141_clearance_speed_governor_plan_20260712.md`
- Edited file: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Mechanism: `speed := min(0.25, max(-1, df - safeF))` in the existing longitudinal avoid state.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0`, `medium=0` |
| Project tests | pass, `11 passed` |
| Track2 1 s | pass, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s | fail, additional road collision |

## Track2 120 s Evidence

Run directory:
`Results/simulations/candidate_v141_clearance_speed_governor_track2_120s_20260712/`

```text
runtime_status=simulate_returned_true
T=120.0 s
cR=2
cO=0
P=9.2
finish_distance_squared=169.5990275934002
```

The comparable v80 result is `T=120,cR=1,cO=0,P=9.6`. The candidate added a
road collision, so the lower terminal distance is not an accepted gain. It is
also not an official finish because `distanceSensor1.d` was not below `0.02`.

## Restore

The candidate assignment was removed and v80's `speed := -1` assignment was
restored. The v141 evidence remains for mechanism review; no v141 source is
retained.

This result does not claim official completion, an 80/80 score, physical UGV
performance, or submission readiness.
