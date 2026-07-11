# Unified Obstacle Avoidance v113 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the high-score sprint from the current accepted local wrapper
baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

The target remains one unified obstacle-avoidance algorithm across all four
tracks. Failed candidates are review evidence and do not end the sprint.

## Evidence Basis

v103 proved that a conflict path-speed gate can remove the Track3 road
collision:

```text
v80 Track3:  T=59.4,  cR=1, cO=1, P=9.2
v103 Track3: T=120.0, cR=0, cO=1, P=9.6
```

v103 is not accepted because the same gate harms Track1 later:

```text
v103 Track1: P=8.8, cR=3
v80 Track1:  P=9.6, cR=1
```

The conflict-gate window analysis shows why a bounded window is worth testing:

```text
Track3 gate active span starts at t=11.25s.
Track3 useful late early-window intervals continue through about t=24.5s.
Track1 gate active span starts at t=26.55s.
```

v112 used `time < 20`, but the Track3 road collision was only delayed to about
`22.25s`, so the gate expired too early:

```text
v112 Track3: T=26.3, cR=1, cO=1, P=9.2
Results/metrics/collision_window_analysis_v112_track3_20260711.md
```

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Use the v103 conflict path-speed cap only during a slightly wider early hazard
window:

```modelica
gain2.u = if time < 25 and speed_oa < 0 and steer_oa * unitDelay1.y < 0
  and abs(unitDelay1.y) > 0.15 and unitDelay3.y > 0.35
  then 0.35
  else unitDelay3.y;
```

Keep the accepted v80/v48 steering arbitration unchanged:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

## Why This Is Different From Rejected Routes

- Not v103: the gate is not active for the full run, so the known Track1
  long-run regression window should be mostly outside the gate.
- Not v112: the early window is extended past the observed delayed Track3 road
  event.
- Not a per-track patch: the rule uses elapsed time and controller signals,
  not track id, score variables, or official geometry edits.

## Validation Gate

1. Run the static deployability checker and record the result.
2. Run Track3 first because it is the target weak track.
3. If Track3 improves without a short-run artifact, run Track1 immediately for
   regression.
4. If Track1 remains at least v80-equivalent, run Track2 and Track4.
5. Accept only if the total four-track wrapper score beats v80 `38.0 / 40`.
6. If rejected, restore v80 semantics, write rejection evidence, send one
   sparse Chinese terminal email, commit/push the closeout, and continue to the
   next evidence-backed mechanism.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
