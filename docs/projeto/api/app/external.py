# função que busca dados de terceiros

import os
import json

def fetch_data():
    # Caminho para o JSON que você acabou de criar
    base = os.path.dirname(__file__)           # api/app
    path = os.path.join(base, "bovespa.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)
    

