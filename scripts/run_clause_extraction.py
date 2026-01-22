from src.pipeline.clause_pipeline import extract_clauses
from src.utils.io_utils import save_clauses

RAW_FILE = "data/raw/apple_extracted_contracts.txt"
OUTPUT_FILE = "data/processed/apple_clauses.json"

def main():
    clauses = extract_clauses(RAW_FILE)
    print(f"Extracted {len(clauses)} clauses")

    save_clauses(clauses, OUTPUT_FILE)
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
