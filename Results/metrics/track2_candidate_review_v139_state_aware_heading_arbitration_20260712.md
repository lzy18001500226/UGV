# Track2 Candidate Review: v139 State-Aware Heading Arbitration

## Decision

Rejected. The candidate is not retained and the controller source was restored
to the v80 comparison semantics. No 700 s run or cross-track expansion was
authorized.

## Candidate

- Design: `Docs/Design/unified_obstacle_avoidance_v139_state_aware_heading_arbitration_plan_20260712.md`
- Edited file: `Models/UGV/Control/ControlAllocate/package.mo`
- Runtime mechanism: conditional side-only reverse-speed release plus same-sign
  path-steer capping during reverse avoidance.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, high=0, medium=0 |
| Project tests | pass, 11 passed |
| Track2 1 s | pass as load/check/simulate only, T=1, cR=0, cO=0, P=10 |
| Track2 120 s comparable gate | fail, SimulateModel=false, exit_state=2 |

## Track2 120 s Evidence

Run directory:
`Results/simulations/candidate_v139_state_aware_heading_arbitration_track2_120s_20260712/`

```text
runtime_status=simulate_failed
T=82.8 s
cR=1
cO=0
P=9.6
finish_distance_squared=610.8130472278172
termination=unclassified_early_termination
```

The score variables did not regress numerically, but the run stopped before
the requested horizon and therefore is not comparable evidence of improvement.
It also retained a road collision. Under the completion-first gate this is a
rejection, not a score gain.

## Restore

The edited `ControlAllocate` expressions were removed and the v80 source
semantics restored. Static recheck and tests are required before closeout.

This result does not claim official completion, an 80/80 result, physical UGV
performance, or submission readiness.
