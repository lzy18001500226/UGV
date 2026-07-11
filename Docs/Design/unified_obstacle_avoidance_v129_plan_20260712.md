# Unified obstacle avoidance v129 plan

## Goal

Preserve v128's straight-line anti-crawl effect without forcing the same speed
floor through sharp path turns. The rule is unified across all four tracks and
does not inspect a track id.

## Candidate

When obstacle avoidance requests negative speed, clamp its contribution so the
combined forward-speed floor becomes:

```text
0.2 / (1 + abs(delayed_path_steer))
```

The floor is near `0.2` on straight segments and falls continuously as path
curvature demand rises. Positive obstacle-speed behavior and steering
arbitration remain unchanged.

## Gates

1. Model check and 1 s Track2 runtime gate.
2. Track2 fixed-solver 180 s comparison with path, speed, steering, and score
   variables exported.
3. Accept only if official finish is observed or path progress improves without
   a new collision; otherwise restore the committed v80 source exactly.
4. A passing Track2 candidate must still run all four tracks unchanged before
   it can replace the baseline.

## Runtime result

The 1 s gate passed. The 180 s fixed-solver Track2 run reached the requested
horizon with `exit_state=0`, but ended with `cR=1`, `cO=0`, `P=9.6`,
`closest_index=27`, and no official finish. Curvature scaling prevented the
v128 early stop but did not remove the road collision. v129 is rejected and
the committed v80 source is restored exactly.

The next candidate should address why the obstacle state remains in negative
speed while path steering continues to demand a sharp turn. Further speed-floor
parameter scans are not justified by this batch.
