# Track3 Candidate Review - v111 Front-Aligned Approach Cap 0.45

Status: rejected_early_stop_artifact, 2026-07-11 CST.

## Baseline

Accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v111_plan_20260711.md
```

Temporary mechanism in `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
gain2.u = if speed_oa < 0 and steer_oa > 0.4 and abs(unitDelay1.y) < 0.12 and unitDelay3.y > 0.45
  then 0.45
  else unitDelay3.y;
```

The intent was to test a front-aligned approach cap stronger than v105 `0.55`
and less aggressive than v107 `0.35`.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v111_front_aligned_approach_cap045_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Track3 run:

```text
Results/simulations/controller_v111_front_aligned_approach_cap045_saidao3_120s_20260711/
runtime_status=simulate_failed
simulation_exit_state=2
T=1.85
cR=0
cO=0
P=10.0
```

The apparent `P=10.0` is not accepted because the run ended at `T=1.85`, far
before a comparable 120 s evaluation window. This is a short-run artifact, not
a stable score improvement over v80.

## Decision

Reject v111 as an accepted baseline.

Reasons:

```text
1. Track3 stops after 1.85 s, which is shorter than v110 and not comparable.
2. The candidate does not provide credible 120 s score evidence.
3. It belongs to the front-aligned cap family that now has v105 no-score-gain,
   v107 timeout, and v111 early-stop evidence.
```

Restore accepted v80 `ControlAllocate` semantics:

```modelica
gain2.u = unitDelay3.y;
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

## Follow-Up Direction

Do not continue front-aligned path-speed cap scalar scans. The next candidate
should use a materially different mechanism, such as a geometry/path-reference
change or a controller state memory change that is not an initial-steer override
and not another speed-only cap.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package readiness claim.
- No official vehicle, road, sensor, scoring, example, or official material edits.
