# Phishing Website Detection Using Machine Learning

📌 Project Overview

Phishing Website Detection is a Python-based Machine Learning project that analyzes website URLs and classifies them as **potentially phishing** or **likely legitimate**.
The system uses URL-based features and two Machine Learning algorithms, Decision Tree and Support Vector Machine (SVM), to identify patterns associated with phishing websites.
The application provides a simple web interface built with Streamlit, allowing users to enter a URL and view the model's prediction along with extracted URL features.

🎯 Objectives

- Detect potentially suspicious URLs using Machine Learning.
- Extract useful URL and domain-related features.
- Train and compare Decision Tree and SVM classifiers.
- Evaluate model performance using classification metrics.
- Build an interactive Python web application for URL analysis.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Algorithms:** Decision Tree, Support Vector Machine (SVM)
- **Web Interface:** Streamlit
- **Model Persistence:** Joblib
- **Development Environment:** macOS Terminal / Linux-compatible command line

## ⚙️ Features

- URL-based feature extraction.
- Phishing and legitimate URL classification.
- Two Machine Learning model options.
- Model evaluation using accuracy, precision, recall, and F1-score.
- Interactive web interface for URL analysis.
- Display of extracted URL characteristics.
- Saved trained models for reuse.

 📂 Project Structure

phishing_detection/
│
├── app.py                 # Streamlit web application
├── train_model.py         # Data preprocessing and model training
├── urls.csv               # Labeled URL dataset
├── saved_models/
│   └── models.joblib       # Saved trained models
├── .venv/                 # Python virtual environment (not committed)
├── .gitignore
└── README.md


🧠 Machine Learning Algorithms

### 1. Decision Tree Classifier

A supervised Machine Learning algorithm that learns decision rules from labeled examples to classify URLs.

## 2. Support Vector Machine (SVM)

A supervised Machine Learning algorithm that learns a decision boundary to distinguish between phishing and legitimate URL examples.

Both models are evaluated on a held-out test dataset to compare their performance.

## 🔍 URL Feature Extraction

The application extracts numerical characteristics from URLs, including:

- URL length
- Domain length
- Number of dots and hyphens
- Number of special characters
- HTTPS usage
- Presence of an IP address in the hostname
- Number of domain components
- URL path length
- Presence of a double slash in the path
- Presence of digits in the hostname

These features are provided to the trained Machine Learning models for classification.

## 🚀 Installation and Setup

### Prerequisites

- Python 3
- pip
- Terminal or a code editor
- Basic knowledge of Python

### Step 1: Clone the repository

git clone (https://github.com/Sairajbhosle)
cd phishing_detection



### Step 2: Create a virtual environment

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install pandas scikit-learn streamlit joblib numpy
```

### Step 4: Train the Machine Learning models

Ensure that `urls.csv` is present in the project directory and contains the required `url` and `label` columns.

```bash
python train_model.py
```

The script trains both classifiers, prints their evaluation metrics, and saves the models in the `saved_models/` directory.

### Step 5: Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to use the application.

## 📊 Model Evaluation

The training script reports the following metrics:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted phishing URLs that are actually phishing in the labeled test data.
- **Recall:** Proportion of phishing URLs correctly identified.
- **F1-score:** Harmonic mean of precision and recall.

Actual performance depends on the dataset, feature quality, and evaluation method. Model results should be measured on representative data that was not used for training.

## 🔮 Future Enhancements

- Use a larger, reliable, and regularly updated phishing URL dataset.
- Improve feature engineering and evaluate additional classification models.
- Add domain reputation and threat-intelligence checks.
- Develop a browser extension for automatic URL checking.
- Build a Python API for integration with other applications.
- Improve the interface with scan history and detailed feature explanations.
- Evaluate generalization on URLs from previously unseen domains.

## ⚠️ Limitations and Disclaimer

This project is an educational prototype developed for learning Python and Machine Learning.
Its predictions are not a guarantee of website safety. Legitimate websites may be classified as phishing, and phishing websites may be classified as legitimate.
The sample dataset used during initial development contains illustrative records and is not sufficient for reliable real-world detection. Use a properly labeled, representative dataset before drawing conclusions about model performance.

Do not enter passwords, payment details, or other sensitive information into suspicious websites for testing.

## 👨‍💻 Author

Sairaj Bhosle

GitHub: https://github.com/Sairajbhosle


