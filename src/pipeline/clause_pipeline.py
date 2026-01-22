from src.ingestion.load_text import load_contract_text
from src.preprocessing.normalize import normalize_text
from src.preprocessing.segment import (
    split_into_paragraphs,
    split_paragraph_into_clauses,
)

def extract_clauses(file_path: str) -> list[str]:
    """
    Full clause extraction pipeline.
    """
    raw_text = load_contract_text(file_path)
    clean_text = normalize_text(raw_text)

    paragraphs = split_into_paragraphs(clean_text)

    clauses = []
    for para in paragraphs:
        clauses.extend(split_paragraph_into_clauses(para))

    return clauses
