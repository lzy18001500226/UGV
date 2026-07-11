# Track1 Candidate Review: v134 Short Reverse Dwell

Status: rejected; v80 controller semantics restored.

## Decision

v134 changed only the longitudinal `avoid -> cruise` dwell from two seconds to
one second.  It retained all trigger thresholds, speed and steering magnitudes,
steering signs, path planning, and control allocation.

The one-second native gate passed, but the comparable 25-second Track1 gate
stopped abnormally at `T=20.55` with `cR=2`, `cO=0`, and `P=9.2`.  The unchanged
v80 diagnostic reached the complete 25-second horizon with the same collision
and score values.  Therefore v134 has no collision or score benefit and worsens
runtime completion.

The candidate is rejected without a 120-second or cross-track run.  A
`1.5 s` follow-up is not justified as a blind scalar scan.  No evidence here
proves an official finish, an 80-point score, or physical-vehicle success.

## Evidence

```text
Results/simulations/diagnostic_v80_track1_allocator_state_25s_20260712/
Results/metrics/v80_track1_allocator_contribution_25s_20260712.md
Results/metrics/v80_track1_signal_windows_25s_20260712.md
Results/evidence/controller_deployability_static_check_v134_short_reverse_dwell_20260712.md
Results/simulations/candidate_v134_short_reverse_dwell_track1_1s_20260712/
Results/simulations/candidate_v134_short_reverse_dwell_track1_25s_20260712/
```
