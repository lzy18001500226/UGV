# Track2 Candidate Review: v142 Side-Choice Hysteresis With Neutral Side Authority

## Decision

Rejected after the Track2 120 s comparable gate. The controller source was
restored to the exact v80 semantic assignments. No 700 s run or cross-track
expansion was run.

## Candidate

- Design: `Docs/Design/unified_obstacle_avoidance_v142_side_hysteresis_neutral_longitudinal_plan_20260712.md`
- Edited file: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Mechanism: front-clear side-risk used neutral longitudinal authority and
  side switching required a symmetric `0.15 m` clearance advantage.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0, medium=0` |
| Project tests | pass, `11 passed` |
| Track2 1 s | pass, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s | fail, early termination at `T=28.55,cR=1,cO=0,P=9.6` |

## Evidence

- 1 s run: `Results/simulations/candidate_v142_side_hysteresis_track2_1s_20260712/`
- 120 s run: `Results/simulations/candidate_v142_side_hysteresis_track2_120s_20260712/`
- Candidate static check: `Results/evidence/controller_deployability_static_check_v142_side_hysteresis_20260712.md`

The 120 s run did not materially improve the v80 comparison and terminated
far before the requested horizon. It is not a finish: `distanceSensor1.d` was
`791.4782768388438`, not below `0.02`. The candidate is therefore not retained.

## Restore

The side-choice transitions and longitudinal assignment were restored to v80:
`speed := -1` in the avoid state and the original strict left/right comparisons.
The v142 design and run evidence remain for audit. This result does not claim
official completion, an 80/80 score, physical UGV performance, or submission
readiness.
