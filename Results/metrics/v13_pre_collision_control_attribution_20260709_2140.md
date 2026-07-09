# v13 Pre-Collision Control Attribution

Generated from saved MWORKS CSV exports. No MWORKS rerun.

## v13_track1

Evidence: `Results/simulations/diagnostic_v13_signals_saidao1_120s_20260709_1658`

| Event/s | min side start->end | steer_pp near | oa filtered near | final steer near | planner dominates? | side margin |
|---:|---:|---:|---:|---:|---|---|
| 5.65 | 0.2227->0.08135 | -0.6928 | 0.2991 | -0.3936 | True | shrinking |
| 30.35 | 0.2455->0.1058 |  |  |  | None | shrinking |
| 51.6 | 0.3928->0.08493 |  |  |  | None | shrinking |

## v13_track3

Evidence: `Results/simulations/diagnostic_v13_signals_saidao3_120s_20260709_1700`

| Event/s | min side start->end | steer_pp near | oa filtered near | final steer near | planner dominates? | side margin |
|---:|---:|---:|---:|---:|---|---|
| 1.05 | 0.5675->0.03458 | -0.1705 | 0.2971 | 0.1266 | False | shrinking |
| 7.35 | 0.2423->0.3822 | 1.636 | 0.2977 | 1.933 | True | not_shrinking |

## v13_track4

Evidence: `Results/simulations/diagnostic_v13_signals_saidao4_120s_20260709_1910`

| Event/s | min side start->end | steer_pp near | oa filtered near | final steer near | planner dominates? | side margin |
|---:|---:|---:|---:|---:|---|---|
| 6.4 | 0.2389->0.1041 | 0.582 | 0.2988 | 0.8808 | True | shrinking |
| 59.15 | 0.3512->0.097 |  |  |  | None | shrinking |
| 91.8 | 0.353->0.09485 |  |  |  | None | shrinking |

## Reading

- Most remaining v13 collisions are road contacts while avoid mode is already active.
- In several events the final steering is dominated by path-planner steering rather than the filtered obstacle-avoidance contribution.
- A useful next candidate should reduce planner fighting or increase obstacle-avoidance authority during severe side-risk, but must remain one controller for all tracks.
