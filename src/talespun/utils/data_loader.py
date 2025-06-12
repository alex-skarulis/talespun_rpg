from pathlib import Path
import ujson as json

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"

def load_index(index_name: str) -> list:
    index_path = DATA_DIR / index_name
    if not index_path.exists():
        raise FileNotFoundError(f"Index file not found: {index_path}")
    with open(index_path, "r") as f:
        return json.load(f)

def load_entry_from_index(index_name: str, entry_id: str) -> dict:
    index = load_index(index_name)
    entry = next((item for item in index if item["id"] == entry_id), None)
    if not entry:
        raise ValueError(f"Entry with id '{entry_id}' not found in {index_name}")
    entry_path = DATA_DIR / entry["file"]
    if not entry_path.exists():
        raise FileNotFoundError(f"Entry file not found: {entry_path}")
    with open(entry_path, "r") as f:
        return json.load(f)

def load_ancestry(ancestry_id: str) -> dict:
    return load_entry_from_index("ancestries.json", ancestry_id)
