import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load All Files
with open('list_num_cols.txt', 'rb') as file_1:
  model_num_col = pickle.load(file_1)

with open('list_cat_cols_o.txt', 'rb') as file_2:
  model_cat_col_o = pickle.load(file_2)

with open('list_cat_cols_n.txt', 'rb') as file_3:
  model_cat_col_n= pickle.load(file_3)

with open('best_model_svm.pkl', 'rb') as model_file:
  model_svm = pickle.load(model_file)


def run():
    with st.form(key="Form_Loan_Status"):
        Loan_ID = st.text_input("Loan_ID", value="")
        Gender = st.selectbox("Gender", ("Male", "Female"))
        Married = st.selectbox("Married", ("Yes", "No"))
        Dependents = st.selectbox("Dependents", (0,1,2,3))
        Education = st.selectbox("Eduation", ("Graduate", "Not Graduate"))
        Self_Employed = st.selectbox("Self_Employed", ("Yes", "No"))
        ApplicantIncome = st.number_input("ApplicantIncome", min_value=0, max_value=1000000, value=2500, help="Applicant Income")
        CoapplicantIncome = st.number_input("CoapplicantIncome", min_value=0, max_value=1000000, value=2500, help="Co Applicant Income")
        LoanAmount = st.number_input("LoanAmount", min_value=0, max_value=1000000, value=100, help="Loant Amount")
        Loan_Amount_Term = st.number_input("Loan_Amount_Term", min_value=0, max_value=1000, value=120, help="Loant Amount Term")
        Credit_History = st.selectbox("Credit_History", (1., 0.))
        Property_Area = st.selectbox("Property_Area", ("Rural", "Urban", 'Semiurban'))
      
        submitted = st.form_submit_button("Predict")

    data_inf = {
        'Loan_ID': Loan_ID,
        'Gender': Gender,
        'Married': Married,
        'Dependents': Dependents,
        'Education': Education,
        'Self_Employed': Self_Employed,
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Property_Area': Property_Area
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

        y_pred = model_svm.predict(data_inf) # Jalankan model
        if y_pred == True:
            st.write("# Approved")
        else:
            st.write("# Not Approved")

if __name__ == "__app__":
    run()