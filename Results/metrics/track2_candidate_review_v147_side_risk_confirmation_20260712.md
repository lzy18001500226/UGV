# Track2 Candidate Review: v147 Side-Risk Confirmation

Decision: rejected; v80 controller semantics restored.

## Mechanism

v147 preserved immediate front-risk avoidance but required a side-only risk to
persist for 0.2 s before entering the unchanged v80 reverse/fixed-steer state.
It used one unified state machine and did not inspect track or score signals.

## Gates

| Gate | Result |
|---|---|
| Deployability | pass, high=0, medium=0 |
| Project tests | pass, 11 passed |
| Track2 1 s | pass, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s request | reject, early termination |

Runtime evidence:

```text
Results/simulations/controller_v147_side_risk_confirmation_saidao2_1s_retry_20260712/
Results/simulations/controller_v147_side_risk_confirmation_saidao2_120s_20260712/
```

The 120 s request ended at `T=71.35` with `cR=1`, `cO=0`, `P=9.6`, and
`distanceSensor1.d=803.1453951320364`. It did not finish, did not remove the
road collision, and terminated earlier than the v80 comparison. The candidate
therefore fails the completion-first promotion gate and is not expanded to
700 s or other tracks.

The result rejects a short side-risk confirmation state as the next mechanism.
It does not prove that all temporal classification is invalid, but another
confirmation-duration scan is not justified without a new discriminating
signal.

No finish, 80/80, physical-vehicle, report, package, or submission claim is made.
