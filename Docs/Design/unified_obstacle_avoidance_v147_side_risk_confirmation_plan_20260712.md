# Unified Obstacle Avoidance v147 Plan

Status: planned before source edit, 2026-07-12 CST.

## Goal

Test one unified completion-first mechanism: preserve immediate avoidance for a
front risk, but require a short persistent observation before a side-distance
trigger can command the v80 reverse and fixed-steer action.

## Evidence Basis

The first road contacts on Tracks 1, 2, and 4 have nearly identical obstacle
controller inputs: the front is clear (`df=2.05..2.59 m`), the left distance is
about `0.10 m`, the right distance is about `0.27 m`, and v80 already commands
`speed_oa=-1`, `steer_oa=+0.6`. The path-steer sign differs between tracks, so
the four instantaneous distances do not support another direction-selection
rule. Previous candidates already rejected distance-sign steering, persistent
lateral direction, path-aligned steering, and longitudinal release families.

Evidence:

```text
Results/metrics/ctrlalloc_contribution_v80_tracks124_20260712.md
Results/metrics/track2_v80_termination_classification_20260712.md
```

## Candidate

Add one `side_pending` state to the existing longitudinal state machine:

1. `df <= mindis` still enters `avoid` immediately.
2. A side-only trigger enters `side_pending`, which keeps cruise outputs.
3. If both sides clear, return to `cruise` without an avoidance action.
4. If front risk appears, enter `avoid` immediately.
5. If side risk persists for `0.2 s`, enter the unchanged v80 `avoid` state.

No track id, score, elapsed race time, road geometry, or official no-edit file
is used. The threshold is not a score scan; this gate tests whether persistence
separates a transient road-edge observation from a durable obstacle risk.

## Gates

1. Deployability checker, project tests, and `git diff --check`.
2. Track2 1 s native load/check/simulation gate.
3. Track2 120 s gate. Reject on syntax/runtime failure, new collision, shorter
   comparable progress, or no material improvement over v80.
4. Only after a material Track2 gain, run a 700 s completion gate and then
   cross-track regression. Official completion requires `SimulateModel=false`,
   `T>10`, and `distanceSensor1.d<0.02`.
5. On rejection, restore exact v80 source semantics and retain negative evidence.

This plan does not claim a finish, 80/80, physical-vehicle performance, report
readiness, or submission readiness.
