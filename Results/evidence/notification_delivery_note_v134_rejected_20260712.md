# v134 Terminal Notification Evidence

The sparse Chinese terminal notice for the rejected v134 candidate was
accepted by the approved email gateway.

```text
gateway_evidence: C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260712_061937.json
subject: UGV v134候选已验证并回滚
delivery_status: gateway accepted
```

The notice states that v134 was rejected, v80 semantics were restored, static
and unit-test gates passed, local commit `7dfaa2d` exists, and the GitHub push
remains blocked by a connection reset.  Gateway acceptance does not prove that
the recipient read the email.
