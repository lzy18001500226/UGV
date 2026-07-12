# Unified Obstacle Avoidance v171 Encounter-Latched Recovery Plan

Status: rejected after Track3 collision regression; exact v148 source restored.

## Goal

Convert v162's near-complete Track3 traversal into an official finish without
repeating v163's global front-clear steering cancellation.

## Evidence Basis

- v162's narrow `df < 0.15` direction correction traversed the Track3 loop but
  missed the origin after returning on an offset heading.
- v163 zeroed steering for every front-clear side-only entry and regressed to
  seven obstacle collisions because front clearance alone did not distinguish
  obstacle traversal from post-obstacle recovery.
- v169/v170 show that stateless allocator cancellation or attenuation also
  destroys route stability.

The missing discriminator is whether the current avoid episode actually saw a
front obstacle. v171 adds that encounter memory inside the existing controller
state lifecycle.

## Candidate

Add `frontEncountered`, reset it in cruise, and latch it while the avoid state
sees `df <= mindis`. Preserve v162's close-front direction correction. Only
after a latched encounter has cleared beyond `safeF` does the lateral initial
state output zero steering and let path authority recenter the vehicle.

The rule is unified and uses only existing sensor inputs and controller state.
It does not inspect track identity, score, position, official geometry, or a
fixed race timestamp.

## Gates

1. Deployability checker, project tests, and diff check.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s completion request. Completion requires the official
   origin-return assertion, `SimulateModel=false`, `T>10`, and
   `distanceSensor1.d<0.02`.
4. Only a verified Track3 finish promotes to Tracks 4, 1, and 2.
5. Any non-finish or collision regression restores exact v148 source semantics.

No finish, 80/80, physical, package, or submission claim is made before the
corresponding runtime evidence exists.

## Result

The source gate and 1 s native gate passed. The strict Track3 request ended at
`T=17.75,cR=1,cO=2,P=8.8`, with official finish distance `292.9712`. This is
earlier than v148 and adds an obstacle collision. Encounter latching alone does
not identify a safe recentering window, so v171 is rejected and exact v148
semantics are restored.
