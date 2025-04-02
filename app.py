import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Customer Churn Prediction ", layout="centered")

# Load model (ensure to upload the model file to Colab if necessary)
@st.cache_resource
def load_model():
    return joblib.load('/Users/bindudevidas/Desktop/DS PROJECT/churn_prediction_pipeline.pkl')

pipeline = load_model()

# Streamlit App Interface
st.title(" Will the Customer Churn❓")

# Threshold Explanation
st.markdown("""
**Threshold Explanation**:
- The threshold determines how the model interprets the probability of a customer churning.
- If the model’s predicted churn probability is **greater than the chosen threshold**, it will output "Yes" (the customer will churn).
- If it is **less than or equal to the threshold**, it will output "No" (the customer will stay).

**Use Cases**:
- **Lower threshold** (e.g., 0.3): Capture more potential churners. Good for retention strategies where it’s okay to reach out to more customers than needed.
- **Higher threshold** (e.g., 0.7): Capture only high-probability churners. Good for more focused retention efforts.

You can adjust the threshold using the slider below to make the model more or less sensitive to predicting churn.
""")

# User inputs with emojis
tenure = st.slider("📅 Tenure (months)", min_value=1, max_value=72, value=12)
internet_service = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("🔒 Online Security", ["Yes", "No"])
tech_support = st.selectbox("🛠️ Tech Support", ["Yes", "No"])
contract = st.selectbox("📝 Contract Type", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("💳 Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

# Threshold slider to adjust sensitivity to churn
threshold = st.slider("Set Churn Probability Threshold", min_value=0.1, max_value=0.9, value=0.5)

# Prediction button
if st.button("Predict Churn 💡"):
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "TechSupport": [tech_support],
        "Contract": [contract],
        "PaymentMethod": [payment_method]
    })

    # Get prediction probabilities
    prediction_prob = pipeline.predict_proba(input_data)[0][1]  # Probability of churn (class 1)
    prediction = "Yes" if prediction_prob > threshold else "No"  # Adjust the threshold

    result = f"{prediction} (Probability of Churn: {prediction_prob:.2f})"

    st.markdown(f"### Prediction: {result}")

    if prediction == "Yes":
        st.error(result)
    else:
        st.success(result)

st.write("💖 We care about every customer! 💖")
