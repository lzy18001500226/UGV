# Track2 v80 Path-Progress Diagnostic

Source:
`Results/simulations/diagnostic_v80_track2_completion_geometry_310s_20260712/extra_timeseries.csv`.

## Findings

- 6104 samples cover 0.00--305.15 s.
- `closest_index` moves from 1 to 30 through 29 forward transitions.
- There are zero backward index transitions, so global nearest-segment relock
  is not supported by this run.
- Long residence at indices 26, 27, and 28 coincides with very low allocated
  speed and persistent reverse avoidance.
- The v80 speed caps are active for most of the run because they use desired
  global heading as if it were local curvature.

## Decision

Do not implement monotonic/windowed closest-index search as v136. Test a
geometry-correct local-curvature speed regulator first. Preserve the v80
obstacle-controller and control-allocation semantics so the experiment isolates
the completion-throughput mechanism.
