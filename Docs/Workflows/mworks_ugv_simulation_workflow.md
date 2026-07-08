# MWORKS UGV Simulation Workflow

## 1. Purpose

Run the official UGV obstacle-avoidance model in MWORKS.Sysplorer and collect
reproducible evidence for baseline and controller versions.

## 2. Preflight

Before live work:

1. Confirm the current plan has not explicitly paused runtime work.
2. Confirm MWORKS 2026a / Sysplorer 26.3 is available.
3. If login/license/activation appears, recover autonomously only when the
   current task/user/project document names an approved credential path. Capture
   redacted evidence, then send a short Chinese notice if an approved email
   route exists; otherwise record the notice text in evidence. Unknown or
   repeatedly failed credential states become blockers.
4. Confirm M1 static model grounding has produced a source evidence note unless
   the user explicitly asks for a runtime-only diagnostic.
5. Load the package from:

```text
Models/UGV/package.mo
```

Official track models depend on the installed MWORKS vehicle dynamics library:

```text
D:\Program Files\MWORKS\Sysplorer 2026a\Library\TADynamics 1.3.2\TADynamics\TADynamics.mol
```

`Scripts/mworks/ugv_baseline_probe.py` opens this dependency before the UGV
package by default. If loading it returns an activation or license error such
as `L5104-B0`, stop the runtime phase and record a license/activation blocker.
Do not continue controller tuning or official-track diagnosis until MWORKS can
load the dependency library.

## 3. Baseline Gate G0

1. Open `UGV.Example.Race1`.
2. Inspect the diagram and confirm the red-frame obstacle-avoidance controller.
3. Record the controller path and interface.
4. Attempt translate/simulate when the baseline runtime phase is active.
5. Save evidence under:

```text
Results/simulations/baseline_<timestamp>/
```

Required evidence:

```text
MANIFEST.md
stdout_or_log.txt
API model evidence or screenshot_or_model_evidence.png
metrics.json when available
```

Project-local baseline helper:

```powershell
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' \
  Scripts\mworks\ugv_baseline_probe.py \
  --project-root C:\Users\HP\Desktop\UGV \
  --out-dir Results\simulations\baseline_<timestamp> \
  --model-name UGV.Example.Race1 \
  --stop-time 12 \
  --request-id M2-baseline-runtime-gate
```

The helper uses `import mworks.sysplorer as pyapi`, then
`StartSysplorer`, dependency `OpenModelFile` for installed `.mol` libraries,
project `OpenModelFile`, `OpenModel`, `CheckModel`, `SimulateModel`,
`GetResultVariables`, `GetVarsValueAt`, and `ExportResult`.
Do not use the nonexistent `mworks.engine` API shape.

The helper also supports:

```text
--option key=value
--load-library name[:version]
--load-model-file path
--no-default-dependency-model-files
```

Use these only for bounded diagnostics and keep each run's evidence under
`Results/simulations/`.

## 4. Algorithm Gate G2

For each controller version:

1. Record the edited file and short algorithm summary.
2. Run one selected track first.
3. Extract or manually record:
   - completion status
   - travel time
   - road collision count
   - obstacle collision count
   - avoidance score
4. Compare against baseline.
5. If the run fails to load, translate, simulate, or complete one lap, write a
   blocker manifest instead of claiming success. Before declaring a blocker,
   inspect the available MWORKS log/error text, local model source, official
   docs, and targeted community notes when safe; record bounded recovery attempts
   in the manifest.

## 5. Four-Track Gate G3

When one-track behavior is acceptable:

1. Run all 4 official tracks.
2. Use one result folder per run.
3. Write a summary table in:

```text
Results/metrics/four_track_summary_<timestamp>.md
```

Minimum columns:

```text
track, controller_version, completion, time_s, road_collisions,
obstacle_collisions, avoidance_score, notes, evidence_path
```

## 6. Do Not

1. Do not edit official materials.
2. Do not modify scoring to improve result.
3. Do not replace the UGV runtime with an unrelated simulator.
4. Do not present screenshots without metrics as score evidence.
5. Do not continue unbounded waits on failed live runtime operations.
6. Do not skip M1 source grounding and controller-interface confirmation just to
   get a quick screenshot.
