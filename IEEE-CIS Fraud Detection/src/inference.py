import joblib

model = joblib.load("models/fraud_lgbm.pkl")

def predict(transaction_df):
    prob = model.predict_proba(transaction_df)[:, 1]
    return prob
