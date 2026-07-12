# Track3 Candidate Review v200 Heading-Error Low-Floor

## Decision

Reject v200 and retain exact v199 source semantics. The candidate changed only
the tracking-error speed ratio floor from `0.35` to `0.15`.

## Gates

| Gate | Result |
|---|---|
| Deployability checker | pass: high=0, medium=0 |
| Project tests | pass: 14 passed |
| Track3 1 s plain native gate | pass |
| Track3 700 s plain decisive run | reject: exceeded 300 s wall-clock limit without result export |

## Evidence

- `Docs/Design/unified_obstacle_avoidance_v200_heading_error_low_floor_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v200_heading_error_low_floor_20260712.md`
- `Results/simulations/controller_v200_heading_error_low_floor_saidao3_1s_20260712/`
- `Results/simulations/controller_v200_heading_error_low_floor_saidao3_700s_20260712/`

## Rollback

`Models/UGV/Control/ControlAllocate/package.mo` was restored to the exact v199
floor (`tracking_speed_floor=0.35`). No v200 semantics remain in the working
controller.

No four-track completion, 80/80, physical-UGV, or submission claim is made.
