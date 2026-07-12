# v183 Open-Side Narrow Recovery Plan

Status: rejected after Track2 regression; exact v148 semantics restored

## Hypothesis

The useful v162 Track3 recovery samples had `df<0.15` while both side
clearances exceeded `0.45 m`. Gate the directional narrow-front recovery by
that open-side geometry so road-edge events retain v148 steering. The same
condition applies to every track and contains no track id, time, score, or
absolute position.

## Result

- Track3 reached the configured 120 s horizon with
  `cR=1,cO=1,P=9.2`, materially beyond the v148 failure.
- Track1 reached the configured 120 s horizon with
  `cR=4,cO=1,P=8.0`, clearing v180's `67.20 s` regression.
- Track2 reproducibly terminated at `T=28.55,cR=1,cO=0,P=9.6`, far from the
  official finish.

The candidate is rejected. A high displayed score at early termination is not
completion. The next candidate must improve road-boundary margin as well as
Track3 recovery, rather than rely on translation-sensitive path perturbations.

Evidence is under:

```text
Results/simulations/candidate_v183_open_side_narrow_recovery_track1_120s_20260712/
Results/simulations/candidate_v183_open_side_narrow_recovery_track2_120s_20260712/
Results/simulations/candidate_v183_open_side_narrow_recovery_track3_120s_20260712/
```
