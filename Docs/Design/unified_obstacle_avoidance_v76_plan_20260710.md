# Unified Obstacle Avoidance v76 Plan

Status: rejected_after_track1_runtime_regression, 2026-07-10 CST

## Goal

Continue from accepted v74 and test a narrow obstacle-controller mechanism for
the remaining early road-edge contacts. The change should be track-agnostic,
front-clear gated, and limited to the active avoid lateral initialization
window.

Current accepted best:

```text
v74 total wrapper score: 37.6
```

## Evidence Basis

Current v74 residual evidence:

```text
Results/metrics/collision_window_analysis_v74_all_tracks_20260710.md
Results/metrics/signal_window_summary_v74_all_tracks_key_events_20260710.md
```

Shared early road-edge windows:

| Track | Time/s | df | dl | dr | flag | steer_oa | P after event |
|---|---:|---:|---:|---:|---:|---:|---:|
| Track1 | 4.45 | 2.051 | 0.1012 | 0.1971 | 1 | 0.6 | 9.6 |
| Track2 | 4.70 | 2.052 | 0.1089 | 0.2710 | 1 | 0.6 | 9.6 |
| Track3 | 4.85 | 2.050 | 0.1060 | 0.2708 | 1 | 0.6 | 9.2 |
| Track4 | 4.35 | 2.052 | 0.1052 | 0.2674 | 1 | 0.6 | 9.6 |

These windows are front-clear (`df > safeF`), left-side extreme, and already in
active avoid mode. The existing lateral initialization uses fixed `steer := 0.6`.

Prior failures to avoid:

- v71 increased severe-side steering without a front-clear guard and later
  introduced a Track4 obstacle collision in a front-obstacle window.
- v75 neutralized a small opposing path contribution in allocation; it did not
  improve Track2 and regressed runtime.
- v30/v66 broad side-danger steering changes did not provide a stable score
  improvement.

## Candidate Mechanism

Allowed scope:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change the active avoid lateral initialization state from unconditional
`steer := 0.6` to:

```modelica
if df > safeF and dl < 0.14 and dl < dr then
  steer := 0.75;
else
  steer := 0.6;
end if;
```

This should affect the v74 early road-edge windows, but not Track3's first
obstacle event (`df` near zero) or v71's later obstacle-regression window.

## Validation Gate

1. Apply the smallest obstacle-controller edit.
2. Run the deployability static checker.
3. Run Track2 first because v74 Track2 is clean runtime with one early road
   event and no obstacle collision.
4. Continue only if Track2 improves or remains non-regressive without a worse
   runtime caveat.
5. If target evidence improves, run Track1, Track3, and Track4 regression.
6. Accept v76 only if four-track total exceeds v74 `37.6` and no target track
   regresses in `P/cR/cO`.

## Non-Goals

- No edits to official vehicle, road, sensor, scoring, example, or track files.
- No report/package work.
- No physical UGV claim.
- No per-track logic.
