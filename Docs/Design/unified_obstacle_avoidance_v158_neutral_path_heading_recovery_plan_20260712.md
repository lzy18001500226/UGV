# v158 Neutral Path-Heading Recovery Plan

Status: rejected after Track3 score/collision regression; v148 is the rollback baseline.

## Geometry Diagnosis

The saved v148 Track3 trajectory was overlaid on the official read-only
`saidao3` geometry:

- obstacle event: `t=1.00`, position `(1.216, 0.0958)`;
- road event: `t=4.10`, position `(4.147, 0.4614)`;
- the road center is `y=0` on this segment;
- at the road event `speed_oa=0`, `steer_oa=+0.6`, and the path heading is
  about `-0.2164`.

The vehicle is being held above the straight road center by a stale positive
OA heading offset after front clearance has reopened. v151/v152 show that
extending longitudinal avoid residence is unsafe. v157 attenuated the OA
filter input, but the filter state decayed too slowly and Track3 regressed.

Evidence:

- `Results/metrics/v148_track3_geometry_diagnosis_20260712.md`
- `Results/figures/v148_track3_geometry_diagnosis_20260712/v148_track3_trajectory_events.png`

## Candidate

Keep the OA filter and path branch unchanged. At the final steering sum, use a
path-side feed-forward cancellation only when the longitudinal OA command is
neutral and the OA/path headings conflict:

```modelica
add1.u1 = if speed_oa == 0
    and steer_oa * unitDelay1.y < 0
    and abs(unitDelay1.y) > 0.15
  then gain3.y - firstOrder.y
  else gain3.y;
```

Because `add1.u2=firstOrder.y`, the guarded branch makes the final desired
heading equal to the existing path command immediately. It does not alter the
initial `speed_oa<0` obstacle maneuver, does not inspect track identity, and
does not change official road, vehicle, sensor, scoring, or example source.

## Validation

1. Source tests, deployability checker, and diff checks.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s gate; only the official origin assertion is a finish.
4. A Track3 finish promotes to Track4, then Track1 and Track2 regression.
5. Any non-finish, abnormal short stop, or collision regression restores v148.

No completion, physical-car, final score, package, or submission claim is made
before the corresponding runtime evidence exists.

## Result

The 1 s gate passed. Track3 then reached `T=79.8`, path index 76, with
`cR=2`, `cO=3`, `P=8.0`, and finish-distance squared `122.2830`. The trajectory
covered substantially more of the official loop than v148, but it did not
finish and materially regressed collisions and score. v158 is rejected.

The geometry overlay shows that the first road event moved from `t=4.10` to
`t=13.80`, while the straight segment oscillated around the centerline. The
`abs(path)>0.15` gate delays recovery until after substantial lateral drift.
This supports one follow-up that removes the magnitude gate without changing
the immediate front-obstacle branch; it does not support gain scanning.

Review: `Results/metrics/track3_candidate_review_v158_neutral_path_heading_recovery_20260712.md`.
