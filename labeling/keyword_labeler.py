def label_clause(text, taxonomy):
    labels = []
    lower = text.lower()

    for risk, patterns in taxonomy.items():
        for p in patterns:
            if p in lower:
                labels.append(risk)
                break

    return labels
