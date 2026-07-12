# Unified Obstacle Avoidance v169 v162 Neutral Path Recovery Plan

## Goal

Combine the only Track3 mechanism that traversed the full loop (v162) with a
bounded allocator recovery that removes stale OA heading only when the path
requests an opposing correction and longitudinal OA authority is neutral.

## Evidence Basis

- v162 traversed the loop and returned to the origin straight twice, but a
  positive OA offset kept it near `y=0.65-0.75` and it missed the official
  `d<0.02` assertion.
- v158, tested on v148, moved the first road event from `4.1 s` to `13.8 s`
  and reached path index 76, proving guarded path recovery changes the correct
  conflict. It did not have v162's stable obstacle-entry behavior and regressed
  collisions.
- v159 removed the meaningful-path gate and regressed further, so v169 keeps
  v158's `abs(path)>0.15` boundary.

## Unified Mechanism

1. Restore v162's direction-aware lateral entry only for `df<0.15`.
2. At the allocator's final steering sum, when `speed_oa==0`, OA and path
   headings oppose, and `abs(path)>0.15`, subtract the filtered OA term from
   the path-side input so the final sum equals the existing path command.
3. Preserve active reverse obstacle authority, all filters, speed allocation,
   state transitions, planner equations, official models, and one common
   parameter set.

## Gates

1. Static checker and all project tests.
2. Track3 1 s native translation gate.
3. Track3 700 s strict completion gate.
4. Cross-track expansion only after verified Track3 finish.

Reject and restore exact v148 controller/allocator semantics on non-finish or
collision regression.
