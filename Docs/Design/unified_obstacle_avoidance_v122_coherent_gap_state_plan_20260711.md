# v122 Coherent Gap-State Avoidance Plan

Status: planned candidate, not accepted

## Problem

The current obstacle controller combines three inconsistent behaviors:

1. each avoid entry starts with a fixed positive `0.6` steer;
2. after two seconds it changes to gap-directed steering;
3. a one-sample longitudinal `flag=false` pulse resets the lateral state even
   while a side distance remains inside the trigger threshold.

v91 changed only the initial command and regressed Track2. v120 preserved only
the lateral state and regressed Track3. v121 added hysteresis but retained the
fixed initial command and regressed Track3 further. Those isolated mechanisms
do not test a coherent gap-following state machine.

## Unified Candidate

Change only the editable red-box obstacle controller. Keep speed commands,
longitudinal timing, path planning, control allocation, and official models
unchanged.

1. On entry, steer toward the larger side gap with bounded magnitude:

```modelica
if dl > dr then
  steer := -max(0.25, min(0.6, 2 * abs(dl - dr)));
else
  steer := max(0.25, min(0.6, 2 * abs(dl - dr)));
end if;
```

2. Preserve the lateral state across a transient `flag=false` pulse until
   front and both sides are actually clear.
3. Apply a `0.08 m` dead band to the four direction-selection transitions in
   `avoid_lateral`.

This is one track-agnostic Bug/Follow-the-Gap style state rule using only the
four official distance inputs.

## Gates

1. Deployability checker and targeted Python tests pass.
2. Track3 1 s `-gui` gate passes.
3. Track3 target run must finish or materially improve comparable progress
   without increasing `cR/cO` or creating a shorter abnormal stop.
4. Only then run Track2 regression, followed by Tracks 1 and 4.
5. On failure, restore the exact committed v80 controller. Do not continue by
   scanning entry magnitude, dead-band width, or release thresholds.

No completion, 80-point, physical-car, report, package, or submission claim is
made by this plan.
