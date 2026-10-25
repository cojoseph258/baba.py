"""Télécharger les archives fournies par Octopus (Git LFS) et les extraire localement."""
from pathlib import Path
from urllib.parse import quote
import hashlib, io, json, zipfile
import requests
ROOT = Path(__file__).resolve().parent

def download():
    root = ROOT / 'data'
    root.mkdir(exist_ok=True)
    records = []
    for name, path in json.loads((ROOT / 'datasets.json').read_text()).items():
        target = root / name
        if target.exists() and any(target.iterdir()):
            continue
        url = 'https://media.githubusercontent.com/media/devtlv/Datasets-DA-Bootcamp-2-/main/' + quote(path)
        response = requests.get(url, timeout=300)
        response.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
            target.mkdir(exist_ok=True)
            for member in archive.infolist():
                if not member.is_dir():
                    (target / Path(member.filename).name).write_bytes(archive.read(member))
        records.append({'dataset': name, 'url': url, 'sha256': hashlib.sha256(response.content).hexdigest()})
        print(name)
    insurance = root / 'insurance.csv'
    if not insurance.exists():
        response = requests.get('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv', timeout=60)
        response.raise_for_status()
        insurance.write_bytes(response.content)
    if records:
        (root / 'downloads.json').write_text(json.dumps(records, indent=2))

if __name__ == '__main__':
    download()
