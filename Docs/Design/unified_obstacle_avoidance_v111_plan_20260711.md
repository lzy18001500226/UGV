# Unified Obstacle Avoidance v111 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
effective contest target: about 76 / 80
```

The immediate target is Track3's first obstacle collision while preserving
Track1, because v103-style conflict speed gates improved Track3 road behavior
but regressed Track1.

## Evidence Basis

Use time-axis-safe summaries only:

```text
Results/metrics/signal_window_summary_v80_v105_track3_20260711.md
Results/metrics/ctrlalloc_contribution_analysis_v80_v105_track3_20260711.md
Results/metrics/four_track_candidate_review_v103_conflict_path_speed_20260711.md
Results/metrics/track3_candidate_review_v107_front_aligned_approach_cap035_20260711.md
```

v105 showed that a front-aligned approach speed cap is physically relevant:

```text
v80 Track3 first obstacle:  t=1.05, final_speed=0.7196, P 10.0 -> 9.6
v105 Track3 first obstacle: t=1.60, final_speed=0.1767, P 10.0 -> 9.6
```

It delayed both Track3 penalties but did not remove them. v107 tested a much
stronger `0.35` cap but produced no readable score evidence because the wrapper
timed out. v111 therefore tests a bounded middle cap that is stronger than
v105 and less aggressive than v107.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Change the path-speed contribution entering `gain2`:

```modelica
gain2.u = if speed_oa < 0 and steer_oa > 0.4 and abs(unitDelay1.y) < 0.12 and unitDelay3.y > 0.45
  then 0.45
  else unitDelay3.y;
```

Keep the accepted v80/v48 opposing path-steer guard:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

This is one unified controller-allocation rule. It does not inspect track id,
model name, time, score variables, official geometry, or result files.

## Difference From Rejected Routes

- Not v103/v106: no conflict-window path-speed gate; it avoids the Track1
  road-edge regression family.
- Not v107: cap is `0.45`, not `0.35`, to reduce timeout/early-stop risk.
- Not v92/v93/v95: no stronger reverse-speed dominance or zero speed
  suppression.
- Not v96-v100: no initial lateral steering sign or magnitude override.

## Target Gate

1. Run the controller deployability checker.
2. Run `UGV.Test.Saidao3Eval` for 120 s first.
3. Accept expansion only if Track3 improves over v80 without a short-run
   artifact:
   - target: `cO` drops from `1` to `0`, or `P` improves beyond `9.2`;
   - reject if runtime shortens severely, score is unchanged, or new penalties
     appear.
4. If Track3 improves, run Track1 regression immediately.
5. If Track1 is safe, run Track2 and Track4, then write a four-track review.
6. If Track3 does not improve or the wrapper blocks, restore v80 semantics,
   write rejection evidence, send a sparse email notice, commit, and continue
   the long score sprint with a different mechanism family.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package readiness claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
