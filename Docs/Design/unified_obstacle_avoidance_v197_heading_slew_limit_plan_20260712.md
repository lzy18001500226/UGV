# Unified Obstacle Avoidance v197 Heading Slew Limit Plan

Status: rejected; exact v148 source semantics restored

## Goal

Prevent reproducible early numerical termination before attempting more
obstacle-distance or state-transition tuning. The same controller and
parameters remain in force on all four tracks.

## Evidence Basis

The cold v148 Track3 diagnostic stopped at `T=21.1` far from the official
finish. No NaN or explicit finish assertion was observed. Immediately before
termination:

- the combined heading command changed by as much as `0.352 rad` in `0.05 s`;
- the heading-loop output changed by about `36.8 rad/s` over the same sample;
- rear-wheel commands showed order-`1000` discontinuities and had reached the
  model's `5000` command range earlier in the run;
- vehicle pose and speed remained finite.

This makes command continuity a more specific next mechanism than another
distance threshold, gain, or state-machine branch.

## Candidate

Add one sampled slew limiter to the final `CtrlAlloc.steer` heading command.
At the existing `0.01 s` sample period, limit command movement to
`0.01 rad/sample` (`1 rad/s`). Preserve the existing path/avoidance blending,
speed channel, obstacle state machine, and official vehicle/PID model.

The limiter uses only the previous combined command and current combined
command. It does not inspect track identity, time, score, collision count, or
absolute position.

## Gates

1. Deployability checker and all project tests pass.
2. Plain `SimulateModel` Track3 1 s native gate passes.
3. Plain `SimulateModel` Track3 decisive run must finish officially or improve
   reproducible completion progress without a new collision regression.
4. Expand unchanged source to all four tracks only after the Track3 gate.
5. Reject and restore exact v148 source bytes if the decisive gate regresses or
   does not support the mechanism.

## Evidence Boundary

This candidate is not four-track completion, `80/80`, physical-car, package,
or submission evidence until the corresponding official gates pass.

## Result

Static checking and the 14 project tests passed, and the Track3 1 s native
gate passed. The decisive plain `SimulateModel` Track3 run stopped at
`T=70.65` with `exit_state=2`, `cR=2`, `cO=1`, `P=8.8`, and
`distanceSensor1.d=192.81082249938794`. This is not an official finish and is
worse than the retained baseline evidence. The candidate was rolled back
exactly; no v197 semantics remain in the working controller.
