# v187 Path-Only Isolation Plan

Status: diagnostic completed; rejected as final candidate; allocator restored

## Goal

Determine whether the current completion blocker is caused by the nominal path
tracker or by the legacy obstacle-avoidance overlay. This is a structural
isolation gate, not a final obstacle-avoidance design.

## Evidence Basis

v148 once produced three official finishes, but current exact-source Track2
runs terminate at 28.55 s. v184-v186 show that direction, magnitude, and
braking changes inside the old fixed-dwell OA state machine can extend runtime
only by accumulating contacts. The project has not recorded a current strict
path-only completion baseline under the official finish assertion.

## Candidate

Preserve the path planner and all official models. In the editable control
allocator only, set both filtered OA gains to zero while retaining the complete
OA controller source and signal interfaces:

```modelica
gain(k=0)
gain1(k=0)
```

The same source applies to every track. There is no track id, time, score,
position, or official-model branch.

## Interpretation Gate

1. If Track2 still fails near the current location, path tracking or runtime
   determinism is the primary blocker; do not keep patching OA.
2. If Track2 officially finishes, the old OA overlay is the primary blocker.
   Then test Track3 and use the path-only result only as a lower-bound baseline
   for rebuilding a minimal bounded safety overlay.
3. A path-only finish does not prove an acceptable avoidance score, physical
   safety, final algorithm quality, or 80/80.

## Runtime Gates

1. Static deployability and all project tests.
2. Track2 1 s native gate.
3. Track2 strict 700 s completion gate, because a 120 s horizon cannot prove a
   lap finish.
4. Expand to Track3 only after a Track2 official finish.
5. Restore the allocator exactly after the diagnostic unless cross-track
   evidence justifies retaining it as the next design baseline.

## Outcome

Two strict Track2 runs reproduced the same endpoint at `T=198.5`, with
`cR=7,cO=8,P=4.0` and finish-distance squared `0.030500187108878623`.
This is close to the origin but does not satisfy the official `<= 0.03`
assertion. The diagnostic shows that the nominal path route can return near the
origin, while removing all OA authority is unsafe. v187 is not retained as the
competition controller.
