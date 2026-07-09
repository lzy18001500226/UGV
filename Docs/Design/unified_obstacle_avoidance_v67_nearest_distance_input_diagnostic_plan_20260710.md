# Unified Obstacle Avoidance v67 Diagnostic Plan - Nearest Distance Input

Status: planned diagnostic, not an accepted controller candidate.

## Goal

Test whether the remaining Track3 v48 failure is primarily caused by missing
nearest-distance risk input rather than by steering/speed scalar tuning.

This plan follows the user's current rule: one unified obstacle-avoidance
algorithm across all four tracks. The diagnostic may use a generated wrapper to
study signal semantics, but any accepted competition candidate must later have
a clean deployment path.

## Baseline

Current accepted baseline:

```text
v48 opposing-steer guard
```

Evidence:

```text
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
Results/evidence/track3_v48_sensor_semantic_gap_20260710.md
```

## Problem Statement

Track3 v48 countPoint diagnostics show:

- `distanceSensor1.DisObstacle` and `countPoint.DisObstacle` reach the
  obstacle threshold near `1.05 s`, while controller `df` is still about
  `0.8306`.
- `distanceSensor1.DisRoad` and `countPoint.DisRoad` reach the road threshold
  near `4.85 s`, while controller `dl/dr` still look relatively safe.

The controller therefore does not receive the same geometric risk surface that
the scorer uses.

## Diagnostic Route

Create a generated diagnostic wrapper under:

```text
Models/UGV/Test/
```

The diagnostic wrapper should not modify official files. It may temporarily
connect score-source sensor outputs into the controller-facing risk inputs to
answer one question:

```text
If nearest obstacle distance is visible to the controller, does Track3 remove
or materially delay the first obstacle event without per-track logic?
```

Start with the narrowest diagnostic:

```modelica
connect(obsAvoidController_Sysblock.front_dist, distanceSensor1.DisObstacle);
connect(obsAvoidController_Sysblock.rear_dist, distanceSensor1.rear_dist);
connect(obsAvoidController_Sysblock.left_dist, distanceSensor1.left_dist);
connect(obsAvoidController_Sysblock.right_dist, distanceSensor1.right_dist);
```

Do not claim this as final competition evidence. It changes the evaluation
wrapper input semantics and exists only to prove or reject the nearest-distance
input hypothesis.

## Acceptance For Diagnostic

The diagnostic is useful if it produces any of the following:

1. Track3 first obstacle event is removed or delayed with comparable runtime.
2. Track3 score improves without an early-stop artifact.
3. The run proves that nearest-distance access is still insufficient, allowing
   us to stop wasting attempts on interface-level changes.

## Rejection Rules

Reject the route if:

- it only improves readable `P` through very early termination;
- it requires editing official `Vehicle`, `saidao`, `CountPoint`, or `Example`
  files;
- it creates per-track behavior;
- it cannot be mapped to a deployable controller/interface story.

## Next Step After Diagnostic

If the diagnostic improves Track3, design the smallest formal interface change
or wrapper-generation workflow that makes nearest-risk signals explicit and
track-agnostic. If it fails, return to v48 and research trajectory-level
avoidance that can work with only the four directional inputs.
