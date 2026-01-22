import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ingestion.load_text import load_contract_text
from src.preprocessing.normalize import normalize_text

RAW_FILE = "data/raw/apple_extracted_contracts.txt"

print("Loading text...")
text = load_contract_text(RAW_FILE)

print("Raw text length:", len(text))
print("\nFirst 300 characters:\n")
print(text[:300])

print("\nNormalizing text...")
clean_text = normalize_text(text)

print("Clean text length:", len(clean_text))
print("\nFirst 300 characters after normalization:\n")
print(clean_text[:300])
