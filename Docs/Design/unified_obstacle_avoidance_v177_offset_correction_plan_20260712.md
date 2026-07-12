# Unified Obstacle Avoidance v177 Offset-Correction Plan

Status: rejected; exact v148 source restored

## Goal

Correct the repeatable Track3 return-line offset observed in v162 without
changing path planning, allocation, official models, or track-specific logic.

## Evidence Basis

v162 traversed the Track3 loop twice. Near the origin, the first return was at
approximately `y=0.743` and the second at `y=0.648`, while the finish radius is
about `0.141`. In both return windows the obstacle controller continued to
request fixed `steer=+0.6`, while the path planner requested negative steering.
The allocated steering remained only slightly negative, leaving insufficient
centerline correction before the origin.

v175 proved that changing the later proportional-state cap is a runtime no-op,
because the fixed entry state dominates each two-second avoid episode. v166's
directional replacement removed required obstacle safety. v177 therefore keeps
the positive safety direction and tests one bounded authority correction.

## Unified Candidate

Starting from exact v148 semantics:

1. retain v162's direction-aware correction only at `df < 0.15`;
2. otherwise use fixed entry steering `+0.55` instead of `+0.60`;
3. leave all timings, thresholds, proportional states, path planning, and
   allocation unchanged.

The same four-sensor rule applies to every track. It does not inspect track
identity, position, score, official geometry, or race time.

## Gates

1. Deployability checker and project tests.
2. Track3 1 s native gate.
3. Strict Track3 700 s completion request.
4. Only a verified Track3 finish promotes unchanged source to Tracks 4, 1,
   and 2.
5. A non-finish or collision regression restores exact v148 semantics. Do not
   scan more fixed-entry magnitudes after this evidence-based value.

No finish, 80/80, physical-car, package, or submission claim precedes saved
runtime evidence.

## Result

Static checks, 14 project tests, and the Track3 1 s native gate passed. The
strict Track3 request ended at `T=18.50,cR=1,cO=0,P=9.6`, with official finish
distance squared `293.7713`. The readable `9.6` is an early-termination score,
not completion. Reducing the fixed positive authority removed the first
obstacle collision but destroyed v162's route stability. Reject v177, restore
exact v148 semantics, and close fixed-entry magnitude scans.
