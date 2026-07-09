# Notification Delivery Note: v51 Rejected

Status: sent, 2026-07-10 02:04:28 CST

Email gateway evidence:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260710_020428.json
```

Subject:

```text
UGV v51已拒绝并恢复v48基线
```

Body:

```text
UGV v51直行制动仲裁在Track3出现T=2.25早停，P=10不可比，已拒绝并恢复v48语义。v48仍是当前最好候选，长任务继续转向新机制/诊断。
```

Notes:

- SMTP `ok=true` proves the gateway accepted the notice; it does not prove the
  user saw the email.
- The same terminal decision is recorded in
  `Results/metrics/track3_candidate_review_v51_straight_brake_arbitration_20260710.md`.
