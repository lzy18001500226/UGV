# v164 Stateful Endpoint Capture Plan

Status: planned before source edit.

## Goal

Combine v162's near-complete Track3 traversal with a generic closed-path
endpoint capture so the planner does not switch back to the first segment
before the vehicle enters the official origin finish radius.

## Evidence Basis

v162 reaches `T=286.55` and traverses the main Track3 loop, but returns along
the start/finish straight around `y=0.5` and misses the origin. Source review
shows `findClosestSegment` globally searches every segment on every evaluation
with no progress memory. Near a closed path's shared start/end, it can select
the first segment before the endpoint is captured.

v163 proves that removing side-only OA authority is unsafe. v164 therefore
restores v162's obstacle semantics and changes only the planner's closed-path
terminal behavior.

## Candidate

1. Restore v162's narrow `df<0.15` lateral recovery on top of v148.
2. Add a code-generation-friendly `lap_departed` discrete state to PathPlanner.
3. After the vehicle has moved more than `3 m` from `path[end]`, latch
   `lap_departed=true`.
4. When a departed vehicle returns within `3 m` of `path[end]`, set the pursuit
   point to the exact final point before steering is calculated.

The `3 m` capture radius is tied to the existing `2 m` base lookahead plus a
bounded margin; it is not a track-specific score threshold. The same planner
logic applies to every supplied path.

## Gates

1. Deployability checker, tests, and Track3 1 s native translation gate.
2. Strict Track3 700 s official completion gate.
3. A Track3 finish promotes to Track4, Track1, and Track2 regression.
4. Non-finish, model translation failure, or collision regression restores
   exact v148 controller and planner semantics.

No completion, 80/80, physical, or submission claim precedes saved runtime
evidence.
