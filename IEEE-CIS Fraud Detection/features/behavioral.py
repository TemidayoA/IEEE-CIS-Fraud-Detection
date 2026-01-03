GLOBAL_AVG = df["TransactionAmt"].mean()

df["avg_transaction_amount_7d"] = (
    df.groupby("card1")["TransactionAmt"]
    .rolling("7D")
    .mean()
    .reset_index(0, drop=True)
)

df["avg_transaction_amount_7d"] = df["avg_transaction_amount_7d"].fillna(GLOBAL_AVG)
