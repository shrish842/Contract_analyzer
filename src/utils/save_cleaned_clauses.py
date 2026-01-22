import json
from pathlib import Path
from typing import List, Dict

def save_cleaned_clauses(
    clauses: List[str],
    output_path: str,
    source: str
) -> None:
    """
    Save cleaned clause / risk-unit data to JSON.

    Args:
        clauses: list of cleaned text clauses
        output_path: target JSON file path
        source: document source metadata
    """

    records: List[Dict] = []

    for idx, clause in enumerate(clauses):
        records.append({
            "id": idx,
            "text": clause,
            "word_count": len(clause.split()),
            "source": source
        })

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
