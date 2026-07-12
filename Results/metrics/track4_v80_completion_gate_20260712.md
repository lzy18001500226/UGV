# Track4 v80 Completion Gate

## Result

The restored v80 controller was evaluated through the official wrapper
`UGV.Test.Saidao4Eval` with a requested 700 s horizon. It did not finish.

| Field | Value |
|---|---:|
| SimulateModel | `false` |
| Exit state | `2` |
| Terminal time | `52.15 s` |
| Road collisions | `1` |
| Obstacle collisions | `0` |
| Avoidance score | `9.6` |
| Finish distance squared | `329.6641216891936` |
| Completion | not observed |

The official completion criterion is not met because the terminal distance is
not below `0.02`. The run is classified as `unclassified_early_termination`:
the API exposed no actionable error text. This establishes Track4's current
baseline as a road-boundary failure rather than an unverified lane.

Evidence: `Results/simulations/controller_v80_track4_completion_gate_700s_20260712/`.

No four-track completion, 80-point result, physical validation, or submission
readiness is claimed.
