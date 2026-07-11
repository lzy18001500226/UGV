# Track3 Candidate Review - v115 Smooth Straight-Front Speed Cap

Date: 2026-07-11 CST

## Candidate

`v115_smooth_straight_front_speed_cap`

v115 tested a smoother straight-front path-speed cap after the rejected v114
hard cap. The goal was to reduce the fixed Track3 early obstacle event without
creating the `T=1.6` short-run artifact seen in v114.

## Evidence

- Plan: `Docs/Design/unified_obstacle_avoidance_v115_plan_20260711.md`
- Static gate: `Results/evidence/controller_deployability_static_check_v115_smooth_straight_front_speed_cap_20260711.md`
- Runtime: `Results/simulations/controller_v115_smooth_straight_front_speed_cap_saidao3_120s_20260711/`
- Collision analysis: `Results/metrics/collision_window_analysis_v115_track3_20260711.md`
- Restored baseline gate: `Results/evidence/controller_deployability_static_check_v80_restored_after_v115_20260711.md`

## Result

| Track | Runtime | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|
| Saidao3Eval | `simulate_failed` | 51.4 | 1 | 1 | 9.2 |

Collision-window evidence shows two score drops:

- `t=1.40`: obstacle collision `cO 0 -> 1`, score `10.0 -> 9.6`
- `t=5.95`: road collision `cR 0 -> 1`, score `9.6 -> 9.2`

## Decision

Rejected.

v115 does not improve the accepted v80 Track3 score variables
(`P=9.2,cR=1,cO=1`) and shortens the run from the v80 caveat
`T=59.4` to `T=51.4`. The source was restored to v80 semantics and the
restored static deployability gate passed.

Do not continue scalar straight-front speed-cap scans. The next candidate
should target a different mechanism, such as state-conditioned release/hold,
obstacle-controller state logic, or trajectory/path geometry correction.

## Non-Claims

- This review does not claim physical UGV success.
- This review does not claim final competition score.
- This review does not modify official vehicle, road, sensor, scoring, example,
  or official-material files.
