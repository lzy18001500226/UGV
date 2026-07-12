# Unified Obstacle Avoidance v201: Continuous Path-Segment Selection

## Status

Rejected and rolled back on 2026-07-12. The candidate did not change the
decisive Track3 result relative to retained v199.

## Hypothesis

The shared PathPlanner selected the globally nearest segment on every sample.
Because official paths contain crossings and return sections, a continuity
window around the previous segment was tested as a track-agnostic mechanism.

## Change Tested

- Added a temporary `findClosestSegmentContinuous` helper.
- Searched segments `previous_index - 25` through `previous_index + 8`.
- Stored the previous segment index in `PathPlanner`.
- No official road, vehicle, sensor, score, or per-track branch was changed.

## Gates And Result

- Deployability checker: passed, `high=0`, `medium=0`.
- Project tests: passed, `14 passed`.
- Track3 1 s native gate: passed, `SimulateModel=true`, `T=1`, `cR=0`, `cO=0`, `P=10`.
- Track3 700 s decisive plain run: failed to finish, `T=92.85`,
  `distanceSensor1.d=1.0824256149658185`, `cR=1`, `cO=1`, `P=9.2`,
  `SimulateModel=false`, `exit_state=2`.

The result is identical to v199 at the reported precision. The continuity
window therefore has no demonstrated benefit and is not retained.

## Evidence

- `Results/simulations/controller_v201_continuous_path_segment_saidao3_1s_20260712/`
- `Results/simulations/controller_v201_continuous_path_segment_saidao3_700s_20260712/`
- `Results/metrics/track3_candidate_review_v201_continuous_path_segment_20260712.md`

## Rollback

`Models/UGV/Control/PathPlanning/Internal/package.mo` and
`Models/UGV/Control/PathPlanning/PathPlanner.mo` were restored to their exact
pre-v201 bytes. The retained source remains v199.
