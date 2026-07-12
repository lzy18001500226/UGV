# v160 Stateful Path-Recovery Arbitration Plan

Status: rejected; exact v148 allocator semantics restored.

## Evidence Basis

v158/v159 prove two facts:

1. neutral-state path recovery extends Track3 from path index 36 to about 76;
2. stateless on/off cancellation produces oscillation and extra collisions.

The next mechanism therefore needs state continuity, not another threshold or
gain scan.

## Candidate

Add one bounded first-order recovery-weight state to `CtrlAlloc`:

```modelica
Modelica.Blocks.Continuous.FirstOrder pathRecoveryWeight(T=1, y_start=0);

pathRecoveryWeight.u = if speed_oa == 0
    and steer_oa * unitDelay1.y < 0
  then 1
  else 0;

add1.u1 = gain3.y -
  (if speed_oa < 0 then 0 else pathRecoveryWeight.y) * firstOrder.y;
```

The one-second time constant matches the existing OA steering filter, so the
arbitration transition has the same physical time scale as the signal it
cancels. Recovery enters and leaves continuously during neutral/cruise
transitions. A new front-obstacle command (`speed_oa<0`) bypasses the recovery
weight immediately, preserving full obstacle authority.

The rule is unified and uses only existing controller signals. It does not
inspect track identity or modify official vehicle, road, sensor, scoring, or
example source.

## Gates

1. Static deployability checker, source tests, and diff checks.
2. Track3 1 s native gate.
3. Strict Track3 700 s official-finish gate with trajectory signals.
4. Only a Track3 finish promotes to Track4, Track1, and Track2 regression.
5. Any non-finish, score regression, or unsafe collision growth restores v148.

No final score, physical-car, package, or submission claim is authorized by
this plan.

## Result

The 1 s gate passed and exported the new state variable. The strict Track3 run
stopped at `T=18.75`, `cR=1`, `cO=1`, `P=9.2`, and finish-distance squared
`298.1579`. It ended earlier than v148 and did not reproduce v158's path
progress. The one-second recovery-weight state enters too slowly to correct
the straight-road drift and adds no score benefit.

v160 is rejected and the added state block is removed. Do not scan its time
constant. Future state continuity must be designed where side-clearance
geometry is available, rather than layering another allocator filter.

Review: `Results/metrics/track3_candidate_review_v160_stateful_path_recovery_20260712.md`.
