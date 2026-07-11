# MWORKS UGV Simulation Workflow

## 1. Purpose

Run the official UGV obstacle-avoidance model in MWORKS.Sysplorer and collect
reproducible evidence for baseline and controller versions.

## 2. Preflight

Before live work:

1. Confirm the current plan has not explicitly paused runtime work.
2. Confirm MWORKS 2026a / Sysplorer 26.3 is available.
3. If login/license/activation appears, recover autonomously only when the
   current task/user/project document names an approved credential path. Do not
   store credentials in docs, logs, evidence, or command history. Capture
   redacted evidence, then send a short Chinese notice if an approved email
   route exists; otherwise record the notice text in evidence. Unknown,
   CAPTCHA/MFA, or repeatedly rejected credential states become blockers.
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
as `L5104-B0`, first run the bounded GUI recovery below before declaring a
blocker. Do not treat the Chinese text "登录失败，请检查网络后重试" as a network
blocker by default; first verify the real Sysplorer window, real login button,
account/password fields, and license activation state.

### Login / License Recovery For `L5104-B0`

Use this exact sequence when the project has an approved credential path and
MWORKS is blocking dependency loads:

1. Bring the real `Sysplorer` window to an inspectable state. Do not operate a
   hidden WebView or stale window handle when the visible top-right UI still
   says `登录`.
2. Open `帮助 -> 使用许可` if the license dialog is not already visible.
3. If the license dialog says `账号：未登录`, click the real `登录` button.
4. In the login window, use `账号密码登录`, fill `用户名/邮箱` and `密码` from the
   approved in-memory credential source, keep the existing agreement checkbox
   selected when it is already checked, then click the real `登 录` button.
5. Wait for the Sysplorer title or account area to show `教育版` / the account
   avatar. If the dialog exposes `激活`, click it once and wait for
   `激活成功`.
6. Close the license dialog or return to the main Sysplorer window.
7. Immediately verify the recovery with a 1 s API probe. GUI success alone is
   not enough.

Minimal verification command:

```powershell
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' `
  Scripts\mworks\ugv_baseline_probe.py `
  --project-root C:\Users\HP\Desktop\UGV `
  --out-dir Results\simulations\license_gui_confirm_1s_<timestamp> `
  --model-name UGV.Test.Saidao2Eval `
  --stop-time 1 `
  --request-id license-gui-confirm `
  --run-label license_gui_confirm `
  --controller-version controller_v5_bounded_linear_deployability `
  --use-simulate-ex `
  --relax-translation-checks `
  --option compileOptions=0
```

Recovery is complete only when the probe records:

```text
open_dependency_model_file: ok
open_model_file: ok
open_model: ok
check_model: ok
simulate_model: ok
available_score_variables include T, cR, cO, P
```

If GUI shows `教育版` / `激活成功` but the API still reports `L5104-B0`, close
the license dialog and retry the 1 s probe once. If it still fails, restart only
the MWORKS/Sysplorer runtime and its Sysplorer API helper processes when safe;
do not restart Codex or unrelated tools. After restart, repeat the real
login-button flow above and re-run the same 1 s probe.

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

`Scripts/mworks/ugv_baseline_probe.py` intentionally attempts result-variable
extraction even when `SimulateModel` / `SimulateModelEx` returns `False`. Some
MWORKS model terminal states return `False` while still leaving readable
`T/cR/cO/P` variables and exportable score timeseries. Treat those runs as:

```text
runtime_status = simulate_failed
completion = finish_reached_official_origin_assertion only when all are true:
  SimulateModel returned false, T > 10, and distanceSensor1.d < 0.02 at termination
```

Readable `T/cR/cO/P` after a false return are usable review evidence, but a
false return is not automatically a completed track. The probe records
`early_stop_finish_not_observed` unless the three-part official finish rule is
met. Conversely, `simulate_returned_true` is always
`simulation_horizon_reached_finish_not_observed`, even if the terminal sample
is close to the origin. It must not be reported as an ordinary clean
simulation return or an official finish.

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
