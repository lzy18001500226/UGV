# Track3 Candidate Review - v124 Native Derivative Risk

Status: rejected before target run

## Candidate

v124 kept the v80 controller structure and attempted to express predictive
front risk directly in the existing state-machine transition with `der(df)`.
It added no component, port, connection, official-model change, or per-track
branch.

## Gates

The deployability checker passed with `high=0`, `medium=0`, and the targeted
Python tests passed (`7 passed`). The Track3 1 s MWORKS gate then failed during
model derivation with explicit compiler error 23:

```text
不支持在Sysblock中使用内置函数der.
```

Evidence:
`Results/simulations/controller_v124_native_derivative_risk_saidao3_1s_20260711/`

## Decision

Reject v124 as non-deployable. Together with v123, this closes predictive
front-closing-rate entry for the current generated four-distance Sysblock:
external derived-signal ports are not accepted and native `der` is forbidden.
No score or completion claim exists. The source is restored to exact v80.
