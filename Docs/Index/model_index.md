# Model Index

## 1. Official Working Copy

```text
Models/UGV/
```

This is copied from the official initial-race material and is the project
working model tree.

## 2. Key Files

| Purpose | File |
|---|---|
| Race example 1 | `Models/UGV/Example/Race1.mo` |
| Race example 2 | `Models/UGV/Example/Race2.mo` |
| Obstacle controller target | `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo` |
| Path planner | `Models/UGV/Control/PathPlanning/PathPlanner.mo` |
| Control allocation | `Models/UGV/Control/ControlAllocate/package.mo` |
| Ackermann PID | `Models/UGV/Control/Ackermann_control/PID_Ackermann.mo` |
| Scoring | `Models/UGV/CountPoint/package.mo` |
| Distance sensor | `Models/UGV/Vehicle/Sensors/distanceSensor1.mo` |
| Official track models | `Models/UGV/saidao/saidao1.mo`, `saidao2.mo`, `saidao3.mo`, `saidao4.mo` |
| Generated M6 evaluation wrappers | `Models/UGV/Test/Saidao1Eval.mo`, `Saidao2Eval.mo`, `Saidao3Eval.mo`, `Saidao4Eval.mo` |

## 3. Entry Models

| Entry | Source File | Internal Model Name | Role |
|---|---|---|---|
| Race example with obstacle controller | `Models/UGV/Example/Race1.mo` | `Race1` | Main editable-controller integration entry. |
| Race example without obstacle controller | `Models/UGV/Example/Race2.mo` | `Race2` | Baseline/comparison entry; no `ObsAvoidController_Sysblock2` instance. |
| Official track LOGO source geometry | `Models/UGV/saidao/saidao1.mo` | `saidao1` | Official source track entry; not the current controller API evaluation entry because it omits `ObsAvoidController_Sysblock2` wiring. |
| Official track comprehensive ring source geometry | `Models/UGV/saidao/saidao2.mo` | `saidao2` | Official source track entry; not the current controller API evaluation entry because it omits `ObsAvoidController_Sysblock2` wiring. |
| Official track triangle source geometry | `Models/UGV/saidao/saidao3.mo` | `saidao3` | Official source track entry; not the current controller API evaluation entry because it omits `ObsAvoidController_Sysblock2` wiring. |
| Official track cloud source geometry | `Models/UGV/saidao/saidao4.mo` | `saidao4` | Official source track entry; not the current controller API evaluation entry because it omits `ObsAvoidController_Sysblock2` wiring. |
| M6 LOGO evaluation wrapper | `Models/UGV/Test/Saidao1Eval.mo` | `Saidao1Eval` | Current M6 controller evaluation entry with official track geometry plus obstacle-controller and control-allocation connections. |
| M6 comprehensive-ring evaluation wrapper | `Models/UGV/Test/Saidao2Eval.mo` | `Saidao2Eval` | Current M6 controller evaluation entry with official track geometry plus obstacle-controller and control-allocation connections. |
| M6 triangle evaluation wrapper | `Models/UGV/Test/Saidao3Eval.mo` | `Saidao3Eval` | Current M6 controller evaluation entry with official track geometry plus obstacle-controller and control-allocation connections. |
| M6 cloud evaluation wrapper | `Models/UGV/Test/Saidao4Eval.mo` | `Saidao4Eval` | Current M6 controller evaluation entry with official track geometry plus obstacle-controller and control-allocation connections. |

Note: the official track file names and internal Modelica model names do not
match one-to-one. Runtime work must open the internal model name exposed by the
loaded package, not infer it from the file name alone.

For current M6 runtime evaluation, use `UGV.Test.Saidao1Eval` through
`UGV.Test.Saidao4Eval`. The direct `UGV.saidao.saidao*` models are preserved as
official source geometry/scoring references and should not be edited during
normal development.

## 4. Controller Interface

`ObsAvoidController_Sysblock2` exposes:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

The initial copied equation body is empty. This is the first implementation
target.

## 5. Signal And Control Path

In `Race1`, sensor outputs enter the obstacle controller and then merge through
control allocation:

```text
distanceSensor1.front_dist -> obsAvoidController_Sysblock.front_dist
distanceSensor1.rear_dist  -> obsAvoidController_Sysblock.rear_dist
distanceSensor1.left_dist  -> obsAvoidController_Sysblock.left_dist
distanceSensor1.right_dist -> obsAvoidController_Sysblock.right_dist

obsAvoidController_Sysblock.speed -> ctrlAlloc.speed_oa
obsAvoidController_Sysblock.steer -> ctrlAlloc.steer_oa
pathPlanner.target_v             -> ctrlAlloc.speed_pp
pathPlanner.steering_angle       -> ctrlAlloc.steer_pp
ctrlAlloc.speed                  -> pID_Ackermann.v_desired
ctrlAlloc.steer                  -> pID_Ackermann.psi_desired
```

`Race2` omits `ObsAvoidController_Sysblock2`; the path planner connects to
`CtrlAlloc`, and the obstacle-avoidance inputs are not driven by the controller
instance because no such instance is present.

`CtrlAlloc` defaults to `factor_pp = 1` and `factor_oa = 0.3`, while the
example and official track entries inspected here instantiate it with
`factor_pp = 1` and `factor_oa = 0.5`.

## 6. Sensor Semantics

`distanceSensor1` exposes directional distances and scoring distances:

```text
front_dist, rear_dist, left_dist, right_dist
DisRoad, DisObstacle
```

Observed static behavior:

- `left_dist` and `right_dist` choose obstacle distance when the obstacle vector
  lies within the vehicle longitudinal span; otherwise they use road lateral
  distance.
- `front_dist` and `rear_dist` choose obstacle distance when the obstacle vector
  lies within the vehicle lateral span; otherwise front uses `fdist` and rear
  uses road rear distance.
- `DisRoad = min(Ldist, Rdist)`.
- `DisObstacle = sqrt(vec_obsB[1]^2 + vec_obsB[2]^2)`.
- The sensor asserts completion with `d >= 0.02 or time <= 10` using message
  `已跑完赛道全程，仿真结束`.

## 7. Score Source

`Models/UGV/CountPoint/package.mo` defines `finalPoints` as:

```text
10 - (counterR + counterO) * 0.4
```

where `counterR` is road collision count and `counterO` is obstacle collision
count.

Count thresholds:

```text
road event: DisRoad < 0.11
obstacle event: DisObstacle < 0.11
release: distance > 0.13
```

`Race1`, `Race2`, and the inspected official track entries expose display
variables `cR`, `cO`, `P`, and `T` sourced from `countPoint.counterR`,
`countPoint.counterO`, `countPoint.finalPoints`, and `time` respectively.

MWORKS CSV export caveat: exported `extra_timeseries.csv` files can contain
duplicate `Time` columns when variables are sampled from different result
groups. Do not parse those files with plain duplicate-key `DictReader` and then
align all signals by row. Preserve duplicate column indexes or use a script
that explicitly handles multiple time axes. Current scripts
`Scripts/analysis/summarize_signal_windows.py` and
`Scripts/analysis/analyze_ctrlalloc_contributions.py` bind each requested signal
to the nearest `Time` column on its left; smoke evidence:
`Results/metrics/signal_window_summary_v48_track3_timeaxis_fix_smoke_20260710.md`
and
`Results/metrics/ctrlalloc_contribution_analysis_v48_timeaxis_fix_smoke_20260710.md`.
