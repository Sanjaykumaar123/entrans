"""
DAY 3 - SUMMARIZATION USING HUGGINGFACE (BART)
"""

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from transformers import pipeline

# Load summarizer model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    framework="pt"
)

text = """
Apple announced the release of its new MacBook powered with an AI-accelerated M4 chip.
The new laptop promises 10x faster performance compared to previous models, improved
battery life lasting up to 20 hours, and advanced neural engines for machine learning tasks.
Developers will also gain access to upgraded APIs, and Apple claims this is the 
biggest leap in laptop innovation in over a decade.
"""

print("\n===== BERT SUMMARIZATION (BART-LARGE-CNN) =====\n")

summary = summarizer(text, max_length=80, min_length=20, do_sample=False)[0]["summary_text"]

print("Original Text:\n", text)
print("\nSummary:\n", summary)

print("\n Summarization Completed Successfully!")
