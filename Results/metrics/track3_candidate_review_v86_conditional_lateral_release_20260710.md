# Track3 Candidate Review v86 Conditional Lateral Release

Status: rejected as an accepted baseline. This file is local wrapper evidence
only; it does not claim final competition score, physical UGV behavior, report
readiness, or submission readiness.

## Candidate

Baseline: v80 sharp curve speed cap.

Candidate source change:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
avoid_lateral.ini_state -> state transition:
after(2,sec)
  -> after(2,sec) or (after(1.5,sec) and abs(dl - dr) > 0.04)
```

Intent: keep the original fixed 2 s lateral hold by default, but release into
side-gap feedback earlier when a visible left/right distance imbalance exists.
This was intended to avoid repeating the v85 fixed-dwell scalar scan while
still trying to reduce the late Track3 road-edge squeeze.

Design note:

```text
Docs/Design/unified_obstacle_avoidance_v86_plan_20260710.md
```

## Static Gate

Initial v86 gate:

```text
Results/evidence/controller_deployability_static_check_v86_conditional_lateral_release_20260710.md
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

Restore gate after rejection:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v86_20260710.md
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
Results/simulations/controller_v86_conditional_lateral_release_saidao3_120s_20260710/
```

MWORKS wrapper result:

```text
model: UGV.Test.Saidao3Eval
stopTime: 120
simulate_returned: true
exit_state: 0
T: 120.0
cR: 4
cO: 1
P: 8.0
```

Trajectory event review:

```text
Results/metrics/trajectory_event_review_v86_conditional_lateral_release_20260710.md
Results/figures/trajectory_event_review_v86_conditional_lateral_release_20260710/controller_v86_conditional_lateral_release_saidao3_trajectory_events.png
```

Recorded events:

```text
t=1.05   cO 0->1, P 10.0->9.6, x=1.2,   y=0.0799, dNearestObs=0.1061
t=5.65   cR 0->1, P 9.6->9.2,  x=3.786, y=0.4642
t=7.70   cR 1->2, P 9.2->8.8,  x=4.816, y=0.4591
t=8.95   cR 2->3, P 8.8->8.4,  x=5.45,  y=0.4653
t=12.70  cR 3->4, P 8.4->8.0,  x=7.522, y=0.4627
```

## Decision

Reject v86. It makes Track3 runtime clean to `T=120`, but the score regresses
from v80 Track3 `P=9.2,cR=1,cO=1` to `P=8.0,cR=4,cO=1`. The conditional early
lateral release causes repeated upper-road-edge collisions, so it is not a
safe accepted baseline and should not be continued as a threshold scan without
new source-level evidence.

Current accepted baseline remains:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
```
