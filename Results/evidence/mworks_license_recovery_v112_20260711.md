# MWORKS License Recovery For v112

Timestamp: 2026-07-11 CST

## Context

The first v112 Track3 runtime attempt was blocked by MWORKS/Sysplorer license
state instead of controller syntax or runtime behavior:

```text
L5104-B0
open_dependency_model_file failed on TADynamics.mol
```

## Recovery

Used the approved project-local GUI recovery route:

1. Started the real Sysplorer window.
2. Opened the license/login flow from the visible Sysplorer UI.
3. Entered the approved in-memory account credentials without writing them to
   project files.
4. Verified recovery with a 1 s API probe.

## Verification

Probe folder:

```text
Results/simulations/license_recovery_probe_1s_20260711_1440/
```

Verified steps:

```text
open_dependency_model_file: ok
open_model_file: ok
open_model: ok
check_model: ok
simulate_model: ok
available_score_variables: T, cR, cO, P
score_values_at_end: T=1.0, cR=0.0, cO=0.0, P=10.0
```

Sparse email notice:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260711_144345.json
```

## Boundary

This proves only that the MWORKS/Sysplorer runtime channel recovered. It does
not prove v112 score improvement, full-track completion, physical UGV behavior,
or final submission readiness.
