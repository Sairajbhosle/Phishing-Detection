
import re
import ipaddress
import joblib
import pandas as pd

from urllib.parse import urlparse
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

BASE_DIR = Path(__file__).resolve().parent


def extract_features(url):
    # Add a scheme if the user or dataset omitted it
    if "://" not in url:
        url = "http://" + url

    parsed = urlparse(url)
    host = parsed.hostname or ""
    path = parsed.path or ""

    try:
        ipaddress.ip_address(host)
        has_ip = 1
    except ValueError:
        has_ip = 0

    features = [
        len(url),
        len(host),
        url.count("."),
        url.count("-"),
        url.count("@"),
        url.count("?"),
        url.count("="),
        url.count("/"),
        int(parsed.scheme == "https"),
        int(has_ip),
        len(host.split(".")),
        len(path),
        int("//" in path),
        int(bool(re.search(r"\d", host))),
    ]

    return features


if __name__ == "__main__":
    data = pd.read_csv(BASE_DIR / "urls.csv")

    data = data[["url", "label"]].dropna()
    data["url"] = data["url"].astype(str)

    # Expected labels: phishing and legitimate
    data["label"] = (
        data["label"].astype(str).str.strip().str.lower()
    )

    label_map = {
        "phishing": 1,
        "legitimate": 0,
    }

    data["label"] = data["label"].map(label_map)
    data = data.dropna(subset=["label"])
    data["label"] = data["label"].astype(int)

    X = pd.DataFrame(
        data["url"].apply(extract_features).tolist()
    )
    y = data["label"]

    if y.nunique() != 2 or y.value_counts().min() < 2:
        raise ValueError(
            "Dataset needs at least two examples of each class."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    models = {
        "Decision Tree": DecisionTreeClassifier(
            max_depth=8, random_state=42,
            class_weight="balanced"
        ),
        "SVM": make_pipeline(
            StandardScaler(),
            SVC(class_weight="balanced")
        ),
    }

    output_dir = BASE_DIR / "saved_models"
    output_dir.mkdir(exist_ok=True)

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        print(f"\n{name}")
        print("Accuracy:", accuracy_score(y_test, predictions))
        print(classification_report(
            y_test, predictions,
            labels=[0, 1],
            target_names=["Legitimate", "Phishing"],
            zero_division=0
        ))

        results[name] = model

    # Save both models for later comparison
    joblib.dump(
        results,
        output_dir / "models.joblib"
    )

    print("Models saved successfully.")
