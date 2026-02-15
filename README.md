📉 Telco Customer Churn Prediction

A beginner-friendly ML project that predicts customer churn for a telecom company using Gradient Boosting and provides an interactive Streamlit app.

🧩 Project Overview

This project demonstrates an end-to-end ML workflow:

Load and clean customer data

Train models: Logistic Regression, Random Forest, Gradient Boosting

Hyperparameter tuning with GridSearchCV

Evaluate model performance (Accuracy, ROC-AUC, Confusion Matrix)

Save and load trained models using joblib

Predict churn interactively via a Streamlit web app

📦 Tech Stack

Python 3.9+

Pandas & NumPy

Scikit-learn

Joblib (model persistence)

Streamlit (UI)

Plotly (interactive charts)

🗂 Project Structure
churn-prediction/
│
├── data/                   # Raw dataset
├── models/                 # Saved models (GradientBoosting_tuned.pkl)
├── src/                    # Python scripts
│   ├── preprocess.py
│   ├── train.py
│   ├── models.py
│   └── evaluate.py
├── app/                    # Streamlit frontend
│   └── app.py
├── main.py                 # Script to train & evaluate models
├── requirements.txt
└── README.md

⚙️ Installation
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .\.venv\Scripts\activate  # Windows
pip install -r requirements.txt

▶️ Run the App
streamlit run app/app.py


Open your browser at: http://localhost:8501

🧪 How It Works

Input customer information (demographics, services, billing)

Predict churn probability (0–100%)

Binary prediction: CHURN or STAY

Visual indicators (risk gauge, colored alerts)

Insights section explains key features affecting churn
