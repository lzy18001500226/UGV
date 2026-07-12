# v161 Longitudinal-Authority Steering Blend Plan

Status: rejected after Track3 runtime; exact v148 source semantics restored.

## Goal

Continue from v148 and test one unified completion-first mechanism on Track3.
Preserve full obstacle steering while emergency reverse authority is active,
then hand conflicting lateral authority back to the path continuously as the
front-risk command recovers to neutral.

## Evidence Basis

v148 stops on Track3 after the fixed positive obstacle heading opposes the
negative path heading. v158 and v159 cancel that obstacle heading only after
`speed_oa == 0`; they advance from path index 36 to about 76 but add road and
obstacle collisions. Their boolean switch is abrupt. v160 replaces the switch
with a one-second first-order state and stops at `T=18.75`; a fixed recovery
lag is too slow.

Changing the lateral state-machine entry direction is not justified: v64,
v91, v120-v122, v144, and v145 already reject direct gap steering, persistent
lateral continuity, neutral entry, and direction hysteresis families.

## Candidate

Keep the v148 obstacle state machines, path planner, OA filter, and opposing
path attenuation unchanged. Change only the final steering sum when OA and
path headings conflict:

```modelica
add1.u1 = if steer_oa * unitDelay1.y < 0
  then gain3.y - min(1, max(0, 1 + speed_oa)) * firstOrder.y
  else gain3.y;
```

The final OA contribution is therefore:

```text
speed_oa = -1 -> 100% OA heading
speed_oa =  0 ->   0% conflicting OA heading
between       -> continuous linear handoff
```

This uses an existing normalized controller state, adds no track branch or
new tunable constant, and avoids both the boolean v158/v159 switch and v160's
new fixed time constant.

## Gates

1. Deployability checker, project tests, and diff check.
2. Track3 1 s native load/check/simulation gate.
3. Strict Track3 700 s gate with position, path, OA, and score exports.
4. Only an official Track3 finish promotes to Track4, then Track1 and Track2.
5. Any non-finish, abnormal short stop, or collision regression rejects v161
   and restores exact v148 source semantics.

No finish, 80/80 score, physical-car result, package, or submission readiness
is claimed before runtime evidence proves it.

## Result

Static checks and the 1 s native gate passed. The strict Track3 request ended
at `T=72.7,cR=2,cO=3,P=8.0`, with official finish distance `132.7676`.
The run did not finish and regressed collisions, so v161 is rejected. Review:
`Results/metrics/track3_candidate_review_v161_longitudinal_authority_blend_20260712.md`.
