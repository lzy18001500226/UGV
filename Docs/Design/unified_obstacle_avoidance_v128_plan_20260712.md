# Unified Obstacle Avoidance v128 Plan

Status: candidate under validation, 2026-07-12 CST.

## Evidence-driven problem

Restored v80 Track2 was rerun with `SimulateModelEx`, `Dassl`, and a fixed
`0.05 s` output interval. The run reached the full 180 s horizon cleanly, but
ended near path index `27/231` with:

```text
pathPlanner.target_v = 0.55
body3DOF1_1.v[1] ~= 0.058
cR = 1
cO = 0
P = 9.6
```

The current allocator combines the path speed with the filtered obstacle speed.
When obstacle avoidance requests `-1` and `factor_oa=0.5`, a path speed of
`0.55` becomes approximately `0.05`. This explains the persistent crawl and
why a 120 s score snapshot is not a finish result.

## Candidate

Apply a unified forward-speed floor in `ControlAllocate.CtrlAlloc` before the
obstacle speed filter:

```modelica
gain1.u = if speed_oa < 0 then max(speed_oa, 2 * (0.2 - unitDelay3.y)) else speed_oa;
```

With `factor_oa=0.5`, this bounds the combined steady-state command at roughly
`0.2` while preserving stronger reverse authority when path speed is high
enough. It uses only existing controller signals, has no track identifier, and
remains suitable for later physical tuning.

## Gate

1. Run source deployability checks and project tests.
2. Run a 1 s Track2 translation/simulation gate.
3. Run Track2 with the fixed `SimulateModelEx` configuration.

## Runtime result

The 1 s translation/runtime gate passed. The 180 s Track2 comparison stopped
at `T=157.9` with `cR=1`, `cO=0`, `P=9.6`, `closest_index=35`, and no official
finish. This improved the v80 crawl (`T=91`, `closest_index=27`) but forced
about `0.2` forward speed while the path steering demand reached about
`1.97 rad`, causing a road collision. The candidate is rejected and superseded
by v129; its runtime artifacts remain as negative evidence.
4. Accept only if path progress/completion improves without new collision or
   runtime regressions.
5. If accepted on Track2, validate the same source on all four tracks; otherwise
   restore committed v80 source exactly.

## Non-claims

- This plan does not claim a finish or score improvement.
- No official road, vehicle, sensor, scoring, or example file is modified.
- The fixed speed floor is a candidate, not a per-track patch.
