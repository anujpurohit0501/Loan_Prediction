
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# 1. Model ko Load Karo
with open('loan_model_v2.pkl', 'rb') as file:
    lr = pickle.load(file)

# 2. Page Configuration aur Title
st.set_page_config(page_title="Loan Amount Predictor", layout="centered")
st.title("💰 Loan Amount Prediction Dashboard")
st.write("Fill in your information below to get an instant estimate of your eligible loan amount.")
st.divider()

# 3. User Inputs (Form Layout)
st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=5000)

with col2:
    co_income = st.number_input("Coapplicant Monthly Income ($)", min_value=0, value=0)
    loan_term = st.number_input("Loan Amount Term (in days, e.g., 360)", min_value=0, value=360)
    credit_history = st.selectbox("Credit History", ["Good (1.0)", "Bad (0.0)"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    
    # Total Income aur EMI calculate karna (Kyunki dataset me ye features hain)
    total_income = income + co_income
    emi = st.number_input("Expected Monthly EMI ($)", min_value=0, value=500)

# --- Encoding (Categorical to Numerical) ---
gender_enc = 1 if gender == "Male" else 0
married_enc = 1 if married == "Yes" else 0

# Dependents mapping
if dependents == "3+":
    dep_enc = 3
else:
    dep_enc = int(dependents)

edu_enc = 1 if education == "Graduate" else 0
emp_enc = 1 if self_employed == "Yes" else 0
cred_enc = 1.0 if "Good" in credit_history else 0.0

# Property Area mapping
if property_area == "Urban":
    prop_enc = 2
elif property_area == "Semiurban":
    prop_enc = 1
else:
    prop_enc = 0

st.divider()

# 4. Prediction Button aur Logic
if st.button("Predict Loan Amount", type="primary"):
    
    # CRITICAL: Yeh sequence bilkul tumhari list ke mutabiq hai:
    # ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 
    #  'CoapplicantIncome', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Total_Income', 'EMI']
    input_data = np.array([[
        gender_enc, married_enc, dep_enc, edu_enc, emp_enc, 
        income, co_income, loan_term, cred_enc, prop_enc, 
        total_income, emi
    ]])
    
    # Model se prediction lena
    prediction = lr.predict(input_data)
    
    st.subheader("📊 Prediction Result:")
    
    if prediction[0] < 0:
        st.error("❌ Sorry, based on your data, you are not eligible for a loan.")
    else:
        st.success(f"🎉 Predicted Eligible Loan Amount: **${prediction[0]:,.2f}**")
