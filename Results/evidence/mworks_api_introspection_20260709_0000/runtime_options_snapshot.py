import json
from pathlib import Path
import mworks.sysplorer as pyapi
out = {}
for name, func in [('ListSimulationOptions', pyapi.ListSimulationOptions), ('ListOptions', pyapi.ListOptions)]:
    try:
        out[name] = func()
    except Exception as exc:
        out[name] = {'error': f'{type(exc).__name__}: {exc}'}
for opt in ['Simulation.Optimization.RuntimeCheck', 'Simulation.CCompiler.CompilerType', 'Simulation.CCompiler.CompilerName', 'Environment.SystemPath.SimulationResultDirectory']:
    try:
        out['GetOption.' + opt] = pyapi.GetOption(opt, '')
    except Exception as exc:
        out['GetOption.' + opt] = {'error': f'{type(exc).__name__}: {exc}'}
Path('Results/evidence/mworks_api_introspection_20260709_0000/runtime_options_snapshot.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'ok': True, 'path': 'Results/evidence/mworks_api_introspection_20260709_0000/runtime_options_snapshot.json'}, ensure_ascii=False))
