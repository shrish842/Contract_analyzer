from pathlib import Path

def load_contract_text(file_path: str) -> str:
    """
    Load raw contract text from a file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8", errors="ignore")
