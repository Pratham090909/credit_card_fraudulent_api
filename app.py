import streamlit as st
import requests
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 Model Performance")

col1, col2 = st.sidebar.columns(2)

with col1:
    st.metric("ROC-AUC", "0.983")
    st.metric("Recall", "0.84")

with col2:
    st.metric("Precision", "0.87")
    st.metric("F1 Score", "0.85")

st.sidebar.markdown("---")

show_advanced = st.sidebar.checkbox(
    "Show Advanced Features (V1-V28)"
)

# =====================================
# HEADER
# =====================================

st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
This application predicts whether a credit card transaction is fraudulent.

Enter transaction details and click **Predict Fraud Risk**.
""")

# =====================================
# SAMPLE TRANSACTIONS
# =====================================

sample = st.selectbox(
    "Load Example Transaction",
    [
        "None",
        "Legitimate Transaction",
        "Fraudulent Transaction"
    ]
)

if sample == "Legitimate Transaction":

    default_amount = 50.0
    default_v1 = 1.2
    default_v2 = 0.1

elif sample == "Fraudulent Transaction":

    default_amount = 2500.0
    default_v1 = -4.5
    default_v2 = 3.2

else:

    default_amount = 100.0
    default_v1 = 0.0
    default_v2 = 0.0

# =====================================
# INPUTS
# =====================================

col1, col2 = st.columns(2)

with col1:

    Time = st.number_input(
        "Transaction Time",
        value=0.0
    )

    Amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=default_amount
    )

with col2:

    st.info(
        """
Amount has the strongest business interpretation.

The remaining V1-V28 variables are PCA-transformed features from the original dataset and are available in Advanced Mode.
        """
    )

# =====================================
# ADVANCED FEATURES
# =====================================

features = {}

for i in range(1, 29):
    features[f"V{i}"] = 0.0

features["V1"] = default_v1
features["V2"] = default_v2

if show_advanced:

    st.markdown("## 🔬 Advanced Features (PCA Components)")

    left, right = st.columns(2)

    for i in range(1, 15):

        with left:

            features[f"V{i}"] = st.number_input(
                f"V{i}",
                value=float(features[f"V{i}"]),
                key=f"left_{i}"
            )

    for i in range(15, 29):

        with right:

            features[f"V{i}"] = st.number_input(
                f"V{i}",
                value=float(features[f"V{i}"]),
                key=f"right_{i}"
            )

# =====================================
# PREDICT BUTTON
# =====================================

if st.button("🚀 Predict Fraud Risk"):

    payload = {
        "Time": Time,
        "Amount": Amount
    }

    payload.update(features)

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        probability = result["fraud_probability"]
        prediction = result["prediction"]

        # ==========================
        # RESULTS
        # ==========================

        st.markdown("---")

        st.subheader("📈 Prediction Results")

        st.metric(
            "Fraud Probability",
            f"{probability:.2%}"
        )

        st.progress(float(probability))

        if probability < 0.30:

            st.success("🟢 Low Risk Transaction")

        elif probability < 0.70:

            st.warning("🟡 Medium Risk Transaction")

        else:

            st.error("🔴 High Risk Transaction")

        st.markdown("---")

        # ==========================
        # BUSINESS INTERPRETATION
        # ==========================

        if prediction == 1:

            st.error(
                f"""
🚨 FRAUD DETECTED

Predicted Fraud Probability: {probability:.2%}

Recommended Action:
- Hold transaction
- Trigger manual verification
- Notify fraud monitoring team
                """
            )

        else:

            st.success(
                f"""
✅ LEGITIMATE TRANSACTION

Predicted Fraud Probability: {probability:.2%}

Recommended Action:
- Approve transaction
- Continue normal processing
                """
            )

        # ==========================
        # HISTORY
        # ==========================

        st.session_state.history.append(
            {
                "Amount": Amount,
                "Fraud Probability": round(probability, 4),
                "Prediction": (
                    "Fraud"
                    if prediction == 1
                    else "Legitimate"
                )
            }
        )

    except Exception as e:

        st.error(f"Error: {str(e)}")

# =====================================
# PREDICTION HISTORY
# =====================================

if len(st.session_state.history) > 0:

    st.markdown("---")

    st.subheader("📝 Recent Predictions")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

# =====================================
# SHAP SECTION
# =====================================

st.markdown("---")

st.subheader("📊 Explainability (SHAP)")

try:

    st.image(
        "shap_summary.png",
        caption="Global Feature Importance"
    )

except:

    st.info(
        "Place 'shap_summary.png' in the project folder to display SHAP explanations."
    )

# =====================================
# MODEL INFO
# =====================================

st.markdown("---")

st.subheader("🤖 Model Information")

st.info(
"""
Model: XGBoost Classifier

Dataset: Credit Card Fraud Detection Dataset

Features:
• Time
• Amount
• V1–V28

Performance:
• ROC-AUC: 0.983
• Precision: 0.87
• Recall: 0.84
• F1 Score: 0.85
"""
)

# =====================================
# SYSTEM ARCHITECTURE
# =====================================

st.markdown("---")

with st.expander("🏗️ System Architecture"):

    st.code(
"""
User
  ↓
Streamlit Dashboard
  ↓
FastAPI Backend
  ↓
XGBoost Model
  ↓
Fraud Prediction
""",
        language="text"
    )