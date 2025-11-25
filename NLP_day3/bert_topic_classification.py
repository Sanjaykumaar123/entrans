"""
DAY 3 - BERT ZERO-SHOT TOPIC CLASSIFICATION (HUGGINGFACE)
No training required!
"""

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from transformers import pipeline

# Load Zero-Shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    framework="pt"
)

print("\n===== BERT ZERO-SHOT TOPIC CLASSIFICATION =====\n")

texts = [
    "Apple announced a new AI-powered MacBook.",
    "Virat Kohli scored a brilliant century in yesterday's match.",
    "The government passed a new healthcare policy.",
    "Scientists discovered a new exoplanet near Proxima Centauri."
]

candidate_labels = ["TECH", "SPORTS", "POLITICS", "SPACE", "HEALTH"]

for text in texts:
    result = classifier(text, candidate_labels)
    print(f"Text: {text}")
    print(f"Predicted Topic: {result['labels'][0]}  (Score: {result['scores'][0]:.4f})\n")

print("✔ Zero-Shot Topic Classification Completed!")
