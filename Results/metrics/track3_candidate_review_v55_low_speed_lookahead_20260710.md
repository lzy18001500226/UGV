# Track3 Candidate Review - v55 Low-Speed Lookahead

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
candidate: v55 low-speed lookahead floor
decision: rejected

## Candidate Change

File changed:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Added parameters and low-speed lookahead floor:

```modelica
parameter Real low_speed_lookahead_trigger = 0.6;
parameter SIunits.Length low_speed_lookahead_floor = 4.0;

lookahead_dist := lookahead_base + lookahead_gain * v;
if v < low_speed_lookahead_trigger and lookahead_dist < low_speed_lookahead_floor then
  lookahead_dist := low_speed_lookahead_floor;
end if;
```

The mechanism was intended to reduce low-speed path-angle opposition during
obstacle avoidance without changing official tracks, scoring, or per-track
branches.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v55_low_speed_lookahead_20260710.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Evidence

Track3 target run:

```text
Results/simulations/controller_v55_low_speed_lookahead_saidao3_120s_20260710/
```

Recorded result variables:

| Candidate | Track | T | cR | cO | P | Runtime |
|---|---|---:|---:|---:|---:|---|
| v48 baseline | Saidao3Eval | 112.45 | 1 | 1 | 9.2 | simulate_failed with result variables |
| v55 | Saidao3Eval | 27.55 | 1 | 1 | 9.2 | simulate_failed with result variables |

## Decision

Reject v55. It did not improve Track3 score or collision count and shortened
the readable run from v48 `T=112.45` to `T=27.55`. Because the target weak
track regressed, v55 should not be expanded to Track1 or four-track regression.

## Follow-Up Direction

Restore v48 semantics. The next candidate should not continue low-speed
lookahead-floor scanning. It should instead inspect whether the Track3 failure
is better addressed by a bounded front-risk state or by improving the
obstacle-controller release/side decision using fresh evidence, while keeping a
single unified algorithm for all tracks.
