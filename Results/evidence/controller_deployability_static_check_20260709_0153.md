# UGV Controller Deployability Static Check

generated_at: 2026-07-09T01:55:14+08:00
controller: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
ready_for_physical_claim: false

## Summary

- high: 1
- medium: 1
- low: 0

## High Findings

- reciprocal_distance_terms_present: 1/distance steering can spike near zero sensor readings; replace or prove saturation before physical-ready claims.
  - line 558: `annotation(__MWORKS(BlockSystem(StateMachine(actionKind = ActionKind.entry or ActionKind.during))));steer := -2 * (1 / dr + 0.1) * abs(dl - dr);`
  - line 607: `annotation(__MWORKS(BlockSystem(StateMachine(actionKind = ActionKind.entry or ActionKind.during))));steer:=2 * (1 / dl + 0.1) * abs(dl - dr);`
  - line 912: `annotation(__MWORKS(BlockSystem(StateMachine(actionKind = ActionKind.entry or ActionKind.during))));  steer := 2 * (1 / dl + 0.1) * abs(dl - dr);`
  - line 961: `annotation(__MWORKS(BlockSystem(StateMachine(actionKind = ActionKind.entry or ActionKind.during))));  steer := -2 * (1 / dr + 0.1) * abs(dl - dr);`

## Medium Findings

- mixed_dwell_values: Multiple dwell durations exist; confirm active transitions before physical tuning.
  - values_s: [1.0, 2.0]
  - line 346: `transition(avoid, cruise, after(2,sec), reset = false)`
  - line 357: `horizontalAlignment=TextAlignment.Left), __MWORKS(BlockSystem(StateMachine(outerTransition = true))), displayText = "[after(1,sec)]");`
  - line 742: `transition(ini_state, state, after(1,sec), reset = false)`
  - line 753: `horizontalAlignment=TextAlignment.Left), __MWORKS(BlockSystem(StateMachine(outerTransition = true))), displayText = "[after(1,sec)]");`
  - line 1072: `transition(ini_state, state, after(2,sec), reset = false)`
  - line 1083: `horizontalAlignment=TextAlignment.Left), __MWORKS(BlockSystem(StateMachine(outerTransition = true))), displayText = "[after(2,sec)]");`

## Low Findings

- none

## Non-Claims

- Does not run MWORKS.
- Does not validate race score.
- Does not prove physical UGV readiness.
