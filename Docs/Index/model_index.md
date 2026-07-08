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

## 3. Controller Interface

`ObsAvoidController_Sysblock2` exposes:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

The initial copied equation body is empty. This is the first implementation
target.

## 4. Score Source

`Models/UGV/CountPoint/package.mo` defines `finalPoints` as:

```text
10 - (counterR + counterO) * 0.4
```

where `counterR` is road collision count and `counterO` is obstacle collision
count.
