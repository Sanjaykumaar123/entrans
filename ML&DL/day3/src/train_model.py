import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
from src.config import DATA_PATH, MODEL_PATH, MEDIANS_PATH


os.makedirs(MODEL_PATH.parent, exist_ok=True)

print("Training started...")

df = pd.read_csv(DATA_PATH)

cols = ["price", "bedrooms", "bathrooms", "sqft_living", "lat", "long"]
df = df[cols].dropna()

X = df[["bedrooms", "bathrooms", "sqft_living", "lat", "long"]]
y = df["price"]

medians = X.median().to_dict()
with open(MEDIANS_PATH, "w") as f:
    json.dump(medians, f)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: {mae:,.0f}")

joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
print(f"Medians saved to {MEDIANS_PATH}")
