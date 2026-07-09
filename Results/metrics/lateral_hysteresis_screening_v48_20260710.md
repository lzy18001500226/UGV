# v48 Lateral Hysteresis Screening

Status: source/static offline analysis, no source edit
Date: 2026-07-10
Baseline: v48 opposing-steer guard

## Purpose

Screen one apparently plausible post-v67 mechanism before editing source:
adding hysteresis to the lateral obstacle-avoidance left/right switch.

This candidate would only be justified if saved v48 signals showed high-rate
left/right steering sign changes or `dl/dr` comparison chatter around the
remaining score-loss windows.

## Inputs

Saved MWORKS CSV exports:

```text
Results/simulations/controller_v48_opposing_steer_guard_saidao1_120s_20260710/extra_timeseries.csv
Results/simulations/controller_v48_opposing_steer_guard_saidao2_120s_20260710/extra_timeseries.csv
Results/simulations/controller_v48_opposing_steer_guard_saidao3_120s_20260710/extra_timeseries.csv
Results/simulations/controller_v48_opposing_steer_guard_saidao4_120s_20260710/extra_timeseries.csv
```

Signals checked:

```text
obsAvoidController_Sysblock.chart.steer
obsAvoidController_Sysblock.chart.flag
obsAvoidController_Sysblock.chart.dl
obsAvoidController_Sysblock.chart.dr
ctrlAlloc.steer
ctrlAlloc.speed
```

## Results

| Track | Samples | chart.steer sign flips | sign flips before 10 s | flag flips |
|---|---:|---:|---:|---:|
| Track1 | 2401 | 0 | 0 | 23 |
| Track2 | 1204 | 0 | 0 | 11 |
| Track3 | 2250 | 0 | 0 | 23 |
| Track4 | 2249 | 0 | 0 | 21 |

Early Track3 first obstacle window (`0.8-1.3 s`):

```text
chart.steer = 0.6 throughout
dl ~= 0.5675-0.5681
dr ~= 0.5669-0.5675
ctrlAlloc.steer ~= 0.1545-0.1662
ctrlAlloc.speed ~= 0.6710-0.7820
```

Track3 road-event window (`4.3-5.1 s`):

```text
chart.steer = 0.6 throughout
dl ~= 0.4988-0.5599
dr ~= 0.5751-0.6362
ctrlAlloc.steer ~= 0.1699-0.2182
ctrlAlloc.speed ~= 0.5081-0.5181
```

## Decision

Do not implement lateral left/right hysteresis as the next controller patch.
The saved v48 evidence does not show steering-direction chatter; the obstacle
controller keeps a consistent positive avoid steering command in the remaining
Track3 event windows.

The remaining issue is better described as insufficient effective command
authority or geometry exposure while avoidance is already active, not lateral
switching instability.

## Non-Claims

- No MWORKS runtime was opened or rerun.
- No source file was edited.
- This does not prove v48 is final or optimized.
- This only rejects the lateral-hysteresis mechanism as an immediate next
  source patch.
