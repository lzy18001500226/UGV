# Track2 Candidate Review - v125 Front-Risk Tiered Brake

Status: rejected and v80 source restored, 2026-07-11 CST.

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v125_plan_20260711.md
```

The candidate kept `speed := -1` for `df <= mindis` and used `speed := -0.4`
for side-triggered avoidance with the front clear. It was a unified four-sensor
rule and did not inspect track identity or scoring state.

## Gates

Source gate:

```text
Results/evidence/controller_deployability_static_check_v125_front_risk_tiered_brake_20260711.md
ready_for_physical_claim=true, high=0, medium=0
```

The first inline conditional-expression spelling failed translation because
Sysblock state machines do not support that expression form. The equivalent
ordinary `if/end if` statement passed model check and the Track2 1 s probe:

```text
Results/simulations/controller_v125_front_risk_tiered_brake_saidao2_1s_retry_20260711/
simulate_returned_true, T=1.0, cR=0, cO=0, P=10.0
```

The failed spelling remains as diagnostic evidence only:

```text
Results/simulations/controller_v125_front_risk_tiered_brake_saidao2_1s_20260711/
```

## Completion Gate

```text
Results/simulations/controller_v125_front_risk_tiered_brake_saidao2_120s_20260711/
```

Measured result:

```text
runtime=simulate_failed / exit_state=2
T=46.15
cR=1
cO=0
P=9.6
distanceSensor1.d=792.4680346712572
completion=early_stop_finish_not_observed
```

v80 Track2 reaches the full 120 s horizon with `cR=1,cO=0,P=9.6`, although it
also does not finish. v125 therefore traded persistent low speed for a severe
off-route early termination and did not improve the official completion gate.

## Decision

Reject v125. Restore exact v80 controller semantics before any further
candidate. Do not treat the shorter runtime or unchanged avoidance score as a
completion improvement.

Reusable result: front-conditioned longitudinal authority is deployable, but
`-0.4` leaves insufficient side-risk control. Any follow-up must inspect saved
trajectory/control evidence or use a separately justified bounded authority
design; do not turn this into an unconstrained scalar scan.

## Non-Claims

- No official finish.
- No 80/80 score claim.
- No physical UGV success.
- No report, package, or submission readiness claim.
