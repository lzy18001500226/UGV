"""Probe UGV load/check/simulate through the MWORKS Python API."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import traceback


def record_step(steps: list[dict], name: str, status: str, **extra) -> None:
    item = {"name": name, "status": status}
    item.update(extra)
    steps.append(item)
    print(json.dumps(item, ensure_ascii=False), flush=True)


def safe_json_value(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, (list, tuple)):
        return [safe_json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): safe_json_value(item) for key, item in value.items()}
    return repr(value)


def write_run_manifest(out_dir: Path, manifest: dict) -> None:
    lines = [
        f"# UGV Runtime Manifest - {manifest['run_label']}",
        "",
        f"request_id: {manifest['request_id']}",
        f"timestamp: {manifest['timestamp']}",
        f"model_root: {manifest['model_root']}",
        f"example_or_track: {manifest['example_or_track']}",
        f"controller_file: {manifest['controller_file']}",
        f"controller_version: {manifest['controller_version']}",
        f"runtime: {manifest['runtime']}",
        f"status: {manifest['status']}",
        f"completion: {manifest['completion']}",
        f"time_s: {manifest['time_s']}",
        f"road_collisions: {manifest['road_collisions']}",
        f"obstacle_collisions: {manifest['obstacle_collisions']}",
        f"avoidance_score: {manifest['avoidance_score']}",
        "",
        "## Artifacts",
        "",
    ]
    for artifact in manifest["artifacts"]:
        lines.append(f"- {artifact}")
    lines.extend(["", "## Blockers", ""])
    if manifest["blockers"]:
        for blocker in manifest["blockers"]:
            lines.append(f"- {blocker}")
    else:
        lines.append("- none")
    lines.extend(["", "## Notes", ""])
    for note in manifest["notes"]:
        lines.append(f"- {note}")
    lines.append("")
    (out_dir / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--model-name", default="UGV.Example.Race1")
    parser.add_argument("--stop-time", type=float, default=1.0)
    parser.add_argument("--request-id", default="M2-baseline-runtime-gate")
    parser.add_argument("--run-label", default="baseline")
    parser.add_argument(
        "--controller-version",
        default="official copied baseline; controller body not edited by this run",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    result_root = out_dir / "native_result"
    result_root.mkdir(parents=True, exist_ok=True)
    package_mo = project_root / "Models" / "UGV" / "package.mo"
    steps: list[dict] = []
    metrics: dict = {
        "request_id": args.request_id,
        "model_name": args.model_name,
        "stop_time_requested": args.stop_time,
        "source": "MWORKS_SYSPLORER_PYAPI",
        "runtime_status": "not_started",
        "completion": "unknown",
        "time_s": None,
        "road_collisions": None,
        "obstacle_collisions": None,
        "avoidance_score": None,
        "available_score_variables": [],
        "missing_score_variables": [],
        "simulation_exit_state": None,
        "simulation_state": None,
        "exported_csv": None,
        "exported_csv_ok": False,
        "notes": [],
    }
    sysplorer_started = False
    pyapi = None
    return_code = 1

    try:
        record_step(
            steps,
            "preflight_paths",
            "ok" if package_mo.exists() else "blocked",
            package_mo=str(package_mo),
            result_root=str(result_root),
        )
        if not package_mo.exists():
            return_code = 2
            return return_code

        import mworks.sysplorer as pyapi_module  # type: ignore
        pyapi = pyapi_module

        record_step(steps, "import_mworks_sysplorer", "ok", module=str(pyapi))

        process_path = r"D:\Program Files\MWORKS\Sysplorer 2026a\Bin64\mworks.exe"
        pyapi.StartSysplorer(processPath=process_path, start_mode="-gui")
        sysplorer_started = True
        record_step(steps, "start_sysplorer", "ok", process_path=process_path)

        load_result = pyapi.OpenModelFile(str(package_mo), True)
        record_step(steps, "open_model_file", "ok" if load_result else "failed", result=repr(load_result))
        if not load_result:
            return_code = 3
            return return_code

        try:
            open_result = pyapi.OpenModel(args.model_name, pyapi.ModelView.Diagram)
        except Exception as exc:  # noqa: BLE001
            open_result = None
            record_step(steps, "open_model", "exception", error=repr(exc))
        else:
            record_step(steps, "open_model", "ok" if open_result else "failed", result=repr(open_result))

        check_result = pyapi.CheckModel(args.model_name)
        record_step(steps, "check_model", "ok" if check_result else "failed", result=repr(check_result))
        if not check_result:
            return_code = 4
            return return_code

        sim_kwargs = {
            "modelName": args.model_name,
            "startTime": 0,
            "stopTime": args.stop_time,
            "path": str(result_root),
        }
        sim_result = pyapi.SimulateModel(**sim_kwargs)
        metrics["runtime_status"] = "simulate_returned_true" if sim_result else "simulate_failed"
        record_step(
            steps,
            "simulate_model",
            "ok" if sim_result else "failed",
            result=repr(sim_result),
            kwargs=sim_kwargs,
        )
        if not sim_result:
            return_code = 5
            return return_code

        try:
            metrics["simulation_exit_state"] = safe_json_value(pyapi.GetSimulationExitState())
            metrics["simulation_state"] = safe_json_value(pyapi.GetSimulationState())
            record_step(
                steps,
                "simulation_state",
                "ok",
                exit_state=metrics["simulation_exit_state"],
                simulation_state=metrics["simulation_state"],
            )
        except Exception as exc:  # noqa: BLE001
            record_step(steps, "simulation_state", "exception", error=repr(exc))

        score_vars = ["T", "cR", "cO", "P"]
        try:
            all_vars = list(pyapi.GetResultVariables(0))
            time_vars = list(pyapi.GetResultVariables(2))
            available = [name for name in score_vars if name in all_vars]
            missing = [name for name in score_vars if name not in all_vars]
            metrics["available_score_variables"] = available
            metrics["missing_score_variables"] = missing
            (out_dir / "result_variables_summary.json").write_text(
                json.dumps(
                    {
                        "all_variable_count": len(all_vars),
                        "timevarying_variable_count": len(time_vars),
                        "available_score_variables": available,
                        "missing_score_variables": missing,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            record_step(
                steps,
                "result_variables",
                "ok",
                total=len(all_vars),
                timevarying=len(time_vars),
                available_score_variables=available,
                missing_score_variables=missing,
            )
        except Exception as exc:  # noqa: BLE001
            all_vars = []
            available = []
            missing = score_vars
            metrics["missing_score_variables"] = missing
            record_step(steps, "result_variables", "exception", error=repr(exc))

        if available:
            try:
                values = pyapi.GetVarsValueAt(available, pyapi.SimulationTime.End)
                score_map = dict(zip(available, safe_json_value(values)))
                metrics["score_values_at_end"] = score_map
                metrics["time_s"] = score_map.get("T")
                metrics["road_collisions"] = score_map.get("cR")
                metrics["obstacle_collisions"] = score_map.get("cO")
                metrics["avoidance_score"] = score_map.get("P")
                metrics["completion"] = "bounded_stop_or_assertion; inspect exit_state/logs"
                record_step(steps, "score_values_at_end", "ok", values=score_map)
            except Exception as exc:  # noqa: BLE001
                record_step(steps, "score_values_at_end", "exception", error=repr(exc))

            try:
                csv_path = out_dir / "score_timeseries.csv"
                export_ok = pyapi.ExportResult(str(csv_path), "csv", available, False)
                metrics["exported_csv"] = str(csv_path)
                metrics["exported_csv_ok"] = bool(export_ok)
                record_step(steps, "export_score_timeseries", "ok" if export_ok else "failed", path=str(csv_path))
            except Exception as exc:  # noqa: BLE001
                record_step(steps, "export_score_timeseries", "exception", error=repr(exc))

        return_code = 0
        return return_code
    except Exception as exc:  # noqa: BLE001
        record_step(steps, "exception", "failed", error=repr(exc), traceback=traceback.format_exc())
        return_code = 1
        return return_code
    finally:
        try:
            if sysplorer_started and pyapi is not None:
                pyapi.Exit()
                record_step(steps, "engine_exit", "ok")
        except Exception as exc:  # noqa: BLE001
            record_step(steps, "engine_exit", "exception", error=repr(exc))

        metrics_path = out_dir / "metrics.json"
        metrics_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")

        probe_manifest = {
            "project_root": str(project_root),
            "out_dir": str(out_dir),
            "model_name": args.model_name,
            "python_executable": sys.executable,
            "cwd": os.getcwd(),
            "return_code": return_code,
            "steps": steps,
        }
        (out_dir / "probe_steps.json").write_text(
            json.dumps(probe_manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        status = "bounded_runtime_gate" if metrics["runtime_status"] == "simulate_returned_true" else "blocked"
        blockers = [] if status == "bounded_runtime_gate" else [metrics["runtime_status"]]
        if metrics["missing_score_variables"]:
            blockers.append("score variables missing or unreadable: " + ", ".join(metrics["missing_score_variables"]))
        write_run_manifest(
            out_dir,
            {
                "run_label": args.run_label,
                "request_id": args.request_id,
                "timestamp": out_dir.name.replace("baseline_", ""),
                "model_root": str(project_root / "Models" / "UGV"),
                "example_or_track": args.model_name,
                "controller_file": str(project_root / "Models" / "UGV" / "Control" / "ObstacleAvoidanceController" / "ObsAvoidController_Sysblock2.mo"),
                "controller_version": args.controller_version,
                "runtime": "MWORKS Sysplorer 2026a Python API",
                "status": status,
                "completion": metrics["completion"],
                "time_s": metrics["time_s"],
                "road_collisions": metrics["road_collisions"],
                "obstacle_collisions": metrics["obstacle_collisions"],
                "avoidance_score": metrics["avoidance_score"],
                "artifacts": [
                    "probe_steps.json",
                    "metrics.json",
                    "stdout_or_log.txt",
                    "native_result/",
                    "result_variables_summary.json when available",
                    "score_timeseries.csv when export succeeds",
                ],
                "blockers": blockers,
                "notes": [
                    f"This run label is {args.run_label}.",
                    "SimulateModel=True proves load/check/simulation API path for the bounded stop time only.",
                    "Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.",
                ],
            },
        )


if __name__ == "__main__":
    raise SystemExit(main())
