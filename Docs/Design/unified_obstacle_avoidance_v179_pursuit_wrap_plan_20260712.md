# Unified Obstacle Avoidance v179 Pursuit-Wrap Plan

Status: rejected after Track3 completion gate; exact v148 source semantics restored

## Goal

Convert v162's near-complete Track3 traversal into an official finish by
repairing one generic closed-path defect: the pursuit point currently stops at
the final path point instead of continuing along the final-to-first segment.

## Evidence Basis

- v162 reaches `T=286.55,cR=2,cO=1,P=8.8`, traverses the main loop, returns
  near the start, and then begins another lap without satisfying the origin
  finish assertion.
- v117 changed three path primitives together. Its Track3 run stopped at
  `T=59.4`, before the closing segment was reached, so it did not test whether
  pursuit wrapping helps a trajectory that actually reaches the endpoint.
- `calculatePursuitPoint` currently exits when `current_index` reaches the
  final path point. If lookahead remains, the output is not assigned by that
  invocation and the final-to-first segment is never traversed.

## Candidate

Use exact v162 obstacle-controller semantics on top of v148. Change only
`Internal.calculatePursuitPoint` so that:

1. the output has a deterministic current-segment fallback;
2. traversal wraps from the final path point to the first point;
3. nearest-segment search and speed interpolation remain unchanged.

This is one unified closed-path behavior. It does not inspect track identity,
time, score, vehicle position, or official finish state.

## Gates

1. Deployability checker, project tests, and candidate diff check.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s request. Completion requires `SimulateModel=false`,
   `T>10`, and `distanceSensor1.d<0.02` at termination.
4. Only an official Track3 finish permits unchanged-source regression on
   Tracks 4, 1, and 2.
5. Any non-finish or material collision regression restores exact v148 source.

No completion, score, physical-car, package, or submission claim is made
before the corresponding runtime evidence exists.

## Result

The 1 s native gate passed. The strict Track3 request stopped without a finish
at `T=110.4,cR=1,cO=1,P=9.2`, with finish distance squared `301.7618`.
Although the pursuit-wrap change was active and materially changed the
trajectory, it regressed far behind v162's `T=286.55` near-loop result. The
candidate is rejected and both source edits are removed.
