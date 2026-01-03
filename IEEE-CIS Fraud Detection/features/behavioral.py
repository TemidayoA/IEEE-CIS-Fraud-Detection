GLOBAL_AVG = df["TransactionAmt"].mean()

df["avg_transaction_amount_7d"] = (
    df.groupby("card1")["TransactionAmt"]
    .rolling("7D")
    .mean()
    .reset_index(0, drop=True)
)

df["avg_transaction_amount_7d"] = df["avg_transaction_amount_7d"].fillna(GLOBAL_AVG)

def add_temporal_features(df):
    df["transaction_hour"] = df["TransactionDT"] % 24
    df["day_of_week"] = (df["TransactionDT"] // 24) % 7
    df["time_since_last_transaction"] = df.groupby("card1")["TransactionDT"].diff()
    return df