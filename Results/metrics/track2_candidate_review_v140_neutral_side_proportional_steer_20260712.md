# Track2 Candidate Review: v140 Neutral Side-Risk With Proportional Steering

## Decision

Rejected after the Track2 120 s comparable gate. The controller source was
restored to v80 semantics. No 700 s run or cross-track expansion was run.

## Candidate

- Design: `Docs/Design/unified_obstacle_avoidance_v140_neutral_side_proportional_steer_plan_20260712.md`
- Edited file: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Mechanism: neutral longitudinal authority for front-clear side risk plus
  proportional lateral magnitude capped at `0.6`.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0`, `medium=0` |
| Project tests | pass, `11 passed` |
| Track2 1 s | pass as load/check/simulate only, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s | fail as candidate acceptance gate |

## Track2 120 s Evidence

Run directory:
`Results/simulations/candidate_v140_neutral_side_proportional_steer_track2_120s_20260712/`

```text
runtime_status=simulate_returned_true
T=120.0 s
cR=2
cO=0
P=9.2
finish_distance_squared=329.7866977251163
```

The run reached the configured horizon, but v80's comparable result is
`T=120,cR=1,cO=0,P=9.6`. The additional road collision is a direct regression,
so the candidate is not retained. The finish-distance value is not an
official finish because it is far above `0.02`.

## Restore

The candidate source was restored to the v80 assignments:

```modelica
speed := -1;
steer := min(0.8, 2 * abs(dl - dr));
steer := -min(0.8, 2 * abs(dl - dr));
```

This result does not claim an 80/80 score, official completion, physical UGV
performance, or submission readiness.
