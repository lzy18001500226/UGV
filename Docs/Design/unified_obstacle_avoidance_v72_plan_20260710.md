# v72 Narrow Opposing Path Authority Plan

Status: planned candidate, 2026-07-10 CST.

## Goal

Keep v48 as the accepted baseline, learn from the v71 Track1 gain, and avoid
the v71 Track4 regression. The next test should not expand model interfaces or
add a per-track branch.

## Evidence Basis

v71 severe-left steering authority produced mixed evidence:

```text
Track1: v48 P=9.2, cR=2 -> v71 P=9.6, cR=1
Track4: v48 P=9.2, cR=2, cO=0 -> v71 P=8.8, cR=2, cO=1
```

Evidence:

```text
Results/simulations/controller_v71_severe_left_steer_authority_saidao1_120s_20260710/
Results/simulations/controller_v71_severe_left_steer_authority_saidao4_120s_20260710/
Results/metrics/collision_window_analysis_v48_v71_track1_track4_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v71_track1_track4_20260710.md
Results/metrics/signal_window_summary_v48_v71_track1_track4_20260710.md
```

Conclusion:

- Severe-side steering authority can remove the second Track1 road collision.
- Implementing it inside the obstacle controller changes later Track4 behavior
  and introduces an obstacle collision.
- `ControlAllocate` currently has no `dl/dr` inputs, so a direct side-distance
  gate there would require an interface expansion. Avoid that risk for this
  candidate.

## Candidate Mechanism

v48 already attenuates path steering to `0.5` when obstacle avoidance is
reversing and path steering opposes obstacle steering:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

v53 proved that removing path authority completely is too broad. v54 proved
that a global `0.35` opposing-path scalar does not help Track3.

v72 tests a narrower condition derived from the Track1 cancellation window:

```modelica
gain3.u = if speed_oa < 0
  and steer_oa > 0
  and unitDelay1.y < -0.6
then 0.25 * unitDelay1.y
else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
then 0.5 * unitDelay1.y
else unitDelay1.y;
```

This targets the saved Track1 event at `t=30.35`, where `steer_oa=0.6` and
`steer_pp=-0.6906` almost cancel. It should not affect Track4's high positive
path-steer event near `t=90.15` because `unitDelay1.y` is positive there.

## Validation Plan

1. Restore v48 obstacle-controller semantics after v71.
2. Apply v72 only to `Models/UGV/Control/ControlAllocate/package.mo`.
3. Run static deployability checker.
4. Run Track1 first:
   `UGV.Test.Saidao1Eval`, stopTime `120`.
5. Accept target expansion only if Track1 keeps or improves v71's gain over v48
   without early-stop artifact.
6. Then run Track4 regression. If Track4 avoids the v71 obstacle regression,
   run four-track regression.
7. If v72 fails, restore v48 `ControlAllocate` semantics and record rejection.

## Acceptance

v72 can supersede v48 only if the four-track total improves and no target
track regresses in `P/cR/cO`. A Track1-only gain is not enough if Track4 loses
more score.

## Non-Goals

- No official hard no-edit zone changes.
- No `dl/dr` interface expansion in this candidate.
- No report/package work during the score sprint.
- No final competition or physical UGV claim.
