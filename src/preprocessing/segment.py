import re

LEGAL_SPLIT_PATTERN = re.compile(
    r"""
    (?:
        (?<=\.)\s+(?=[A-Z]) |
        (?=\(\w+\)) |
        (?=\d+\.\d+) |
        (?=\d+\.)
    )
    """,
    re.VERBOSE
)

def split_into_paragraphs(text: str) -> list[str]:
    paragraphs = []
    current = []

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Detect section headings (short, title-case lines)
        if len(line.split()) <= 6 and line.isalpha():
            if current:
                paragraphs.append(" ".join(current))
                current = []
            current.append(line)
        else:
            current.append(line)

    if current:
        paragraphs.append(" ".join(current))

    return [p for p in paragraphs if len(p.split()) > 30]



# LEGAL_KEYWORDS = (
#     "shall", "must", "may", "will",
#     "is required to", "is subject to",
#     "could", "cannot", "agrees",
#     "liable", "responsible", "obligated"
# )

# def is_legal_clause(text: str) -> bool:
#     text_lower = text.lower()
#     return any(k in text_lower for k in LEGAL_KEYWORDS)

def split_paragraph_into_clauses(paragraph: str) -> list[str]:
    raw = re.split(LEGAL_SPLIT_PATTERN, paragraph)

    clauses = []
    for c in raw:
        c = c.strip()
        if len(c.split()) < 40:
            continue
        # if not is_legal_clause(c):
        #     continue
        clauses.append(c)

    return clauses
