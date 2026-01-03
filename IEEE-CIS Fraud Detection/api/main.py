from fastapi import FastAPI
import joblib
import pandas as pd
import yaml

app = FastAPI()
model = joblib.load("models/fraud_lgbm.pkl")


with open("configs/inference.yaml") as f:
    cfg = yaml.safe_load(f)

pipeline = joblib.load(cfg["model_path"])
threshold = joblib.load(cfg["threshold_path"])


@app.post("/predict")
def predict(payload: dict):
    df = pd.DataFrame([payload])
    prob = model.predict_proba(df)[:, 1][0]

    return {
        "fraud_probability": round(float(prob), 4),
        "is_fraud": prob > 0.5
    }

from src.utils.cache import prediction_cache

@app.post("/predict")
def predict(payload: FraudRequest):
    tx_id = payload.TransactionID

    if tx_id in prediction_cache:
        return prediction_cache[tx_id]

    df = pd.DataFrame([payload.dict()])
    prob = model.predict_proba(df)[:, 1][0]

    result = {
        "fraud_probability": round(float(prob), 4),
        "is_fraud": prob > 0.5
    }

    prediction_cache[tx_id] = result
    return result
