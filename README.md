# churn-prediction
📊 Telco Customer Churn Prediction App

An end-to-end Machine Learning project that predicts customer churn using supervised learning, featuring:

Model training & tuning

Model persistence

Inference pipeline

Interactive web app (Streamlit UI)

Real-time predictions

This project demonstrates the full ML workflow from data → model → deployment → user interface.

🚀 Project Overview

Customer churn prediction helps telecom companies identify customers likely to leave their service.

This app allows users to:

Input customer information

Run a trained ML model

Get:

Churn probability

Binary prediction (Yes / No)

Visual outputs (charts & indicators)

🧠 ML Pipeline
Raw Data
   ↓
Preprocessing
   ↓
Feature Encoding
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Selection
   ↓
Model Saving (joblib)
   ↓
Model Loading
   ↓
Inference
   ↓
Streamlit UI

📦 Models Used

Logistic Regression

Random Forest

Gradient Boosting (final selected model)

With hyperparameter tuning using grid search.

🛠️ Tech Stack

ML / Data

Python

Pandas

Scikit-learn

Joblib

Backend / App

Streamlit

Visualization

Plotly

🧩 Project Structure
churn-prediction/
│
├── data/
│
├── models/
│   └── GradientBoosting_tuned.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── models.py
│   └── evaluate.py
│
├── app/
│   └── app.py   # Streamlit app
│
├── main.py
├── requirements.txt
└── README.md

⚙️ Installation
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

▶️ Run the App
streamlit run app/app.py
