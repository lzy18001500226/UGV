# v149 Neutral-Side Same-Sign Heading Suppression Plan

Status: rejected; v148 restored.

## Evidence Basis

v148 completes Tracks 1, 2, and 4 but Track3 stops at `T=21.1`, path index
36, far from the finish. In the final five-second window:

- front clearance remains mostly clear;
- neutral side-only avoidance has `speed_oa=0` and `steer_oa=+0.6`;
- the path heading rises to about `1.73 rad`;
- the allocator adds the same-sign OA offset and reaches about `2.03 rad`;
- right clearance falls to about `0.041 m` before termination.

The candidate suppresses only that redundant same-sign side-only OA heading
addition:

```modelica
effective_steer_oa = if speed_oa == 0 and steer_oa * delayed_path_steer > 0
  then 0 else steer_oa;
```

Front-risk reverse avoidance, opposite-sign correction, path heading, speed
logic, thresholds, and official track models remain unchanged. The rule is
track-independent and uses existing allocator inputs only.

## Gates

1. Static deployability and all tests pass.
2. Track3 1 s passes native load/check/simulation.
3. Track3 must progress materially beyond v148's `T=21.1`, index 36 without
   adding obstacle collisions.
4. A material gain promotes to the 700 s official completion gate.
5. Only a Track3 finish promotes v149 to Track1/2/4 regression. Any loss of a
   v148 finish rejects v149 and restores v148.

No horizon-only run is completion. This plan does not claim 4/4, 80/80, or
physical-vehicle readiness.

## Result

Static checks, 14 tests, and the Track3 1 s gate passed. The 120 s request
terminated at `T=18.7`, earlier than v148's `T=21.1`, with unchanged
`cR=1,cO=1,P=9.2` and finish distance squared `299.5152`. Removing the
same-sign OA offset did not solve Track3 and regressed runtime, so v149 is
rejected and v148 allocation semantics are restored.
