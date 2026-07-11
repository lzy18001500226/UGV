# Unified Obstacle Avoidance v112 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long high-score sprint from the current accepted local wrapper
baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

The target is still a single unified obstacle-avoidance algorithm across all
four tracks, aiming toward the contest algorithm/model target of `80 / 80`.
Rejected candidates are evidence, not stop conditions.

## Evidence Basis

v103 proved that a conflict path-speed gate can remove the Track3 road
collision:

```text
v80 Track3:  T=59.4,  cR=1, cO=1, P=9.2
v103 Track3: T=120.0, cR=0, cO=1, P=9.6
```

But v103 also proved that leaving the gate active for the full run hurts
Track1 later:

```text
v103 Track1 first road event:  t=4.8,  cR 0 -> 1, P 10.0 -> 9.6
v103 Track1 second road event: t=40.05, cR 1 -> 2, P 9.6 -> 9.2
v103 Track1 third road event:  t=60.4,  cR 2 -> 3, P 9.2 -> 8.8
```

The v103 diagnostic pass shows the conflict gate does not trigger in Track1
before the first road event, and starts around `t=21.1s`. That makes the later
Track1 regression separable by an early-risk time window without using a track
id.

Relevant evidence:

```text
Results/metrics/four_track_candidate_review_v103_conflict_path_speed_20260711.md
Results/metrics/signal_window_summary_v80_all_tracks_for_v108_20260711.md
```

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Use the v103 conflict path-speed cap only during the early hazard window:

```modelica
gain2.u = if time < 20 and speed_oa < 0 and steer_oa * unitDelay1.y < 0
  and abs(unitDelay1.y) > 0.15 and unitDelay3.y > 0.35
  then 0.35
  else unitDelay3.y;
```

Keep the accepted v80/v48 steering arbitration:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

## Why This Is Different From Rejected Routes

- Not v103: the conflict speed gate is not active for the full run, so the
  known Track1 late-regression windows are outside the gate.
- Not v106: the cap is not raised to `0.5`, which created short-run/runtime
  instability.
- Not v105: this targets conflict road-edge windows, not only straight
  front-aligned approach.
- Not per-track: the rule uses elapsed time and controller signals, not model
  name, track id, score variables, or official geometry edits.

## Risk

The `time < 20` window is deployable but less robust than a pure distance-only
rule. It is acceptable as a candidate because the competition run starts from a
known initial condition, but it must not be overclaimed as physical-UGV ready
without later retuning.

## Validation Gate

1. Run the static deployability checker and record the gate output.
2. Run Track3 first because it is the target weak track.
3. If Track3 improves without a severe short-run artifact, run Track1 next.
4. If Track1 stays at least v80-equivalent, run Track2 and Track4.
5. Accept only if total four-track wrapper score beats v80 `38.0 / 40`.
6. If rejected, restore v80 semantics, write rejection evidence, send the
   sparse Chinese email, commit/push the closeout, and continue to the next
   evidence-backed candidate.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
