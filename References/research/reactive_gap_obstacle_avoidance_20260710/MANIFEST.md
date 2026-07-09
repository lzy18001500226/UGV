# Reactive Gap Obstacle Avoidance Research Manifest

timestamp: 2026-07-10 CST
scope: UGV four-distance-sensor obstacle avoidance after v55-v57 rejection

## Purpose

Find a safer next mechanism after these Track3 mechanisms failed to improve
over v48:

- low-speed path lookahead floor;
- obstacle speed-filter-only acceleration;
- simple front `safeF` entry threshold.

## Sources

| Topic | Source | Notes |
|---|---|---|
| Vector Field Histogram | Borenstein and Koren, "The Vector Field Histogram - Fast Obstacle Avoidance for Mobile Robots", CMU-hosted PDF | Classic range-sensor obstacle-density method; useful conceptually, but the current UGV interface has only four distances, not a dense polar histogram. |
| MATLAB VFH implementation | MathWorks Vector Field Histogram documentation | Confirms practical parameters such as distance limits and histogram thresholds; useful for parameter naming and safety bounds, not directly reusable in Sysblock. |
| Gap navigation | "Admissible gap navigation: A new collision avoidance approach" | Reinforces gap selection with vehicle constraints; relevant because current model has a strong vehicle/steering constraint. |
| Range-sensor efficient avoidance | "Range Sensor-Based Efficient Obstacle Avoidance through Gap Detection", PMC | Uses entry/bypass-style behavior around gaps; relevant to a compact state-machine design. |
| Closest gap navigation | IROS closest-gap reactive navigation material | Supports gap/opening analysis rather than blind steering scalar tuning. |

## Initial Conclusion

For this project, a full VFH/DWA implementation is likely overkill because the
controller boundary exposes only front, rear, left, and right distances plus
path/control allocation. The transferable idea is not the full algorithm, but
the state split:

```text
front-risk detection
  -> choose admissible/open side only when side evidence is strong
  -> otherwise slow/hold a bounded arc
  -> bypass/release with hysteresis
```

This suggests the next candidate should not be another scalar scan. It should
either:

1. build a small front-risk/bypass state in the obstacle controller, or
2. shift target to Track1/Track4 road-collision windows if Track3 remains
   insensitive to simple reactive changes.

## Non-Reuse

No external code was copied. These sources are used only for design direction.
