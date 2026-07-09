# Unified Obstacle Avoidance v51 Plan

Status: rejected_after_target_track_validation, 2026-07-10 CST

## Goal

Continue from v48, the current review-ready best four-track candidate, with one
unified mechanism. Do not branch by track name, wrapper name, run id, or
scoring variables.

## Evidence Basis

Current best:

```text
v48 total wrapper score: 37.2
Track1: P=9.2, cR=2, cO=0
Track2: P=9.6, cR=1, cO=0, simulate_failed with result variables
Track3: P=9.2, cR=1, cO=1, simulate_failed with result variables
Track4: P=9.2, cR=2, cO=0, simulate_failed with result variables
```

Fresh v48/v50 evidence:

```text
Results/metrics/signal_window_summary_v48_path_ctrl_20260710.md
Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md
```

The persistent Track3 obstacle collision occurs at `1.05 s` while avoidance is
already active:

```text
df=0.8306
dl=0.5677
dr=0.5673
flag=1
pathPlanner.steering_angle=-0.03857
ctrlAlloc.speed_pp=1
ctrlAlloc.speed_oa=-1
ctrlAlloc.firstOrder1.y=-0.2804
ctrlAlloc.speed=0.7196
```

This is not a trigger failure. It is a straight-line early obstacle window
where the path-planner forward-speed contribution still dominates the filtered
obstacle-avoidance braking contribution.

Rejected nearby routes:

- v24 reduced the obstacle-avoidance filter time constant globally and caused
  early termination without score improvement.
- v28 doubled the obstacle-avoidance speed channel and produced a
  non-comparable early stop.
- v49 attenuated path speed during all reverse avoidance and also produced an
  early stop.
- v50 lowered the curvature speed threshold and did not improve Track3
  collision counts or score.

## Hypothesis

Use a narrow arbitration guard in `ControlAllocate`: when obstacle avoidance is
asking for reverse/braking and the delayed path steering is nearly straight,
temporarily reduce the path-planner forward-speed contribution. This targets
the straight-on obstacle collision without suppressing path speed during
curves, wall-following, or later road-contact windows.

Proposed logic:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10
  then 0.4 * unitDelay3.y
  else unitDelay3.y;
```

Rationale:

- Track3 early obstacle event has `abs(steer_pp) ~= 0.04`, so the guard should
  activate.
- Road-contact windows in v48 usually have `abs(steer_pp) ~= 0.22` or larger,
  so the guard should not become v49-style broad path-speed attenuation.
- The rule is track-agnostic, bounded, and deployable as a local arbitration
  safety rule.

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
2. Run Track3 first.
3. Accept target-track continuation only if Track3 removes the early obstacle
   collision, improves `P`, or improves collision counts without a worse
   non-comparable terminal state.
4. If Track3 does not improve, reject v51, restore v48 source semantics, send a
   sparse Chinese notice, and continue with another evidence-backed mechanism
   or research path.
5. If Track3 improves, run all four tracks before accepting v51.

## Closeout

v51 ran Track3 and is rejected:

```text
runtime: simulate_failed with result variables
exit_state: 2
T=2.25
cR=0
cO=0
P=10.0
```

The readable `P=10.0` is not valid improvement evidence because the run exits
at only `2.25 s`, before the comparable 120 s review window.

Evidence:

```text
Results/simulations/controller_v51_straight_brake_arbitration_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v51_straight_brake_arbitration_20260710.md
Results/metrics/collision_window_analysis_v51_straight_brake_arbitration_track3_20260710.md
Results/metrics/signal_window_summary_v51_straight_brake_arbitration_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v51_20260710.md
```

Source was restored to v48 semantics. Do not continue path-speed attenuation
or straight-brake arbitration scans without a different mechanism reason.

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV success.
- This plan does not authorize final submission packaging or sending.
