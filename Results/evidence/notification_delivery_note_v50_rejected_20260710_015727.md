# Notification Delivery Note: v50 Rejected

Status: sent, 2026-07-10 01:57:27 CST

Email gateway evidence:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260710_015727.json
```

Subject:

```text
UGV v50已拒绝并恢复v48基线
```

Body:

```text
UGV v50降低曲率降速阈值后，Track3运行更干净但仍为T=120,cR=1,cO=1,P=9.2，未改善分数或碰撞，已拒绝并恢复v48语义。下一步继续从新机制推进，不停止长任务。
```

Notes:

- SMTP `ok=true` proves the gateway accepted the notice; it does not prove the
  user saw the email.
- The same terminal decision is recorded in
  `Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md`.
