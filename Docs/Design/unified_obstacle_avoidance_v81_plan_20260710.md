# Unified Obstacle Avoidance v81 Plan

Status: rejected, 2026-07-10 CST

## Goal

Refine the v80 extreme-curvature speed cap after v80 improved Track4 but added
a Track3 runtime caveat.

v81 keeps the same unified mechanism and changes only the extreme-curvature
speed cap from `0.55` to `0.65`.

## Evidence Basis

v80 result:

```text
Track4: v74 P=9.2 -> v80 P=9.6
Track3: v74 simulate_returned_true/T=120 -> v80 simulate_failed/T=59.4,
        but P stayed 9.2
```

The v80 mechanism is useful because it removes one Track4 road collision, but
the `0.55` cap may be too aggressive for Track3 runtime comparability.

## Planned Source Change

Allowed source:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Change:

```modelica
parameter Real sharp_curve_slowdown_speed = 0.65;
```

## Validation Gate

1. Run source deployability checker.
2. Run Track4 first. Continue only if Track4 keeps `P=9.6`.
3. Run Track3 next. Prefer v81 over v80 only if Track3 runtime is cleaner or
   not worse while keeping `P=9.2`.
4. Run Track1/2 regression only if Track4 and Track3 gates pass.

## Non-Goals

- No final competition score claim.
- No physical UGV success claim.
- No report/package work.
- No official material or scoring edits.

## Result

v81 is rejected. Track4 kept exported `P=9.6,cR=1,cO=0`, but runtime quality
regressed from v80 `simulate_returned_true/T=120.0` to
`simulate_failed/T=52.6`.

Review: `Results/metrics/track4_candidate_review_v81_sharp_curve_speed_cap065_20260710.md`.
