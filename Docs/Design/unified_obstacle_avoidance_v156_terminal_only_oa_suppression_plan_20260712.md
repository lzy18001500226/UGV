# v156 Terminal-Only OA Suppression Plan

Status: rejected; exact v148 allocator semantics restored.

v155's `1.0 rad` trigger causes repeated early-route looping. v156 raises the
trigger to `1.5 rad`, below v148's terminal path steering of `1.734 rad` but
above most of v155's earlier route. The other gates remain unchanged:

```modelica
firstOrder.u = if speed_oa == 0
    and abs(unitDelay1.y) > 1.5
    and steer_oa * unitDelay1.y > 0
  then 0
  else gain.y;
```

This was the final test in the same-sign OA suppression family. Static/tests,
Track3 1 s, and strict Track3 700 s completed. Track3 stopped at `T=21.65`,
`cR=1`, `cO=1`, and `P=9.2`, without an official finish. The extra `0.55 s`
over v148 is not completion evidence. The family is closed and direct OA
connection semantics from v148 are restored.

Review: `Results/metrics/track3_candidate_review_v156_terminal_only_oa_suppression_20260712.md`.
