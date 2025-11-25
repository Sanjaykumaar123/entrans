"""
DAY 2 - SENTIMENT CLASSIFICATION USING SPACY (WORKING FOR SPACY 3.8+)
"""

import spacy
from spacy.training.example import Example
from spacy.util import minibatch
import random

# Create blank English pipeline
nlp = spacy.blank("en")

# Add text classifier
textcat = nlp.add_pipe("textcat_multilabel")
textcat.add_label("POSITIVE")
textcat.add_label("NEGATIVE")

# Training data
train_data = [
    ("I love this phone, it's amazing", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("This is the best product ever", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("I hate this phone", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("This is the worst item I bought", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
    ("The laptop has excellent build quality", {"cats": {"POSITIVE": 1, "NEGATIVE": 0}}),
    ("Battery life is horrible", {"cats": {"POSITIVE": 0, "NEGATIVE": 1}}),
]

optimizer = nlp.initialize()

# Training loop
for i in range(12):
    random.shuffle(train_data)
    losses = {}

    batches = minibatch(train_data, size=2)
    for batch in batches:
        texts = [text for text, ann in batch]
        cats = [ann for text, ann in batch]

        # Convert to Example objects
        examples = []
        for text, ann in batch:
            doc = nlp.make_doc(text)
            examples.append(Example.from_dict(doc, ann))

        nlp.update(examples, sgd=optimizer, losses=losses)

    print(f"Epoch {i+1} - Loss: {losses['textcat_multilabel']:.3f}")

# TESTING
test_data = [
    ("I love this laptop", "POSITIVE"),
    ("This phone is horrible", "NEGATIVE"),
    ("Amazing performance", "POSITIVE"),
    ("Worst camera experience", "NEGATIVE"),
]

correct = 0

for text, actual in test_data:
    doc = nlp(text)
    scores = doc.cats

    predicted = "POSITIVE" if scores["POSITIVE"] > scores["NEGATIVE"] else "NEGATIVE"

    print(f"\nText: {text}")
    print(f"Actual: {actual} | Predicted: {predicted}")

    if predicted == actual:
        correct += 1

accuracy = correct / len(test_data)
print(f"\nFINAL ACCURACY: {accuracy * 100:.2f}%")
print("\n✔ SpaCy Sentiment Model Completed Successfully!")
