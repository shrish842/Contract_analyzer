import sys
from pathlib import Path
import random

# Path fix
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.pipeline.clause_pipeline import extract_clauses

clauses = extract_clauses("data/raw/apple_extracted_contracts.txt")

print("Total clauses:", len(clauses))

print("\n--- SAMPLE CLAUSES ---\n")
for _ in range(5):
    clause = random.choice(clauses)
    print("=" * 80)
    print(f"Word count: {len(clause.split())}")
    print(clause[:1200])  # limit printing
