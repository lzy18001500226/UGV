# Track1 / Track3 Candidate Review - v20 / v21

timestamp: 2026-07-09 CST
scope: controller tuning review after v19 rejection
accepted_controller_after_review: v13_side_trigger045

## Baseline For This Review

Current accepted controller remains v13:

```text
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45, reset = false)
avoid speed: -1
avoid_lateral initial steer: 0.6
```

Four-track v13 review evidence:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

## Candidate v20 - Front-Gated Side-Clearance Steering

Change tested:

```text
avoid_lateral initial fixed steer 0.6
  -> side-clearance direction gated by front clearance
```

Static check:

```text
Results/evidence/controller_deployability_static_check_v20_front_gated_side_20260709_1745.md
ready_for_physical_claim=true, high=0, medium=0
```

Track1 runtime evidence:

```text
Results/simulations/controller_v20_front_gated_side_saidao1_120s_20260709_1750/
T=120.0, cR=0, cO=10, P=6.0
```

Decision: reject v20. It removed Track1 road collisions but created many
obstacle collisions, so it is not an improvement over v13.

## Candidate v21 - Stronger Reverse Speed

Change tested:

```text
avoid speed -1 -> -1.2
avoid_lateral initial steer remains 0.6
```

Static check:

```text
Results/evidence/controller_deployability_static_check_v21_avoid_speed_minus12_20260709_1805.md
ready_for_physical_claim=true, high=0, medium=0
```

Track3 runtime evidence:

```text
Results/simulations/controller_v21_avoid_speed_minus12_saidao3_120s_20260709_1810/
T=120.0, cR=1, cO=1, P=9.2
```

Track1 runtime evidence:

```text
Results/simulations/controller_v21_avoid_speed_minus12_saidao1_120s_20260709_1815/
simulate_false_with_result_variables
T=7.05, cR=1, cO=0, P=9.6
```

Decision: reject v21. Track3 is unchanged versus v13, while Track1 stops early
and does not provide a credible improvement path.

## Source Restoration

The controller source was restored to v13 semantics after v20/v21:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Restoration static check:

```text
Results/evidence/controller_deployability_static_check_v13_restored_after_v20_v21_20260709_1855.md
ready_for_physical_claim=true, high=0, medium=0
```

## Next Direction

Do not continue raw scalar changes to fixed steer or reverse speed. The next
candidate should inspect `ControlAllocate` interaction and test a conservative
state-release or risk-gated behavior only when it has a clear target-track
hypothesis. Keep v13 as the accepted controller until a new candidate proves
target improvement and passes regression checks.
