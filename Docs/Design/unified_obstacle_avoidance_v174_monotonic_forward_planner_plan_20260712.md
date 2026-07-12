# Unified Obstacle Avoidance v174 Monotonic Forward Planner Plan

Status: candidate pending runtime gates.

## Goal

Preserve path progress through the full Track3 loop without v173's narrow
window or the original planner's final-to-first index wrap.

## Candidate

Keep v162 obstacle behavior and the sampled progress state introduced by v173.
At each 20 Hz update, search from the previous segment through every remaining
forward segment. The accepted index may stay or increase, but cannot decrease
or wrap to segment one.

This allows recovery after larger lateral deviation while preserving path
order. It is unified across all paths and contains no track id, score, fixed
coordinate, or race-time branch.

## Gates

1. Static checks and tests remain required after the one-line policy change.
2. Track3 1 s native gate.
3. Track3 700 s official finish gate.
4. A verified finish promotes unchanged source to Tracks 4, 1, and 2.
5. Failure restores exact v148 and the original global planner.
