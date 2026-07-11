# Unified Obstacle Avoidance v110 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the current accepted local wrapper
baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
effective contest target: about 76 / 80
```

The target is still Track3's remaining combined obstacle/road weakness without
regressing Track1:

```text
v80 Track3: T=59.4,cR=1,cO=1,P=9.2
v80 Track1: T=17.4,cR=1,cO=0,P=9.6
```

## Evidence Basis

Use the time-axis-safe summaries:

```text
Results/metrics/signal_window_summary_v80_all_tracks_countpoint_pose_20260710.md
Results/metrics/signal_window_summary_v80_track3_pose_path_6s_20260710.md
Results/metrics/four_track_candidate_review_v103_conflict_path_speed_20260711.md
Results/metrics/four_track_candidate_review_v109_asymmetric_left_squeeze_20260711.md
```

The relevant v80 event split is:

```text
Track1 road event: steer_pp ~= +0.284, cR=1,cO=0,P=9.6
Track2 road event: steer_pp ~= -0.220, cR=1,cO=0,P=9.6
Track3 road event: steer_pp ~= -0.221, cR=1,cO=1,P=9.2
Track4 road event: steer_pp ~= -0.222, cR=1,cO=0,P=9.6
```

v103 proved that changing the conflict window can improve Track3, but its
speed-gate route regressed Track1. v109 proved that asymmetric initial-steer
variants can create short-run artifacts and are not reliable. v110 therefore
moves the experiment to the path-planning layer and uses a sign-specific
moderate-curve trigger, rather than changing active obstacle-avoidance state
actions or broad speed gates.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add a guarded negative moderate-curve short-lookahead trial. The trigger is
only the path-planner steering sign and magnitude:

```modelica
base_steering_angle < -0.18 and base_steering_angle > -0.28
```

The trial recomputes the pursuit point with a shorter lookahead. It must roll
back to the original pursuit point if the recomputed steering flips sign or
becomes too aggressive.

Expected impact:

```text
1. Track3/2/4 negative moderate road windows can receive earlier right-curve
   authority.
2. Track1 positive road window is not triggered by the sign gate.
3. Existing v80 extreme-curvature speed cap remains intact.
```

## Difference From Rejected Routes

- Not v103/v106: no conflict-window speed gate.
- Not v96-v100/v109: no obstacle-controller initial-steer reversal or squeeze.
- Not v50/v108: not a scalar speed threshold scan.
- Not per-track: no track id, score variable, time, result file, or official
  geometry branch.

## Target Gate

1. Run static deployability gate.
2. Run `UGV.Test.Saidao3Eval` for 120 s first.
3. If Track3 does not improve score/collision/runtime comparability, reject and
   restore v80.
4. If Track3 improves, run Track1 before four-track acceptance because Track1
   is the main regression risk after v103.
5. Accept only after four-track evidence beats v80 total `38.0 / 40` without a
   new short-run artifact.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.
