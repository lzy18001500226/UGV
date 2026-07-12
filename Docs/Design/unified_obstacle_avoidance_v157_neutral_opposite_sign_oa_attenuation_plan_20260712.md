# v157 Neutral Opposite-Sign OA Attenuation Plan

Status: rejected; exact v148 allocator semantics restored.

## Evidence Basis

v148 makes side-only obstacle states longitudinally neutral. In Track3, the
first obstacle event still has active reverse authority and must retain the
full avoidance command. At the later road event, however, front clearance is
open (`speed_oa=0`), the path requests a meaningful negative heading, and the
positive lateral avoidance offset reverses that correction.

Earlier v94/v119 candidates acted during `speed_oa<0` and terminated at
`T=2.4`; they did not test v148's neutral side-only state. v155/v156 instead
suppressed same-sign OA at large path headings and did not finish.

## Candidate

Modify only `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
firstOrder.u = if speed_oa == 0
    and steer_oa * unitDelay1.y < 0
    and abs(unitDelay1.y) > 0.15
  then 0.35 * gain.y
  else gain.y;
```

The `0.15` meaningful-path threshold and `0.35` bounded attenuation come from
the previously documented v94 conflict branch. The structural difference is
the neutral `speed_oa==0` gate introduced by v148: initial front-obstacle
authority remains unchanged.

## Validation

1. Run source tests, deployability checker, and diff checks.
2. Run Track3 for 1 s to prove translation and initial simulation.
3. Run strict Track3 for 700 s; only the official origin assertion is a finish.
4. Promote only a verified finish to Track4, then Track1 and Track2 regression.
5. Reject and restore v148 on non-finish, abnormal stop, or collision regression.

No per-track branch, official no-edit source change, completion claim, physical
vehicle claim, report packaging, or submission action is authorized by this
plan.

## Result

The 1 s gate passed. The strict Track3 run then stopped abnormally at
`T=20.40`, `cR=1`, `cO=1`, `P=9.2`, and finish-distance squared `305.6024`.
This is slightly worse than v148's `T=21.10` and does not finish. v157 is
rejected, direct OA connection semantics are restored, and this scalar
attenuation direction is closed.

Review: `Results/metrics/track3_candidate_review_v157_neutral_opposite_sign_oa_attenuation_20260712.md`.
