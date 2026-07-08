# Notification Delivery Note

date: 2026-07-09 02:19 CST
scope: UGV deployability gate pass and Git push blocker notice

## Notice Sent

Evidence JSON:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260709_021914.json
```

Observed fields:

```text
ok: true
subject: UGV状态通知-实车可部署静态门禁通过但Git推送阻塞-20260709-0229
to: 1062771286@qq.com
recipient_explicit: false
recipient_warning: using_default_recipient
cooldown_reason: cooldown_disabled
refused_recipients: {}
```

## Summary

- Source-only deployability checker passed after the controller replaced reciprocal distance steering with bounded linear steering.
- Latest gate evidence: `Results/evidence/controller_deployability_static_check_20260709_0222.md`.
- Local commits mentioned in the notice: `995f360` and `6380563`.
- `git push origin main` remained blocked by HTTPS `Recv failure: Connection was reset`.
- SMTP acceptance does not prove mailbox visibility; this notice used the default QQ recipient.

## Non-Claims

- No MWORKS runtime was run for this notice.
- No official four-track score, physical UGV deployment, final package, or final submission success is claimed.
