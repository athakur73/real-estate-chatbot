import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_json(filename: str):
    with open(DATA_DIR / filename, "r") as f:
        return json.load(f)

def load_all_properties():
    basics = load_json("property_basics.json")
    images = load_json("property_images.json")
    characteristics = load_json("property_characteristics.json")

    images_map = {i["id"]: i for i in images}
    char_map = {c["id"]: c for c in characteristics}

    merged = []
    for prop in basics:
        pid = prop["id"]
        merged.append({
            **prop,
            **images_map.get(pid, {}),
            **char_map.get(pid, {})
        })

    return merged
