# v139 State-Aware Heading Arbitration Plan

## Status

Rejected after the Track2 120 s gate. The v80 controller semantics are
restored; the decision is recorded in
`Results/metrics/track2_candidate_review_v139_state_aware_heading_arbitration_20260712.md`.

## Failure Mechanism

The v80 Track2 long run reaches a side-only avoidance condition with the front
clear, but the obstacle controller continues to output `speed_oa=-1`. The
allocated speed then falls to about `0.06 m/s` and path progress stops. v137
removed that reverse contribution globally and restored progress, but allowed
the path planner to keep a larger same-direction steering request, which
introduced a road collision. v138 did not change this behavior materially.

Evidence:

- `Results/metrics/track2_v80_termination_classification_20260712.md`
- `Results/metrics/track2_v80_v132_event_windows_20260712.md`
- `Results/metrics/track2_candidate_review_v137_neutral_side_guard_20260712.md`
- `Results/metrics/track2_candidate_review_v138_adaptive_lateral_magnitude_20260712.md`

## Unified Mechanism

Implement the arbitration in `ControlAllocate.CtrlAlloc`, without changing
the sensor thresholds or the official track models:

1. When reverse obstacle avoidance is active, the path planner may release its
   reverse contribution only when its steering request and obstacle steering
   request have the same sign and the path request is more aggressive.
2. In that same case, cap the path steering contribution to the obstacle
   steering request. This prevents the v137 failure mode where neutral speed
   exposes an unbounded path turn toward the near road boundary.
3. Preserve the existing v48 opposing-steer guard for opposite-sign requests.
4. Leave all forward-cruise and non-reverse behavior unchanged.

The expressions are deliberately bounded and use existing signals only:

```modelica
speed_oa_eff = if speed_oa < 0 and steer_oa * steer_pp > 0
  and abs(steer_pp) > abs(steer_oa) then 0 else speed_oa;
steer_pp_eff = if speed_oa < 0 and steer_oa * unitDelay1.y > 0
  and abs(unitDelay1.y) > abs(steer_oa) then steer_oa else unitDelay1.y;
```

The implementation uses the existing gain inputs rather than adding ports,
new state blocks, or edits to the official track packages.

## Gates

1. Run the source deployability checker and `python -m pytest Scripts/tests -q`.
2. Run Track2 at 1 s; this is only a load/check/simulate gate.
3. Run Track2 at 120 s. Accept the candidate for the extended gate only if it
   is comparable to v80, has no new collision, and advances materially beyond
   v80 path index 26 without the v137 collision regression.
4. Only after gate 3, run Track2 at 700 s. Official completion requires
   `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02` at termination.
5. Only after a Track2 official finish, run Track1 collision regression and
   then expand to Tracks 3 and 4. One controller and one parameter set must
   serve all four tracks.
6. Any syntax/runtime failure, early stop, collision regression, or absent
   material progress rejects v139. Restore exact v80 semantics, rerun static
   checks/tests, record the decision, and continue with a new mechanism only.

This plan makes no claim of an 80-point result, official completion, physical
UGV success, or submission readiness.
