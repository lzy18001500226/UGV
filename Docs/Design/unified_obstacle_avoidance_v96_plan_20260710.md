# Unified Obstacle Avoidance v96 Plan

Status: planned, 2026-07-10 CST.

## Baseline

Accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

Latest rejected candidate:

```text
v95_early_front_brake_marker
Results/metrics/track3_candidate_review_v95_early_front_brake_marker_20260710.md
```

## Evidence Basis

The v80 road events across all four wrapper tracks share a severe side-squeeze
pattern:

```text
Track1 cR: dl=0.1012, dr=0.1971, steer_oa=0.6
Track2 cR: dl=0.1089, dr=0.2710, steer_oa=0.6
Track3 cR: dl=0.1060, dr=0.2708, steer_oa=0.6
Track4 cR: dl=0.1052, dr=0.2674, steer_oa=0.6
```

The lateral state machine's avoid initial state always outputs `steer := 0.6`
for 2 s. Later feedback states would choose negative steering when `dr > dl`,
but the initial state can be re-entered during side-squeeze windows and keep the
vehicle steering in the collision direction.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

In the lateral avoid initial state, keep the v80 fixed `0.6` command for normal
front-risk starts, but override it when a severe left-side squeeze already
exists:

```modelica
if dl < 0.2 and dr > dl then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

This is a narrow geometry-gated correction. It is not a dwell-time scan and does
not alter the feedback transitions, speed allocation, path planner, official
tracks, or scoring.

## Difference From Rejected Routes

- Not v85/v86: it does not shorten or conditionally release the 2 s dwell.
- Not v91: it does not replace the initial command with direct gap steering for
  all starts.
- Not v94: it does not alter control allocation.
- Not v95: it does not strengthen braking or create a short-run speed artifact.
- Not per-track: the rule uses only four-distance geometry.

## Target Gate

Run Track3 first because it has both obstacle and road-event evidence:

```text
UGV.Test.Saidao3Eval
```

If Track3 reduces `cR` without increasing `cO` or creating an early-stop
artifact, run all four tracks before accepting. If unchanged or worse, restore
v80 semantics, run the restore static gate, write review evidence, commit,
push/email, and continue.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No per-track algorithm branch.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
