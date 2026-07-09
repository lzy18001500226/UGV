# Unified Obstacle Avoidance v52 Plan

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

Fresh v48/v50/v51 diagnostic evidence:

```text
Results/metrics/signal_window_summary_v48_v50_v51_track3_for_v52_20260710.md
Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md
Results/metrics/track3_candidate_review_v51_straight_brake_arbitration_20260710.md
```

The persistent Track3 first obstacle collision is not a trigger failure. In
v48 it appears around `1.05 s` while avoidance is already active:

```text
df=0.8306
dl=0.5677
dr=0.5673
flag=1
speed_pp=1
speed_oa=-1
steer_pp=-0.03857
steer_oa=0.6
speed=0.7196
steer=0.1623
```

Rejected nearby routes:

- v49 broad path-speed attenuation produced an early non-comparable stop.
- v50 lowered the curve-speed threshold and did not improve Track3 collision
  count or score.
- v51 straight-brake arbitration also produced early-stop score inflation.

## Hypothesis

Use a narrower `ControlAllocate` brake-turn coupling guard. Only when obstacle
avoidance is braking, path steering is nearly straight, and obstacle steering
opposes the delayed path steering, reduce forward-speed contribution and flip
the opposing delayed path steer into mild assistance.

Temporary v52 source hypothesis:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10 and steer_oa * unitDelay1.y < 0 then 0.75 * unitDelay3.y else unitDelay3.y;
gain3.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10 and steer_oa * unitDelay1.y < 0 then -0.5 * unitDelay1.y else if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

Rationale:

- Keep the change track-agnostic and bounded.
- Avoid v49/v51 broad speed suppression by requiring both near-straight path
  steering and opposing obstacle/path steering.
- Test the target weak window before any four-track expansion.

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
4. If Track3 does not improve, reject v52, restore v48 source semantics, send a
   sparse Chinese notice, and continue with another evidence-backed mechanism
   or research path.
5. If Track3 improves, run all four tracks before accepting v52.

## Closeout

v52 ran Track3 and is rejected:

```text
runtime: simulate_failed with result variables
exit_state: 2
T=8.35
cR=1
cO=1
P=9.2
```

This does not improve v48 Track3 (`T=112.45`, `cR=1`, `cO=1`, `P=9.2`) and
terminates much earlier. The first obstacle collision still appears around
`1.1 s`, so the brake-turn coupling did not solve the weak window.

Evidence:

```text
Results/evidence/controller_deployability_static_check_v52_brake_turn_coupling_20260710.md
Results/simulations/controller_v52_brake_turn_coupling_saidao3_120s_20260710/
Results/metrics/collision_window_analysis_v52_brake_turn_coupling_track3_20260710.md
Results/metrics/signal_window_summary_v52_brake_turn_coupling_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v52_20260710.md
```

Source was restored to v48 semantics. Do not continue brake-turn coupling,
straight-brake arbitration, or path-speed attenuation scans without a different
mechanism reason.

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV success.
- This plan does not authorize final submission packaging or sending.
