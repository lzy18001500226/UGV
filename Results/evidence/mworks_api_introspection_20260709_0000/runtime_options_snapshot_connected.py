import json
from pathlib import Path
import mworks.sysplorer as pyapi
out = {'steps': []}
try:
    process_path = r'D:\Program Files\MWORKS\Sysplorer 2026a\Bin64\mworks.exe'
    pyapi.StartSysplorer(processPath=process_path, start_mode='-gui')
    out['steps'].append({'StartSysplorer': True})
    try:
        out['ListSimulationOptions'] = pyapi.ListSimulationOptions()
    except Exception as exc:
        out['ListSimulationOptions_error'] = f'{type(exc).__name__}: {exc}'
    try:
        out['ListOptions'] = pyapi.ListOptions()
    except Exception as exc:
        out['ListOptions_error'] = f'{type(exc).__name__}: {exc}'
    for opt in ['Simulation.Optimization.RuntimeCheck', 'Simulation.CCompiler.CompilerType', 'Simulation.CCompiler.CompilerName', 'Environment.SystemPath.SimulationResultDirectory']:
        try:
            out['GetOption.' + opt] = pyapi.GetOption(opt, '')
        except Exception as exc:
            out['GetOption.' + opt] = {'error': f'{type(exc).__name__}: {exc}'}
finally:
    try:
        pyapi.Exit()
        out['steps'].append({'Exit': True})
    except Exception as exc:
        out['steps'].append({'Exit_error': f'{type(exc).__name__}: {exc}'})
Path('Results/evidence/mworks_api_introspection_20260709_0000/runtime_options_snapshot_connected.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'ok': True, 'path': 'Results/evidence/mworks_api_introspection_20260709_0000/runtime_options_snapshot_connected.json'}, ensure_ascii=False))
