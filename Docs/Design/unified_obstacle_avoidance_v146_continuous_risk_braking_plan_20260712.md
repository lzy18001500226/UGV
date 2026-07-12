# v146 Continuous Risk Braking Plan

Status: rejected after Track2 120 s; exact v80 source semantics restored.

## Mechanism

v80 applies full reverse authority for every front or side trigger and stalls
Track2. v137 removes all side-only reverse authority and currently reproduces a
road-boundary failure. v146 replaces these two extremes with one normalized,
bounded risk function:

```modelica
speed := -min(1, max(
  max(0, (mindis-df)/mindis),
  max(0, (0.15-min(dl,dr))/0.15)));
```

Front intrusion and extremely small side clearance independently increase
reverse authority. Side distances above 0.15 release longitudinal braking while
the existing immediate lateral steering remains unchanged. This is one unified
controller for all tracks, with no track identification or official-model edit.

## Gates

Static deployability and tests, Track2 1 s, then Track2 120 s. Extend only if
the run exceeds the reproducible v137 `T=28.55` failure without worsening v80's
`cR=1,cO=0`. Any regression restores exact v80 semantics. Official completion
still requires `SimulateModel=false`, `T>10`, and finish distance below `0.02`.

## Result

Static deployability reported `high=0,medium=0`, all 11 tests passed, and the
Track2 1 s runtime gate passed. The 120 s request terminated at `T=39.3` with
`cR=1,cO=0,P=9.6`, finish distance squared `788.8771`. This exceeds the current
reproducible v137 failure time but is still an early road-boundary termination
and materially worse than v80's 120 s stability. Continuous longitudinal risk
weighting alone is therefore rejected.
