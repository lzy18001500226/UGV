# Track3 v48 Sensor Semantic Gap

Status: diagnostic evidence, 2026-07-10 CST

## Finding

The current accepted v48 controller receives four directional distance inputs:

```text
front_dist
rear_dist
left_dist
right_dist
```

The official sensor model also computes the two scalar distances used by the
score counter:

```text
distanceSensor1.DisObstacle -> countPoint.DisObstacle
distanceSensor1.DisRoad     -> countPoint.DisRoad
```

Those scalar distances are not connected to the obstacle controller in the
current `Models/UGV/Test/Saidao*Eval.mo` wrappers.

## Track3 Evidence

Diagnostic run:

```text
Results/simulations/diagnostic_v48_track3_countpoint_6s_20260710/
```

At the first Track3 obstacle event:

| t/s | countPoint.DisObstacle | distanceSensor1.DisObstacle | controller df | controller flag | ctrlAlloc.speed | ctrlAlloc.steer |
|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | 0.1061 | 0.1061 | 0.8306 | 1 | 0.7196 | 0.1623 |

At the first Track3 road event:

| t/s | countPoint.DisRoad | distanceSensor1.DisRoad | controller dl | controller dr | ctrlAlloc.speed | ctrlAlloc.steer |
|---:|---:|---:|---:|---:|---:|---:|
| 4.85 | 0.1049 | 0.1049 | 0.5177 | 0.6173 | 0.5105 | 0.1847 |

## Interpretation

The remaining v48 Track3 events are not explained only by state-machine
constants or steering magnitude. The score-relevant nearest obstacle/road
distances already show danger, but the current controller-facing directional
signals still look relatively safe.

This explains why repeated post-v48 scalar changes did not robustly remove the
collision events:

- stronger initial steering does not fix missing nearest-distance semantics;
- front-threshold scans act on `front_dist`, not on nearest obstacle distance;
- road-edge steering scans act on side directional signals, not on
  `DisRoad`;
- speed-only changes reduce velocity but do not add the missing geometric
  risk input.

## Next Diagnostic

Before another formal controller candidate, run a diagnostic-only wrapper that
tests whether exposing `distanceSensor1.DisObstacle` to the controller-facing
front-risk path improves Track3 attribution. This is not final competition
evidence unless the interface and official deployment path are reviewed.

Do not edit:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```
