# Unified Obstacle Avoidance v199 Heading-Error Speed Governor

## Status

Retained as the current research candidate; it is not an official four-track
completion baseline. v200 was evaluated as a refinement and rolled back.

## Evidence basis

The v148 Track3 command-feasibility run exported the path, obstacle, allocator,
and Ackermann signals. Before about 17 s the wrapped desired/current heading
error stayed near zero. During the later high-curvature segment, the desired
heading reached about 2.03 rad while actual heading reached about 2.41 rad;
the wrapped error was about -0.38 rad and the PID command reached about
-38 rad/s before the same early termination at `T=21.1`.

This is a command-feasibility mechanism, not another obstacle threshold or
scalar gain scan.

## Candidate

Add the existing vehicle yaw (`body3DOF1_1.angles[3]`) as a read-only input to
`ControlAllocate.CtrlAlloc`. Compute the wrapped error between the final
blended desired heading and measured heading. When the absolute error grows,
continuously reduce the positive longitudinal command while retaining the
existing steer/path/obstacle blending. The mechanism is identical on all four
official evaluation models and uses no track id, time, score, collision count,
or absolute position.

## Gates

1. `check_controller_deployability.py`: high=0, medium=0.
2. Full project tests pass.
3. Plain `SimulateModel` Track3 1 s native gate passes.
4. Plain Track3 decisive run must officially finish or show a reproducible
   completion/collision improvement without early-stop regression.
5. Only after Track3 passes, evaluate unchanged source on Tracks 1, 2, and 4.
6. On failure, restore exact pre-candidate bytes and record the result.

This candidate is not four-track completion, 80/80, physical-UGV, or
submission evidence until those gates pass.

## Result

Static deployability (`high=0, medium=0`), 14 project tests, and the Track3 1 s
plain native gate passed. The Track3 700 s plain run ended at `T=92.85`,
`cR=1`, `cO=1`, `P=9.2`, and `distanceSensor1.d=1.0824256`. It did not cross
the strict finish threshold `d<0.02`, but it is a reproducible closure-progress
improvement over v148 and is retained for the next structural investigation.
