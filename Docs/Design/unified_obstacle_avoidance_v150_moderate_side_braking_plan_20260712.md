# v150 Moderate Side-Only Braking Plan

Status: rejected; v148 longitudinal semantics restored before v151.

## Evidence Basis

v80 applies full reverse authority during persistent side risk and stalls.
v148 removes that longitudinal authority, completes Tracks 1, 2, and 4, but
Track3 leaves the road at `T=21.1` while allocated speed is about `0.55 m/s`
through a large heading change. v149 proves that removing same-sign OA heading
does not solve this failure.

v150 keeps the continuous front-risk mapping but caps the side-only command at
moderate reverse authority:

```modelica
speed := min(-0.5, max(-1, df - mindis));
```

This preserves `-1` near a front obstacle and approaches `-0.5` when the front
is clear but a side trigger remains active. With the current allocator and
Track3 curve target, the expected steady speed is about `0.30 m/s`, between
v80's stall and v148's road-departure speed. Heading logic, sensor thresholds,
paths, and official models remain unchanged.

## Gates

1. Static deployability and all tests pass.
2. Track3 1 s passes native load/check/simulation.
3. Track3 must progress beyond v148's `T=21.1`, index 36 without adding an
   obstacle collision.
4. Material progress promotes to the 700 s official completion gate.
5. A Track3 finish promotes to Track1/2/4 regression. Any lost v148 finish
   rejects v150 and restores v148.

## Result

The native Track3 run terminated at `T=35.35`, `cR=1`, `cO=1`, path index
`36`, and finish-distance squared `288.8562`. This is longer runtime than
v148 (`T=21.1`) but reaches the same failure region and does not finish.
Changing only the side-only speed cap therefore delays the same road departure
without correcting its geometry. v150 is rejected; further scalar scans of
this cap are not justified.

This is one unified controller. It does not claim 4/4, 80/80, or physical UGV
readiness before the declared gates pass.
