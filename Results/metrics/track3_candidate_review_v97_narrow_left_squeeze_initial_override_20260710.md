# Track3 Candidate Review - v97 Narrow Left-Squeeze Initial Override

Status: rejected, 2026-07-10 CST.

## Baseline

Accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v97_plan_20260710.md
```

Mechanism tested in the lateral avoid initial state:

```modelica
if df > 1.8 and dl < 0.13 and dr - dl > 0.13 then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

This narrowed v96's broad left-squeeze override using the observed difference
between the Track3 v80 road event and the Track1 v96 early-stop tail.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v97_narrow_left_squeeze_initial_override_20260710.md
high=0, medium=0
```

## Runtime Result

Track3:

```text
Results/simulations/controller_v97_narrow_left_squeeze_initial_override_saidao3_120s_20260710/
simulate_failed, exit_state=2
T=32.45, cR=13, cO=1, P=4.4
```

Diagnostics:

```text
Results/metrics/collision_window_analysis_v97_track3_20260710.md
Results/metrics/signal_window_summary_v97_track3_20260710.md
```

## Decision

Reject v97 immediately. It massively regresses Track3 road collisions and score
relative to v80, so it is not expanded to Track1/Track2/Track4.

Restore v80 semantics before continuing.

## Reusable Learning

- Reversing initial lateral steer only at a very narrow left-squeeze threshold
  is worse than both v80 and v96 on Track3.
- v96's Track3 improvement was not captured by a simple one-shot threshold on
  `df`, `dl`, and `dr-dl`; the timing/state interaction is more fragile than
  the event sample suggested.
- Do not continue the direct initial-steer override family without a different
  state-aware mechanism or stronger diagnostics.
