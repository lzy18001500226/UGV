# Track2 v187/v188 Path-Overlay Review

## Decision

Both candidates are rejected. The committed allocator is restored exactly.

## Results

| Candidate | Mechanism | T | cR | cO | P | Finish distance squared | Classification |
|---|---|---:|---:|---:|---:|---:|---|
| v187 | Disable OA steering and speed | 198.5 | 7 | 8 | 4.0 | 0.0305001871 | unclassified early termination |
| v187 retry | Disable OA steering and speed | 198.5 | 7 | 8 | 4.0 | 0.0305001871 | unclassified early termination |
| v188 | Keep OA steering, disable OA speed | 29.1 | 1 | 0 | 9.6 | 793.6885770 | unclassified early termination |

v187 reproducibly returned close to the official origin, but remained outside
the strict `distanceSensor1.d <= 0.03` assertion and accumulated fifteen total
collisions. v188 removed obstacle collisions, but the steering overlay caused
the vehicle to leave the viable return route after 29.1 s. Neither candidate
is a finish or a retained score improvement.

## Mechanism Conclusion

The old OA steering signal is not a minimal safety overlay for the path-only
route, while removing all OA authority is unsafe. The next candidate must use
a bounded collision-imminent steering intervention with explicit release to
path authority; it must not restore the old continuous OA steering channel or
repeat scalar edge-recovery scans.

## Evidence

- `Docs/Design/unified_obstacle_avoidance_v187_path_only_isolation_plan_20260712.md`
- `Docs/Design/unified_obstacle_avoidance_v188_steer_only_safety_overlay_plan_20260712.md`
- `Results/simulations/candidate_v187_path_only_track2_700s_20260712/`
- `Results/simulations/candidate_v187_path_only_track2_retry1_700s_20260712/`
- `Results/simulations/candidate_v188_steer_only_overlay_track2_1s_20260712/`
- `Results/simulations/candidate_v188_steer_only_overlay_track2_700s_20260712/`

No official four-track completion, 80/80 score, physical UGV result, or
submission readiness is claimed.
