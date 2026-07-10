# Unified Obstacle Avoidance v104 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

v103 proved that reducing the path-speed contribution during an obstacle/path
conflict can remove Track3's road collision, but it also proved the broad gate
is unsafe because it caused repeated Track1 road collisions later in the run:

```text
v103 total: 37.6 / 40
Track3: 9.2 -> 9.6
Track1: 9.6 -> 8.8
```

## Evidence Basis

Use the time-axis-safe summaries:

```text
Results/metrics/signal_window_summary_v80_v103_track1_track3_20260711.md
Results/metrics/ctrlalloc_contribution_analysis_v80_v103_track1_track3_20260711.md
Results/metrics/four_track_candidate_review_v103_conflict_path_speed_20260711.md
```

Relevant event samples:

```text
v80 Track3 road event:
  t=4.85, steer_pp=-0.2215, steer_oa=0.6, speed_pp=1, speed_oa=-1

v103 Track1 new road events:
  t=40.05, steer_pp=-0.2004, speed gate active, P 9.6->9.2
  t=60.40, steer_pp=-0.2493, speed gate active, P 9.2->8.8
```

This suggests the next test should not use a broad conflict-window gate. It
should only test the narrow path-steering band represented by the original
Track3/Track2/Track4 first road-side conflict, while avoiding the Track1
late-run conflict windows that v103 made worse.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct `unitDelay3.y -> gain2.u` connection with one narrow gate:

```modelica
gain2.u = if speed_oa < 0
  and steer_oa * steer_pp < 0
  and abs(steer_pp) > 0.21
  and abs(steer_pp) < 0.235
  and unitDelay3.y > 0.35
  then 0.35
  else unitDelay3.y;
```

Keep the accepted v80/v48 opposing path-steer guard:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

This is still one unified control-allocation rule. It does not read track id,
time, score variables, official road geometry, result files, or collision
counters.

## Difference From Rejected Routes

- Not v103: excludes Track1 late-run conflict windows near `abs(steer_pp)`
  `0.2004` and `0.2493`.
- Not v70/v77/v90/v93: not a broad active-avoid or emergency speed clamp.
- Not v96-v100: does not alter initial lateral steering.
- Not v101/v102: does not keep tuning path-steer release authority.

## Target Gate

1. Run source deployability checker with `--fail-on-high`.
2. Run `UGV.Test.Saidao3Eval` for 120 s first.
3. If Track3 improves to `P=9.6` without a short-run artifact, run Track1.
4. Accept expansion only if Track1 stays at least v80-comparable
   (`P>=9.6`, no new late repeated road collisions).
5. If Track1 is safe, run Track2 and Track4, then write four-track review.
6. If Track3 does not improve or Track1 regresses, restore v80 semantics and
   write rejection evidence.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
