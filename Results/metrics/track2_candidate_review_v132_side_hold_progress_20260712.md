# Track2 Candidate Review - v132 Side-Hold Progress

## Scope

- Candidate: retain lateral obstacle state after the existing two-second avoid
  action while requesting forward speed.
- Editable surface: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo` only.
- Target runtime: `UGV.Test.Saidao2Eval`, MWORKS Sysplorer Python API, `-gui`.

## Gates

| Gate | Result |
|---|---|
| Static deployability before runtime | passed, high=0, medium=0 |
| Python tests before runtime | passed, 7 passed |
| Track2 1 s load/check/simulate | passed |
| Track2 120 s diagnostic | rejected |
| Track2 700 s completion | not run; prerequisite failed |
| Track1/3/4 regression | not run; prerequisite failed |

## Comparable Runtime Result

| Controller | Runtime status | T/s | cR | cO | P | Finish-distance squared |
|---|---|---:|---:|---:|---:|---:|
| v80 baseline | simulate_returned_true | 120.0 | 1 | 0 | 9.6 | 813.7304 |
| v132 | simulate_failed, exit state 2 | 43.6 | 2 | 0 | 9.2 | 761.4365 |

The v132 run exported score and control timeseries, but stopped before the
120-second diagnostic horizon. It adds a road collision and lowers the score.
No official origin-return finish occurred. Its smaller terminal distance is not
an accepted gain because it is paired with an early abnormal termination.

## Decision

Reject v132. Remove the `side_hold` state and its transitions, restore v80
semantics, and do not spend the 700-second gate or other-track runtime budget.

## Evidence

```text
Results/simulations/controller_v132_side_hold_progress_saidao2_1s_20260712/
Results/simulations/diagnostic_v132_side_hold_progress_track2_120s_20260712/
Results/evidence/controller_deployability_static_check_v80_restored_after_v132_20260712.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v132_20260712.json
```
