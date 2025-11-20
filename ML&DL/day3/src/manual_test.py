import json
import joblib
import pandas as pd
from src.config import MODEL_PATH, MEDIANS_PATH

model = joblib.load(MODEL_PATH)
with open(MEDIANS_PATH) as f:
    medians = json.load(f)

def get_value(prompt, key):
    raw = input(prompt)
    if raw.strip() == "":
        return float(medians[key])
    return float(raw)

print("House Price Manual Tester")
print("Press Enter to use median value for any field.\n")

while True:
    ans = input("Test a house? (y/n): ").lower()
    if ans != "y":
        break

    bedrooms = get_value("Bedrooms: ", "bedrooms")
    bathrooms = get_value("Bathrooms: ", "bathrooms")
    sqft = get_value("Sqft living: ", "sqft_living")
    lat = get_value("Latitude: ", "lat")
    long = get_value("Longitude: ", "long")

    row = pd.DataFrame([{
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft,
        "lat": lat,
        "long": long
    }])

    pred = model.predict(row)[0]
    print(f"Predicted price: ${pred:,.0f}\n")
