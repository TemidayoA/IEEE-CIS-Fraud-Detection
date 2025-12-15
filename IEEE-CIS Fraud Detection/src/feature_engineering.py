import numpy as np

def add_features(df):
    df["TransactionAmt_log"] = np.log1p(df["TransactionAmt"])
    df["card_email_combo"] = (
        df["card1"].astype(str) + "_" + df["P_emaildomain"].astype(str)
    )
    return df
