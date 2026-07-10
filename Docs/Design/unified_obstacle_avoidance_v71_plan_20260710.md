# v71 Severe-Side Steering Authority Plan

Status: planned candidate, 2026-07-10 CST.

## Goal

Improve the current v48 four-track controller by reducing remaining road-edge
contacts without creating a per-track branch or touching official road,
vehicle, sensor, scoring, or example files.

Current accepted baseline:

```text
v48 = v13 side trigger + v45 curvature speed cap + v48 opposing-steer guard
four-track local wrapper total P = 37.2 / 40
```

## Evidence Basis

H2 is based on saved v48 Track1 and Track4 collision-window evidence:

```text
Results/metrics/collision_window_analysis_v48_track1_track4_for_h2_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_track1_track4_for_h2_20260710.md
Results/metrics/signal_window_summary_v48_track1_track4_for_h2_20260710.md
```

Observed road-collision windows:

| Track | Time/s | dl | dr | flag | final_speed | steer_pp | steer_oa | final_steer | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Track1 | 6.55 | 0.1037 | 0.2667 | 1 | 0.5057 | 0.3006 | 0.6 | 0.5987 | Left clearance is already severe while active avoidance is running. |
| Track1 | 30.35 | 0.1087 | 0.2699 | 1 | 0.2535 | -0.6906 | 0.6 | -0.0463 | Path steering cancels obstacle steering near the left edge. |
| Track4 | 4.35 | 0.1052 | 0.2674 | 1 | 0.5244 | -0.2222 | 0.6 | 0.1796 | Left clearance is severe; final steering is too weak. |
| Track4 | 90.15 | 0.1087 | 0.2710 | 1 | 0.2539 | 1.6400 | 0.6 | 1.9390 | Large path steering is present; this event may not be fixed by stronger positive steer. |

The common signal is not general speed. v70 already tested a narrow active-avoid
speed clamp on Track3 and did not improve `P/cR/cO`. The open mechanism is
severe-side-window steering authority.

## Candidate Mechanism

v71 changes only the obstacle-avoidance controller lateral output inside the
active avoid path:

```text
if flag is active and dl <= 0.12 and dl < dr:
  command a stronger positive avoid steer
else:
  keep v48 steering behavior
```

Implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

The intended implementation is a narrow floor/boost in the active avoid
lateral states, not a global path-planner edit, not a speed scan, and not a
per-track branch. The first threshold is `dl <= 0.12` because the saved
collision windows are around `0.103-0.109`, while the existing trigger
`dl <= 0.45` is much broader.

MWORKS state-machine compatibility note: do not implement this as an inline
conditional expression. Prior v32 evidence and the first v71 compile attempt
show that state-machine actions reject `if ... then ... else ...` expressions.
Use a normal algorithm block:

```modelica
if dl <= 0.12 and dl < dr then
  steer := 0.8;
else
  steer := 0.6;
end if;
```

## Validation Plan

1. Apply the smallest source edit inside the allowed controller boundary.
2. Run:

```powershell
python Scripts\quality\check_controller_deployability.py --repo . --json-out Results\evidence\controller_deployability_static_check_v71_severe_left_steer_authority_20260710.json --md-out Results\evidence\controller_deployability_static_check_v71_severe_left_steer_authority_20260710.md --fail-on-high
```

3. First target Track1 because it has a clean v48 runtime and a clear
   cancellation window at `t=30.35`.
4. If Track1 improves `P`, `cR`, or does not regress while improving a collision
   window, run Track4.
5. Run four-track regression only after target evidence improves.
6. If v71 regresses or only creates an early-stop artifact, restore v48 source
   semantics and record a rejection review.

## Acceptance

v71 can supersede v48 only if:

1. at least one target weak track improves `P` or road-collision count;
2. the run is not a misleading early `P=10` stop;
3. static deployability remains `high=0`;
4. no hard no-edit zone is touched;
5. four-track total does not regress after target improvement.

## Non-Goals

- No official model, road, vehicle, sensor, scoring, or example edits.
- No report/package work in this candidate loop.
- No per-track special case.
- No claim of final competition or physical UGV success from local wrapper
  evidence.
