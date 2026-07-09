# Track3 Candidate Review: v62 Front-Centered Initial Bypass

## Scope

- Candidate: `v62_front_centered_initial_bypass`
- Plan: `Docs/Design/unified_obstacle_avoidance_v62_plan_20260710.md`
- Source file tested: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Target track: `UGV.Test.Saidao3Eval`
- Goal: test whether a front-close, left/right-symmetric sensor gate should
  use a small negative initial bypass instead of the v48 fixed positive
  initial bypass.

No official vehicle, road, sensor, scoring, example, or official material files
were modified.

## Candidate Mechanism

Inside the `avoid_lateral` `ini_state`, v62 tested:

```modelica
if df < 1.2 and abs(dl - dr) < 0.02 then
  steer := -0.45;
else
  steer := 0.6;
end if;
```

This is a unified sensor rule, not a track-specific branch.

## Evidence

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v62_front_centered_initial_bypass_20260710.md
Results/evidence/controller_deployability_static_check_v62_front_centered_initial_bypass_20260710.json
```

Runtime evidence:

```text
Results/simulations/controller_v62_front_centered_initial_bypass_saidao3_120s_20260710/
```

Offline analysis:

```text
Results/metrics/collision_window_analysis_v48_v62_track3_20260710.md
Results/metrics/collision_window_analysis_v48_v62_track3_20260710.json
Results/metrics/signal_window_summary_v48_v62_track3_20260710.md
Results/metrics/signal_window_summary_v48_v62_track3_20260710.json
```

Restoration evidence:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v62_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v62_20260710.json
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 baseline | Track3 | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 | keep |
| v62 | Track3 | simulate_failed with result variables | 2 | 51.8 | 1 | 1 | 9.2 | reject |

Collision windows:

| Candidate | First obstacle event | Road event |
|---|---|---|
| v48 | `1.05 s`, `cO: 0 -> 1` | `4.85 s`, `cR: 0 -> 1` |
| v62 | `1.00 s`, `cO: 0 -> 1` | `5.15 s`, `cR: 0 -> 1` |

At the target early obstacle event, v62 caused final steering to be about
`0.053`, lower than v48's about `0.162`, and the obstacle collision happened
slightly earlier. The negative initial bypass direction is therefore worse in
the current controller/allocation coupling.

## Decision

Reject v62. It did not improve Track3 score, did not remove the early obstacle
event, and shortened the run versus v48. Because the target weak-track result
regressed, Track1/Track2/Track4 regression and four-track evaluation were not
run.

Restore v48 semantics and continue from v48 for the next evidence-backed
unified mechanism.

Do not continue front-centered negative initial-bypass scans without a new
source-level explanation for the controller/allocation coupling that made v62
reduce final steering.

This review does not create a submission package and does not claim physical
UGV success.
