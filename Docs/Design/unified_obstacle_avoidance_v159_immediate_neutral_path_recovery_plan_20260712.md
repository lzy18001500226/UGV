# v159 Immediate Neutral Path Recovery Plan

Status: rejected; exact v148 allocator semantics restored.

## Basis

v158 proves that neutral-state path recovery can extend Track3 from path index
36 to 76, but `abs(path heading)>0.15` delays correction on the straight road.
The vehicle oscillates and reaches the first road event at `t=13.80`.

## Candidate

Use the same feed-forward cancellation as v158, but remove only the magnitude
gate:

```modelica
add1.u1 = if speed_oa == 0 and steer_oa * unitDelay1.y < 0
  then gain3.y - firstOrder.y
  else gain3.y;
```

This is not a gain scan. It changes the state boundary so any directionally
valid path recovery acts as soon as front-obstacle authority is neutral. The
`speed_oa<0` initial avoidance branch remains unchanged.

## Gates

Static/tests, Track3 1 s, then strict Track3 700 s. Only an official finish
promotes to Track4, Track1, and Track2 regression. A non-finish or collision
regression restores v148 and closes immediate cancellation.

## Result

The 1 s gate passed. The strict Track3 run stopped at `T=78.7`, `cR=3`,
`cO=3`, `P=7.6`, and finish-distance squared `96.9383`. It covered much more
of the route than v148 but did not finish and regressed collisions and score
further than v158. v159 is rejected and immediate stateless cancellation is
closed.

Review: `Results/metrics/track3_candidate_review_v159_immediate_neutral_path_recovery_20260712.md`.
