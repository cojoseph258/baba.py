"""Exécuter et sauvegarder tous les notebooks, arrêt immédiat à la première erreur."""
from pathlib import Path
import json, os, sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
ROOT = Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / 'data' / '.matplotlib'))
report = []
paths = [ROOT / arg for arg in sys.argv[1:]] if len(sys.argv)>1 else sorted(ROOT.rglob('*.ipynb'))
for path in paths:
    if '.ipynb_checkpoints' in str(path):
        continue
    nb = nbformat.read(path, as_version=4)
    km = KernelManager(kernel_name='python3')
    km.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    client = NotebookClient(nb, km=km, timeout=600, resources={'metadata':{'path':str(path.parent)}})
    try:
        client.execute()
    finally:
        if km.has_kernel:
            km.shutdown_kernel(now=True)
    nbformat.write(nb, path)
    count = sum(cell.cell_type == 'code' for cell in nb.cells)
    report.append({'notebook':str(path.relative_to(ROOT)), 'code_cells':count, 'status':'passed'})
    print(f'OK {path.relative_to(ROOT)} ({count} cellules)', flush=True)
report_path = ROOT / 'results' / 'validation.json'
if len(sys.argv)>1:
    # Include only verified saved notebooks, never assume an unexecuted file passed.
    for saved in sorted(ROOT.rglob('*.ipynb')):
        if saved not in paths:
            existing = nbformat.read(saved, as_version=4)
            code = [c for c in existing.cells if c.cell_type=='code']
            if code and all(c.execution_count is not None and not any(o.output_type=='error' for o in c.outputs) for c in code):
                report.append({'notebook':str(saved.relative_to(ROOT)), 'code_cells':len(code), 'status':'passed'})
report_path.write_text(json.dumps(report,indent=2))
