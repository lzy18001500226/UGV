# Four-Direction Reactive Obstacle Avoidance - Source Notes

timestamp: 2026-07-10 CST
baseline context: v48 is current accepted wrapper baseline; v67 rejected nearest-distance wrapper input as a score route

## What Transfers

### Follow the Gap / Disparity Extender

FTG normally uses a dense LiDAR scan:

```text
range preprocessing
  -> find closest obstacle
  -> create safety bubble
  -> find largest safe gap
  -> steer to best point in that gap
```

Current UGV does not have a scan array inside the controller. The transferable
part is therefore not "largest gap over LiDAR"; it is:

```text
front risk + side clearance imbalance -> choose a conservative gap proxy
```

Disparity Extender's useful lesson is obstacle inflation: a single close range
should affect neighboring steering choices. In the UGV controller, this maps to
using `min(dl, dr)` and `abs(dl - dr)` together, rather than reacting to `df`
alone.

### Bug / Wall Following

Bug methods switch between:

```text
go-to-goal
boundary-follow
leave-boundary
```

This matches the official UGV architecture better than DWA/TEB because the
existing path planner already supplies the go-to-goal/path-following command.
The obstacle controller should act as a boundary-following safety overlay, not
as a full planner.

The risk is that pure wall following can get stuck or over-follow boundaries.
That means any UGV wall-follow mechanism must be short, bounded, and gated by
the same four-track score evidence.

### Ultrasonic PID Wall Following

Small physical robots often use a side-distance error:

```text
e = desired_side_distance - measured_side_distance
steer = Kp * e + Kd * de/dt
```

The official controller has only the current scalar distances, and adding
stateful derivative variables inside Sysblock risks syntax/runtime churn. The
low-risk transfer is proportional centerline correction:

```text
side_center_error = dr - dl
steer_correction = bounded_gain * side_center_error
```

Previous candidates already showed that raw side steering can regress. A future
candidate must therefore combine center correction with mode/hysteresis and
speed limiting, rather than changing one scalar alone.

## What Does Not Transfer

Do not implement these as the next step:

| Pattern | Reason |
|---|---|
| Full FTG over LiDAR scan | The controller has four scalar distances, not a scan. |
| DWA / TEB local planning | Needs pose, velocity model, obstacle map, and optimizer/costmap not present in the official controller boundary. |
| Potential field over map/grid | No obstacle coordinates or map inside the controller. |
| Learned policy | High risk for physical transfer, hard to justify from official evidence, and unnecessary before the reactive baseline is exhausted. |
| Per-track trajectory hacks | User requires one algorithm for all four tracks. |

## New Evidence From v67

v67 connected `distanceSensor1.DisObstacle` into controller `front_dist` in a
diagnostic wrapper. It changed runtime health but not score:

```text
Track3: T=120.0, cR=1, cO=1, P=9.2
first obstacle event: still 1.05 s
road event: 4.5 s
```

This means the next useful change should not just expose a different front
distance. It must change how the controller holds and releases the safety
overlay.

## v68 Mechanism Direction

The source and signal evidence show a repeated pattern:

```text
longitudinal avoid releases after 2 s
flag can drop and re-enter while risk persists
lateral avoid repeatedly starts from fixed initial steering
chart.steer remains 0.6 at key Track3 collision windows
```

A direct repeat of v58/v62/v66 is not acceptable. Those tested initial bypass
direction/magnitude and failed. v41 also already tested broad guarded avoid
release and regressed Track4 by adding obstacle collisions. Therefore the next
mechanism must not simply "hold avoid longer" or repeat the v41 guard.

The remaining useful direction is a narrower trajectory/controller interaction
diagnostic:

```text
identify whether path-following target speed/lookahead/steering authority is
placing the vehicle into the early Track3 obstacle and road windows before the
reactive overlay can change the trajectory
```

Candidate design requirements:

1. One unified condition over `df`, `dl`, and `dr`; no track id or wrapper
   branch.
2. Do not edit official vehicle/road/sensor/scoring/example files.
3. Avoid repeating v41's broad guarded-release regression.
4. Preserve v48 path-speed regulation and opposing-steer guard.
5. Track3 target run first; expand to all four tracks only if Track3 improves
   without early-stop artifacts.

Initial hypothesis for a future design note:

```text
test a small path-level lookahead/speed interaction change that reduces early
Track3 risk exposure while preserving v48's accepted ControlAllocate and
obstacle-controller semantics
```

This is still a hypothesis. It needs a v68 plan before any controller edit.
