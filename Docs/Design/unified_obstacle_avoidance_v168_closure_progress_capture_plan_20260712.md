# Unified Obstacle Avoidance v168 Closure-Progress Capture Plan

## Goal

Use v162's verified near-complete Track3 traversal and prevent the closure
segment from switching to segment 1 before the official origin assertion.

## Evidence Basis

- v162 reaches closure indices `103/104`, then switches to index `1` around
  `y=0.65-0.75` and begins another lap.
- v164 added a departure event and regressed before the loop.
- v165 added a continuous closure geometry calculation and regressed before
  its predicate became true.
- v166/v167 changed all lateral re-entry windows and regressed collisions.

The planner already computes `closest_index` and `path_progress`. The official
closed arrays repeat the origin at `path[end-1]` and append the first outgoing
point at `path[end]`.

## Unified Mechanism

Keep v162's narrow front-obstacle recovery. Immediately after the existing
pursuit-point calculation:

```modelica
if closest_index >= size(path,1) - 2 and path_progress > 0.5 then
  pursuit_point := {path[end-1,1], path[end-1,2]};
end if;
```

This uses only existing algebraic outputs, adds no state/event/function call,
and is generic for every official closed path using the same repeated-origin
representation. It is inactive at startup (`closest_index=1`).

## Gates

1. Static checker and all tests.
2. Track3 1 s native gate.
3. Track3 700 s strict official completion gate.
4. If Track3 finishes, run Tracks 4, 1, and 2 unchanged.

Reject and restore v148 on non-finish or material collision regression.
