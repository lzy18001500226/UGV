# Track1 / Track4 Candidate Review - v30 Side-Danger Steering Floor

generated_at: 2026-07-09 21:16 CST

## Decision

Reject `v30_side_danger_steering_floor`.

The candidate stayed track-agnostic and passed the static source gate, but it
did not improve the target weak tracks against the accepted v13 baseline. The
source was restored to v13 semantics after the target runs.

## Candidate

Baseline:

```text
v13 side-trigger 0.45
df <= mindis or dl <= 0.45 or dr <= 0.45
```

v30 attempted mechanism:

```modelica
min(0.8, max(0.35, 2 * abs(dl - dr)))
```

Scope:

- one unified controller for all tracks
- no branch on track name, wrapper name, run id, or scoring variables
- implementation target only: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- no edits to official vehicle, road, sensor, scoring, or example packages

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v30_side_danger_steering_floor_20260709_2109.md
```

Target runs:

```text
Results/simulations/controller_v30_side_danger_steering_floor_saidao1_120s_20260709_2110/
Results/simulations/controller_v30_side_danger_steering_floor_saidao4_120s_20260709_2112/
```

Source restored static gate:

```text
Results/evidence/controller_deployability_static_check_v13_restored_after_v30_20260709_2116.md
```

## Result Summary

| Track | Runtime status | T/s | cR | cO | P | v13 comparison |
|---|---|---:|---:|---:|---:|---|
| Track1 `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 120.0 | 3 | 0 | 8.8 | no improvement |
| Track4 `UGV.Test.Saidao4Eval` | `simulate_failed` with readable score variables | 112.95 | 3 | 0 | 8.8 | no improvement |

Accepted v13 target-track comparison:

```text
Track1: T=120.0, cR=3, cO=0, P=8.8
Track4: T=113.1, cR=3, cO=0, P=8.8
```

## Interpretation

- The steering floor did not reduce road collisions or improve score on either
  target weak track.
- Since Track1 and Track4 did not improve, v30 does not satisfy its acceptance
  gate and should not be expanded to Track2/Track3 regression.
- The repeated no-improvement pattern from v29 and v30 suggests that simply
  strengthening avoid-mode response is not enough. The next attempt should
  start from fresh failure-window or trajectory evidence, not another blind
  scalar adjustment.

## Non-Claims

- This is not a final competition score claim.
- This does not claim physical UGV readiness.
- This does not authorize final submission packaging or sending.
