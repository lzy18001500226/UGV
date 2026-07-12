# UGV Controller Deployability Static Check

generated_at: 2026-07-12T18:14:26+08:00
controller: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
ready_for_physical_claim: true

## Summary

- high: 0
- medium: 0
- low: 2

## High Findings

- none

## Medium Findings

- none

## Low Findings

- avoid_release_dwell_present:
  - values_s: [2.0]
  - line 346: `transition(avoid, cruise, after(2,sec) and (df <= 0 or df > mindis) and dl > 0.45 and dr > 0.45, reset = false)`
- initialization_dwell_observed:
  - values_s: [1.0, 2.0]
  - line 742: `transition(ini_state, state, after(1,sec), reset = false)`
  - line 1072: `transition(ini_state, state, after(2,sec), reset = false)`

## Non-Claims

- Does not run MWORKS.
- Does not validate race score.
- Does not prove physical UGV readiness.
