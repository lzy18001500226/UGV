# Runtime Channel Blocker - v80 Health Check After v108

Status: blocked_runtime_wrapper_timeout, 2026-07-11 CST.

## Context

The accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
target-equivalent score: about 76 / 80
```

v107 and v108 were rejected because their Track3 probes exceeded bounded
runtime timeouts and produced no readable score evidence. Source semantics were
restored to v80 after v108.

## Static Restore Gate

The v80 restore gate after v108 passed:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v108_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Health Checks

Two known-baseline v80 health probes were attempted without changing source:

```text
Results/simulations/health_v80_restored_after_v108_saidao3_120s_20260711/
```

Result:

```text
120 s Track3 wrapper probe exceeded a 20-minute command timeout.
Only an empty native_result directory was produced.
No metrics.json, score_timeseries.csv, or readable score variables were produced.
```

A control probe against the official example entry was then attempted:

```text
Results/simulations/health_official_race1_1s_after_v108_20260711/
```

Result:

```text
UGV.Example.Race1 with stopTime=1 exceeded a 5-minute command timeout.
Only an empty native_result directory was produced.
No metrics.json, score_timeseries.csv, or readable score variables were produced.
```

```text
Results/simulations/health_v80_restored_after_v108_saidao3_1s_20260711/
```

Result:

```text
1 s Track3 wrapper probe exceeded a 5-minute command timeout.
Only an empty native_result directory was produced.
No metrics.json, score_timeseries.csv, or readable score variables were produced.
```

Residual MWORKS, Sysplorer ACP, docsearch, and MWORKS Python processes spawned
by these two timed-out probes were stopped by exact PID after evidence capture.
Unrelated Python processes from other tasks were left untouched.

## Decision

Do not launch another algorithm candidate until the MWORKS/Sysplorer API route
is healthy again. The current blocker is not an algorithm-score blocker and not
just a generated-wrapper blocker; it is a runtime channel blocker because both
a known v80 wrapper 1 s probe and an official `UGV.Example.Race1` 1 s probe
cannot produce score evidence.

## Required Recovery Before Next Candidate

1. Re-establish the MWORKS/Sysplorer API route with a bounded official-example
   1 s probe.
2. Confirm the output contains readable score or run-step evidence, not only an
   empty `native_result` directory.
3. Then rerun the restored v80 wrapper 1 s probe.
4. Keep source at v80 semantics until a new candidate has static-gate and
   runtime score evidence.
5. After the runtime channel is healthy, resume score sprint from v80 and avoid
   the already rejected speed-gate scalar families unless new diagnostics
   justify them.

## Non-Claims

- No new candidate was accepted.
- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package readiness claim.
- No official road, vehicle, sensor, scoring, example, or official material
  edits.

## Recovery Addendum

Recovered on 2026-07-11 CST and superseded for execution by:

```text
Results/metrics/runtime_channel_recovery_v80_after_v108_20260711.md
```

The recovery proof includes an official `UGV.Example.Race1` 1 s probe with
`simulate_returned_true`, a restored v80 `UGV.Test.Saidao3Eval` 1 s probe with
`simulate_returned_true`, and a restored v80 Track3 120 s recheck that again
produced readable score variables (`T=59.4`, `cR=1`, `cO=1`, `P=9.2`) rather
than an empty timeout. The algorithm sprint may resume from v80; this addendum
is not a new score claim.
