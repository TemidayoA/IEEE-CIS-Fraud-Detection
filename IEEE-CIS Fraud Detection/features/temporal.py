def add_temporal_features(df):
    df = df.sort_values("TransactionTimestamp")

    df["transaction_hour"] = df["TransactionTimestamp"].dt.hour
    df["day_of_week"] = df["TransactionTimestamp"].dt.dayofweek

    df["time_since_last_transaction"] = (
        df.groupby("card1")["TransactionTimestamp"]
        .diff()
        .dt.total_seconds()
    )

    assert (df["time_since_last_transaction"] >= 0).all(), \
        "Detected future timestamp leakage"

    return df
