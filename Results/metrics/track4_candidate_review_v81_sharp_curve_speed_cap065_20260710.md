# Track4 Candidate Review - v81 Sharp Curve Speed Cap 0.65

Status: rejected, 2026-07-10 CST

## Candidate

v81 keeps the v80 extreme-curvature speed-cap mechanism but raises the cap from
`0.55` to `0.65`:

```modelica
parameter Real sharp_curve_slowdown_speed = 0.65;
```

The intent was to preserve v80 Track4 score improvement while reducing the
runtime caveat risk seen on v80 Track3.

## Result

| Track | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| Saidao4Eval | `simulate_failed` | 2 | 52.6 | 1 | 0 | 9.6 | `Results/simulations/controller_v81_sharp_curve_speed_cap065_saidao4_120s_20260710/` |

v81 kept the exported Track4 score at `P=9.6`, but regressed runtime quality
from v80's clean `simulate_returned_true/T=120.0` Track4 run to
`simulate_failed/T=52.6`.

## Decision

Reject v81. It does not improve score over v80 and makes the target Track4
runtime less comparable. Restore the source to v80's `0.55` cap before the next
experiment.

## Evidence

- Plan: `Docs/Design/unified_obstacle_avoidance_v81_plan_20260710.md`
- Static source gate: `Results/evidence/controller_deployability_static_check_v81_sharp_curve_speed_cap065_20260710.md`
- Runtime manifest: `Results/simulations/controller_v81_sharp_curve_speed_cap065_saidao4_120s_20260710/MANIFEST.md`
