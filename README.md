# Loan_Prediction
# Loan Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a loan application will be **Approved** or **Rejected** based on applicant details using Machine Learning.

The objective is to automate the loan approval process by analyzing applicant information such as income, education, credit history, property area, and employment status.

---

## 📂 Dataset Features

The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| Loan_ID | Unique Loan Identifier |
| Gender | Applicant Gender |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Graduate / Not Graduate |
| Self_Employed | Self-employed Status |
| ApplicantIncome | Applicant's Monthly Income |
| CoapplicantIncome | Co-applicant's Monthly Income |
| LoanAmount | Loan Amount Requested |
| Loan_Amount_Term | Loan Repayment Term |
| Credit_History | Credit History of Applicant |
| Property_Area | Urban, Semiurban or Rural |

**Target Variable**
- Loan_Status
  - Y → Loan Approved
  - N → Loan Rejected

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Handled missing values
  - Categorical columns → Filled using Mode
  - Numerical columns → Filled using Median
- Encoded categorical variables into numerical values
- Removed unnecessary columns (`Loan_ID`)
- Converted `Dependents` values (`3+` → `3`)
- Prepared the dataset for model training

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Missing Value Handling
4. Categorical Encoding
5. Exploratory Data Analysis (EDA)
6. Feature Selection
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Prediction

---

## 📈 Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

*(Update this section according to the models you trained.)*

---

## 📊 Evaluation Metrics

The models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📁 Project Structure

```
Loan-Prediction/
│
├── Loan_Prediction.ipynb
├── loan_prediction.csv
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Loan-Prediction.git
```

2. Navigate to the project folder

```bash
cd Loan-Prediction
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Open Jupyter Notebook

```bash
jupyter notebook
```

5. Run the notebook.

---

## 🎯 Future Improvements

- Hyperparameter Tuning
- Feature Engineering
- Cross Validation
- Model Deployment using Flask or Streamlit
- Interactive Web Interface

---

## 👨‍💻 Author

Your Name: Anuj Purohit

GitHub: https://github.com/anujpurohit0501
