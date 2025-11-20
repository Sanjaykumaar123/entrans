import json
import sqlite3
from datetime import datetime

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.config import DATA_PATH, MODEL_PATH, MEDIANS_PATH, DB_PATH

app = FastAPI(title="House Price API")

# CORS enable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model + medians
model = joblib.load(MODEL_PATH)
with open(MEDIANS_PATH) as f:
    medians = json.load(f)

df_full = pd.read_csv(DATA_PATH)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            bedrooms REAL,
            bathrooms REAL,
            sqft_living REAL,
            lat REAL,
            long REAL,
            predicted_price REAL
        )
    """)
    return conn

class HouseFeatures(BaseModel):
    n_bed: float | None = None
    n_bath: float | None = None
    sqft: float | None = None
    lat: float | None = None
    long: float | None = None


@app.get("/descriptive")
def descriptive_stats():
    cols = ["price", "bedrooms", "bathrooms", "sqft_living", "lat", "long"]
    desc = df_full[cols].describe().to_dict()
    return {"descriptive": desc}


@app.get("/inferential")
def inferential_stats():
    num_cols = ["price", "bedrooms", "bathrooms", "sqft_living",
                "sqft_lot", "floors", "grade", "lat", "long"]
    num_cols = [c for c in num_cols if c in df_full.columns]
    corr = df_full[num_cols].corr()["price"].sort_values(ascending=False)
    return {"price_correlations": corr.to_dict()}


@app.post("/predict")
def predict(features: HouseFeatures):
    b = features.n_bed if features.n_bed is not None else medians["bedrooms"]
    ba = features.n_bath if features.n_bath is not None else medians["bathrooms"]
    s = features.sqft if features.sqft is not None else medians["sqft_living"]
    la = features.lat if features.lat is not None else medians["lat"]
    lo = features.long if features.long is not None else medians["long"]

    row = pd.DataFrame([{
        "bedrooms": b,
        "bathrooms": ba,
        "sqft_living": s,
        "lat": la,
        "long": lo
    }])

    price = float(model.predict(row)[0])

    conn = get_conn()
    conn.execute(
        "INSERT INTO predictions (created_at, bedrooms, bathrooms, sqft_living, lat, long, predicted_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (datetime.utcnow().isoformat(), b, ba, s, la, lo, price)
    )
    conn.commit()
    conn.close()

    return {
        "predicted_price": price,
        "used_values": {
            "bedrooms": b,
            "bathrooms": ba,
            "sqft_living": s,
            "lat": la,
            "long": lo
        }
    }
