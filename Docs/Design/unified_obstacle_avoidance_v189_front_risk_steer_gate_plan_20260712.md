# v189 Front-Risk Steer Gate Plan

Status: rejected after Track2 strict gate; committed allocator restored

## Goal

Preserve v187's near-origin path return while preventing its immediate
obstacle contacts, without reintroducing v188's continuous OA steering that
caused a Track2 road departure.

## Candidate

Keep the OA speed contribution disabled. Admit the filtered OA steering only
while the obstacle controller is commanding negative longitudinal speed:

```modelica
gain1(k=0)
firstOrder.u = if speed_oa < 0 then gain.y else 0;
```

`speed_oa < 0` is the existing front-risk/avoid-state signal. When that state
releases, the allocator input returns to zero and path steering regains
authority. The same rule is used on every track and contains no track id,
time, score, path index, or absolute-coordinate branch.

## Evidence Basis

v187 path-only first contacted an obstacle at `t=1.6` and returned near the
origin, but accumulated eight obstacle collisions. v188 continuously admitted
OA steering and removed obstacle contacts, but left the viable route at
`T=29.1`. The missing mechanism is state-bounded steering authority, not a new
steering-magnitude threshold.

## Gates

1. Static deployability and all project tests.
2. Track2 1 s native gate.
3. Track2 strict 700 s gate with position, path progress, controller outputs,
   and distance-sensor diagnostics.
4. Retain only on official finish or a reproducible near-finish with fewer
   collisions than v187 and no v188-style early route loss.
5. Expand to Track3 only after Track2 passes the completion-first gate.

## Outcome

The 1 s native gate passed. The strict Track2 run ended at `T=164.95` with
`cR=15,cO=2,P=3.2` and finish-distance squared `377.9933562`.

The exported collision windows disprove the gate premise. At the first
obstacle event (`t=1.6`), the controller output was `speed_oa=1,steer_oa=0`.
At the second (`t=15.1`), it was `speed_oa=0,steer_oa=0.6`. Neither event
satisfied `speed_oa<0`. The candidate was not expanded to Track3.
