from scipy.stats import ks_2samp

def detect_drift(train_col, new_col):
    stat, p_value = ks_2samp(train_col, new_col)
    return p_value < 0.05
