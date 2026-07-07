import joblib
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Lab  winequality-red.csv"
MODEL_PATH = BASE_DIR / "wine_quality_model.pkl"

FEATURE_COLUMNS = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]


def build_model():
    data = pd.read_csv(DATA_PATH, sep=";")
    X = data[FEATURE_COLUMNS]
    y = data["quality"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("regressor", RandomForestRegressor(n_estimators=200, random_state=42)),
        ]
    )
    model.fit(X_train, y_train)
    test_score = r2_score(y_test, model.predict(X_test))
    print(f"Wine quality model R^2 score: {test_score:.3f}")
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


def predict_wine_quality(input_data):
    model = load_model()
    frame = pd.DataFrame([input_data], columns=FEATURE_COLUMNS)
    return float(model.predict(frame)[0])


def classify_wine_quality(score):
    if score >= 7.5:
        return "Excellent"
    if score >= 5.5:
        return "Good"
    if score >= 4.5:
        return "Average"
    return "Poor"


if __name__ == "__main__":
    sample = {
        "fixed acidity": 7.4,
        "volatile acidity": 0.7,
        "citric acid": 0.0,
        "residual sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur dioxide": 11.0,
        "total sulfur dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
    }
    print(predict_wine_quality(sample))
