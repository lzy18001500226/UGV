# Unified Obstacle Avoidance v176 Phase-Aligned Feedback Plan

Status: rejected; exact v148 source restored

## Goal

Convert the v162 near-complete Track3 traversal into an official finish while
making the existing lateral clearance states reachable.

## Evidence Basis

The accepted v148 state-machine timings contain a phase boundary defect:

- longitudinal avoidance exits after `2.0 s` and sets `flag=false`;
- lateral avoidance leaves its fixed `steer=+0.6` entry state after `2.0 s`;
- loss of `flag` exits lateral avoidance at the same boundary.

Saved v162 evidence confirms the consequence: throughout the near-complete
Track3 run, obstacle steering remains `+0.6` even though the model already has
bounded left/right clearance states. Those states receive no durable execution
window. Earlier candidates that shortened the lateral commitment destabilized
the initial obstacle encounter, while a three-second longitudinal dwell caused
broad road-collision regression. v176 tests the minimum phase-order correction,
not a dwell scan.

## Unified Candidate

Starting from exact v148 semantics:

1. retain v162's direction-aware correction only at `df < 0.15`;
2. change longitudinal avoid release from `after(2,sec)` to `after(2.1,sec)`;
3. leave the lateral `after(2,sec)` boundary and its existing bounded gap
   steering unchanged.

This gives the existing side-clearance feedback a 0.1 s execution window after
the safety commitment. The rule uses only the four official sensor inputs and
the existing state machine. It does not inspect track identity, position,
official geometry, score, or race time.

## Gates

1. Deployability checker and project tests.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s gate. Completion requires `SimulateModel=false`,
   `T>10`, and official `distanceSensor1.d<0.02`.
4. Only a verified Track3 finish promotes unchanged source to Tracks 4, 1,
   and 2.
5. Any non-finish or collision regression restores exact v148 semantics.

No finish, 80/80, physical-car, package, or submission claim precedes saved
runtime evidence.

## Result

The source checker passed with `high=0, medium=0`, all 14 project tests passed,
and the Track3 1 s native gate passed. The strict Track3 request ended at
`T=108.10,cR=2,cO=1,P=8.8`, with official finish distance squared `295.5409`.

The 0.1 s phase-aligned feedback window changed the trajectory and ran longer
than v148, but it did not finish and materially regressed the v162 diagnostic
runtime of `T=286.55`. Reject v176, restore exact v148 semantics, and close
longitudinal/lateral dwell phase alignment as a completion route.
