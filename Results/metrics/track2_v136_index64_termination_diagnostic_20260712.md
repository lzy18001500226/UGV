# Track2 v136 Index-64 Termination Diagnostic

## Conclusion

The saved runs do not isolate `pathPlanner.closest_index=64` as a controller
defect. Both the restored v80 baseline and v136 terminate through the same
MWORKS API failure channel (`SimulateModel=false`, `exit_state=2`, empty
`GetLastErrors`), while the v80 run reaches a later time. This is a runtime
termination/reproducibility concern first, not evidence for another blind
controller parameter change.

## Evidence

| Run | End time | Index | cR | cO | P | Finish distance squared | API result |
|---|---:|---:|---:|---:|---:|---:|---|
| v80 baseline | 305.15 s | not exported in this run | 1 | 0 | 9.6 | 1004.6703 | `SimulateModel=false`, `exit_state=2` |
| v136 candidate | 159.95 s | 64 | 1 | 0 | 9.6 | 551.2135 | `SimulateModel=false`, `exit_state=2` |

Sources:

- `Results/simulations/controller_v80_track2_completion_gate_700s_20260712/`
- `Results/simulations/candidate_v136_path_curvature_speed_regulation_track2_completion_gate_700s_20260712/`

The v136 export shows a normal path-segment transition at the boundary:
`closest_index=63` with `path_progress` approaching `1`, followed by
`closest_index=64` with `path_progress` restarting near `0`. The adjacent
configured path points remain approximately `4.665 m` apart. Near the end of
the v136 export, the controller signals remain finite (`target_v=0.55`,
`ctrlAlloc.speed` positive and bounded, obstacle distances finite), and no new
obstacle collision is recorded. This does not prove the model is healthy; it
only rules out a demonstrated NaN/Inf or collision-triggered finish claim from
the saved fields.

## Decision

- v136 remains rejected because it fails the completion gate despite improving
  120 s path throughput.
- v80 remains the comparison source; no controller source change is accepted
  from this diagnostic.
- Before v137, reproduce an unchanged-v80 run with the same extra signal set
  and inspect native solver/translation diagnostics. If the API still returns
  `exit_state=2` with empty errors, classify the issue as a runtime-channel or
  model-termination blocker and do not tune around it.

## Non-Claims

This evidence proves neither an official finish nor an 80/80 result. It also
does not prove physical UGV readiness.
