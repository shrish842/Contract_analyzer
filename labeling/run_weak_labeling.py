import json
from pathlib import Path

from taxonomy.risk_taxonomy import RISK_LABELS
from labeling.keyword_labeler import label_clause

INPUT_PATH = "data/processed/cleaned/clauses.json"
OUTPUT_PATH = "data/weak_labels/clauses.json"

def main():
    # load clauses
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        clauses = json.load(f)

    labeled = []

    for c in clauses:
        text = c["text"]
        labels = label_clause(text, RISK_LABELS)

        labeled.append({
            "text": text,
            "labels": labels,
            "source": c.get("source", "unknown")
        })

    # ensure output directory exists
    Path("data/weak_labels").mkdir(parents=True, exist_ok=True)

    # save weak labels
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(labeled, f, indent=2)

    print(f"Saved {len(labeled)} labeled clauses to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
