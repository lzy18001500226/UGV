# Unified Obstacle Avoidance v99 Plan

Status: planned before source edit, 2026-07-10 CST.

## Goal

Continue the long 80-point score sprint from the accepted local baseline
`v80_sharp_curve_speed_cap` without repeating rejected scalar scans.

The immediate target is to reduce the remaining early road-edge events while
preserving Track3 obstacle behavior and avoiding short-run score artifacts.

## Baseline

Accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

Current v80 residual events:

```text
Track1: cR=1, cO=0, P=9.6
Track2: cR=1, cO=0, P=9.6
Track3: cR=1, cO=1, P=9.2
Track4: cR=1, cO=0, P=9.6
```

The shared road-edge events occur near the early straight-side squeeze window:

```text
Track1 road event: df ~= 2.05, dl ~= 0.10, dr ~= 0.20
Track2 road event: df ~= 2.05, dl ~= 0.11, dr ~= 0.27
Track3 road event: df ~= 2.05, dl ~= 0.11, dr ~= 0.27
Track4 road event: df ~= 2.05, dl ~= 0.11, dr ~= 0.27
```

The Track3 first obstacle event is different:

```text
t=1.05, x ~= 1.20, y ~= 0.08, df ~= 0.013, cO +1
```

## Rejected Routes Not To Repeat

- Global fixed initial-steer scalar changes (`0.45`, `0.8`) regressed.
- Direct negative initial-steer overrides (`v96`, `v97`, `v98`) either caused
  Track1 short-run artifacts or worsened Track3.
- Stronger reverse/braking markers (`v90`, `v95`) produced early-stop artifacts.
- Broad path-authority neutralization and side-squeeze allocation markers
  regressed runtime or did not improve score.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add a small centerline-error damping term after the normal Pure Pursuit
steering calculation. The planner already knows the closest path segment and
the current vehicle position. v99 uses that information to compute signed
lateral error relative to the closest centerline segment.

Rule:

```text
if abs(centerline_error) > 0.25 m:
  steering_angle += clamp(0.25 * centerline_error_signed, -0.15, 0.15)
```

Sign convention:

- On the initial straight section, positive `y` gives a negative signed error.
- Adding the signed correction increases negative steering when the vehicle has
  drifted upward toward the road edge.
- The first Track3 obstacle event at `y ~= 0.08` should not trigger the
  correction, because it is below the 0.25 m deadband.

This is a unified path-tracking mechanism. It does not branch on track name,
score variable, time, official geometry, or wrapper model.

## Acceptance Gate

1. Static deployability checker passes with `high=0, medium=0`.
2. Run `UGV.Test.Saidao3Eval` first.
3. Accept for Track1 regression only if Track3 improves `cR`, `cO`, `P`, or
   runtime comparability without a new short-run artifact.
4. If Track3 improves, run Track1 next because v96 showed Track1 is the
   sensitive regression gate.
5. Only after Track3 and Track1 pass, expand to Track2 and Track4.

## Rejection Rule

Reject and restore v80 semantics if v99:

- keeps Track3 score unchanged while shortening runtime materially;
- creates a short-run `P=10` artifact;
- increases Track3 obstacle or road collisions;
- regresses Track1 below v80 when regression is run.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No per-track algorithm branch.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.
