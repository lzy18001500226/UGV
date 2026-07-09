# Unified Obstacle-Avoidance v30 Plan

> One controller algorithm must run all four official tracks. This document
> records the v30 design and closeout after v13 was accepted and v14-v30 were
> rejected.

Status: executed and rejected, 2026-07-09 CST.

Closeout evidence:

```text
Results/evidence/controller_deployability_static_check_v30_side_danger_steering_floor_20260709_2109.md
Results/simulations/controller_v30_side_danger_steering_floor_saidao1_120s_20260709_2110/
Results/simulations/controller_v30_side_danger_steering_floor_saidao4_120s_20260709_2112/
Results/metrics/track1_track4_candidate_review_v30_side_danger_steering_floor_20260709_2116.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v30_20260709_2116.md
```

Decision: reject v30. It passed the static source gate, but Track1 and Track4
both stayed at `P=8.8`, `cR=3`, `cO=0`, matching v13 instead of improving it.
The source was restored to v13 semantics.

## 1. Goal

Build one Sysblock-compatible obstacle-avoidance controller that can be
evaluated on all four generated official-track wrappers:

```text
UGV.Test.Saidao1Eval
UGV.Test.Saidao2Eval
UGV.Test.Saidao3Eval
UGV.Test.Saidao4Eval
```

The controller may react to sensor inputs and internal state, but it must not
branch on track name, wrapper name, model path, scoring variables, or run id.

## 2. Current Accepted Baseline

Accepted controller:

```text
v13 side-trigger 0.45
```

Accepted evidence:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

Current wrapper metrics:

| Track | T/s | cR | cO | P |
|---|---:|---:|---:|---:|
| Track1 | 120.0 | 3 | 0 | 8.8 |
| Track2 | 91.9 | 1 | 0 | 9.6 |
| Track3 | 120.0 | 1 | 1 | 9.2 |
| Track4 | 113.1 | 3 | 0 | 8.8 |

Total wrapper score: `36.4`.

## 3. Failure Evidence

Use the saved diagnostics before making another controller edit:

```text
Results/metrics/collision_window_analysis_v13_track1_track3_20260709_1705.md
Results/metrics/signal_window_summary_v13_track1_track3_20260709_1705.md
Results/metrics/collision_window_analysis_v13_track4_20260709_1910.md
Results/metrics/signal_window_summary_v13_track4_20260709_1910.md
Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md
```

Observed pattern:

- Track1 and Track4 road contacts occur while `flag=1`, so v13 already entered
  avoid mode.
- Several contacts happen with one side distance near zero, so the failure is
  lateral clearance recovery, not only risk detection.
- v29 speed-only regulation did not improve Track1 or Track4, so speed alone is
  not enough for the next mechanism.

## 4. v30 Mechanism Hypothesis

Candidate:

```text
v30_side_danger_steering_floor
```

Mechanism:

- Keep v13 longitudinal trigger semantics:

```modelica
df <= mindis or dl <= 0.45 or dr <= 0.45
```

- Keep the same four-distance controller boundary.
- In avoid-lateral steering, retain the existing sign rule from side clearance:
  steer toward the side with more available clearance.
- Add a bounded steering floor in avoid mode so severe side-risk windows do not
  produce too-weak steering recovery.

Implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Allowed expression family:

```modelica
min(0.8, max(floor_value, 2 * abs(dl - dr)))
```

This is a mechanism-level change, not a track-specific patch. It should apply
to every track through the same state machine.

## 5. Acceptance Gate

v30 can be accepted only if all conditions hold:

1. Static deployability checker reports `high=0` and `medium=0`.
2. The first target run is comparable, not an early-stop score artifact.
3. Track1 or Track4 improves collision count or `P` against v13.
4. Four-track regression does not reduce total wrapper score against v13.
5. The source is restored to v13 if v30 fails.

Reject v30 if it:

- Improves one track by overfitting and regresses total score.
- Uses track names, wrapper names, or scoring variables in controller logic.
- Requires editing official road, vehicle, sensor, scoring, or example packages.
- Produces a high-looking but non-comparable early-stop result.

## 6. Execution Order

1. Record this design and update the status board.
2. Implement v30 in `ObsAvoidController_Sysblock2.mo`.
3. Run `Scripts/quality/check_controller_deployability.py`.
4. Run Track1 and Track4 first because v13/v29 evidence points there.
5. If target evidence improves, run Track2 and Track3 regression.
6. Write a candidate review under `Results/metrics/`.
7. Send one short Chinese terminal email at completion, blocker, or
   review-required state.
8. Commit with path-limited staging.

## 7. Non-Claims

- This plan does not claim physical UGV success.
- This plan does not claim final competition score.
- This plan does not authorize final submission/package sending.
