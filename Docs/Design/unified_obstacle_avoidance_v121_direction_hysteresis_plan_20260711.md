# v121 Lateral Continuity With Direction Hysteresis Plan

Status: planned candidate, not accepted

## Evidence

v120 proved that preserving the lateral avoidance state across the
longitudinal controller's one-sample `flag=false` pulse changes the actual
steering behavior.  It also exposed a second structural weakness: once the
gap-directed state remains active, small changes in `dl - dr` repeatedly flip
`steer_oa` between left and right.  The Track3 result regressed from v80
`T=59.4,cR=1,cO=1,P=9.2` to v120 `T=52.95,cR=1,cO=2,P=8.8`.

This candidate tests whether the continuity mechanism needs a dead band around
equal left/right gaps.  It is not a per-track parameter patch: the same state
logic remains active on every official track.

## Candidate

Retain v120's actual-clear outer lateral release:

```modelica
not flag and df > mindis and dl > 0.45 and dr > 0.45
```

Add one shared gap hysteresis value:

```modelica
SysplorerEmbeddedCoder.Types.Auto steer_hysteresis(start=0.08)
```

Apply it only to the four direction-selection transitions inside
`avoid_lateral`:

```modelica
state -> turn_left:       dl > dr + steer_hysteresis
state -> turn_right:      dr > dl + steer_hysteresis
turn_left -> turn_right:  dr > dl + steer_hysteresis
turn_right -> turn_left:  dl > dr + steer_hysteresis
```

Do not alter longitudinal timing, speed commands, fixed initial action, cruise
lateral logic, path planning, control allocation, vehicle, road, scoring, or
official track models.

## Gates

1. Controller deployability checker reports no high/medium findings and the
   targeted Python tests pass.
2. A Track3 1 s `-gui` load/check/simulate gate succeeds.
3. A Track3 120 s run must either finish or materially improve comparable
   progress without increasing collision counts or introducing a runtime
   regression.
4. Expand to Tracks 1, 2, and 4 only after Gate 3 passes.
5. On failure, restore the exact committed v80 controller source and retain
   the candidate plan, runtime evidence, and rejection review.
