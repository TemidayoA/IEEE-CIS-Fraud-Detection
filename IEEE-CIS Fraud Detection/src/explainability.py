import shap
import joblib

def explain(sample):
    model = joblib.load("models/fraud_lgbm.pkl")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(sample)

    shap.summary_plot(shap_values, sample)
