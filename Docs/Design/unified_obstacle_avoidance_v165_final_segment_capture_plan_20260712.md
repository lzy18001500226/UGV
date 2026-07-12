# Unified Obstacle Avoidance v165 Final-Segment Capture Plan

## Goal

Preserve v162's Track3 loop traversal while preventing the global closest-
segment search from switching from the final segment to segment 1 before the
official origin assertion is reached.

## Evidence Basis

- v162 reaches the origin area twice after `time>100`.
- On each return, `pathPlanner.closest_index` changes from final indices
  `103/104` to index `1` while the vehicle is still about `0.65-0.75 m` from
  the origin.
- Official completion requires `distanceSensor1.d < 0.02`, approximately a
  `0.141 m` radius.
- v164's discrete departure state changed the early numerical trajectory and
  is rejected.

## Candidate

Keep v162's narrow front-obstacle recovery. The official closed road arrays
append the first outgoing point after repeating the origin, so the finish
segment is `path[end-2] -> path[end-1]` and `path[end-1]` is the official
origin. In `PathPlanner`, calculate the vehicle projection onto that closure
segment. Force the pursuit point to the exact origin only when:

1. the vehicle is geometrically close to the final segment;
2. projection lies inside the latter half of that segment; and
3. projection is still below the endpoint value, so the initial point and
   departure beyond the endpoint do not trigger capture.

This rule is path-geometric, stateless, unified across tracks, and contains no
track identifier or per-track parameter branch.

## Gates

1. Static deployability checker and all script tests.
2. Track3 1 s native translation gate; initial steering/path behavior must
   remain valid.
3. Track3 700 s strict completion gate.
4. Only after verified Track3 completion, run Tracks 4, 1, and 2.

Reject and restore v148 if Track3 does not finish or collision/runtime behavior
regresses materially.
