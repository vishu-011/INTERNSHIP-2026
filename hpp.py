import joblib
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "House_Rent_Dataset.csv"
MODEL_PATH = BASE_DIR / "house_rent_prediction.pkl"

FEATURE_COLUMNS = [
    "BHK",
    "Size",
    "Floor",
    "Area Type",
    "Area Locality",
    "City",
    "Furnishing Status",
    "Tenant Preferred",
    "Bathroom",
    "Point of Contact",
]
NUMERIC_COLUMNS = ["BHK", "Size", "Bathroom"]
CATEGORICAL_COLUMNS = [col for col in FEATURE_COLUMNS if col not in NUMERIC_COLUMNS]


def build_model():
    data = pd.read_csv(DATA_PATH)
    x = data[FEATURE_COLUMNS]
    y = data["Rent"]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                NUMERIC_COLUMNS,
            ),
            (
                "cat",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                CATEGORICAL_COLUMNS,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )
    model.fit(x, y)
    return model


def load_model():
    if MODEL_PATH.exists():
        try:
            artifact = joblib.load(MODEL_PATH)
            if hasattr(artifact, "predict"):
                return artifact
        except Exception:
            pass

    model = build_model()
    joblib.dump(model, MODEL_PATH)
    return model


def predict_rent(input_data):
    model = load_model()
    frame = pd.DataFrame([input_data], columns=FEATURE_COLUMNS)
    return float(model.predict(frame)[0])


def main():
    sample = {
        "BHK": 2,
        "Size": 1200,
        "Floor": "1 out of 3",
        "Area Type": "Super Area",
        "Area Locality": "Bandel",
        "City": "Kolkata",
        "Furnishing Status": "Semi-Furnished",
        "Tenant Preferred": "Family",
        "Bathroom": 2,
        "Point of Contact": "Contact Owner",
    }
    print("Predicted Rent:", predict_rent(sample))


if __name__ == "__main__":
    main()
