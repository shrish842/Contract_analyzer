import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.pipeline.clause_pipeline import extract_clauses

clauses = extract_clauses("data/raw/apple_extracted_contracts.txt")
print("Clauses:", len(clauses))
