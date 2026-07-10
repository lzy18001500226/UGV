# Notification Delivery Note - v84 Rejected

Status: sent, 2026-07-10 CST

## Notice

Subject:

```text
UGV v84 早停，继续从 v80 找新机制
```

Body:

```text
UGV v84 initial-lane y bias 已拒绝：Track3 仅运行到 T=1.2，cO=1，P=9.6 为早停假象，不是可比较提升。源码语义已恢复到 v80，静态门禁通过，提交并推送：485e117。下一步继续从 v80 诊断寻找新的统一避障机制。
```

## Gateway Evidence

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260710_173809.json
```

## Related UGV Evidence

```text
Docs/Design/unified_obstacle_avoidance_v84_plan_20260710.md
Results/metrics/track3_candidate_review_v84_initial_lane_y_bias_20260710.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v84_20260710.md
```

## Non-Claims

- SMTP acceptance does not prove the user saw the email.
- v84 does not improve the accepted score baseline.
- No final submission, physical UGV success, or 80/80 result is claimed.
