# Unified Obstacle Avoidance v82 Plan

Status: rejected_after_track2_gate, 2026-07-10 CST

## Goal

Continue from accepted v80 and test one unified path-tracking geometry
mechanism for the repeated early road-edge event. This candidate is not a
per-track patch, not a speed clamp, not a ControlAllocate path-authority scalar
scan, and not another obstacle-controller fixed-steer boost.

## Baseline

Current accepted local wrapper candidate:

```text
v80 total wrapper score: 38.0
Track1: P=9.6, cR=1, cO=0, simulate_failed/T=17.4
Track2: P=9.6, cR=1, cO=0, clean T=120
Track3: P=9.2, cR=1, cO=1, simulate_failed/T=59.4
Track4: P=9.6, cR=1, cO=0, clean T=120
```

## Evidence Basis

v80 control-window evidence shows the same early road-edge pattern on all four
tracks:

```text
flag = 1
dl around 0.10 at first road event
speed_oa = -1
steer_oa = 0.6
```

Track2 was rerun only for geometry export:

```text
Results/simulations/diagnostic_v80_track2_geometry_120s_20260710/
Results/metrics/trajectory_geometry_review_v80_track2_diagnostic_20260710.md
```

The clean Track2 diagnostic confirms the first score loss is a road-edge event:

```text
t = 4.70 s
x = 3.644
y = 0.4601
dRoadCenter = 0.4601
dNearestObs = 1.767
```

The 0-5 s exported control window shows the vehicle has already drifted toward
the road boundary before the road event. This is a path-tracking/road-margin
problem, not an obstacle-contact problem.

## Rejected Routes Not Repeated

Do not implement v82 as any of these:

- side-trigger threshold widening, already rejected by v40;
- fixed initial steering magnitude, already rejected by v66/v71 style tests;
- broader speed clamp or stronger reverse speed, already rejected by v21/v65/v70;
- ControlAllocate opposing-path neutralization/scalar scan, rejected by v53,
  v54, and v75;
- max-steer clipping, rejected by v79;
- low-speed lookahead floor, rejected by v55.

## Candidate Mechanism

v73/v74 showed that guarded shorter pure-pursuit lookahead can improve
road-edge behavior when the path angle is already medium-to-large. v82 extends
that idea to the smaller steering window that appears before the early road
event, while excluding the first Track3 obstacle event where path steering is
near zero.

Allowed source:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add parameters:

```modelica
parameter Real road_edge_short_lookahead_steer_min = 0.08;
parameter Real road_edge_short_lookahead_steer_max = 0.35;
parameter Real road_edge_short_lookahead_factor = 0.55;
parameter SIunits.Length road_edge_short_lookahead_min = 1.0;
parameter Real road_edge_short_lookahead_output_max = 0.6;
```

After the base steering angle is computed and before the existing v74
medium-curve short-lookahead branch, recompute the pursuit point only when:

```text
0.08 < abs(base_steering_angle) < 0.35
```

If the recomputed steering is too aggressive, restore the original pursuit
point and steering. This keeps v82 bounded and avoids repeating broad pursuit
geometry scans.

## Validation Gate

1. Run `Scripts/quality/check_controller_deployability.py`.
2. Run Track2 first, because v80 Track2 is clean runtime and has exactly one
   early road-edge event.
3. Accept expansion only if Track2 improves collision/score or stays clean
   without an earlier terminal state.
4. If Track2 improves, run Track3 next because it carries both the first
   obstacle event and the early road event.
5. Accept v82 only after all four tracks exceed v80 total or improve a weak
   track without reducing total score or introducing a worse runtime caveat.

## Gate Result

v82 is rejected. Track2 was the required first target gate because v80 Track2
was clean and carried the early road-edge event. The small-angle road-edge
short-lookahead mechanism regressed Track2 from v80 `P=9.6,cO=0` to
`P=9.2,cO=1`, so it must not be expanded to all four tracks.

Evidence:

```text
Results/simulations/controller_v82_road_edge_short_lookahead_saidao2_120s_20260710/
Results/metrics/trajectory_geometry_review_v82_track2_20260710.md
Results/metrics/track2_candidate_review_v82_road_edge_short_lookahead_20260710.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v82_20260710.md
```

The source was restored to v80 semantics after rejection. Do not continue
small-angle short-lookahead scans without new source-level evidence.

## Non-Goals

- No official vehicle, road, sensor, scoring, example, or material edits.
- No report/package work.
- No physical UGV success claim.
- No final competition or submission-readiness claim.
