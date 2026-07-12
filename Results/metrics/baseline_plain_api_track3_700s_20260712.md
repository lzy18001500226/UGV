# Track3 plain API baseline review

- Date: 2026-07-12 CST
- Source semantics: exact current baseline (no candidate accepted)
- Model: `UGV.Test.Saidao3Eval`
- API lane: `SimulateModel` (official comparison lane)
- Requested horizon: `700 s`
- Observed termination: `simulate_failed`, `T=21.1 s`
- Official finish assertion: not observed
- Score variables at termination: `cR=1`, `cO=1`, `P=9.2`
- Finish-distance squared: `301.43126761991095`
- Exported score/diagnostic CSV: `Results/simulations/baseline_head_track3_700s_plain_api_20260712/`

## Decision

This is a non-finish baseline, not a score improvement and not evidence of
four-track completion. It confirms that the current exact baseline still has
an early Track3 road/obstacle failure. Keep the baseline unchanged. The next
candidate must be based on a new structural diagnosis, must use plain
`SimulateModel`, and must pass the existing static, test, Track2, and Track3
gates before any broader run.

## Boundary

No MWORKS/ROS2/UE live-system success, physical-vehicle success, or 80-point
claim is made by this artifact.
