import joblib

model = joblib.load("models/fraud_lgbm.pkl")

def predict(transaction_df):
    prob = model.predict_proba(transaction_df)[:, 1]
    return prob

FEATURE_NAMES = joblib.load("models/feature_names.pkl")

def prepare_features(df):
    missing = set(FEATURE_NAMES) - set(df.columns)
    if missing:
        raise ValueError(f"Missing features: {missing}")

    return df[FEATURE_NAMES]
