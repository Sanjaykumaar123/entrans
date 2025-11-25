"""
Day 1 - NLP Basics using SpaCy
Includes:
- Tokenization
- Stopwords
- Lemmatization
- Naive Stemming (concept only, no NLTK)
- Named Entity Recognition (NER)
- Rule-based Matching
"""

import spacy
from spacy.matcher import Matcher, PhraseMatcher

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample text for all demos
TEXT = (
    "Apple is looking at buying a U.K. startup for $1 billion. "
    "Elon Musk tweeted about artificial intelligence. "
    "Runners were running fast yesterday."
)


def print_title(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# -------------------------------
# 1. Tokenization + Features
# -------------------------------
def demo_tokenization(text):
    print_title("1. TOKENIZATION + BASIC FEATURES")
    doc = nlp(text)

    print(f"{'TOKEN':15} {'LEMMA':15} {'POS':8} {'DEP':12} {'STOPWORD'}")
    print("-" * 70)

    for tok in doc:
        print(
            f"{tok.text:15} {tok.lemma_:15} {tok.pos_:8} "
            f"{tok.dep_:12} {tok.is_stop}"
        )


# -------------------------------
# 2. Stopwords
# -------------------------------
def demo_stopwords(text):
    print_title("2. STOPWORDS")
    doc = nlp(text)

    stopwords = [t.text for t in doc if t.is_stop]
    content = [t.text for t in doc if not t.is_stop]

    print("Stopwords:", stopwords)
    print("\nText without stopwords:")
    print(" ".join(content))


# -------------------------------
# 3. Naive Stemming (concept only)
# -------------------------------
def stem(word):
    suffixes = ["ing", "ed", "s"]
    for suf in suffixes:
        if word.endswith(suf) and len(word) > len(suf) + 2:
            return word[: -len(suf)]
    return word


def demo_stemming_vs_lemma():
    print_title("3. STEMMING (NAIVE) VS. LEMMATIZATION")

    words = ["running", "jogged", "cats", "better", "was"]
    doc = nlp(" ".join(words))

    print(f"{'WORD':12} {'STEM':10} {'LEMMA'}")
    print("-" * 40)

    for tok in doc:
        print(f"{tok.text:12} {stem(tok.text):10} {tok.lemma_}")


# -------------------------------
# 4. Named Entity Recognition
# -------------------------------
def demo_ner(text):
    print_title("4. NAMED ENTITY RECOGNITION")
    doc = nlp(text)

    for ent in doc.ents:
        print(f"{ent.text:25} --> {ent.label_}")


# -------------------------------
# 5. Rule-based Matching
# -------------------------------
def demo_rule_matching(text):
    print_title("5. RULE-BASED MATCHING")

    doc = nlp(text)
    matcher = Matcher(nlp.vocab)

    # Pattern: "artificial intelligence"
    pattern_ai = [{"LOWER": "artificial"}, {"LOWER": "intelligence"}]
    matcher.add("AI_PHRASE", [pattern_ai])

    # Pattern: "looking at buying"
    pattern_buying = [
        {"LEMMA": "look"},
        {"LOWER": "at"},
        {"LEMMA": "buy"},
    ]
    matcher.add("LOOKING_AT_BUYING", [pattern_buying])

    matches = matcher(doc)

    print("Matcher Results:")
    for match_id, start, end in matches:
        span = doc[start:end]
        print("-", span.text)

    # PhraseMatcher example
    phrase_matcher = PhraseMatcher(nlp.vocab)
    company_patterns = [nlp.make_doc("Apple"), nlp.make_doc("U.K. startup")]
    phrase_matcher.add("COMPANIES", company_patterns)

    pmatches = phrase_matcher(doc)
    print("\nPhraseMatcher Results:")
    for match_id, start, end in pmatches:
        span = doc[start:end]
        print("-", span.text)


# -------------------------------
# Run all demos
# -------------------------------
if __name__ == "__main__":
    demo_tokenization(TEXT)
    demo_stopwords(TEXT)
    demo_stemming_vs_lemma()
    demo_ner(TEXT)
    demo_rule_matching(TEXT)

    print("\n Day 1 SpaCy tasks completed successfully!")
