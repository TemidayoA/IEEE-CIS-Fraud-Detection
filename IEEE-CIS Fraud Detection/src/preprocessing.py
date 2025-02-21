from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    encoders = {}

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le
        else:
            df[col] = df[col].fillna(df[col].median())

    return df, encoders
