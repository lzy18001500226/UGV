# v184 Dual-Window Entry Recovery Plan

Status: rejected after Track2 collision explosion

## Goal

Make the currently reproducible Track2 road-boundary exit robust without
removing the narrow-front mechanism that traverses Track3.

## Evidence

- Track2 now reproducibly exits at `T=28.55`, path index 20. The measured
  boundary window has `dl=0.02353`, `dr=0.18837`, a clear front sector, and the
  fixed `+0.6` entry command points toward the constrained side.
- v145 directed every entry and progressed farther, but added four obstacle
  collisions.
- v167 directed all front-clear entries and regressed Track3.
- v162's direction recovery is useful only in the extreme-front window; v183
  shows an open-side gate preserves Track1 to 120 s.

## Unified Candidate

Inside the existing two-second lateral entry state:

1. For `df<0.15` with both sides above `0.45`, use bounded proportional
   direction recovery.
2. For `df>safeF` and either side below `0.10`, steer toward the more open side
   with the existing `0.6` magnitude.
3. Otherwise retain the original fixed `+0.6` command.

The same sensor-only rule applies to all tracks. It adds no track id, absolute
position, score, time, planner state, or official-model edit.

## Gates

1. Static checker and project tests.
2. Track2 1 s native gate.
3. Track2 120 s must pass `28.55 s`, reach the horizon, and avoid obstacle
   collision growth.
4. Track3 120 s must materially exceed the v148 failure.
5. Only then run strict completion and unchanged-source cross-track expansion.

Any early stop or material collision regression rejects v184 and restores the
committed baseline.

## Result

Static checks, 14 tests, and the Track2 1 s gate passed. Track2 then reached
the 120 s horizon instead of exiting at 28.55 s, but accumulated
`cR=61,cO=1,P=-14.8`. The fixed `0.6` severe-side correction oscillates across
the road boundary and is rejected. v185 retains the measured window but makes
its direction authority proportional and capped at `0.3`.
