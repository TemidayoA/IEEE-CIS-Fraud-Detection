from scipy.stats import ks_2samp, chi2_contingency
import numpy as np

def numeric_drift(train, live):
    stat, p = ks_2samp(train, live)
    return p < 0.05

def categorical_drift(train, live):
    table = np.vstack([
        train.value_counts(),
        live.value_counts()
    ]).fillna(0)

    _, p, _, _ = chi2_contingency(table)
    return p < 0.05
