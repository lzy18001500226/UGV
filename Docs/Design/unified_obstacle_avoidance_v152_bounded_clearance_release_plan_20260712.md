# v152 Bounded Clearance Release Plan

Status: rejected; exact v148 longitudinal-state release restored.

## Mechanism

v151 proves that clearance-only release can lock avoid indefinitely. v152
retains v148's longitudinal command and allows release after two seconds when
all sensors are clear, but enforces an unconditional three-second maximum:

```modelica
speed := min(0, max(-1, df - mindis));
transition(avoid, cruise,
  after(3,sec) or
    (after(2,sec) and df > mindis and dl > 0.45 and dr > 0.45),
  reset=false);
```

This is a bounded state-persistence test, not a dwell scalar scan: the early
release remains clearance-aware and the hard cap directly removes v151's
permanent-lock failure. It is still one sensor-driven controller for all
tracks.

## Gates

Static checker and tests, Track3 1 s, then Track3 700 s. Only a strict Track3
finish promotes to Track4 regression. Any non-finish, avoid-lock recurrence,
or collision explosion rejects v152 and restores v148.

## Result

Track3 terminated at `T=48.45`, `cR=9`, `cO=1`, `P=6.0`, and
finish-distance squared `397.5869`. The bounded extension avoids v151's long
lock but still sharply increases road collisions and does not finish. v152 is
rejected. The exact v148 two-second longitudinal-state release is restored.
