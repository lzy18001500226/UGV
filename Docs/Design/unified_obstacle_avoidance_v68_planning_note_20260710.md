# Unified Obstacle Avoidance v68 Planning Note

Status: planning / decision note, no source edit yet
baseline: v48 opposing-steer guard

## Why v68 Is Not A Direct Controller Patch Yet

The latest rejected routes eliminated the obvious low-risk scans:

| Route | Lesson |
|---|---|
| v58/v62/v66 initial bypass direction or magnitude | Does not remove the first Track3 obstacle event and can add collisions. |
| v41 guarded avoid release | Confirms avoid-reset chatter exists, but holding avoid broadly adds Track4 obstacle collisions. |
| v51 path-speed brake arbitration | Can create non-comparable early-stop score inflation. |
| v65 front emergency hold | Reduces allocated speed and delays the first Track3 obstacle event, but still keeps `cR=1`, `cO=1`, `P=9.2`. |
| v67 nearest-distance diagnostic | Cleans runtime state but keeps Track3 `cR=1`, `cO=1`, `P=9.2`. |

Therefore v68 should not start by changing a scalar, threshold, direction, or
release dwell. The next source edit needs one more attribution step.

## Evidence Basis

Track3 v48 event evidence:

```text
Results/metrics/trajectory_geometry_review_v48_20260710.md
Results/metrics/signal_geometry_window_summary_v48_20260710.md
Results/metrics/track3_candidate_review_v67_nearest_distance_input_diagnostic_20260710.md
References/research/four_direction_reactive_obstacle_avoidance_20260710/source_notes.md
```

At the first Track3 obstacle event:

```text
t = 1.05 s
pathPlanner.target_v = 1
pathPlanner.steering_angle ~= -0.03857
obsAvoidController_Sysblock.chart.speed = -1
obsAvoidController_Sysblock.chart.steer = 0.6
ctrlAlloc.speed ~= 0.7196
ctrlAlloc.steer ~= 0.1623
```

Interpretation:

```text
avoidance is active, but the final allocated command still keeps substantial
forward speed and modest steering during the early collision window.
```

## v68 Diagnostic Goal

Before changing source, run or compute a targeted allocation/trajectory
attribution that answers:

1. How much final steering is lost through ControlAllocate filtering and path
   opposition at `0.8-1.2 s` and `4.5-4.9 s`?
2. Is the limiting factor steering authority, forward speed, or a geometry
   path that drives through the obstacle before the overlay can respond?
3. Is there a narrow deployable rule that does not repeat v51/v65 early-stop
   failure or v41 avoid-hold regression?

## Candidate Families Still Allowed

Allowed after diagnostic evidence:

| Family | Condition |
|---|---|
| Narrow steering-authority arbitration | Only if analysis shows v48 loses obstacle steering specifically through allocation/filtering at the first Track3 event, and the rule is not a simple global filter-time or gain scan. |
| Path/trajectory speed schedule | Only if it uses current path/steering evidence and avoids v51/v49 broad path-speed attenuation. |
| Report/physical-transfer consolidation | If diagnostic evidence shows the four-distance boundary is exhausted without changing official interfaces. |

Not allowed without a new mechanism reason:

```text
initial steering magnitude/direction scans
nearest-distance wrapper input changes
avoid-release/longer-dwell guards
path-speed attenuation/brake scans
emergency reverse-speed scans
per-track branches
official road/vehicle/sensor/scoring/example edits
```

## Next Step

Run a source/static allocation attribution over saved v48/v67 timeseries before
any v68 source edit. If that attribution does not identify a narrow source
mechanism, switch to report/readiness/physical-transfer work rather than
pretending another blind controller attempt is justified.

## Post-v67 Attribution Result

The attribution step was completed with saved CSV exports only:

```text
Results/metrics/signal_window_summary_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/post_v67_v68_attribution_decision_20260710.md
```

Decision: do not patch v68 immediately. The apparent next source mechanism,
straight-line risk speed arbitration in `ControlAllocate`, was already covered
by rejected v51 and produced a non-comparable early stop. v67 also showed that
nearest-distance wrapper input changes clean the runtime state but do not
improve Track3 score. Continue through report/readiness and physical-transfer
deliverables until a genuinely different deployable four-scalar mechanism is
identified.
