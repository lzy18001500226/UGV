# Track3 Candidate Review v197 Heading Slew Limit

## Decision

Reject v197 and retain exact v148 source semantics.

## Gates

| Gate | Result |
|---|---|
| Deployability checker | pass: high=0, medium=0 |
| Project tests | pass: 14 passed |
| Track3 1 s plain native gate | pass |
| Track3 700 s plain `SimulateModel` | reject: `T=70.65`, `exit_state=2` |

## Decisive Metrics

`cR=2`, `cO=1`, `P=8.8`, `distanceSensor1.d=192.81082249938794`.
The vehicle passed the v148 early-stop time but did not finish; this is not a
score improvement or completion evidence.

## Evidence

- `Results/simulations/controller_v197_heading_slew_limit_saidao3_1s_20260712/`
- `Results/simulations/controller_v197_heading_slew_limit_saidao3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v197_heading_slew_limit_20260712.json`
- `Results/evidence/controller_deployability_static_check_v197_heading_slew_limit_20260712.md`
- `Docs/Design/unified_obstacle_avoidance_v197_heading_slew_limit_plan_20260712.md`

## Rollback

The added final-command slew limiter was removed from
`Models/UGV/Control/ControlAllocate/package.mo`. The retained source has no
semantic diff from the v148 baseline for this module.

No four-track completion, 80/80, physical-UGV, or submission claim is made.
