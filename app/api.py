# app/api.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from src.preprocess import build_preprocessor

# -------------------------
# 1️⃣ Initialize app
# -------------------------
app = FastAPI(title="Telco Churn Predictor")

# -------------------------
# 2️⃣ Load model
# -------------------------
model = joblib.load("models/GradientBoosting_tuned.pkl")  # pick your best

# -------------------------
# 3️⃣ Define input data
# -------------------------
class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# -------------------------
# 4️⃣ Prediction endpoint
# -------------------------
@app.post("/predict")
def predict_churn(data: Customer):
    # Convert JSON to DataFrame
    df = pd.DataFrame([data.dict()])

    # Predict probability
    pred_proba = model.predict_proba(df)[:, 1][0]

    # Binary prediction with threshold 0.5
    pred_label = int(pred_proba > 0.5)

    return {
        "churn_probability": float(pred_proba),
        "churn_prediction": pred_label
    }
