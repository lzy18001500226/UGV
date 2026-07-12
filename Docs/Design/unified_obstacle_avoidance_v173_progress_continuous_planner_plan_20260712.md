# Unified Obstacle Avoidance v173 Progress-Continuous Planner Plan

Status: rejected after Track3 mid-route departure; superseded by v174 before final source restoration.

## Goal

Convert v162's complete Track3 loop traversal into an official finish by
preventing the path tracker from jumping from the final path region back to
the first segment before the endpoint is reached.

## Evidence Basis

- v162 traversed the main Track3 loop and reached path indices `103/104`, but
  the global nearest-segment search then selected index `1` near the shared
  start/end region. The vehicle began another lap and missed the finish radius.
- `findClosestSegment` searches every segment independently on every solver
  evaluation and has no progress continuity.
- v164/v165/v168 endpoint-capture branches were rejected because they added a
  special finish condition without correcting the underlying segment-selection
  architecture.

## Candidate Architecture

1. Keep v162's bounded `df<0.15` direction correction, the only controller
   mechanism that traversed the full Track3 loop.
2. Add a generic local-window nearest-segment function.
3. Sample path progress at 20 Hz and search only two segments behind and eight
   segments ahead of the previous accepted index.
4. Do not wrap the search window from the final segment to segment one. A new
   lap can only begin after the official scenario terminates or a separately
   designed lap-reset rule is introduced.

This is a standard progress-continuity mechanism. It uses path order and
vehicle position, not track identity, score, hard-coded coordinates, or race
time. The same code applies to all four paths.

## Gates

1. Controller deployability checker, project tests, and source diff review.
2. Track3 1 s native load/check/simulate gate.
3. Strict Track3 700 s official finish gate.
4. A verified Track3 finish promotes unchanged source to Tracks 4, 1, and 2.
5. Translation failure, non-finish, or material collision regression restores
   exact v148 controller and original global planner semantics.

No finish, 80/80, physical, package, or submission claim precedes saved
runtime evidence.

## Result

The source gate, tests, and 1 s native gate passed. The strict Track3 request
ended at `T=49.3,cR=1,cO=1,P=9.2`, closest index `48`, with official finish
distance squared `385.5061`. The bounded backward/forward window changed normal
mid-route segment selection and did not finish. v173 is rejected. v174 keeps
the progress-state architecture but replaces the small bidirectional window
with a monotonic search over all remaining forward segments.
