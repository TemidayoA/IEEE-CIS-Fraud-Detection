import yaml

with open("configs/features.yaml") as f:
    FEATURES = yaml.safe_load(f)

ALL_FEATURES = sum(FEATURES.values(), [])

def validate_features(df):
    missing = set(ALL_FEATURES) - set(df.columns)
    extra = set(df.columns) - set(ALL_FEATURES)

    if missing:
        raise ValueError(f"Missing features: {missing}")
    if extra:
        raise ValueError(f"Unexpected features: {extra}")
