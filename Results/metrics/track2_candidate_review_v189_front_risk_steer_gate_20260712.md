# Track2 v189 Front-Risk Steer-Gate Review

## Decision

Rejected. The committed allocator is restored exactly.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0, medium=0` |
| Project tests | pass, `14 passed` |
| Track2 1 s native | pass, `T=1.0,cR=0,cO=0,P=10.0` |
| Track2 strict 700 s | reject, early stop at `T=164.95` |

The strict run ended with `cR=15,cO=2,P=3.2`, finish-distance squared
`377.9933562181551`, and `unclassified_early_termination`. It did not satisfy
the official finish assertion.

## Collision-Window Finding

The front-risk gate did not cover either obstacle event:

| Event time | cO | front | left | right | OA speed | OA steer |
|---:|---:|---:|---:|---:|---:|---:|
| 1.6 | 1 | 1.33 | 0.57 | 0.57 | 1.0 | 0.0 |
| 15.1 | 2 | -1.41 | 0.47 | 0.64 | 0.0 | 0.6 |

The later road-collision sequence reached `cR=15`; many events occurred while
the path steering itself was already large. Therefore `speed_oa<0` is not a
valid collision-imminent predicate, and this allocator gate must not be tuned
further. The next redesign needs a controller-level risk signal derived from
the actual distance inputs or a reference-backed local planner interface,
rather than inferring risk from the old OA output state.

## Evidence

- `Docs/Design/unified_obstacle_avoidance_v189_front_risk_steer_gate_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v189_front_risk_steer_gate_20260712.md`
- `Results/evidence/pytest_v189_front_risk_steer_gate_20260712.console.txt`
- `Results/simulations/candidate_v189_front_risk_steer_gate_track2_1s_20260712/`
- `Results/simulations/candidate_v189_front_risk_steer_gate_track2_700s_20260712/`

No official completion, 80/80 result, physical UGV result, or submission
readiness is claimed.
