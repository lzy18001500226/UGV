# Unified Obstacle Avoidance v105 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

v103 and v104 showed that conflict-window path-speed gates can help Track3
road contact but are not a safe next mechanism. v103 regressed Track1, and
v104 regressed Track3 directly.

## Evidence Basis

Track3 still has an early front-obstacle collision:

```text
Results/metrics/signal_window_summary_v80_track3_pose_path_6s_20260710.md

t=1.05
df=0.01324
speed_oa=-1
steer_oa=0.6
speed_pp=1
steer_pp=-0.03857
final_speed=0.7196
final_steer=0.1623
cO: 0 -> 1
P: 10.0 -> 9.6
```

Rejected lessons:

- v47 startup speed cap at `0.75` did not remove the obstacle collision.
- v92/v93/v95 stronger emergency reverse/brake routes either kept the penalty,
  added penalties, shortened runtime, or created early-stop artifacts.
- v103/v104 conflict speed gates target later path/obstacle conflicts and are
  not a safe front-obstacle solution.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct `unitDelay3.y -> gain2.u` connection with a bounded
front-aligned obstacle approach cap:

```modelica
gain2.u = if speed_oa < 0
  and steer_oa > 0.4
  and abs(steer_pp) < 0.12
  and unitDelay3.y > 0.55
  then 0.55
  else unitDelay3.y;
```

This caps only the path-speed contribution during straight-ahead obstacle
approach while preserving the existing obstacle speed contribution and keeping
the final speed positive/comparable. It is not reverse dominance and not a
track-specific branch.

Keep the accepted v80/v48 opposing path-steer guard:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

## Difference From Rejected Routes

- Not v47: active only when obstacle avoidance is already braking/steering, and
  caps the delayed path-speed contribution to `0.55`, not a broad startup cap.
- Not v92/v93/v95: no strong reverse, no path-speed suppression to zero, no
  emergency negative-speed dominance.
- Not v103/v104: avoids path/obstacle conflict windows by requiring
  `abs(steer_pp)<0.12`, so early road-side events with `abs(steer_pp)` around
  `0.22` are outside the intended gate.

## Target Gate

1. Run source deployability checker with `--fail-on-high`.
2. Run `UGV.Test.Saidao3Eval` for 120 s first.
3. Accept expansion only if Track3 improves over v80 without a short-run
   artifact:
   - target: `cO` drops from `1` to `0`, or `P` improves from `9.2`;
   - reject if runtime shortens severely or new penalties appear.
4. If Track3 improves, run Track1 next because Track1 is the main regression
   guard after v103/v96.
5. If Track1 is safe, run Track2 and Track4, then write four-track review.
6. If Track3 does not improve or regresses, restore v80 semantics and write
   rejection evidence.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
