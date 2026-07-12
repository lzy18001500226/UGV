# Track2 v186 Coupled Edge-Braking Review

## Decision

Rejected. The committed controller is restored exactly.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0, medium=0` |
| Project tests | pass, `14 passed` |
| Track2 1 s native | pass, `T=1.0,cR=0,cO=0,P=10.0` |
| Track2 120 s | reject, `SimulateModel=false`, `T=25.15` |

Track2 ended with `cR=17,cO=0,P=3.2`, finish-distance squared `530.7769`, and
termination class `unclassified_early_termination`. The candidate combined
full reverse OA speed with v184-style severe-side steering only when
`df>safeF and min(dl,dr)<0.10`; this narrow coupling still destabilized the
current runtime and did not pass the first extended gate.

## Evidence

- Design: `Docs/Design/unified_obstacle_avoidance_v186_coupled_edge_braking_plan_20260712.md`
- Static: `Results/evidence/controller_deployability_static_check_v186_coupled_edge_braking_20260712.md`
- Tests: `Results/evidence/pytest_v186_coupled_edge_braking_20260712.console.txt`
- Native 1 s: `Results/simulations/candidate_v186_coupled_edge_braking_track2_1s_retry_20260712/`
- Native 120 s: `Results/simulations/candidate_v186_coupled_edge_braking_track2_120s_20260712/`

No official completion, 80/80 result, physical UGV success, or submission
readiness is claimed.
