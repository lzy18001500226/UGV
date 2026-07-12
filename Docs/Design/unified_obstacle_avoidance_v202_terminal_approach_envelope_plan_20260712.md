# Unified Obstacle Avoidance v202: Terminal Approach Envelope

## Status

Rejected and rolled back on 2026-07-12.

## Diagnostic Basis

The v199 Track3 closure diagnostic shows that the path planner reaches the
final return segments (`closest_index=97..103`) and the pursuit point converges
to the official origin. The remaining failure is vehicle feasibility:

- at `t=89.95`, `d=3.1841`, speed is `0.7003` and heading error is `0.0862`;
- at `t=90.95`, `d=1.7510`, speed is `0.2715` and heading error is `-0.6338`;
- by `t=91.95`, heading error is `-0.9252` and PID output is `-92.76`;
- the run terminates at `d=1.0824`, about `1.04 m` from the origin.

The pursuit target is correct; braking begins too late for the final turn.

## Candidate

Add the official finish-distance-squared signal as a read-only input to the
shared allocator. Arm terminal handling only after the vehicle has first moved
well away from the origin. Once armed and back within the terminal approach
region, cap positive speed by a distance-shaped envelope while preserving the
existing obstacle/path steering and v199 heading-error governor.

The mechanism is identical across all four evaluation wrappers and contains no
track id, elapsed-time, score, collision-count, or absolute-coordinate branch.
The departure latch prevents the origin-distance envelope from stopping the
vehicle at startup.

## Gates And Result

1. Source deployability check: `high=0`, `medium=0`.
2. Project tests: `14 passed`.
3. Track3 1 s plain native gate: passed.
4. Track3 700 s plain run: exceeded the 6 minute bounded wall-clock limit
   without producing metrics or a return packet.

The candidate is rejected for runtime-efficiency regression. The Sysplorer
process started for the bounded run was terminated after the run left an
orphaned process; no other project process was targeted. All v202 source
changes were restored to the exact retained v199 bytes.

## Evidence

- `Results/evidence/controller_deployability_static_check_v202_terminal_approach_envelope_20260712.md`
- `Results/simulations/controller_v202_terminal_approach_envelope_saidao3_1s_20260712/`
- `Results/simulations/controller_v202_terminal_approach_envelope_saidao3_700s_20260712/`
- `Results/metrics/track3_candidate_review_v202_terminal_approach_envelope_20260712.md`
