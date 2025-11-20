from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "kc_house_data.csv"
MODEL_PATH = BASE_DIR / "models" / "house_price_model.joblib"
MEDIANS_PATH = BASE_DIR / "models" / "feature_medians.json"
DB_PATH = BASE_DIR / "models" / "predictions.db"
