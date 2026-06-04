# 💳 Credit Card Fraud Detection System

## Overview

This project is an end-to-end Machine Learning application designed to detect fraudulent credit card transactions in real time. The system leverages an XGBoost classifier trained on highly imbalanced transaction data and provides predictions through a FastAPI backend and an interactive Streamlit dashboard.

The application helps identify potentially fraudulent transactions by analyzing transaction features and estimating the probability of fraud.

---

## 🚀 Features

- Real-time fraud prediction
- XGBoost-based classification model
- SMOTE for class imbalance handling
- SHAP explainability for model interpretation
- FastAPI REST API backend
- Streamlit interactive dashboard
- Fraud probability scoring
- Risk level classification
- Prediction history tracking
- Business-oriented fraud recommendations

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- XGBoost
- Scikit-Learn
- Imbalanced-Learn (SMOTE)
- SHAP

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- SHAP

---

## 📊 Model Performance

| Metric | Score |
|----------|----------|
| ROC-AUC | 0.983 |
| Precision | 0.87 |
| Recall | 0.84 |
| F1 Score | 0.85 |

### Confusion Matrix

| | Predicted Legitimate | Predicted Fraud |
|---|---|---|
| Actual Legitimate | 56,852 | 12 |
| Actual Fraud | 16 | 82 |

---

## 📂 Project Structure

```text
credit-card-fraud-detection/
│
├── api.py
├── streamlit.py
├── fraud_system.pkl
├── shap_summary.png
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🏗️ System Architecture

```text
User
 ↓
Streamlit Dashboard
 ↓
FastAPI Backend
 ↓
XGBoost Model
 ↓
Fraud Prediction
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Backend

```bash
uvicorn api:app --reload
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit Dashboard

```bash
streamlit run streamlit.py
```

### Dashboard URL

```text
http://localhost:8501
```

---

## 📈 Explainability

The project includes SHAP (SHapley Additive Explanations) to provide insights into feature importance and model decision-making.

The dashboard displays a SHAP summary plot that highlights the most influential features contributing to fraud predictions.

---

## 📸 Screenshots

### Dashboard
<img width="1902" height="565" alt="Screenshot 2026-06-05 010539" src="https://github.com/user-attachments/assets/22fe4fb0-740e-4f80-a4e0-556fb8be991f" />


### Prediction Results
<img width="1595" height="883" alt="Screenshot 2026-06-05 010815" src="https://github.com/user-attachments/assets/651d0f0c-6932-4ba4-9066-54926918dc12" />


### SHAP Explainability
<img width="565" height="712" alt="Screenshot 2026-06-05 010657" src="https://github.com/user-attachments/assets/0fce3852-10b4-4746-8a9d-1cc852fe542e" />


---

## 📝 Example Prediction Output

```json
{
  "fraud_probability": 0.99995,
  "prediction": 1
}
```

Where:

- `prediction = 1` → Fraudulent Transaction
- `prediction = 0` → Legitimate Transaction

---

## 🔮 Future Improvements

- PostgreSQL integration for storing predictions
- Docker containerization
- Cloud deployment (Render/AWS/Railway)
- Real-time transaction monitoring
- Model versioning and experiment tracking with MLflow

---

## 👨‍💻 Author

**Pratham Bisht**

Aspiring Machine Learning Engineer with interests in FinTech, Data Science, and AI-powered systems.

---
⭐ If you found this project useful, consider giving it a star on GitHub.
