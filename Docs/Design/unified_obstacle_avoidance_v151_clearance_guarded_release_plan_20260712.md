# v151 Clearance-Guarded Avoid Release Plan

Status: rejected; superseded by bounded-persistence candidate v152.

## Hypothesis

Track3 v148 and v150 both leave the road at path index 36 while lateral risk
is active. A fixed two-second avoid release can discard obstacle-side steering
before the vehicle has physically cleared the side obstacle. v151 keeps v148's
continuous front-risk and neutral side-only longitudinal command, but requires
all three measured clearances to be safe before returning to cruise.

```modelica
speed := min(0, max(-1, df - mindis));
transition(avoid, cruise,
  after(2,sec) and df > mindis and dl > 0.45 and dr > 0.45,
  reset=false);
```

This interaction differs from rejected v41: v41 combined guarded release with
the old full-reverse avoid command. v151 tests persistence under v148's neutral
side-only longitudinal authority. It remains a unified sensor-driven rule and
contains no track identifier or official-model modification.

## Gates

1. Static deployability checker and test suite pass.
2. Track3 1 s native compile/simulation gate passes.
3. Track3 must finish under the strict finish classifier before cross-track
   expansion.
4. If Track3 finishes, Track4 runs first because v41 regressed Track4; loss of
   the v148 Track4 finish rejects v151 immediately.
5. Only unchanged-source Track1/2/3/4 finishes can supersede v148.

Permanent avoid lock, increased obstacle collision count, or another road
departure rejects v151 and restores exact v148 state and speed semantics.

## Result

Track3 did not finish. The native run terminated at `T=301.3`, with `cR=33`,
`cO=6`, `P=-5.6`, and finish-distance squared `261.4286`. Requiring complete
clearance before release creates a persistent avoid lock and repeated
collisions. v151 is rejected. Clearance may permit early release, but cannot
be the sole release condition.
