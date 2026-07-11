# v136 Path-Curvature Speed-Regulation Plan

Status: rejected after the extended Track2 gate; v80 semantics restored.

## Evidence Basis

The 310-second Track2 diagnostic disproves the suspected path-index relock:
`pathPlanner.closest_index` advanced monotonically from 1 to 30 with 29
forward changes and no backward change. The real failure is extremely low
progress after index 25:

| Index | Continuous residence | Position displacement |
|---:|---:|---:|
| 26 | 60.95 s | 3.34 m |
| 27 | 74.25 s | 4.31 m |
| 28 | 51.30 s | 2.80 m |

The v80 speed regulator treats `pathPlanner.steering_angle` as a local turn
angle. It is actually the desired global path heading consumed by the
downstream heading PID. In the saved Track2 run:

- `abs(steering_angle) > 0.35` for 95.18% of samples;
- `abs(steering_angle) > 1.0` for 70.28% of samples;
- `target_v=0.55` for 4290 of 6104 samples;
- after 100 s, final allocated speed stays near 0.05--0.06 while avoidance
  remains active.

Evidence source:

```text
Results/simulations/diagnostic_v80_track2_completion_geometry_310s_20260712/
```

## Unified Candidate

Keep the v80 obstacle controller, control allocation, pursuit point, and
desired global heading unchanged. In `PathPlanner`, calculate a local path
turn angle between the current segment and a bounded segment three points
ahead. Apply the existing two speed caps from that local geometry:

```text
local turn > 0.18 rad -> target_v <= 0.75
local turn > 0.45 rad -> target_v <= 0.55
```

This is one track-independent mechanism. It uses only the configured path,
does not add wrapper inputs, and does not modify official vehicle, road,
sensor, scoring, example, or evaluation models.

## Gates

1. Deployability checker and all project tests pass.
2. Native Track2 one-second load/check/simulation gate passes.
3. A 120-second Track2 diagnostic must advance materially farther than v80
   without increasing `cR=1` or `cO=0`.
4. Only after gate 3, run the extended official completion gate. Completion
   requires `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. If Track2 finishes, run Track1 collision regression before expanding to
   Tracks3-4. Any collision regression, early abnormal stop, or loss of
   progress rejects v136 and restores v80.

No horizon-only run is a finish, and no result from this plan alone proves an
80-point score or physical-vehicle performance.

## Result

The candidate passed static checks, all eight unit tests, and native Track2
one-second translation/simulation. At 120 seconds it retained `cR=1`, `cO=0`,
and `P=9.6`, while advancing to path index 28 instead of v80's index 26.

The extended gate rejected it. The run stopped abnormally at `T=159.95`, path
index 64, with `distanceSensor1.d=551.2135`; this is not the official finish.
It preserved the collision score but lost v80's longer runtime stability
(`T=305.15`). The geometry diagnosis remains useful, but this implementation
must not be retained or threshold-scanned. v80 source semantics were restored.
