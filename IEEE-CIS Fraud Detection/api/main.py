from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/fraud_lgbm.pkl")

@app.post("/predict")
def predict(payload: dict):
    df = pd.DataFrame([payload])
    prob = model.predict_proba(df)[:, 1][0]

    return {
        "fraud_probability": round(float(prob), 4),
        "is_fraud": prob > 0.5
    }
