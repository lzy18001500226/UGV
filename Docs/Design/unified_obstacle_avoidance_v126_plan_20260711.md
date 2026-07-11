# Unified Obstacle Avoidance v126 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Preserve v125's forward-progress gain only in moderate side proximity while
restoring full reverse authority for front danger and severe side squeeze.

## Evidence Basis

v125's front-conditioned `-0.4` side-only command translated successfully but
Track2 terminated off-route at `T=46.15`. Earlier all-track collision windows
identify side distance around `0.10-0.11` as the severe road-edge band. v88
used `0.12` as the same severe-band boundary, although strengthening reverse
beyond `-1` did not help. v126 therefore keeps the accepted `-1` authority in
that band rather than strengthening it, and relaxes authority only outside it.

## Candidate Mechanism

Modify only the longitudinal avoid state in:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

```modelica
if df <= mindis or dl <= 0.12 or dr <= 0.12 then
  speed := -1;
else
  speed := -0.4;
end if;
flag := true;
```

This is a unified four-distance safety envelope. It does not inspect track
identity, scoring state, result files, or official geometry.

## Gates

1. Source deployability and targeted Python tests.
2. Track2 1 s translation gate.
3. Track2 120 s official completion gate.
4. Expand to Track1 only for a finish or material comparable progress without
   abnormal termination/new collision regression.
5. Restore exact v80 source on rejection.

## Non-Claims

- No official finish or 80/80 claim before runtime evidence.
- No physical UGV, report, package, or submission claim.
- No official no-edit-zone changes.
