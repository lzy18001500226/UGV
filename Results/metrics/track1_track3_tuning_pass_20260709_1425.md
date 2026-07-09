# Track1 / Track3 Tuning Pass - 20260709_1425

## Scope

Active task: targeted Track 1 / Track 3 tuning after the M6 wrapper baseline.

Allowed controller target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Official no-edit zones were not modified. The controller source was restored to
the previous v5 candidate after rejected experiments; no v7-v11 parameter
change remains in the source.

Baseline:

```text
Results/metrics/four_track_summary_20260709_120547.md
Track1: T=86.9, cR=4, cO=3, P=7.2
Track3: T=50.4, cR=2, cO=5, P=7.2
```

## Experiments

| Version | Change | Track | T/s | cR | cO | P | Evidence | Decision |
|---|---|---|---:|---:|---:|---:|---|---|
| v7 | Avoid-lateral initialization dwell `2s -> 0.5s` | Track3 | 73.5 | 7 | 6 | 4.8 | `Results/simulations/controller_v7_quick_lateral_saidao3_120s_20260709_140903/` | Rejected: severe road-collision regression. |
| v8 | Front avoid reverse speed `-1 -> -0.7` | Track3 | 50.85 | 4 | 1 | 8.0 | `Results/simulations/controller_v8_reverse_speed_saidao3_120s_20260709_141117/` | Track3 improves, but not globally accepted. |
| v8 | Front avoid reverse speed `-1 -> -0.7` | Track1 | 85.1 | 6 | 6 | 5.2 | `Results/simulations/controller_v8_reverse_speed_saidao1_120s_20260709_141228/` | Rejected: Track1 regression. |
| v9 | Front avoid reverse speed `-1 -> -0.85` | Track3 | 49.65 | 3 | 4 | 7.2 | `Results/simulations/controller_v9_reverse_speed_saidao3_120s_20260709_141426/` | Not accepted: no score gain. |
| v9 | Front avoid reverse speed `-1 -> -0.85` | Track1 | 84.45 | 4 | 3 | 7.2 | `Results/simulations/controller_v9_reverse_speed_saidao1_120s_20260709_141541/` | Not accepted: no score gain. |
| v10 | Reverse speed `-0.7` plus steer cap `0.8 -> 0.7` | Track3 | 50.85 | 4 | 1 | 8.0 | `Results/simulations/controller_v10_reverse_steer_saidao3_120s_20260709_141805/` | Track3 improves, but not globally accepted. |
| v10 | Reverse speed `-0.7` plus steer cap `0.8 -> 0.7` | Track1 | 85.1 | 6 | 6 | 5.2 | `Results/simulations/controller_v10_reverse_steer_saidao1_120s_20260709_141927/` | Rejected: Track1 regression. |
| v11 | Steer cap `0.8 -> 0.7` only | Track3 | 50.4 | 2 | 5 | 7.2 | `Results/simulations/controller_v11_steer_cap_saidao3_120s_20260709_142134/` | Not accepted: identical to baseline. |
| v11 | Steer cap `0.8 -> 0.7` only | Track1 | 86.9 | 4 | 3 | 7.2 | `Results/simulations/controller_v11_steer_cap_saidao1_120s_20260709_142254/` | Not accepted: identical to baseline. |

## Checks

Static deployability checks passed for attempted source states:

```text
Results/evidence/controller_deployability_static_check_v7_quick_lateral_20260709.md
Results/evidence/controller_deployability_static_check_v8_reverse_speed_20260709.md
Results/evidence/controller_deployability_static_check_v9_reverse_speed_20260709.md
Results/evidence/controller_deployability_static_check_v10_reverse_steer_20260709.md
Results/evidence/controller_deployability_static_check_v11_steer_cap_20260709.md
Results/evidence/controller_deployability_static_check_restored_v5_20260709.md
```

Each MWORKS run returned `simulate_failed` with `exit_state=2`, but score
variables `T/cR/cO/P` were readable and `score_timeseries.csv` was exported.
This follows the current M6 wrapper evidence rule.

## Decision

No v7-v11 change is accepted as the project controller.

Current controller candidate remains:

```text
controller_v5_front_dwell_2s / controller_v5_bounded_linear_deployability
```

Reason:

- v8/v10 show that weaker reverse speed can reduce Track3 obstacle collisions,
  but it damages Track1 badly.
- v9 is a neutral trade: it changes collision composition but does not improve
  score.
- v11 proves steer-cap reduction alone does not move either weak track.
- v7 proves shorter avoid-lateral initialization is unsafe for Track3.

## Next Engineering Step

Do not keep blind scalar tuning. The next useful step is a diagnostic run that
exports controller-relevant variables or a visual/trajectory trace around the
collision jumps, then redesign the state logic with a track-independent rule:

```text
Track3 needs obstacle-collision reduction without Track1 road-collision
regression.
```

Useful diagnostics:

- export extra result variables containing controller distance inputs and
  speed/steer outputs;
- compare collision-jump windows from `score_timeseries.csv`;
- identify whether Track1 regression under v8/v10 comes from delayed obstacle
  clearance, road-boundary overrun, or reverse/steer interaction.
