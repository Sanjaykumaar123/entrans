"""
DAY 2 - Bag of Words (BOW) + TF-IDF Implementation
Classification using Multinomial Naive Bayes
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Dataset (topic classification)
texts = [
    "Apple launches new iPhone with AI camera",
    "Google unveils quantum computer breakthrough",
    "The match was thrilling and full of energy",
    "Ronaldo scored a stunning goal",
    "Government passed a new education bill",
    "Prime Minister announced a new policy"
]

labels = [
    "TECH",
    "TECH",
    "SPORTS",
    "SPORTS",
    "POLITICS",
    "POLITICS"
]

# Test samples
test_texts = [
    "The new AI laptop is super fast",
    "Parliament members are voting today",
    "The football match was exciting",
]

test_labels = ["TECH", "POLITICS", "SPORTS"]

# ------------------------------
# 1. BAG OF WORDS IMPLEMENTATION
# ------------------------------
print("\n================ BOW CLASSIFICATION ================")

bow_vectorizer = CountVectorizer()
X_train_bow = bow_vectorizer.fit_transform(texts)
X_test_bow = bow_vectorizer.transform(test_texts)

model_bow = MultinomialNB()
model_bow.fit(X_train_bow, labels)

pred_bow = model_bow.predict(X_test_bow)

print("Predictions (BOW):", pred_bow)
acc_bow = accuracy_score(test_labels, pred_bow)
print("BOW Accuracy =", acc_bow * 100, "%")


# ------------------------------
# 2. TF-IDF IMPLEMENTATION
# ------------------------------
print("\n================ TF-IDF CLASSIFICATION ================")

tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(texts)
X_test_tfidf = tfidf_vectorizer.transform(test_texts)

model_tfidf = MultinomialNB()
model_tfidf.fit(X_train_tfidf, labels)

pred_tfidf = model_tfidf.predict(X_test_tfidf)

print("Predictions (TF-IDF):", pred_tfidf)
acc_tfidf = accuracy_score(test_labels, pred_tfidf)
print("TF-IDF Accuracy =", acc_tfidf * 100, "%")


# ------------------------------
# FINAL COMPARISON
# ------------------------------
print("\n================ FINAL COMPARISON ================")
print("BOW Accuracy:   ", round(acc_bow * 100, 2), "%")
print("TF-IDF Accuracy:", round(acc_tfidf * 100, 2), "%")

if acc_tfidf > acc_bow:
    print("\n✔ TF-IDF performed better")
else:
    print("\n✔ BOW performed better")
