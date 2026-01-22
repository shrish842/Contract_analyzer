import json
from pathlib import Path

def save_clauses(clauses: list[str], output_path: str):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clauses, f, indent=2, ensure_ascii=False)
