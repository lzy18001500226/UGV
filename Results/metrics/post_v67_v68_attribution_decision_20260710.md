# Post-v67 / v68 Attribution Decision

Status: source-static/offline analysis complete, no new source edit
Date: 2026-07-10
Baseline: v48 opposing-steer guard

## Purpose

This note records the decision after the rejected v67 nearest-distance
diagnostic. The goal is to keep the long competition task moving without
repeating blind parameter scans or renaming already rejected mechanisms.

## New Offline Evidence

Generated from saved MWORKS CSV exports only; MWORKS was not rerun.

```text
Results/metrics/signal_window_summary_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/signal_window_summary_v48_all_tracks_v67_track3_post_research_20260710.json
Results/metrics/ctrlalloc_contribution_analysis_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_all_tracks_v67_track3_post_research_20260710.json
```

## Key Findings

At every current v48 score-loss event, obstacle avoidance is active
(`flag=1`) and requests braking/reverse (`speed_oa=-1`) plus positive obstacle
steer (`steer_oa=0.6`). The remaining collisions are therefore not caused by
the front/side trigger being absent.

Track3 first obstacle event:

```text
t = 1.05 s
df ~= 0.013
dl ~= 0.488
dr ~= 0.647
speed_pp = 1
speed_oa = -1
oa_speed_filtered ~= -0.280
final_speed ~= 0.720
steer_pp ~= -0.039
steer_oa = 0.6
oa_steer_filtered ~= 0.182
final_steer ~= 0.162
```

Track1/2/4 road events are different: they mostly occur with side distance
near `0.10` and with the same active avoid command. This means a single
front-trigger or steering-magnitude change is unlikely to fix both failure
types.

v67 changed the diagnostic wrapper so nearest obstacle distance feeds
`front_dist`. It made Track3 runtime clean (`exit_state=0`) but did not change
the score window (`cR=1`, `cO=1`, `P=9.2`, first obstacle event still at
`1.05 s`). Therefore nearest-distance input changes are not an accepted score
route.

## Rejected Mechanism Coverage

The most obvious next mechanism was already tested as v51:

```text
speed_oa < 0 and abs(path steer) small -> suppress path speed
```

v51 early-stopped Track3 at `T=2.25` with non-comparable readable `P=10.0`,
so this mechanism must not be retried as v68 without a materially different
source-level reason.

Other nearby routes are also exhausted by evidence:

```text
initial steering magnitude/direction scans
direct steering-filter time-constant scans
speed filter / reverse speed escalation
front emergency hold
front-clear side reentry
path-speed attenuation or straight brake arbitration
nearest-distance wrapper input changes
per-track patches
official road/vehicle/sensor/scoring/example edits
```

## Decision

Do not patch v68 immediately. The source evidence does not currently justify a
new low-risk controller mechanism inside the four-distance interface that has
not already been covered by rejected v49-v67 families.

Continue the long task through deliverable progress:

1. refresh the report/readiness surface with v67 and this attribution;
2. strengthen final-race / physical-transfer notes around the current bounded
   controller and its limitations;
3. continue targeted research only if it can produce a genuinely different
   deployable four-scalar reactive mechanism, not another scalar scan.

This is not a stop condition. It prevents unproductive controller churn while
the project advances toward a reviewable competition deliverable.

## Non-Claims

- No final optimized score is claimed.
- No final submission approval is claimed.
- No physical UGV success is claimed.
- No MWORKS runtime was opened or rerun for this note.
