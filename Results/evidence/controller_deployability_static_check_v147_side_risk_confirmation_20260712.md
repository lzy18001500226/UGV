# UGV Controller Deployability Static Check

generated_at: 2026-07-12T10:25:53+08:00
controller: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
ready_for_physical_claim: true

## Summary

- high: 0
- medium: 0
- low: 3

## High Findings

- none

## Medium Findings

- none

## Low Findings

- avoid_release_dwell_present:
  - values_s: [2.0]
  - line 353: `transition(avoid, cruise, after(2,sec), reset = false)`
- initialization_dwell_observed:
  - values_s: [1.0, 2.0]
  - line 749: `transition(ini_state, state, after(1,sec), reset = false)`
  - line 1079: `transition(ini_state, state, after(2,sec), reset = false)`
- other_dwell_observed:
  - values_s: [0.2]
  - line 352: `transition(side_pending, avoid, after(0.2,sec) and (dl <= 0.45 or dr <= 0.45), reset = false, priority = 3);`

## Non-Claims

- Does not run MWORKS.
- Does not validate race score.
- Does not prove physical UGV readiness.
