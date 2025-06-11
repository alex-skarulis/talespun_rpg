from pathlib import Path
import ujson as json

DATA_DIR = Path(__file__).parent / "data"

def load_ancestries():
    ancestry_path = DATA_DIR / "ancestries.json"
    return json.loads(ancestry_path.read_text())

def get_ancestry_by_name(name: str):
    ancestries = load_ancestries()
    for ancestry in ancestries:
        if ancestry["name"].lower() == name.lower():
            return ancestry
    raise ValueError(f"Ancestry '{name}' not found.")