"""Lectures et analyses communes aux notebooks du Day 1."""
from pathlib import Path
from collections import Counter
import re
import pandas as pd
from textblob import TextBlob
ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
RESULTS = ROOT / 'results'
RESULTS.mkdir(exist_ok=True)

def load(dataset, filename=None, **kwargs):
    folder = DATA / dataset
    if filename is None:
        files = sorted(folder.glob('*.csv'))
        if len(files) != 1:
            raise ValueError(f'Préciser le fichier pour {dataset}: {files}')
        path = files[0]
    else:
        path = folder / filename
    return pd.read_csv(path, **kwargs)

def classify(df, mapping):
    assert set(df.columns) == set(mapping), (set(df.columns) - set(mapping), set(mapping) - set(df.columns))
    return pd.DataFrame([{'colonne': c, 'dtype pandas': str(df[c].dtype), 'type et justification': mapping[c]} for c in df])

def text_analysis(series):
    valid = series.dropna().astype(str)
    polarity = valid.map(lambda s: TextBlob(s).sentiment.polarity)
    label = polarity.map(lambda p: 'positif' if p > .1 else ('négatif' if p < -.1 else 'neutre'))
    stop = set('the a an and or to of is it in this that i my was for but with on are be not so very as have had me you they these we at from would'.split())
    words = Counter(w for s in valid.str.lower() for w in re.findall(r"[a-z]+", s) if len(w)>2 and w not in stop)
    return pd.DataFrame({'texte': valid, 'polarité': polarity, 'sentiment_estimé': label}), words
