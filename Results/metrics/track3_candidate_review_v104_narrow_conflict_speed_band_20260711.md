# v104 Narrow Conflict Speed Band Review

Timestamp: 2026-07-11 CST

## Candidate

`v104_narrow_conflict_speed_band` tested a narrower ControlAllocate conflict
speed gate after `v103_conflict_path_speed` improved Track3 but regressed
Track1.

Changed mechanism under test:

```modelica
gain2.u = if speed_oa < 0 and steer_oa * steer_pp < 0
  and abs(steer_pp) > 0.21 and abs(steer_pp) < 0.235
  and unitDelay3.y > 0.35 then 0.35 else unitDelay3.y;
```

## Runtime Evidence

Track3 run:

```text
Results/simulations/controller_v104_narrow_conflict_speed_band_saidao3_120s_20260711/
```

Extracted score variables:

```text
T = 25.1
cR = 2
cO = 1
P = 8.8
simulation_exit_state = 2
completion = simulate_false_with_result_variables
```

Current accepted v80 Track3 comparison:

```text
T = 59.4
cR = 1
cO = 1
P = 9.2
```

## Decision

Rejected. v104 regresses Track3 from `P=9.2` to `P=8.8` and increases road
collisions from `cR=1` to `cR=2`. Do not expand this candidate to the other
three tracks.

Restore accepted v80 ControlAllocate semantics and keep v104 as negative
evidence against narrow steering-band conflict speed gates.
