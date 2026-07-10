# Unified Obstacle Avoidance v89 Plan

Status: rejected_as_accepted_baseline after Track2 target gate, 2026-07-10 CST.
This document does not claim score improvement, physical UGV behavior, report
readiness, or submission readiness.

## Baseline

Current accepted local wrapper baseline:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

Latest target-gate evidence:

```text
Results/metrics/track2_candidate_review_v87_front_clear_sustained_side_steer_20260710.md
Results/metrics/track2_candidate_review_v88_side_squeeze_speed_hold_20260710.md
Results/metrics/signal_window_summary_v87_v88_track2_timeaxis_20260710.md
```

v87 changed the side-squeeze avoid steering from `0.6` to `0.8`, but Track2
still stayed at `cR=1,P=9.6`. v88 reduced longitudinal speed in the same
front-clear side-squeeze window, but Track2 still stayed at `cR=1,P=9.6` and
runtime regressed. The aligned v87/v88 diagnosis shows that Track2's event
still has a negative path-planner steering contribution around `-0.22` while
obstacle avoidance requests right steering.

## Candidate Mechanism

Allowed targets:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
Models/UGV/Control/ControlAllocate/package.mo
```

v89 tests a narrow combined mechanism:

1. In active avoid-lateral positive steering states, detect the same front-clear
   left side-squeeze window and command a stronger but bounded avoid steering:

```modelica
if df > safeF and dl <= 0.12 and dl < dr then
  steer := 1.0;
else
  ...
end if;
```

2. In `ControlAllocate`, only when obstacle avoidance is reversing, the avoid
   steering command is the v89 side-squeeze marker (`steer_oa >= 1.0`), and
   path steering is opposing left, neutralize that path contribution:

```modelica
gain3.u = if speed_oa < 0 and steer_oa >= 1.0 and unitDelay1.y < 0 then 0
  else if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

This is not a per-track patch. It uses only existing controller/allocation
signals and is narrower than v75 because the allocation branch only activates
when the obstacle controller emits the v89 side-squeeze marker.

## Difference From Rejected Routes

- Not v87 alone: it pairs the side-squeeze marker with allocation behavior.
- Not v75 broad path neutralization: it does not neutralize all moderate
  opposing path steering, only the v89 side-squeeze marker window.
- Not v88 speed escalation: it does not change longitudinal speed.

## Target Gate

Run Track2 first:

```text
UGV.Test.Saidao2Eval
v80 Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true
```

Accept v89 for wider regression only if Track2 improves `cR` or `P` without a
new obstacle collision or worse runtime caveat. If Track2 remains unchanged or
regresses, reject v89, restore v80 source semantics, run the restore static
gate, and record the evidence.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.

## Result

v89 is rejected:

```text
Track2 v80 baseline: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true
Track2 v89 result:   T=5.15,  cR=1, cO=0, P=9.6, simulate_failed / exit_state=2
```

The first implementation attempt used an inline if expression in a
state-machine action and failed `CheckModel`; the Sysblock-compatible rewrite
used a normal `if ... then ... else ... end if` action and passed
`CheckModel`, but regressed runtime without score gain. Source semantics are
restored to v80 and the restore static gate passed.

Review:

```text
Results/metrics/track2_candidate_review_v89_side_squeeze_marker_20260710.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v89_20260710.md
```
