# Unified Obstacle Avoidance v127 Plan

Status: runtime candidate from the committed v80 baseline.

## Goal

Keep one controller for all four official tracks while making official finish
the primary gate. v127 tests whether obstacle steering should be a transient
heading correction instead of a persistent heading offset.

## Evidence Basis

The path planner already supplies a global desired heading. In v80 the control
allocator low-pass filters `steer_oa` and adds it continuously to that heading.
Track2 trajectory evidence shows a persistent lateral offset followed by an
off-route turn. Speed-only v125-v126 did not produce a finish, and v118's
instantaneous sign alignment regressed Track3.

## Candidate

Use the existing first-order state as a washout filter:

```text
avoid_transient = factor_oa * steer_oa - lowpass(factor_oa * steer_oa)
steer = path_heading + avoid_transient
lowpass time constant = 2 s
```

For a constant avoidance request, this preserves a material initial correction
but decays toward zero so the path heading can recover. It adds no controller
port and does not modify an official no-edit area.

## Gates

1. Deployability checker reports no high or medium risk.
2. Targeted Python tests pass.
3. Track2 translates and runs with the GUI start mode required by the project.
4. Prefer v127 only if it records an official finish, or material comparable
   completion progress without collision/runtime regression.
5. If rejected, restore `ControlAllocate/package.mo` exactly to committed v80,
   rerun the static gate, and retain only design/review evidence.
6. Expand to all four tracks only after the target-track gate justifies it.

## Non-Claims

This plan does not claim translation, simulation, completion, score gain, or
physical-vehicle readiness.
