# Unified Obstacle Avoidance v53 Plan

Status: rejected_after_target_track_validation, 2026-07-10 CST

## Goal

Continue from v48, the current review-ready best four-track candidate, with one
unified mechanism. Do not branch by track name, wrapper name, run id, or
scoring variables.

## Evidence Basis

Current best:

```text
v48 total wrapper score: 37.2
Track1: P=9.2, cR=2, cO=0, simulate_returned_true
Track2: P=9.6, cR=1, cO=0, simulate_failed with result variables
Track3: P=9.2, cR=1, cO=1, simulate_failed with result variables
Track4: P=9.2, cR=2, cO=0, simulate_failed with result variables
```

Fresh diagnostic evidence:

```text
Results/metrics/ctrlalloc_contribution_analysis_v48_tracks134_for_v53_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v28_v35_v48_track3_for_v53_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v52_track3_20260710.md
```

Key reading:

- Track3 first obstacle collision is not a trigger failure. Avoidance starts
  early, but simply making speed braking stronger has already produced
  early-stop or no-improvement candidates in v28, v35, v49, v51, and v52.
- v48 improved the score by attenuating path steering when it opposes obstacle
  steering during reverse obstacle avoidance.
- Remaining v48 road-contact windows still show path steering opposing or
  dominating obstacle steering in some cases. Example Track1 at `30.35 s`:

```text
speed_pp=0.75
speed_oa=-1
steer_pp=-0.6906
steer_oa=0.6
final_steer=-0.04632
dl=0.2055
dr=0.3704
```

## Hypothesis

Keep v48's conflict-detection condition, but make the path-steer handoff
complete instead of half strength. When obstacle avoidance is braking and the
path planner asks for steering opposite to the obstacle-avoidance command,
temporarily neutralize the delayed path-steering contribution:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0
  else unitDelay1.y;
```

This is not a final-steering limiter and does not clip positive/negative
steering globally. It only removes the path-planner steering contribution
during an active path/avoidance conflict.

## Source Scope

Allowed edit:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Do not edit:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## Validation Gate

1. Run static deployability gate.
2. Run Track1 first because v48 Track1 is a complete 120 s reference and has
   two road contacts.
3. Accept target-track continuation only if Track1 improves `P`, `cR`, or road
   collision timing without adding obstacle collisions or producing an earlier
   terminal state.
4. If Track1 does not improve, reject v53, restore v48 source semantics, send a
   sparse Chinese notice, and continue with another evidence-backed mechanism
   or research path.
5. If Track1 improves, run Track3 next before any four-track acceptance,
   because Track3 is the known regression-sensitive track for steering
   authority changes.
6. If Track3 does not regress, run all four tracks before accepting v53.

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV success.
- This plan does not authorize final submission packaging or sending.

## Closeout

v53 ran Track1 and is rejected:

```text
runtime: simulate_failed with result variables
exit_state: 2
T=50.55
cR=4
cO=0
P=8.4
```

This regresses against v48 Track1 (`T=120.0`, `cR=2`, `cO=0`, `P=9.2`).
Collision-window evidence shows road contacts at `6.55 s`, `25.2 s`,
`40.5 s`, and `45.05 s`; v48 had only two road contacts at `6.55 s` and
`30.35 s`.

Evidence:

```text
Results/evidence/controller_deployability_static_check_v53_path_conflict_neutralization_20260710.md
Results/simulations/controller_v53_path_conflict_neutralization_saidao1_120s_20260710/
Results/metrics/collision_window_analysis_v48_v53_track1_20260710.md
Results/metrics/signal_window_summary_v48_v53_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v53_track1_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v53_20260710.md
```

Source was restored to v48 semantics. Do not continue complete path-steer
neutralization. The v48 half attenuation is currently safer than zeroing the
path-steering contribution.
