# Track1/Track3 Candidate Review - v96 Severe Side Initial Steer Override

Status: rejected, 2026-07-10 CST.

## Baseline

Accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track1: simulate_failed, T=17.4, cR=1, cO=0, P=9.6
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v96_plan_20260710.md
```

Mechanism tested in the lateral avoid initial state:

```modelica
if dl < 0.2 and dr > dl then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v96_severe_side_initial_steer_override_20260710.md
high=0, medium=0
```

## Runtime Results

Target Track3:

```text
Results/simulations/controller_v96_severe_side_initial_steer_override_saidao3_120s_20260710/
simulate_failed, exit_state=2
T=35.9, cR=0, cO=1, P=9.6
```

Regression check Track1:

```text
Results/simulations/controller_v96_severe_side_initial_steer_override_saidao1_120s_20260710/
simulate_failed, exit_state=2
T=4.5, cR=0, cO=0, P=10.0
```

Track3 has a real score-variable improvement versus v80 (`P=9.2 -> 9.6` by
removing one road collision), but Track1 regresses into a much shorter early
stop artifact. The apparent Track1 `P=10.0` is not comparable and is worse than
v80's already-known early-terminal caveat.

## Diagnostics

```text
Results/metrics/collision_window_analysis_v96_track1_track3_20260710.md
Results/metrics/signal_window_summary_v96_track1_track3_20260710.md
```

## Decision

Reject v96 as an accepted baseline. Do not expand to Track2/Track4 because the
Track1 regression already violates the four-track acceptance gate. Restore v80
semantics and continue the score sprint with a mechanism that preserves Track1
runtime comparability.

Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v96_20260710.md
high=0, medium=0
```

## Reusable Learning

- Severe side-squeeze initial steer override can remove Track3 road collision.
- The same override can create an unacceptable Track1 short-run artifact.
- A future candidate may need a runtime-comparable way to keep the Track3 road
  benefit while not triggering the Track1 early-stop behavior.
