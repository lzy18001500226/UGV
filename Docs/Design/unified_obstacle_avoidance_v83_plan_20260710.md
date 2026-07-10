# Unified Obstacle Avoidance v83 Plan

Status: rejected_after_target_gate, 2026-07-10 CST

## Goal

Continue from accepted v80 and test one unified road-edge recovery mechanism
that targets the remaining early road-boundary score events without repeating
the rejected initial-steering, broad speed-clamp, filter-time, or lookahead
scans.

## Baseline

Current local wrapper best:

```text
v80 total wrapper score: 38.0
Track1: P=9.6, cR=1, cO=0, simulate_failed/T=17.4
Track2: P=9.6, cR=1, cO=0, clean T=120
Track3: P=9.2, cR=1, cO=1, simulate_failed/T=59.4
Track4: P=9.6, cR=1, cO=0, clean T=120
```

## Evidence Basis

v80 Track3 short-window diagnostic:

```text
Results/simulations/diagnostic_v80_track3_geometry_6s_20260710/
```

Key event geometry:

```text
1.05 s obstacle event:
  DisObstacle ~= 0.106 < 0.11
  x ~= 1.200, y ~= 0.080
  df ~= 0.831
  steer_oa = 0.6

4.85 s road event:
  DisRoad ~= 0.106 < 0.11
  x ~= 3.364, y ~= 0.462
  df ~= 0.071
  dl ~= 0.518, dr ~= 0.617
  steer_oa = 0.6
```

The first obstacle event and the later road event need opposite treatment:
stronger positive initial steer risks pushing deeper toward the road boundary,
while the road event already has a very small front-distance reading and a
clear side imbalance. v83 therefore targets only the road-edge window.

## Rejected Routes Not Repeated

- v22 quick lateral initialization dwell.
- v24 filter-time scan.
- v42/v64 open-side initial steering as a standalone broad mechanism.
- v63 direct early steering feedforward.
- v65 stronger front emergency braking.
- v66 initial steering magnitude boost.
- v70/v81 broad speed clamp variants.
- v82 small-angle short-lookahead.

## Candidate Mechanism

Implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Inside the existing `avoid_lateral.ini_state`, replace the unconditional
fixed positive initial steering with a narrow road-edge recovery branch:

```modelica
if df < 0.15 and dl < dr then
  steer := -min(0.6, 2 * abs(dl - dr));
elseif df < 0.15 and dr < dl then
  steer := min(0.6, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

This branch is intentionally inactive during the Track3 first obstacle event
because `df` is around `0.83` there. It becomes active only when the front
distance is extremely small, matching the road-edge grazing window.

## Validation Gate

1. Run `Scripts/quality/check_controller_deployability.py`.
2. Run Track3 first because it has both the remaining obstacle event and the
   road event.
3. Accept expansion only if Track3 removes the road event or otherwise improves
   `P` without creating an earlier non-comparable terminal state.
4. If Track3 improves, run all four tracks and accept only if total wrapper
   score beats v80 without introducing worse runtime caveats.
5. If Track3 is unchanged or regresses, restore v80 semantics and record a
   rejection.

## Non-Goals

- No official vehicle, road, sensor, scoring, example, or material edits.
- No per-track branches.
- No report/package work.
- No physical UGV or final competition score claim.

## Review Outcome

v83 ran the Track3 target gate successfully to 120 s, but score variables did
not improve:

```text
Track3 v83: T=120.0, cR=1, cO=1, P=9.2, simulate_returned_true
```

It is rejected as a score candidate because it preserved the same `P/cR/cO`
as v80 on Track3. Source semantics were restored to v80, and the restore gate
passed at:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v83_20260710.md
```

Review:

```text
Results/metrics/track3_candidate_review_v83_road_edge_recovery_20260710.md
```
