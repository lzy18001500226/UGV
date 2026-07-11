# UGV Controller Deployability Static Check

generated_at: 2026-07-11T20:47:39+08:00
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
  - line 351: `transition(avoid, cruise, after(2,sec), reset = false)`
- initialization_dwell_observed:
  - values_s: [1.0, 2.0]
  - line 747: `transition(ini_state, state, after(1,sec), reset = false)`
  - line 1077: `transition(ini_state, state, after(2,sec), reset = false)`

## Non-Claims

- Does not run MWORKS.
- Does not validate race score.
- Does not prove physical UGV readiness.
