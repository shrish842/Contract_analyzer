from collections import Counter
import json

data = json.load(open("data/weak_labels/clauses.json"))

counter = Counter()
for c in data:
    for label in c["labels"]:
        counter[label] += 1

print(counter)
