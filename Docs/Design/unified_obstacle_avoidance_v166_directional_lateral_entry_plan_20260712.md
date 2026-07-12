# Unified Obstacle Avoidance v166 Directional Lateral Entry Plan

## Goal

Convert v162's near-complete Track3 traversal into an official finish without
adding planner equations, new discrete state, track identifiers, or per-track
parameters.

## Evidence Basis

- v162 proves that direction-aware steering during very close front-obstacle
  entry can traverse the Track3 loop.
- The lateral avoid state machine then spends two seconds in `ini_state` with
  fixed `steer=+0.6` on every later re-entry before its existing directional
  states become active.
- v162 returns to the origin straight around `y=0.65-0.75`, switches from the
  closure segment to path segment 1, and begins another lap.
- v163 removed front-clear authority entirely and regressed collisions. v64
  added front-clear direction without v162's close-front stabilization and
  stopped early. Their exact combination has not been tested.

## Unified Mechanism

Change only `avoid_lateral.ini_state`:

```modelica
if dl < dr then
  steer := -min(0.6, 2 * abs(dl - dr));
elseif dr < dl then
  steer := min(0.6, 2 * abs(dl - dr));
else
  steer := 0;
end if;
```

This subsumes v162's close-front branch and extends the same measured
direction rule to front-clear side-risk re-entry. It preserves nonzero
proportional side authority, unlike v163, and leaves the existing directional
states after the two-second entry interval unchanged.

## Gates

1. Static deployability checker and all project tests.
2. Track3 1 s native translation gate.
3. Track3 700 s strict official completion gate.
4. Only after Track3 finishes, run Tracks 4, 1, and 2 with identical source.

Reject and restore exact v148 semantics on non-finish, early instability, or
material collision regression.
