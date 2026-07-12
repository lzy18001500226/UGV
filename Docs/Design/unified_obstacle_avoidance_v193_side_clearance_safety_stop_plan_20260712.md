# v193 Side-Clearance Safety Stop Candidate

## Objective

Prevent the reproducible Track2 boundary exits with one track-agnostic safety
arbitration rule while avoiding v186's unstable reverse-and-steer recovery.

## Evidence Basis

v192's two Track2 road contacts occurred with clear front distance and narrow
side clearance:

```text
t=5.25:  df=2.10, min(dl,dr)=0.108, speed_oa=0
t=101.5: df=2.055, min(dl,dr)=0.171, speed_oa=0
```

The current longitudinal state enters avoidance on side risk but computes its
speed command only from `df`, so the allocator continues forward. v29's
filtered side-speed regulation and v186's full reverse plus forced steering
were rejected. Neither tested an immediate neutral safety stop while leaving
steering unchanged.

## Mechanism

- In the existing avoidance state, combine the committed front-distance term
  with the bounded continuous side-risk term
  `max(-1,10*(min(dl,dr)-0.25))`. This makes `speed_oa<-0.5` exactly when
  `min(dl,dr)<0.20` without an unsupported state-action `if` expression.
- In the allocator, treat `speed_oa<-0.5` as collision-imminent and output
  `speed=0` immediately. Do not reverse and do not alter steering.
- Preserve all existing state timing, path steering, obstacle steering,
  filters, and normal-speed allocation.

The same sensor-only rule applies to every track and adds no track, time,
score, position, or official-model branch.

## Gates

1. Static deployability and repository tests.
2. Track2 1 s native gate.
3. Track2 120 s must pass the 28.55 s baseline termination with bounded
   contacts and without becoming permanently stationary.
4. Only a promising 120 s result may proceed to strict 700 s completion.

## Rollback

Any early termination, repeated contact growth, or stationary deadlock rejects
v193 and restores the exact pre-candidate controller and allocator objects.
