# v191 Brake-Then-Steer Handoff Candidate

## Objective

Restore Track2 completion with one track-agnostic controller rule. The
candidate separates imminent front-risk braking from lateral OA authority:
slow early, but do not let the fixed lateral OA command override the path
planner until the obstacle controller is actually in reverse/escape mode.

## Mechanism

- Controller front entry threshold: `mindis=1.5` metres.
- Allocator passes `steer_oa` only when `speed_oa < 0`; otherwise the path
  steering remains authoritative.
- OA speed and all official models remain unchanged apart from the controller
  threshold. No track/time/score/absolute-coordinate branch is introduced.

## Gates

1. Static deployability and repository tests.
2. Track2 1 s native gate.
3. Track2 strict 700 s official completion predicate.
4. Only after Track2 completion, evaluate the same bytes on Tracks 1, 3, and 4.

## Rollback

Restore both controller and allocator to exact `HEAD` semantics if Track2 does
not complete or if the candidate produces a non-comparable early failure.
