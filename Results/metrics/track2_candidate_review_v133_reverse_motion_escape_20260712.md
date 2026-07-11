# Track2 Candidate Review: v133 Reverse-Motion Escape

## Decision

Reject v133 and retain the restored v80 controller semantics.

## Candidate Scope

v133 swapped the left/right steering signs only in the `avoid_lateral` state
machine while reverse avoidance was active.  It did not alter thresholds,
longitudinal logic, the path planner, the forward `curise_lateral` state
machine, official track assets, scoring, or vehicle models.

## Gate Results

| Gate | v133 result | Decision relevance |
|---|---|---|
| Static deployability | `ready_for_physical_claim=true`, `high=0`, `medium=0` | Source shape is acceptable. |
| Python tests | `7 passed` with `D:\Dev\Anaconda3\python.exe -m pytest Scripts\tests -q` | Helper tests pass. |
| Native Track2 1 s | `simulate_returned_true`, `T=1.0`, `cR=0`, `cO=0`, `P=10.0` | Load/check/short simulation only. |
| Native Track2 120 s | `simulate_failed`, `exit_state=2`, `T=91.0`, `cR=1`, `cO=0`, `P=9.6` | Reject: early terminal state and no score gain. |
| v80 comparator | `simulate_returned_true`, `exit_state=0`, `T=120.0`, `cR=1`, `cO=0`, `P=9.6` | v80 reaches the requested horizon. |

The v80 extended diagnostic also reached `T=305.15` before its own terminal
state, so the v133 `T=91.0` outcome is a material regression rather than a
completion improvement.

## Evidence

```text
Results/simulations/candidate_v133_reverse_motion_escape_final_track2_1s_20260712/
Results/simulations/candidate_v133_reverse_motion_escape_final_track2_120s_20260712/
Results/simulations/controller_v80_finish_gate_saidao2_120s_20260711/metrics.json
Results/simulations/diagnostic_v80_track2_completion_geometry_310s_20260712/metrics.json
Results/evidence/controller_deployability_static_check_v133_reverse_motion_escape_final_20260712.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v133_20260712.md
Results/evidence/pytest_v133_reverse_motion_escape_final_20260712.console.txt
Results/evidence/pytest_v80_restored_after_v133_20260712.console.txt
Results/evidence/notification_delivery_note_v133_rejected_20260712.md
```

## Rollback And Next Constraint

The two v133 `avoid_lateral` sign changes were restored exactly to the v80
mapping and the restored source passed the static gate and tests.  Do not retry
reverse-motion lateral-sign swapping.  Do not widen this rejected candidate to
the 310-second Track2 diagnostic or other tracks.  The next candidate must be
a distinct, deployable mechanism justified by a fresh Track2 failure-window
analysis or targeted control research, then evaluated on one track first.
