# v188 Steer-Only Safety Overlay Plan

Status: rejected after Track2 strict gate; committed allocator restored

## Goal

Retain the path-only near-return behavior observed in v187 while restoring
obstacle steering protection, without restoring the legacy reverse-speed
interference that caused Track2 early exits.

## Candidate

In the editable allocator, keep the obstacle steering channel at its normal
factor and keep the obstacle speed channel disabled:

```modelica
gain(k=factor_oa)  // obstacle steering
gain1(k=0)        // obstacle speed
```

This is one unified allocation rule for all tracks. It does not branch on
track, time, score, absolute position, or path index. The official models and
the obstacle controller signal interfaces remain unchanged.

## Evidence Basis

v187 path-only ran reproducibly to `T=198.5` and returned near the origin, but
with `cO=8`. v184-v186 showed that restoring reverse speed in the old side
windows causes early termination or road-contact growth. v188 isolates whether
the steering channel alone can remove obstacle collisions without that speed
interference.

## Gates

1. Static deployability and all project tests.
2. Track2 1 s native gate.
3. Track2 strict 700 s gate. Retain only if it reduces obstacle collisions and
   either satisfies official finish or materially improves comparable progress
   without a new early failure.
4. Only then evaluate Track3 and expand to all tracks.

## Outcome

The 1 s native gate passed. The strict Track2 run terminated at `T=29.1`
with `cR=1,cO=0,P=9.6` and finish-distance squared `793.6885769997737`.
Steering-only OA removed v187's obstacle collisions but also removed its
near-origin return behavior. The candidate was not expanded to Track3 and the
committed allocator was restored.
