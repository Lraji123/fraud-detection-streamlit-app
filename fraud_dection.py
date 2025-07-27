import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("Frad_detection_analysis_model.pkl")

# App Title and Instructions
st.title("🔍 Fraud Detection Prediction App")
st.write("## Please enter the transaction details and click the Predict button below")
st.divider()

# Input Fields
trasaction_type = st.selectbox("Transaction Type", ["PAYMENT", "CASH_IN", "CASH_OUT", "DEBIT", "TRANSFER"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=0.0)
newbalanceOrg = st.number_input("New Balance (Sender)", min_value=0.0, value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Prediction Button
if st.button("Predict"):
    # Create DataFrame for input
    input_data = pd.DataFrame([{
        "type": trasaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.subheader(f"Prediction: {int(prediction)}")
    if prediction == 1:
        st.error("⚠️ This transaction may be fraudulent!")
    else:
        st.success("✅ This transaction does not appear to be fraudulent.")
