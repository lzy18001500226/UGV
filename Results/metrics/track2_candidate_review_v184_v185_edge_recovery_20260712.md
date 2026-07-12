# Track2 v184-v185 Edge-Recovery Review

## Decision

Both candidates are rejected. The committed v148 controller is restored.

## Comparable Runtime Results

| Candidate | Track2 result | Completion class | Decision |
|---|---|---|---|
| committed v148 cold rerun | `T=28.55,cR=1,cO=0,P=9.6` | `unclassified_early_termination` | current reproducibility blocker |
| v184 fixed `0.6` severe-side recovery | `T=120.0,cR=61,cO=1,P=-14.8` | horizon only, not official finish | reject |
| v185 proportional cap `0.3` | `T=28.75,cR=17,cO=0,P=3.2` | `unclassified_early_termination` | reject |

v184 proved that the measured front-clear severe-side window can keep the
simulation alive, but its fixed correction oscillated across the road edge.
v185 reduced the correction magnitude and lost that progress while retaining
large road-contact growth. This closes further direct magnitude scans in this
window.

## Verification

- Restored controller diff against `HEAD`: empty.
- Restored static deployability: `high=0, medium=0`.
- Restored tests: `14 passed`.
- Static evidence:
  `Results/evidence/controller_deployability_static_check_v148_restored_after_v185_20260712.md`
- Test evidence:
  `Results/evidence/pytest_v148_restored_after_v185_20260712.console.txt`
- Runtime evidence:
  `Results/simulations/candidate_v184_dual_window_track2_120s_20260712/` and
  `Results/simulations/candidate_v185_edge_recovery_track2_120s_20260712/`.

## Next Gate

Track2 reproducible official completion is now part of the hard gate. The next
family must use a narrow severe-side condition to alter forward/path authority
smoothly, then pass Track2 120 s with bounded contacts before any Track3 or
four-track expansion.
