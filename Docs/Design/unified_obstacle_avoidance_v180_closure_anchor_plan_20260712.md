# Unified Obstacle Avoidance v180 Closure-Anchor Plan

Status: rejected after cross-track regression; exact v148 semantics restored

## Goal

Convert v162's near-complete Track3 traversal into an official finish without
adding progress state or wrapping the pursuit point onto the repeated outgoing
segment.

## Evidence Basis

- Track3 stores the origin at `path[end-1]` and repeats its first outgoing
  point at `path[end]`.
- v162 reaches indices 103/104 but returns about 0.65-0.75 m off the origin.
- v179 wrapped pursuit traversal to the first segment and regressed to
  `T=110.4`; the repeated outgoing segment is not a useful closure target.
- v173/v174 progress-state planners changed mid-route reacquisition and
  stopped at index 48, so sampled global progress is closed.

## Candidate

Use exact v162 controller behavior. In `calculatePursuitPoint`, choose the
closer of the last two path points to `path[1]` as the generic closure anchor.
Preserve the existing pursuit calculation before that anchor. If lookahead
would pass the anchor, clamp the pursuit point to the anchor instead of leaving
the output unassigned or wrapping onto the outgoing segment.

This applies one rule to every path and uses only path topology. It introduces
no track identifier, score, time, position threshold, or persistent state.

## Gates

1. Deployability checker, project tests, and diff review.
2. Track3 1 s native gate.
3. Strict Track3 700 s completion gate.
4. Expand unchanged source to Tracks 4, 1, and 2 only after a verified Track3
   finish.
5. Non-finish or collision regression restores exact v148 source semantics.

## Result

The first v180 Track3 run reached the official finish assertion at
`T=89.50,cR=1,cO=1,P=9.2`, and Track4 also finished at
`T=89.65,cR=3,cO=0,P=8.8`. Track1 regressed to an unclassified termination at
`T=67.20`, so v180 was not promoted.

Two isolation checks followed. v181 restricted the closure anchor to an exact
penultimate origin but reproduced the Track1 failure. v182 restored v148
obstacle behavior and finished Tracks 3 and 1, but reproducibly regressed
Track2 to `T=28.55`. The early v148/v182 trajectory difference was only about
`1e-5` before the road-boundary event, showing that this path-function edit is
numerically fragile across translated models. It is rejected as a completion
mechanism. Exact v148 path and obstacle-controller semantics were restored.

No four-track completion, 80/80, physical-car, package, or submission claim is
made.
