# Unified Obstacle Avoidance v87 Plan

Status: planned target-track candidate after v86 rejection. This document does
not claim score improvement, physical UGV behavior, report readiness, or
submission readiness.

## Baseline

Current accepted local wrapper baseline:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

v85 and v86 showed that earlier lateral release is harmful. v63 showed that
early front-obstacle steering feedforward is harmful. v75 showed that
allocation-only moderate opposing-path neutralization is harmful. v76 showed
that an initialization-only front-clear side-steer boost did not improve Track2
and worsened Track1 runtime.

## Evidence Basis

v80's remaining road-edge events share a front-clear left-side squeeze:

```text
Results/metrics/signal_window_summary_v80_all_tracks_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v80_all_tracks_20260710.md
```

Examples:

```text
Track2 t=4.70: df=2.0521, dl=0.1089, dr=0.2710, steer_oa=0.6, final_steer=0.1816
Track3 t=4.85: df=2.0498, dl=0.1060, dr=0.2709, steer_oa=0.6, final_steer=0.1849
Track4 t=4.35: df=2.0524, dl=0.1052, dr=0.2674, steer_oa=0.6, final_steer=0.1796
```

The v71/v72 review is also relevant:

```text
Results/metrics/track1_track4_candidate_review_v71_v72_steering_authority_20260710.md
```

v71 proved that sustained severe-side steering authority can remove a Track1
road collision, but it regressed Track4 by introducing a front-obstacle event
at `df ~= 0.01685`. v87 therefore adds the missing front-clear gate and tests a
target track before any regression expansion.

## Candidate Mechanism

Allowed target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change the active avoid-lateral positive steering states so that severe
front-clear left-side squeeze uses a stronger but still bounded right steering
command:

```modelica
if df > safeF and dl <= 0.12 and dl < dr then
  steer := 0.8;
else
  steer := 0.6;                         // initialization state
  // or the existing min(0.8, 2 * abs(dl - dr)) in sustained state
end if;
```

This is not a per-track branch. It uses only the existing front/left/right
distance signals already inside the obstacle controller.

## Target Gate

Run Track2 first:

```text
UGV.Test.Saidao2Eval
v80 Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true
```

Accept v87 for wider regression only if Track2 improves `cR` or `P` without a
new obstacle collision or worse runtime caveat. If Track2 remains `cR=1` or
early-stops, reject v87, restore v80 source semantics, run the restore static
gate, and record the evidence.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.
