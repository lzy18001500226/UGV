# Unified Obstacle Avoidance v175 Narrow Recovery and Adaptive Side Plan

Status: candidate pending runtime gates.

## Goal

Retain v162's only demonstrated full-main-loop Track3 behavior while reducing
the fixed lateral oversteer that leaves the vehicle offset from the origin on
the return straight.

## Candidate

Use one unified state-machine policy on every track:

1. In the initial lateral-avoid state, retain fixed `+0.6` by default, but when
   `df < 0.15`, steer away from the closer side with a bounded proportional
   command. This is the v162 mechanism.
2. In the established left/right lateral states, retain their existing sign
   and `2*abs(dl-dr)` law, but cap magnitude at `0.6` instead of `0.8`. This is
   the isolated v138 adaptive-side mechanism.

The candidate does not inspect track id, score, absolute position, race time,
or path index. It does not modify official track, vehicle, road, sensor,
scoring, or example sources.

## Gates

1. Deployability checker and all project tests.
2. Track3 1 s native gate.
3. Track3 700 s official finish gate.
4. Only a verified Track3 finish promotes unchanged source to Tracks 4, 1,
   and 2.
5. Failure restores exact v148 semantics and records a rejected candidate.

Completion still requires `SimulateModel=false`, `T>10`, and
`distanceSensor1.d<0.02`. A readable score or long runtime is not completion.
