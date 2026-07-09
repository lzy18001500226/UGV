# Notification Delivery Note - v59 Rejected

timestamp: 2026-07-10 03:59:12 CST
scope: UGV v59 close-side initial-direction rejection notice

## Email

subject: UGV v59已拒绝并恢复v48

body:

```text
UGV避障长任务进展：v59 close-side initial-direction 已完成Track1验证，结果T=3.85,cR=0,cO=0,P=10.0但属于simulate_failed早停高分，不可与v48 Track1 T=120,P=9.2比较，已拒绝并恢复v48语义。证据：Results/metrics/track1_candidate_review_v59_close_side_initial_direction_20260710.md。
```

gateway evidence:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260710_035912.json
```

## Notes

- This notice does not claim final competition submission readiness.
- This notice does not claim physical UGV success.
- MWORKS was used for the v59 Track1 wrapper run; the run returned
  `simulate_failed` with readable result variables.
