import joblib
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from config import MODEL_PARAMS, TARGET

import numpy as np
FEATURE_NAMES = X_train.columns.tolist()

joblib.dump(FEATURE_NAMES, "models/feature_names.pkl")

pos = y_train.sum()
neg = len(y_train) - pos

scale_pos_weight = neg / pos

MODEL_PARAMS["scale_pos_weight"] = scale_pos_weight

def train(df):
    y = df[TARGET]
    X = df.drop(columns=[TARGET, "TransactionID"])

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = lgb.LGBMClassifier(**MODEL_PARAMS)
    model.fit(
        X_train, y_train,
        eval_set=[(X_val, y_val)],
        eval_metric="auc",
        early_stopping_rounds=50,
        verbose=100
    )

    preds = model.predict_proba(X_val)[:, 1]
    print("AUC:", roc_auc_score(y_val, preds))

    joblib.dump(model, "models/fraud_lgbm.pkl")
