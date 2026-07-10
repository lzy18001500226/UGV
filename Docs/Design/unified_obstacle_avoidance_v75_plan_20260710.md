# Unified Obstacle Avoidance v75 Plan

Status: rejected_after_track2_regression, 2026-07-10 CST

## Goal

Continue from accepted v74 and test a narrow allocation-layer mechanism for the
remaining early road-edge contacts. The target is not a broad path-authority
scan; it is a small branch derived from v74 event windows.

Current accepted best:

```text
v74 total wrapper score: 37.6
```

## Evidence Basis

v74 residual collision evidence:

```text
Results/metrics/collision_window_analysis_v74_all_tracks_20260710.md
Results/metrics/signal_window_summary_v74_all_tracks_key_events_20260710.md
```

Observed early road-edge events:

| Track | Time/s | steer_oa | steer_pp | final_steer | dl | dr | P after event |
|---|---:|---:|---:|---:|---:|---:|---:|
| Track2 | 4.70 | 0.6 | -0.2205 | 0.1816 | 0.1089 | 0.2710 | 9.6 |
| Track3 | 4.85 | 0.6 | -0.2215 | 0.1849 | 0.1060 | 0.2708 | 9.2 |
| Track4 | 4.35 | 0.6 | -0.2222 | 0.1796 | 0.1052 | 0.2674 | 9.6 |

Common signal: active obstacle avoidance requests right steering, while a small
negative path-planner steering contribution partially cancels it. v48's broad
opposing-steer guard halves the path contribution, but still leaves enough
cancellation to keep final steering around `0.18`.

Prior failures to avoid:

- v53 full path-steer neutralization was too broad and regressed Track1.
- v54 global `0.35` opposing-path scalar did not improve Track3.
- v72 targeted large negative path steering below `-0.6`; v74's remaining
  early road-edge events are around `-0.22`, not that window.

## Candidate Mechanism

Allowed scope:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

When obstacle avoidance is reversing, requests right steering, and path
steering is a small-to-moderate opposing left command, neutralize only that
path contribution:

```modelica
gain3.u = if speed_oa < 0 and steer_oa > 0
  and unitDelay1.y < -0.15 and unitDelay1.y > -0.35
then 0
else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
then 0.5 * unitDelay1.y
else unitDelay1.y;
```

This branch should affect the v74 early Track2/3/4 road-edge windows, but not
Track3's first obstacle event (`steer_pp` near `-0.04`), v72's large negative
path window, or Track4's late large positive path-steer event.

## Validation Gate

1. Apply the smallest `ControlAllocate` edit.
2. Run the deployability static checker.
3. Run Track2 first because v74 Track2 has exactly one early road event and no
   obstacle collision.
4. Continue to Track3 and Track4 only if Track2 improves or does not regress.
5. Run Track1 regression before accepting because v53 showed broad path
   authority changes can regress Track1.
6. Accept v75 only if four-track total exceeds v74 `37.6` without introducing
   a worse runtime caveat.

## Result

v75 is rejected after the Track2 target gate:

```text
v74 Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true / exit_state=0
v75 Track2: T=8.7, cR=1, cO=0, P=9.6, simulate_failed / exit_state=2
```

Review:

```text
Results/metrics/track2_candidate_review_v75_moderate_opposing_path_neutralization_20260710.md
```

Decision: reject v75 because it does not improve Track2 score/collisions and
introduces a worse runtime caveat. Do not expand this branch to Track1/3/4.
Source semantics were restored to v74.

## Non-Goals

- No edits to official vehicle, road, sensor, scoring, example, or track files.
- No report/package work.
- No physical UGV claim.
- No per-track logic.
