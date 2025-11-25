"""
DAY 2 - TOPIC CLASSIFICATION USING SPACY (WORKING FOR SPACY 3.8+)
"""

import spacy
from spacy.training.example import Example
from spacy.util import minibatch
import random

# Blank pipeline
nlp = spacy.blank("en")

# Add textcat multilabel
textcat = nlp.add_pipe("textcat_multilabel")
textcat.add_label("TECH")
textcat.add_label("SPORTS")
textcat.add_label("POLITICS")

# Training dataset (small but enough for Day-2)
train_data = [
    ("Apple released a new iPhone with AI features.", {"cats": {"TECH": 1, "SPORTS": 0, "POLITICS": 0}}),
    ("Google announced a new quantum computer.", {"cats": {"TECH": 1, "SPORTS": 0, "POLITICS": 0}}),

    ("The football match yesterday was exciting.", {"cats": {"TECH": 0, "SPORTS": 1, "POLITICS": 0}}),
    ("Virat Kohli scored a century.", {"cats": {"TECH": 0, "SPORTS": 1, "POLITICS": 0}}),

    ("The government announced a new policy.", {"cats": {"TECH": 0, "SPORTS": 0, "POLITICS": 1}}),
    ("Elections will be held next month.", {"cats": {"TECH": 0, "SPORTS": 0, "POLITICS": 1}}),
]

optimizer = nlp.initialize()

# Training loop
for i in range(12):
    random.shuffle(train_data)
    losses = {}

    batches = minibatch(train_data, size=2)
    for batch in batches:
        examples = []
        for text, ann in batch:
            doc = nlp.make_doc(text)
            examples.append(Example.from_dict(doc, ann))

        nlp.update(examples, sgd=optimizer, losses=losses)

    print(f"Epoch {i+1} - Loss: {losses['textcat_multilabel']:.3f}")

# Test set
test_data = [
    ("AI will change smartphone technology.", "TECH"),
    ("Real Madrid won the Champions League.", "SPORTS"),
    ("The new law was passed by parliament.", "POLITICS"),
]

correct = 0

for text, actual in test_data:
    doc = nlp(text)
    scores = doc.cats

    predicted = max(scores, key=scores.get)

    print(f"\nText: {text}")
    print(f"Actual: {actual} | Predicted: {predicted}")

    if predicted == actual:
        correct += 1

accuracy = correct / len(test_data)
print(f"\nFINAL TOPIC CLASSIFICATION ACCURACY = {accuracy * 100:.2f}%")
print("\n✔ Topic Classification Completed Successfully!")
