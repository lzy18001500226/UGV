# Unified Obstacle Avoidance v54 Plan

Status: planned_for_target_track_validation, 2026-07-10 CST

## Purpose

Continue from v48, the current review-ready best four-track wrapper candidate,
without treating rejected follow-up candidates as a stopping condition.

v49-v53 showed that stronger scalar speed suppression, straight braking,
brake-turn coupling, and complete path-steer neutralization do not improve the
weak tracks. v54 therefore tests a narrow path-authority mechanism instead of
another broad threshold scan.

## Baseline

Current accepted baseline:

```text
v48 total wrapper score: 37.2
Track1: T=120.0, cR=2, cO=0, P=9.2
Track2: T=60.15, cR=1, cO=0, P=9.6
Track3: T=112.45, cR=1, cO=1, P=9.2
Track4: T=112.4, cR=2, cO=0, P=9.2
```

Important caveat: Track2/3/4 v48 values are read from exported result
variables after `SimulateModel` returned false with `exit_state=2`; this is not
final competition or physical UGV proof.

## Evidence Used

Local analysis:

```text
Results/metrics/ctrlalloc_contribution_analysis_v48_v52_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v53_track1_20260710.md
Results/metrics/signal_window_summary_v45_v48_tracks134_20260710.md
```

Research notes:

```text
References/research/deployable_ugv_avoidance_algorithms_20260709/source_notes.md
References/research/robust_physical_ugv_navigation_20260709/source_notes.md
References/research/steering_authority_wall_following_20260710/source_notes.md
```

## Hypothesis

v48 fixed one Track1 road-collision mode by attenuating opposing path steering
to 50% while obstacle avoidance is reversing. v53 proved that reducing this
path contribution to zero is too aggressive and regresses Track1.

v54 tests a middle ground:

```text
when obstacle avoidance is active and reversing
and obstacle steering opposes path steering:
  keep a small path contribution, but less than v48's 50%
```

This is intended to give the safety layer more steering authority in the early
Track3 obstacle window while still retaining enough path authority to avoid the
Track1 regression seen in v53.

## Candidate Change

Implementation target:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Temporary v54 source hypothesis:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.35 * unitDelay1.y
  else unitDelay1.y;
```

This remains one unified algorithm:

- no track-name branch
- no wrapper-name branch
- no run-id branch
- no score-variable branch
- no official road, vehicle, sensor, scoring, or example edits

## Why This Is Not A Blind Scalar Scan

The tested scalar is not a general speed, dwell, or side-threshold sweep. It is
the only remaining continuous value inside the already accepted v48
path-authority mechanism, bounded by two observed facts:

- v48 `0.5` improves Track1 versus v45.
- v53 `0.0` regresses Track1.

v54 tests whether a slightly stronger but nonzero safety-layer authority can
remove or delay the Track3 early obstacle event without triggering the Track1
regression.

## Validation Plan

1. Run source deployability checker after editing.
2. Run Track3 first because it contains the earliest obstacle collision that
   v49-v52 failed to remove.
3. Accept target-track expansion only if Track3 improves collision count,
   score, or comparable terminal behavior without a new non-comparable early
   stop.
4. If Track3 improves, run Track1 regression next before four-track expansion.
5. If Track3 does not improve, reject v54, restore v48 semantics, record
   evidence, send the sparse terminal email, commit the rejected attempt, and
   continue with the next evidence-backed mechanism.

## Acceptance Rule

v54 can replace v48 only if it improves total four-track evidence or gives a
clear target-track improvement without a Track1/Track4 regression. Otherwise
v48 remains the current review-ready best.

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV success.
- This plan does not authorize a final package or submission email.
