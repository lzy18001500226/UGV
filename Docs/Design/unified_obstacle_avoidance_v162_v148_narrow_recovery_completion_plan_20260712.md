# v162 v148 Narrow-Recovery Completion Plan

Status: rejected after Track3 completion gate; exact v148 source restored.

## Goal

Test whether the previously runtime-stabilizing v83 narrow road-edge recovery,
combined with the current v148 longitudinal semantics, can complete Track3.
Official completion is the first gate; collision/score optimization follows.

## Evidence Basis

v83 was tested on the older v80 baseline. It changed only the lateral initial
state when `df < 0.15` and reached the full 120 s request on Track3 with
`cR=1,cO=1,P=9.2`, whereas v80 terminated at `T=59.4`. It was rejected under
the old score-first gate because collision variables did not improve. It was
never tested against the official completion condition or combined with v148.

v148 now finishes Tracks 1, 2, and 4 and uses neutral longitudinal authority
for side-only risk. Track3 still terminates at `T=21.1`. v158-v161 prove that
allocator-level path recovery extends progress but adds collisions. v162 moves
the recovery decision back to the obstacle state machine and reopens only the
specific v83 mechanism that already demonstrated longer stable runtime.

## Candidate

Keep exact v148 semantics except for `avoid_lateral.ini_state`:

```modelica
if df < 0.15 and dl < dr then
  steer := -min(0.6, 2 * abs(dl - dr));
elseif df < 0.15 and dr < dl then
  steer := min(0.6, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

The rule is unified and uses only the existing four-direction sensor state.
It does not inspect track identity, time, score, position, or official geometry.

## Gates

1. Deployability checker, project tests, and diff check.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s request. Completion requires the official origin-return
   assertion, `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
4. A Track3 finish promotes to Track4, Track1, and Track2 regression using the
   same source.
5. Non-finish or collision regression restores exact v148 semantics.

No completion, 80/80 score, physical result, or submission readiness is
claimed before the corresponding runtime evidence exists.

## Result

The 1 s gate passed. The strict request reached `T=286.55,cR=2,cO=1,P=8.8`
but did not finish; official finish distance was `295.9073`. v162 traversed the
main loop and is valuable structural evidence, but the added road collision
and missed origin reject it as a retained controller. See
`Results/metrics/track3_candidate_review_v162_v148_narrow_recovery_20260712.md`.
