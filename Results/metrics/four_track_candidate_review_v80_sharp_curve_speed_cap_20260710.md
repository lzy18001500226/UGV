# Four-Track Candidate Review - v80 Sharp Curve Speed Cap

Status: accepted_as_current_high_score_candidate_with_runtime_caveat, 2026-07-10 CST

## Candidate

v80 starts from accepted v74 and adds a narrow PathPlanner speed cap only when
the final path steering angle is extreme:

```modelica
parameter Real sharp_curve_slowdown_steer = 1.0;
parameter Real sharp_curve_slowdown_speed = 0.55;

if abs(steering_angle) > sharp_curve_slowdown_steer
   and target_v > sharp_curve_slowdown_speed then
  target_v := sharp_curve_slowdown_speed;
end if;
```

This is a unified path-curvature mechanism, not a per-track branch and not a
broad active-avoid speed clamp.

## Four-Track Result

| Track | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| Saidao1Eval | `simulate_failed` | 2 | 17.4 | 1 | 0 | 9.6 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao1_120s_20260710/` |
| Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao2_120s_20260710/` |
| Saidao3Eval | `simulate_failed` | 2 | 59.4 | 1 | 1 | 9.2 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710/` |
| Saidao4Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao4_120s_20260710/` |

Total wrapper score: `38.0`.

## Comparison To v74

v74 total wrapper score was `37.6`:

```text
Track1 P=9.6, Track2 P=9.6, Track3 P=9.2, Track4 P=9.2
```

v80 keeps Track1, Track2, and Track3 score variables unchanged and improves
Track4 from `P=9.2,cR=2,cO=0` to `P=9.6,cR=1,cO=0`. The Track4 104 s road
collision present in v74 disappears in v80.

## Caveat

v80 worsens Track3 runtime comparability versus v74:

```text
v74 Track3: simulate_returned_true, T=120.0, cR=1, cO=1, P=9.2
v80 Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

This candidate is accepted only as the current high-score local wrapper
candidate. It does not prove final competition score, physical UGV behavior, or
submission readiness.

## Decision

Accept v80 as the current score-leading candidate because it improves total
wrapper score from `37.6` to `38.0` and cleanly improves Track4. Keep the
Track3 runtime caveat visible in future comparisons. Continue from v80 with a
new evidence-backed mechanism rather than repeating broad speed clamps or
max-steer clipping.

## Evidence

- Plan: `Docs/Design/unified_obstacle_avoidance_v80_plan_20260710.md`
- Static source gate: `Results/evidence/controller_deployability_static_check_v80_sharp_curve_speed_cap_20260710.md`
- Track4 comparison: `Results/metrics/collision_window_analysis_v74_v80_track4_20260710.md`
- Four-track event analysis: `Results/metrics/collision_window_analysis_v80_all_tracks_20260710.md`
