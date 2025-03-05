import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def prediction(input_data):
    pred = model.predict(input_data)[0]
    
    if pred == 1:
        return 'High Risk of Readmission', '⚠️ The patient is at high risk of readmission. Consider additional monitoring and intervention.'
    else:
        return 'Low Risk of Readmission', '✅ The patient has a low risk of readmission.'

# Streamlit UI
def main():
    # Set page layout
    st.set_page_config(page_title="Diabetes Readmission Prediction", layout="wide")

    # Layout using two columns for landscape view
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔢 Patient Information")
        gender = st.selectbox('Gender', [0.0, 1.0], format_func=lambda x: 'Male' if x == 0.0 else 'Female')
        age = st.slider('Age Group (1: 0-10, 2: 10-20, ..., 10: 90-100)', 1, 10)
        admission_type_id = st.selectbox('Admission Type', range(1, 9))
        time_in_hospital = st.slider('Hospital Stay (Days)', 1, 30)
        num_lab_procedures = st.number_input('Lab Procedures', min_value=0, step=1, help="Total number of lab tests conducted.")
        num_medications = st.number_input('Medications', min_value=0, step=1, help="Total number of medications prescribed.")
        number_inpatient = st.number_input('Previous Inpatient Visits', min_value=0, step=1, help="Number of times the patient was admitted before.")
        diag_1 = st.number_input('Primary Diagnosis Code', step=1, help="ICD-9 code for the primary diagnosis.")
        diag_2 = st.number_input('Secondary Diagnosis Code', step=1, help="ICD-9 code for the secondary diagnosis.")
        diag_3 = st.number_input('Additional Diagnosis Code', step=1, help="ICD-9 code for another diagnosis.")
        metformin = st.selectbox('Metformin Use', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
        insulin = st.selectbox('Insulin Use', [1.0, 2.0, 3.0], format_func=lambda x: {1.0: 'No', 2.0: 'Up', 3.0: 'Steady'}[x])
        change = st.selectbox('Change in Medications', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
        diabetesMed = st.selectbox('Diabetes Medication', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
        discharged_to = st.slider('Discharge Destination Code', 1, 30, help="Code representing the discharge destination.")
    
    with col2:
        st.image("image.webp", use_container_width=True)
    
    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    # Prediction Button
    if st.button("🔍 Predict Readmission Risk"):
        response, advice = prediction(input_list)
        st.success(f"**{response}**")
        st.info(advice)

# Run the app
if __name__ == "__main__":
    main()
