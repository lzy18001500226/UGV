# Runtime Channel Recovery - v80 After v108

Status: recovered_api_route_for_next_candidate, 2026-07-11 CST.

## Context

The previous runtime blocker was recorded in:

```text
Results/metrics/runtime_channel_blocker_v80_after_v108_20260711.md
```

It showed that restored v80 Track3 probes and an official `UGV.Example.Race1`
1 s probe were timing out with only empty `native_result` directories after
v107/v108 candidate timeouts. No controller source change was made during this
recovery step.

## License / API Health Observation

A bounded Sysplorer license query was executed through the MWORKS Python API.
The API returned:

```text
License info: education edition (教育版, displayed through the API)
Feature list includes: MW_Lib_TADynamics, MW_Sysblk_Env
expired_days: 115
errors: empty string
```

Evidence folder:

```text
Results/evidence/mworks_license_recovery_summary_20260711.json
```

The UTF-8/console encoding of Chinese license keys is not a scoring artifact;
the important recovery signal is the readable feature list including
`MW_Lib_TADynamics` and `MW_Sysblk_Env`, plus the successful API probes below.

## Official Example 1 s Recovery Probe

```text
Results/simulations/health_official_race1_1s_license_query_after_v108_20260711_093722/
```

Result from `metrics.json`:

```text
model_name: UGV.Example.Race1
runtime_status: simulate_returned_true
simulation_exit_state: 0
available_score_variables: T, cR, cO, P
T=1.0, cR=0.0, cO=0.0, P=10.0
exported_csv_ok: true
```

This satisfies the required recovery gate that an official-example 1 s API
probe must produce readable run/score evidence rather than only an empty
`native_result` directory.

## Restored v80 Wrapper 1 s Recovery Probe

```text
Results/simulations/health_v80_restored_after_v108_saidao3_1s_recovered_20260711_094056/
```

Result from `metrics.json`:

```text
model_name: UGV.Test.Saidao3Eval
runtime_status: simulate_returned_true
simulation_exit_state: 0
available_score_variables: T, cR, cO, P
T=1.0, cR=0.0, cO=0.0, P=10.0
exported_csv_ok: true
```

This satisfies the required recovery gate that the restored v80 wrapper route
is healthy at 1 s.

## Restored v80 Track3 120 s Recheck

```text
Results/simulations/health_v80_restored_after_v108_saidao3_120s_recovered_20260711_094331/
```

Result from `metrics.json`:

```text
model_name: UGV.Test.Saidao3Eval
runtime_status: simulate_failed
completion: simulate_false_with_result_variables; inspect messages/assertions
simulation_exit_state: 2
available_score_variables: T, cR, cO, P
T=59.4, cR=1.0, cO=1.0, P=9.2
exported_csv_ok: true
exported_extra_csv_ok: true
```

This reproduces the known v80 Track3 runtime caveat while proving that the
score-variable extraction route is functioning again. It is not a new score
improvement; it is a channel-health recheck of the restored v80 baseline.

## Decision

The MWORKS/Sysplorer API route is recovered enough to resume evidence-based
controller work from the restored v80 baseline:

1. Official example 1 s probe passes with readable score variables.
2. Restored v80 Track3 wrapper 1 s probe passes with readable score variables.
3. Restored v80 Track3 120 s probe again produces the known v80 readable
   `T/cR/cO/P` caveat (`T=59.4`, `cR=1`, `cO=1`, `P=9.2`) rather than timing
   out with empty output.

Next controller candidate work may resume, but should still avoid the rejected
speed-gate/scalar families and must keep v80 as the accepted baseline unless a
new candidate improves score evidence without regression.

## Non-Claims

- No new controller candidate was accepted in this recovery step.
- No improvement beyond the existing v80 wrapper score is claimed.
- No final 80/80 score claim.
- No physical UGV success claim.
- No final submission/package claim.
- No official road, vehicle, sensor, scoring, example, or official material
  edits.
