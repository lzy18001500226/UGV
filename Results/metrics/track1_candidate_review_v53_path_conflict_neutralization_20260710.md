# Track1 Candidate Review: v53 Path-Conflict Neutralization

Status: rejected_target_track_regression, 2026-07-10 CST

## Candidate

v53 continued from v48 and tested a stronger path-authority handoff in
`ControlAllocate`: when obstacle avoidance is braking and the path planner
steers opposite to obstacle avoidance, the delayed path-steering contribution
is set to zero instead of being halved as in v48.

Temporary v53 source hypothesis:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0
  else unitDelay1.y;
```

The mechanism remained unified and track-agnostic. It did not branch on track
name, wrapper name, score variables, or run id.

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v53_path_conflict_neutralization_20260710.md
```

Target run:

```text
Results/simulations/controller_v53_path_conflict_neutralization_saidao1_120s_20260710/
```

Post-run analysis:

```text
Results/metrics/collision_window_analysis_v48_v53_track1_20260710.md
Results/metrics/signal_window_summary_v48_v53_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v53_track1_20260710.md
```

Restored-source gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v53_20260710.md
```

## Result

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 Track1 | simulate_returned_true | 0 | 120.0 | 2 | 0 | 9.2 |
| v53 Track1 | simulate_failed with result variables | 2 | 50.55 | 4 | 0 | 8.4 |

v53 worsens the target track and does not qualify for Track3 or four-track
expansion.

## Decision

Reject v53 and keep v48 as the current review-ready best candidate.

Reason:

```text
Complete path-steer neutralization during obstacle/path conflict causes extra
Track1 road contacts and an earlier terminal state. v48's half attenuation is
currently safer than zeroing the path contribution.
```

The source was restored to v48 semantics and passed the static deployability
gate.

## Non-Claims

- This review does not claim final competition score.
- This review does not claim physical UGV success.
- This review does not authorize final package creation or submission.
