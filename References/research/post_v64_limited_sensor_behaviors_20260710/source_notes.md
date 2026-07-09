# Post-v64 Limited-Sensor Behavior Notes

Status: source_notes_only, 2026-07-10 CST

## Local Evidence

Track3 v48 timing around the first obstacle event:

```text
flag enters avoid at about 0.12 s
df at 1.00 s: about 0.049
df at 1.05 s: about 0.013
ctrlAlloc.speed at 1.05 s: about 0.51
ctrlAlloc.steer at 1.05 s: about 0.16
pathPlanner.steering_angle at 1.05 s: about -0.27
```

The issue is not that avoid mode starts late; it starts early. The problem is
that the vehicle still has positive forward speed when the front range is
collision-imminent.

## Rejected Routes Not To Repeat

- v21 / v28: broad speed-channel escalation.
- v29: side-danger speed regulation.
- v35: broad front-open reverse braking.
- v49-v52: broad path-speed / brake-turn arbitration.
- v60 / v63: direct faster steering or early steer feedforward.
- v64: front-clear side-reentry steering.

## Candidate Implication

The only narrow speed-side mechanism still worth one target-track test is an
emergency close-front hold:

```text
if avoid mode is active and df is extremely low,
  command a stronger bounded reverse speed;
else
  keep the v48 obstacle speed semantics.
```

This differs from v35 because it is not a broad `df <= 0.9 and open side`
braking rule. It only triggers inside the collision-imminent band.
