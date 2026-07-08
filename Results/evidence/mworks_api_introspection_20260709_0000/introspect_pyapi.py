import inspect, json
from pathlib import Path
import mworks.sysplorer as pyapi
names = sorted([n for n in dir(pyapi) if not n.startswith('__')])
interesting = [n for n in names if any(k.lower() in n.lower() for k in ['Simulate','Translate','Option','Parameter','Model','Setting','Compiler','Check','Message','Error'])]
summary = {'module': repr(pyapi), 'interesting_names': interesting}
for name in interesting:
    obj = getattr(pyapi, name, None)
    item = {'repr': repr(obj), 'type': type(obj).__name__}
    try:
        item['signature'] = str(inspect.signature(obj))
    except Exception as exc:
        item['signature_error'] = f'{type(exc).__name__}: {exc}'
    try:
        item['doc'] = inspect.getdoc(obj)
    except Exception as exc:
        item['doc_error'] = f'{type(exc).__name__}: {exc}'
    summary[name] = item
Path('Results/evidence/mworks_api_introspection_20260709_0000/pyapi_introspection.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'ok': True, 'count': len(interesting), 'path': 'Results/evidence/mworks_api_introspection_20260709_0000/pyapi_introspection.json'}, ensure_ascii=False))
