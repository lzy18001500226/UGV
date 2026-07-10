# v98 front-memory left-recovery candidate review

## Verdict

Rejected. Keep `v80_sharp_curve_speed_cap` as the current accepted baseline.

## Candidate

- Plan: `Docs/Design/unified_obstacle_avoidance_v98_plan_20260710.md`
- Source under test: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Mechanism: remember whether the current avoid episode has seen a near-front obstacle, then allow the lateral avoid initial state to steer left when `front_close_seen and dl < 0.2 and dr > dl`.
- Reason for trying: v96 showed that negative initial steering can reduce Track3 road collisions, but it caused a severe Track1 early-stop artifact. v98 tried to gate that behavior behind a previous near-front obstacle so it would not fire on ordinary road-edge side events.

## Static Gate

- Gate: `Results/evidence/controller_deployability_static_check_v98_front_memory_left_recovery_20260710.md`
- Result: passed, `ready_for_physical_claim=true`, `high=0`, `medium=0`.

## Runtime Evidence

- Run: `Results/simulations/controller_v98_front_memory_left_recovery_saidao3_120s_20260710/`
- Model: `UGV.Test.Saidao3Eval`
- Requested stop time: `120 s`
- Runtime status: `simulate_failed`, `exit_state=2`
- End metrics: `T=43.9`, `cR=1`, `cO=1`, `P=9.2`

## Decision

v98 does not improve Track3 over v80. It keeps the same `P=9.2`, `cR=1`, `cO=1` score variables and shortens runtime versus v80 Track3 (`T=59.4`). Because it fails the intended Track3 improvement gate, do not run Track1/Track2/Track4 regression for this candidate.

The controller source was restored to v80 semantics after this review. Do not continue the direct initial-steer override family without a fresh mechanism and supporting signal evidence.
