# Unified Obstacle Avoidance v170 v162 Bounded OA Decay Plan

## Goal

Retain v162's full-loop stability while reducing its stale opposing OA offset
gradually rather than using v169's collision-heavy immediate cancellation.

## Evidence Basis

- v169 combined v162 with v158 immediate cancellation and reached
  `T=116.75`, finish-distance squared `88.61`, but accumulated nine collisions.
- v157's existing bounded mechanism retained `35%` of OA filter input and did
  not add collisions on v148, although v148 lacked v162's stable loop entry.
- This is a combination test of two existing evidence-backed mechanisms, not a
  new attenuation-factor scan.

## Unified Mechanism

1. Keep v162's narrow front-obstacle lateral recovery.
2. Restore the normal final steering sum.
3. Only when longitudinal OA is neutral, OA/path headings oppose, and
   `abs(path)>0.15`, feed `0.35*OA` into the existing first-order filter;
   otherwise use the full OA input.

No planner equation, new state, track id, official model, or new parameter is
introduced.

## Gates

Static/tests, Track3 1 s, then strict Track3 700 s. Expand to all tracks only
after an official Track3 finish. Reject and restore v148 on non-finish or
collision regression.
