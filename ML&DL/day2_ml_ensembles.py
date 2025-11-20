import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# -----------------------------------------------------
# CREATE SIMPLE DATASET (Easy for manual verification)
# Rule: label = 1 if (f1 + f2 >= 10), else 0
# -----------------------------------------------------

data = {
    "f1": [2,3,4,6,7,8,5,9,1,10],
    "f2": [3,1,5,4,6,3,5,2,8,1],
}
df = pd.DataFrame(data)
df["label"] = (df["f1"] + df["f2"] >= 10).astype(int)

X = df[["f1", "f2"]]
y = df["label"]

# -----------------------------------------------------
# TRAIN ALL MODELS
# -----------------------------------------------------

models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=50),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(),
    "Bagging": BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=20),
    "AdaBoost": AdaBoostClassifier(n_estimators=30),
    "Gradient Boosting": GradientBoostingClassifier()
}

for name, model in models.items():
    model.fit(X, y)

print("\nAll models trained successfully!")

# -----------------------------------------------------
# MANUAL INPUT LOOP
# -----------------------------------------------------

while True:
    print("\nEnter feature values manually (type 'exit' to stop):")
    
    f1_input = input("Enter Feature 1 value: ")
    if f1_input.lower() == "exit":
        break
    
    f2_input = input("Enter Feature 2 value: ")
    if f2_input.lower() == "exit":
        break

    f1 = float(f1_input)
    f2 = float(f2_input)

    manual_label = 1 if (f1 + f2 >= 10) else 0

    print("\nManual Calculation:")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"Manual Label = {manual_label}")

    print("\n--- MODEL PREDICTIONS ---")
    for name, model in models.items():
        inp = pd.DataFrame([[f1, f2]], columns=["f1", "f2"])
        pred = model.predict(inp)[0]
        print(f"{name}: Predicted = {pred} | Correct? {pred == manual_label}")