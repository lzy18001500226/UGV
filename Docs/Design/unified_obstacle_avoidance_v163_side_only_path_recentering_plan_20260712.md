# v163 Side-Only Path Recentering Plan

Status: rejected after Track3 collision regression; exact v148 source restored.

## Goal

Convert v162's near-complete Track3 loop into an official finish by removing
the persistent side-only OA heading on the start/finish straight, while
preserving immediate front-obstacle steering authority.

## Evidence Basis

v162 extends Track3 from v148 `T=21.1` to `T=286.55`, keeps `cO=1`, and
traverses the main loop. Its trajectory returns along the start/finish straight
near `y=0.5` instead of the official centerline `y=0`, so the origin-return
assertion is missed. The fixed positive lateral re-entry remains active when
the front is clear and a side distance alone triggers avoidance.

Rejected candidates define the boundary:

- v144 set every lateral re-entry to zero and added obstacle collisions;
- v64 chose a side-distance direction during front-clear re-entry and stopped
  early;
- v158-v161 changed allocator-level path/OA arbitration and added collisions.

v163 keeps v162's narrow `df<0.15` recovery and changes only the front-clear,
side-only entry. This preserves the default `+0.6` whenever front risk remains.

## Candidate

```modelica
if df < 0.15 and dl < dr then
  steer := -min(0.6, 2 * abs(dl - dr));
elseif df < 0.15 and dr < dl then
  steer := min(0.6, 2 * abs(dl - dr));
elseif df > mindis then
  steer := 0;
else
  steer := 0.6;
end if;
```

The rule is unified, code-generation-oriented, and uses only existing sensor
state. It does not inspect track, score, position, time, or official geometry.

## Gates

1. Static checker, tests, and Track3 1 s native gate.
2. Strict Track3 700 s official completion gate.
3. Only a Track3 finish promotes to Track4, Track1, and Track2 regression.
4. Non-finish or obstacle-collision regression restores exact v148 semantics.

No completion, score, physical, or submission claim precedes runtime evidence.

## Result

The 1 s gate passed, but the strict request ended at
`T=80.0,cR=5,cO=7,P=5.2`, finish distance `124.9077`. Stateless front-clear
side-only zero steering destroys obstacle clearance and is rejected. Review:
`Results/metrics/track3_candidate_review_v163_side_only_path_recentering_20260712.md`.
