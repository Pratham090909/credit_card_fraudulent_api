from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create app
app = FastAPI()

# Load artifacts once when server starts
artifacts = joblib.load("fraud_system.pkl")

model = artifacts["model"]
threshold = artifacts["threshold"]


# Input schema
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}


@app.post("/predict")
def predict(transaction: Transaction):

    data = pd.DataFrame([transaction.dict()])

    probability = float(
        model.predict_proba(data)[0][1]
    )

    prediction = int(
        probability > threshold
    )

    return {
        "fraud_probability": probability,
        "prediction": prediction
    }