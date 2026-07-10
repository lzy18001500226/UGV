# Track3 Candidate Review v85 Short Lateral Initial Hold

Status: rejected as an accepted baseline. This file is local wrapper evidence
only; it does not claim final competition score, physical UGV behavior, report
readiness, or submission readiness.

## Candidate

Baseline: v80 sharp curve speed cap.

Candidate source change:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
avoid_lateral.ini_state -> state transition:
after(2,sec) -> after(1.2,sec)
```

Intent: reduce the post-obstacle road-edge event seen in v80 Track3 by letting
side-distance steering take over earlier, without changing the longitudinal
avoid dwell, path planner, speed caps, official scoring, vehicle, road, or
wrappers.

Design note:

```text
Docs/Design/unified_obstacle_avoidance_v85_plan_20260710.md
```

## Static Gate

Initial v85 gate:

```text
Results/evidence/controller_deployability_static_check_v85_short_lateral_initial_hold_20260710.md
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

Restore gate after rejection:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v85_20260710.md
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Run folder:

```text
Results/simulations/controller_v85_short_lateral_initial_hold_saidao3_120s_20260710/
```

MWORKS wrapper result:

```text
model: UGV.Test.Saidao3Eval
stopTime: 120
simulate_returned: false
exit_state: 2
T: 2.55
cR: 0
cO: 1
P: 9.6
```

Trajectory event review:

```text
Results/metrics/trajectory_event_review_v85_short_lateral_initial_hold_20260710.md
Results/figures/trajectory_event_review_v85_short_lateral_initial_hold_20260710/controller_v85_short_lateral_initial_hold_saidao3_trajectory_events.png
```

The only recorded score event is still the first obstacle hit at `t=1.05 s`,
with nearest obstacle distance about `0.1061`, below the official
`CountPoint.mindis=0.11` threshold.

## Decision

Reject v85. Although the shorter lateral hold removes the later road-hit row
from the short exported result, the run terminates at `T=2.55`, far earlier
than v80 Track3 `T=59.4`. That makes the candidate non-comparable and unsafe as
an accepted high-score baseline.

Do not continue this route as a scalar dwell scan unless new evidence shows a
way to keep comparable runtime. The failed result suggests that the fixed
initial lateral hold is also carrying short-term stability, so the next
mechanism should not simply shorten or remove it.

Current accepted baseline remains:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
```
