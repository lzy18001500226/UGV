# Track3 v48 Event Source Attribution

timestamp: 2026-07-10 06:16 CST
baseline: v48 opposing-steer guard
scope: offline analysis of saved MWORKS evidence; no live run in this note

## Evidence Inputs

```text
Results/simulations/diagnostic_v48_track3_countpoint_6s_20260710/
Results/simulations/controller_v48_signal_geometry_saidao3_120s_20260710/
Results/metrics/track3_v48_countpoint_source_attribution_20260710.md
Results/metrics/track3_v48_countpoint_source_attribution_20260710.json
```

## Source-Level Facts

- `distanceSensor1.DisObstacle` is the Euclidean distance from the vehicle to
  the nearest obstacle point in body coordinates.
- `distanceSensor1.front_dist` is not always the nearest obstacle distance. It
  switches to obstacle front distance only when the obstacle lies inside the
  lateral body-width gate; otherwise it uses path lookahead distance.
- `CountPoint` increments obstacle and road collisions when the scoring
  distance falls below `mindis=0.11`.
- Current v48 longitudinal avoid mode enters on
  `df <= mindis or dl <= 0.45 or dr <= 0.45`, then commands `speed=-1` and
  `flag=true` for the lateral avoid state.
- Current v48 `avoid_lateral` initial state commands fixed `steer := 0.6` for
  two seconds before the side-distance comparison states take over.

## Track3 Event Attribution

The saved 6 s diagnostic shows two score changes:

| Time/s | Score change | Key window values | Interpretation |
|---:|---|---|---|
| 1.05 | `cO: 0 -> 1`, `P: 10.0 -> 9.6` | `DisObstacle ~= 0.106`, `DisRoad ~= 0.488`, `df ~= 0.013`, `flag=1`, `steer_oa=0.6`, `final_steer ~= 0.162` | The obstacle event occurs while v48 is already in avoid mode. Front/side triggering is not absent; the effective early lateral action is limited by the fixed initial steer plus allocation dynamics. |
| 4.85 | `cR: 0 -> 1`, `P: 9.6 -> 9.2` | `DisRoad ~= 0.105`, `DisObstacle ~= 1.397`, `dl ~= 0.105`, `dr ~= 0.270`, `flag=1`, `steer_oa=0.6`, `final_steer ~= 0.185` | The road event also occurs in avoid mode and while the lateral state is still producing fixed initial steer, not the later side-distance state. |

## Candidate Implication

Do not continue front-only emergency braking, front-centered negative bypass,
or close-side direction switching. Those routes are already rejected or
mechanistically weak for the observed events.

The remaining narrow hypothesis is to keep v48's initial steering direction
but increase its magnitude only when the vehicle is already in avoid mode and a
side scoring distance is truly close. This targets the Track3 road event
without changing the early obstacle event where both side distances are still
well above the road threshold.

This note does not claim improved score or physical UGV readiness.
