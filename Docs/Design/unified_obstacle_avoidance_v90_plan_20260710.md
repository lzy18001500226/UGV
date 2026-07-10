# Unified Obstacle Avoidance v90 Plan

Status: rejected after Track3 target gate; source restored to v80 semantics,
2026-07-10 CST.

## Baseline

Current accepted local wrapper baseline:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

Latest rejection:

```text
Results/metrics/track2_candidate_review_v89_side_squeeze_marker_20260710.md
```

## Evidence Basis

v80 Track3 loses one obstacle collision at `t=1.05 s` and one road collision at
`t=4.85 s`:

```text
Results/metrics/collision_window_analysis_v80_all_tracks_20260710.md
Results/metrics/trajectory_event_review_diagnostic_v80_track3_pose_20260710.md
```

The saved Track3 signal window shows obstacle avoidance already requests
reverse at about `t=0.15 s`, but the final allocated speed is still positive
near the first obstacle collision:

```text
t=1.05 s
speed_oa=-1
ctrlAlloc.speed ~= +0.72
obsAvoidController_Sysblock.chart.steer=0.6
```

So the immediate Track3 problem is not lack of detection. It is slow/weak early
braking through the allocation and first-order speed channel.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct `speed_oa -> gain1.u` connection with a conditional speed
command before the existing `factor_oa` gain:

```modelica
gain1.u = if speed_oa < 0 then 2 * speed_oa else speed_oa;
```

This keeps the forward/cruise side unchanged and increases only the reverse
avoidance braking request:

```text
old reverse contribution before first-order: -1 * factor_oa = -0.3
v90 reverse contribution before first-order: -2 * factor_oa = -0.6
```

The existing first-order filter remains in place, so this is not a hard
instantaneous speed jump.

## Difference From Rejected Routes

- Not v70/v77: it does not clamp the path-planner speed contribution.
- Not v88: it does not reduce speed only in a side-squeeze window.
- Not v84/v85: it does not add an initial pose/lane bias or dwell shortcut.
- Not v89: it does not alter steering or path-steering arbitration.

## Target Gate

Run Track3 first:

```text
UGV.Test.Saidao3Eval
```

Accepted v80 Track3 baseline:

```text
T=59.4
cR=1
cO=1
P=9.2
simulate_failed / exit_state=2
```

Accept v90 for wider regression only if Track3 improves `cO`, `cR`, `P`, or
runtime comparability without creating a non-comparable early-stop artifact.
If Track3 remains unchanged or regresses, reject v90, restore v80 source
semantics, run the restore static gate, and record the evidence.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.

## Result And Decision

Target Track3 run:

```text
Results/simulations/controller_v90_early_brake_weight_saidao3_120s_20260710/
T=4.60
cR=0
cO=0
P=10.0
simulate_failed / exit_state=2
```

Decision: reject v90. The run stopped at `T=4.60 s`, so the apparent `P=10.0`
is a non-comparable early-stop artifact, not a valid score improvement over
v80 Track3. The source was restored to the v80 direct `connect(speed_oa,
gain1.u)` semantics and the restore static gate passed:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v90_20260710.md
Results/metrics/track3_candidate_review_v90_early_brake_weight_20260710.md
```
