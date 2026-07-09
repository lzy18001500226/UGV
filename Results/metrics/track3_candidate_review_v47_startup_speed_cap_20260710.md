# Track3 Candidate Review: v47 Startup Speed Cap

Status: rejected_no_target_improvement, 2026-07-10 CST

## Candidate

v47 keeps the accepted v45 curvature speed cap and adds one unified startup
speed cap in `PathPlanner`:

```modelica
parameter Real startup_slow_time = 2.0;
parameter Real startup_slow_speed = 0.75;

if time < startup_slow_time and target_v > startup_slow_speed then
  target_v := startup_slow_speed;
end if;
```

This is one track-agnostic startup safety mechanism. It does not add per-track
logic and does not modify official vehicle, road, sensor, scoring, example, or
track files.

## Target Track Evidence

Target run:

```text
Results/simulations/controller_v47_startup_speed_cap_saidao3_120s_20260710/
```

Track3 result:

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v45 | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |
| v47 | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |

Collision-window analysis:

```text
Results/metrics/collision_window_analysis_v47_startup_speed_cap_track3_20260710.md
```

## Decision

Reject v47. It preserves runtime comparability but does not improve Track3
score, road collision count, or obstacle collision count compared with v45.
Do not continue this candidate to four-track regression.

Restore accepted v45 source semantics before the next candidate.

## Lesson

Track3's first obstacle contact is not solved by a simple two-second startup
target-speed cap at `0.75`. The next mechanism should inspect trajectory or
steering authority around the first obstacle rather than only reducing the
early path target speed.
