# Track2 Candidate Review: v145 Directional Immediate Lateral Avoidance

## Decision

Rejected. Restore and retain v80 as the comparison baseline. Do not run the
extended completion gate or expand v145 to other tracks.

## Motivation

Two current-runtime repetitions of the v137 longitudinal rule stopped at
`T=28.55,cR=1,cO=0,P=9.6`, path index 20. This contradicts the older v137 run
that reportedly reached index 112. At the reproducible stop, `dl=0.02353`,
`dr=0.18837`, and the lateral avoidance entry state still commanded `+0.6`.
Source review showed that this fixed command is held for two seconds before the
left/right sensor-driven states become reachable.

v145 retained the v137 neutral side-only longitudinal rule and changed only
that immediate lateral command to `0.6*sign(dl-dr)`. This preserves full
steering magnitude and differs from v144's rejected zero-steer entry and v138's
later-state magnitude change.

## Gates

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0, medium=0` |
| Project tests | pass, `11 passed` |
| First inline-if implementation | compiler rejected; replaced by branch-free equivalent |
| Track2 1 s retry | pass, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s | reject, `SimulateModel=false`, `T=101.65,cR=0,cO=4,P=8.4` |
| Official finish distance squared | `340.84515126716076`, not finished |

## Interpretation

The candidate removed the reproduced road collision but caused four obstacle
collisions. Instantaneous `dl-dr` sign is therefore not a stable substitute for
the fixed re-entry direction. v137's historical index-112 result must not be
used as a current retained mechanism unless it can be reproduced under an exact
source/runtime snapshot.

Evidence:

- `Results/simulations/diagnostic_v137_track2_second_collision_105s_20260712/`
- `Results/simulations/diagnostic_v137_track2_second_collision_120s_retry1_20260712/`
- `Results/evidence/controller_deployability_static_check_v145_directional_reentry_20260712.md`
- `Results/simulations/candidate_v145_directional_reentry_track2_1s_retry1_20260712/`
- `Results/simulations/candidate_v145_directional_reentry_track2_120s_20260712/`

No official completion, 80-point score, physical validation, or submission
readiness is claimed.
