# Track2 v191 Brake-Then-Steer Handoff Review

## Verdict

Rejected and rolled back. v191 increased runtime and route progress, but it did
not satisfy the official completion predicate and materially increased
collisions.

## Baseline Reproduction

Current exact `HEAD` on Track2:

```text
T=28.55
cR=1
cO=0
P=9.6
finish_distance_squared=791.4782768388438
termination=unclassified_early_termination
```

Evidence: `Results/simulations/baseline_head_track2_700s_20260712/`.

## Candidate

- `mindis=1.5` for earlier front-risk speed response.
- OA steering admitted by the allocator only while `speed_oa<0`.
- Same rule for every track; no track/time/score/position branch.
- Official vehicle, road, sensor, scoring, and track files unchanged.

## Gates And Result

- Static deployability: `high=0`, `medium=0`.
- Tests: `14 passed`.
- Track2 1 s native gate: passed, `T=1,cR=0,cO=0,P=10`.
- Track2 strict 700 s: rejected.

```text
T=87.4
cR=3
cO=4
P=7.2
finish_distance_squared=332.56125186253496
termination=unclassified_early_termination
```

The increased progress is not a finish and comes with seven collisions. Do not
expand v191 to the other tracks and do not retain its source changes.

## Decision

Restore controller and allocator to exact `HEAD` bytes. Close the family that
combines a larger front threshold with OA-steer admission based only on the OA
speed sign. The next candidate needs a better collision-imminence or local-path
interface, not another threshold or allocator-sign scan.
