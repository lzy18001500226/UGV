# M6 MWORKS Activation Blocker - 20260708_235918

## Scope

Phase: M6 official four-track evaluation for the UGV initial race.

Target diagnostic:

```text
UGV.saidao.saidao1
controller_v5_front_dwell_2s
SimulateModelEx stopTime=1
compileOptions=0
translationEvaluateParametersToReduceModels=true
translationCheckConnection_Strictly=false
```

No official vehicle, road, sensor, scoring, example, or track file was edited.

## What Changed Safely

Scripts/mworks/ugv_baseline_probe.py was extended to support:

```text
--option key=value
--load-library name[:version]
--load-model-file path
--no-default-dependency-model-files
```

The script now attempts to open the installed commercial vehicle dependency before loading the UGV project package:

```text
D:\Program Files\MWORKS\Sysplorer 2026a\Library\TADynamics 1.3.2\TADynamics\TADynamics.mol
```

This is a script/evidence workflow change only. It does not modify the UGV official model tree.

## Evidence

Latest dependency-load diagnostic folder:

```text
Results/simulations/diagnostic_saidao1_open_tadynamics_mol_compileOptions0_1s_20260708_235749/
```

Important files:

```text
probe_steps.json
metrics.json
MANIFEST.md
```

Observed blocker from metrics.json:

```text
错误(9308): (v2.2.3.27)软件尚未激活，请前往菜单栏“帮助”>“使用许可”窗口激活软件后重试，错误码：L5104-B0。
```

The failure occurred while opening TADynamics.mol, before Models/UGV/package.mo and before CheckModel / SimulateModelEx for the official track.

## Classification

This is a MWORKS license/activation blocker, not a controller-score failure and not an official-track compile-equation result.

Earlier evidence showed the official track depends on TADynamics through files such as:

```text
Models/UGV/Vehicle/Tire/Wheel.mo
Models/UGV/Road/TabularRoad.mo
Models/UGV/Road/TabularRoadObstacle.mo
```

The installed TADynamics package exists on disk, but the current MWORKS runtime blocks loading it because the software is not activated.

## Next Safe Step After Activation Recovery

After MWORKS activation/license is restored, rerun:

```powershell
$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$out = "Results\simulations\diagnostic_saidao1_open_tadynamics_mol_compileOptions0_1s_$ts"
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' Scripts\mworks\ugv_baseline_probe.py --project-root C:\Users\HP\Desktop\UGV --out-dir $out --model-name UGV.saidao.saidao1 --stop-time 1 --request-id M6-saidao1-open-tadynamics-mol-compileOptions0 --run-label diagnostic_saidao1_open_tadynamics_mol_compileOptions0 --controller-version controller_v5_front_dwell_2s --use-simulate-ex --relax-translation-checks --option compileOptions=0
```

If dependency loading and CheckModel pass, continue the SimulateModelEx option matrix and then all four official tracks.

## Work Not Claimed

- No four-track score is claimed.
- No final report readiness is claimed.
- No physical UGV readiness is claimed.
- No official no-edit zone was changed.
