# Notification Delivery Note: v46 Rejected

Status: sent, 2026-07-10 CST

## Notice

UGV unified obstacle-avoidance long task: v46 changed only the
obstacle-avoidance speed-channel gain to `1.2*factor_oa`. Track3 target
validation produced `T=45.2`, `cR=1`, `cO=1`, `P=9.2`,
`simulate_failed`, which is worse than the v45 120 s comparable run. v46 is
rejected; v45 remains the current best candidate with total wrapper score
`36.8`.

## Gateway Evidence

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260710_010659.json
```

## UGV Evidence

```text
Docs/Design/unified_obstacle_avoidance_v46_plan_20260710.md
Results/simulations/controller_v46_speed_channel_120pct_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v46_speed_channel_120pct_20260710.md
Results/metrics/collision_window_analysis_v46_speed_channel_120pct_track3_20260710.md
```
