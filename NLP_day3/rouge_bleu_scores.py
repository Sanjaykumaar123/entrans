"""
DAY 3 - ROUGE & BLEU SCORE IMPLEMENTATION
"""

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from transformers import pipeline
import evaluate
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import nltk

# Download NLTK data
nltk.download("punkt")

# --------------------------------------------------------
# Summarization Model
# --------------------------------------------------------
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    framework="pt"
)

text = """
Artificial intelligence is rapidly transforming industries across the world.
From healthcare to autonomous vehicles, AI systems are enabling automation,
improving accuracy, and revolutionizing the way people work. New advancements
in deep learning models, natural language processing, and computer vision
continue to expand AI's capabilities. Governments and companies are investing 
heavily in AI research to stay competitive in the global market.
"""

# Generate summary
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]

# Reference summary (gold standard)
reference = """
AI is transforming global industries through automation and advanced deep learning.
It is used in healthcare, vehicles, and many fields. Governments and companies are
investing heavily in AI research to stay competitive.
"""

print("\n===== GENERATED SUMMARY =====\n")
print(summary)

print("\n===== REFERENCE SUMMARY =====\n")
print(reference)


# --------------------------------------------------------
# 1. ROUGE SCORE (ROUGE-1, ROUGE-2, ROUGE-L)
# --------------------------------------------------------

rouge = evaluate.load("rouge")

result = rouge.compute(
    predictions=[summary],
    references=[reference]
)

print("\n===== ROUGE SCORES =====\n")
for key, value in result.items():
    print(f"{key}: {value:.4f}")


# --------------------------------------------------------
# 2. BLEU SCORE
# --------------------------------------------------------

smoothing = SmoothingFunction().method1
bleu_score = sentence_bleu(
    [reference.split()], summary.split(),
    smoothing_function=smoothing
)

print("\n===== BLEU SCORE =====\n")
print(f"BLEU Score: {bleu_score:.4f}")

print("\n✔ ROUGE & BLEU Score Evaluation Completed Successfully!")
