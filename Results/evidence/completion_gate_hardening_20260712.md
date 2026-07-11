# UGV Official Completion Gate Hardening

timestamp: 2026-07-12 CST
scope: probe classifier, regression tests, and execution-gate wording only

## Source Grounding

`Models/UGV/Vehicle/Sensors/distanceSensor1.mo` terminates with the official
message only when `time > 10` and `distanceSensor1.d < 0.02`.

## Corrected Rule

`Scripts/mworks/ugv_baseline_probe.py` now reports
`finish_reached_official_origin_assertion` only if all conditions hold:

1. `SimulateModel` returned `false`, consistent with the assertion termination
   path rather than a configured horizon return.
2. `T > 10`.
3. `distanceSensor1.d < 0.02` at termination.

`SimulateModel=true` is classified as
`simulation_horizon_reached_finish_not_observed`, including a terminal sample
near the origin. A false return outside the threshold remains
`early_stop_finish_not_observed`.

## Non-Claims

This is a validation-gate correction. It does not establish any new track
finish, score gain, controller acceptance, or physical-vehicle result.
