# v155 Extreme Same-Sign OA Suppression Plan

Status: rejected; threshold activated too broadly and caused repeated looping.

## Evidence Basis

The final v148 Track3 window reaches path steering `1.734 rad` while
side-only obstacle avoidance contributes another `+0.6 rad` before its 0.3
gain/filter, producing final steering `2.031 rad`. Track3 then leaves the road
at path index 36. A global path clamp was already rejected by v79, and v149's
all-phase same-sign OA suppression terminated earlier because it also removed
avoidance authority during moderate path steering.

## Candidate

Suppress only the additional obstacle offset when all of these are true:

1. side-only avoidance is active (`speed_oa == 0`);
2. delayed path steering is already extreme (`abs(path) > 1.0 rad`);
3. path and obstacle commands have the same sign.

```modelica
firstOrder.u = if speed_oa == 0
    and abs(unitDelay1.y) > 1.0
    and steer_oa * unitDelay1.y > 0
  then 0
  else gain.y;
```

This keeps initial and moderate-turn obstacle authority, preserves opposite
sign correction, and removes only redundant same-sign addition after the path
planner already commands a sharp turn. It is one track-independent allocator
rule and does not modify official road, vehicle, sensor, scoring, or example
models.

## Gates

1. Static deployability checker and tests pass.
2. Track3 1 s native gate passes.
3. Track3 700 s must meet the strict finish classifier before regression.
4. A strict Track3 finish promotes first to Track4, then Tracks 1 and 2.
5. Any non-finish or loss of a v148 finish rejects v155 and restores direct
   `connect(gain.y, firstOrder.u)` semantics.

No horizon-only run is a finish, and no wrapper value is an `80/80` claim.

## Result

Track3 terminated at `T=209.35`, `cR=7`, `cO=6`, `P=4.8`, and
finish-distance squared `304.6513`. The final five-second window remained
between path indices 11 and 29, proving repeated early-route looping rather
than completion progress. The `1.0 rad` threshold suppresses obstacle steering
too broadly. v155 is rejected. One final evidence-bounded narrowing to
`1.5 rad` is tested as v156 because v148's terminal path command is
`1.734 rad`; failure closes this suppression family.
