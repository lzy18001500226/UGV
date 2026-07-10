# Unified Obstacle Avoidance v88 Plan

Status: planned target-track candidate after v87 rejection. This document does
not claim score improvement, physical UGV behavior, report readiness, or
submission readiness.

## Baseline

Current accepted local wrapper baseline:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

Latest rejected candidate:

```text
v87 front-clear sustained side steer
Results/metrics/track2_candidate_review_v87_front_clear_sustained_side_steer_20260710.md
```

v87 showed that increasing the positive avoid-lateral steering command alone
does not improve the clean Track2 target gate.

## Evidence Basis

v80 residual road-edge contacts share a front-clear side-squeeze pattern:

```text
Results/metrics/collision_window_analysis_v80_all_tracks_20260710.md
Results/metrics/signal_window_summary_v80_all_tracks_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v80_all_tracks_20260710.md
```

Representative windows:

| Track | Time/s | df | dl | dr | final_speed | final_steer | Event |
|---|---:|---:|---:|---:|---:|---:|---|
| Track1 | 4.45 | 2.051 | 0.1012 | 0.1971 | 0.5358 | 0.5705 | cR +1 |
| Track2 | 4.70 | 2.052 | 0.1089 | 0.2710 | 0.5224 | 0.1816 | cR +1 |
| Track3 | 4.85 | 2.050 | 0.1060 | 0.2708 | 0.5105 | 0.1849 | cR +1 |
| Track4 | 4.35 | 2.052 | 0.1052 | 0.2674 | 0.5244 | 0.1796 | cR +1 |

Track3's first obstacle collision is different:

```text
t=1.05, df=0.01324, dl=0.4876, dr=0.6474
```

The v88 gate should not trigger in that first obstacle event because it is not
front-clear.

## Candidate Mechanism

Allowed target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change only the longitudinal avoid state's speed command:

```modelica
if df > safeF and (dl <= 0.12 or dr <= 0.12) then
  speed := -1.3;
else
  speed := -1;
end if;
flag := true;
```

This is not a per-track patch. It uses only the controller's existing
front/left/right distance inputs and targets a physically explainable behavior:
slow or reverse more aggressively only when the vehicle is already in obstacle
avoidance, the front is clear, and a side boundary is dangerously close.

## Difference From Rejected Routes

- Not v21 broad avoid-speed escalation: v88 is gated by `df > safeF` and a
  tight side-squeeze threshold.
- Not v70/v77 broad speed clamp: v88 lives in the obstacle controller's active
  avoid state, not in the path planner or global target-speed logic.
- Not v87 steering boost: v88 changes longitudinal safety behavior, not
  lateral steering magnitude.

## Target Gate

Run Track2 first:

```text
UGV.Test.Saidao2Eval
v80 Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true
```

Accept v88 for wider regression only if Track2 improves `cR` or `P` without a
new obstacle collision or worse runtime caveat. If Track2 remains unchanged or
regresses, reject v88, restore v80 source semantics, run the restore static
gate, and record the evidence.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.
