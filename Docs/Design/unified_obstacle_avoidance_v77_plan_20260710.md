# Unified Obstacle Avoidance v77 Plan

Status: rejected_early_stop_artifact, 2026-07-10 CST

## Goal

Continue from accepted v74 and test whether the earlier v70 active-avoid
path-speed clamp becomes useful when combined with v74's guarded curve
short-lookahead baseline.

This is not a new scalar sweep. v76 showed that extra side steering worsens
Track1 early termination. v70 showed that active-avoid path-speed clamping can
reduce final speed and delay Track3 collision events, but it was rejected from
v48 because it did not improve score. v77 retests the same bounded speed
arbitration only as a v74 runtime-caveat and road-edge recovery candidate.

## Evidence Basis

Current accepted best:

```text
v74 total wrapper score: 37.6
```

Current residual evidence:

```text
Results/metrics/collision_window_analysis_v74_all_tracks_20260710.md
Results/metrics/signal_window_summary_v74_all_tracks_key_events_20260710.md
Results/metrics/trajectory_geometry_review_v74_all_tracks_20260710.md
Results/metrics/track1_track2_candidate_review_v76_front_clear_side_steer_boost_20260710.md
Results/metrics/track3_candidate_review_v70_active_avoid_speed_clamp_20260710.md
```

v74 remaining events are mostly road-edge contacts after active avoidance has
already engaged. v76 extra steering made Track1's early terminal caveat worse.
v70 did not improve v48 score, but it lowered final speed near active-avoid
events and delayed Track3 events, so it is worth one bounded combination test
from v74.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct path-speed contribution:

```modelica
connect(unitDelay3.y, gain2.u)
```

with the v70 bounded active-avoid path-speed clamp:

```modelica
gain2.u = if speed_oa < 0 and unitDelay3.y > 0.55 then 0.55 else unitDelay3.y;
```

All obstacle-controller, PathPlanner, official road, vehicle, sensor, scoring,
example, and official material files remain unchanged.

## Validation Gate

1. Run `check_controller_deployability.py --fail-on-high`.
2. Run Track1 first because v74's biggest accepted caveat is
   `simulate_failed / T=17.4` despite `P=9.6`.
3. Continue only if Track1 improves runtime comparability or score without a
   worse `P/cR/cO`.
4. If Track1 passes, run Track2/3/4 regression.
5. Accept v77 only if it improves v74 total score or preserves score while
   materially improving the Track1 early-terminal caveat and does not regress
   any other track.

## Rejection Conditions

- Track1 score or collision count worsens.
- Track1 remains early-terminal with no material improvement.
- Track2/3/4 regress after Track1 passes.
- Static deployability gate reports high risk.

If rejected, restore v74 `ControlAllocate` semantics and write a rejection
review before continuing.

## Non-Goals

- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package work.
- No per-track logic.
