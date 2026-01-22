import sys
from pathlib import Path

# Fix import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.pipeline.clause_pipeline import extract_clauses
from src.utils.save_cleaned_clauses import save_cleaned_clauses

RAW_FILE = "data/raw/apple_extracted_contracts.txt"
OUTPUT_FILE = "data/processed/cleaned/clauses.json"
SOURCE_NAME = "Apple 10-K 2022"

def main():
    clauses = extract_clauses(RAW_FILE)

    print(f"Extracted {len(clauses)} cleaned risk units")

    save_cleaned_clauses(
        clauses=clauses,
        output_path=OUTPUT_FILE,
        source=SOURCE_NAME
    )

    print(f"Saved cleaned clauses to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
