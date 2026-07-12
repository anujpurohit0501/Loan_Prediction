import streamlit as st
import pandas as pd
import pickle
import numpy as np

# 1. Model ko Load Karo (lr model jo pkl file me hai)
with open('loan_model_v2.pkl', 'rb') as file:
    lr = pickle.load(file)

# 2. Page Configuration aur Title
st.set_page_config(page_title="Loan Amount Predictor", layout="centered")
st.title("💰 Loan Amount Prediction Dashboard")
st.write("Apne details niche enter karein aur check karein aap kitne Loan Amount ke liye eligible hain.")
st.divider()

# 3. User Inputs (Form Layout)
st.subheader("📋 Applicant Information")

# Screen ko do columns me divide kiya taaki frontend sundar lage
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=5000)
    credit_score = st.slider("Credit Score (CIBIL)", min_value=300, max_value=850, value=700)

with col2:
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    # AGAR KOI AUR COLUMN HAI (e.g., Married, Gender) toh use yahan add kar sakte ho:
    # married = st.selectbox("Married", ["Yes", "No"])

# Categorical Text ko Numbers me convert karne ke liye
edu_encoded = 1 if education == "Graduate" else 0

st.divider()

# 4. Prediction Button aur Logic
if st.button("Predict Loan Amount", type="primary"):
    
    # ⚠️ CRITICAL WARNING: Is array ke andar variables ka sequence (order)
    # bilkul wahi hona chahiye jo tumhare 'inp.columns' (Jupyter Notebook) me tha.
    input_data = np.array([[income, credit_score, edu_encoded]])
    
    # Model se prediction lena
    prediction = lr.predict(input_data)
    
    st.subheader("📊 Prediction Result:")
    
    # Agar output negative me chala jaye (kabhi-kabhi linear regression me hota hai)
    if prediction[0] < 0:
        st.error("❌ Sorry, based on your data, you are not eligible for a loan.")
    else:
        # Sahi format me approved loan amount dikhane ke liye
        st.success(f"🎉 Predicted Eligible Loan Amount: **${prediction[0]:,.2f}**")
