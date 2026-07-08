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
| Official track models | `Models/UGV/saidao/saidao5.mo`, `saidao7.mo`, `saidao8.mo`, `saidao9.mo` |

## 3. Entry Models

| Entry | Source File | Internal Model Name | Role |
|---|---|---|---|
| Race example with obstacle controller | `Models/UGV/Example/Race1.mo` | `Race1` | Main editable-controller integration entry. |
| Race example without obstacle controller | `Models/UGV/Example/Race2.mo` | `Race2` | Baseline/comparison entry; no `ObsAvoidController_Sysblock2` instance. |
| Official track LOGO | `Models/UGV/saidao/saidao5.mo` | `saidao1` | Official scored track candidate. |
| Official track comprehensive ring | `Models/UGV/saidao/saidao7.mo` | `saidao2` | Official scored track candidate. |
| Official track triangle | `Models/UGV/saidao/saidao8.mo` | `saidao3` | Official scored track candidate. |
| Official track cloud | `Models/UGV/saidao/saidao9.mo` | `saidao4` | Official scored track candidate. |

Note: the official track file names and internal Modelica model names do not
match one-to-one. Runtime work must open the internal model name exposed by the
loaded package, not infer it from the file name alone.

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

`Race1`, `Race2`, and the inspected official track entries expose display
variables `cR`, `cO`, `P`, and `T` sourced from `countPoint.counterR`,
`countPoint.counterO`, `countPoint.finalPoints`, and `time` respectively.
