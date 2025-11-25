"""
DAY 3 - BERT SENTIMENT CLASSIFICATION (FORCE PYTORCH ONLY)
"""

import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import torch
from transformers import pipeline

# Force PyTorch model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)

texts = [
    "I love this phone, it's absolutely amazing!",
    "This is the worst product I have ever bought.",
    "The performance is good but battery is weak.",
    "I feel very happy using this laptop."
]

print("\n===== BERT SENTIMENT CLASSIFICATION (PyTorch) =====\n")

for text in texts:
    result = classifier(text)[0]
    print(f"Text: {text}")
    print(f"Label: {result['label']} | Score: {result['score']:.4f}\n")

print("✔ BERT Sentiment Classification Completed!")
