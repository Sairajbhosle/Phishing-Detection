import joblib
import pandas as pd
import streamlit as st

from pathlib import Path
from train_model import extract_features

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "saved_models" / "models.joblib"

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Phishing Website Detection")
st.write(
    "Analyze URL patterns using Machine Learning."
)

st.warning(
    "Educational prototype only. Predictions can be wrong. "
    "Do not enter passwords or sensitive information."
)

if not MODEL_PATH.exists():
    st.error("Models not found. Run train_model.py first.")
    st.stop()

models = joblib.load(MODEL_PATH)

model_name = st.selectbox(
    "Choose Machine Learning algorithm",
    ["Decision Tree", "SVM"]
)

url = st.text_input(
    "Enter website URL",
    placeholder="https://example.com/login"
)

if st.button("Scan URL", type="primary"):
    if not url.strip():
        st.error("Please enter a URL.")
    else:
        features = extract_features(url)

        # Feature names correspond to extract_features()
        feature_names = [
            "url_length", "domain_length", "dots",
            "hyphens", "at_symbols", "question_marks",
            "equals_signs", "slashes", "uses_https",
            "has_ip_address", "domain_parts",
            "path_length", "double_slash_in_path",
            "digits_in_domain"
        ]

        X = pd.DataFrame(
            [features], columns=feature_names
        )

        model = models[model_name]
        prediction = int(model.predict(X)[0])

        st.subheader("Scan Result")

        if prediction == 1:
            st.error("⚠️ Predicted: Potential Phishing")
        else:
            st.success("Predicted: Likely Legitimate")

        st.caption(
            "This result is a model prediction, not a safety guarantee."
        )

        st.subheader("Extracted URL Features")
        st.dataframe(X, use_container_width=True)
