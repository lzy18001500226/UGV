# Unified Obstacle Avoidance v91 Plan

Status: rejected after Track2 target gate; source restored to v80 semantics,
2026-07-10 CST.

## Baseline

Current accepted local wrapper candidate:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

Latest rejection:

```text
Results/metrics/track3_candidate_review_v90_early_brake_weight_20260710.md
```

## Evidence Basis

v80 still has one early road contact on Track1, Track2, and Track4, and Track3
has one early obstacle contact plus one early road contact:

```text
Results/metrics/collision_window_analysis_v80_all_tracks_20260710.md
Results/metrics/signal_window_summary_v80_all_tracks_early_events_20260710.md
```

At the early event windows, obstacle avoidance is already active:

```text
flag=1
speed_oa=-1
steer_oa=0.6
```

The remaining issue is therefore not lack of avoid-mode entry. The current
`avoid_lateral` initial state emits a fixed positive `steer := 0.6` for its
initial period. If the controller exits and immediately re-enters avoid mode
while the side trigger remains true, this fixed initial output can repeatedly
override the gap-based lateral state.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Replace the fixed positive initial avoid-lateral steering output:

```modelica
steer := 0.6;
```

with gap-directed initial steering:

```modelica
if dl > dr then
  steer := -min(0.8, 2 * abs(dl - dr));
else
  steer := min(0.8, 2 * abs(dl - dr));
end if;
```

This keeps the existing output bound, keeps the same four-distance interface,
and makes the initial avoid-lateral state consistent with the later dynamic
left/right states.

## Difference From Rejected Routes

- Not v71/v76/v87: it does not simply increase a positive side-steer constant.
- Not v53/v54/v89: it does not change path-steering authority in
  `ControlAllocate`.
- Not v70/v77/v90: it does not clamp path speed or amplify reverse speed.
- Not v85: it does not shorten the lateral initial dwell; it changes the
  initial command from fixed to gap-directed.
- Not v62: it does not force a negative front-centered bypass; it selects the
  sign from left/right clearance.

## Target Gate

Run Track2 first:

```text
UGV.Test.Saidao2Eval
```

Accepted v80 Track2 baseline:

```text
T=120.0
cR=1
cO=0
P=9.6
simulate_returned_true / exit_state=0
```

Accept v91 for wider regression only if Track2 improves the road-collision
count or score without losing clean runtime. If Track2 is unchanged or
regresses, reject v91, restore v80 source semantics, run the restore static
gate, and record the evidence.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.

## Result And Decision

Target Track2 run:

```text
Results/simulations/controller_v91_gap_directed_initial_steer_saidao2_120s_20260710/
T=104.55
cR=2
cO=1
P=8.8
simulate_failed / exit_state=2
```

Decision: reject v91. It regressed the clean v80 Track2 gate from
`T=120.0,cR=1,cO=0,P=9.6` to `T=104.55,cR=2,cO=1,P=8.8`. The source was
restored to the v80 fixed initial `steer := 0.6` semantics and the restore
static gate passed:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v91_20260710.md
Results/metrics/track2_candidate_review_v91_gap_directed_initial_steer_20260710.md
```
