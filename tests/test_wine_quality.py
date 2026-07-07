import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from wine_quality import classify_wine_quality, predict_wine_quality


class WineQualityTests(unittest.TestCase):
    def test_prediction_returns_float(self):
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
        prediction = predict_wine_quality(sample)
        self.assertIsInstance(prediction, float)
        self.assertGreaterEqual(prediction, 0.0)

    def test_classification_labels(self):
        self.assertEqual(classify_wine_quality(8.5), "Excellent")
        self.assertEqual(classify_wine_quality(5.2), "Average")


if __name__ == "__main__":
    unittest.main()
