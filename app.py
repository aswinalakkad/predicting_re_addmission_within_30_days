import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction function
def prediction(input_data):
    pred = model.predict(input_data)[0]
    if pred == 1:
        return '⚠️ High Risk of Early Readmission'
    else:
        return '✅ Low Risk of Early Readmission'

# Main app
def main():
    st.set_page_config(page_title="Diabetic Readmission Predictor", layout="centered")
    st.title('🩺 Early Readmission Prediction for Diabetic Patients')
    st.markdown('---')
    st.markdown("""
        This application uses a trained machine learning model to predict whether a **diabetic patient** is at **high risk of early hospital readmission**.
        Please fill in the following patient information to receive a prediction.
    """)

    st.markdown('### 👤 Demographics & Admission Info')
    gender = st.radio('Gender', ['Male (0)', 'Female (1)'])
    gender = 0.0 if 'Male' in gender else 1.0

    age = st.slider('Age Group (1: 0-10, ..., 10: 90-100)', 1.0, 10.0, step=1.0)
    admission_type_id = st.selectbox('Admission Type', {
        1.0: 'Emergency', 2.0: 'Urgent', 3.0: 'Elective',
        4.0: 'Newborn', 5.0: 'Not Available', 6.0: 'NULL',
        7.0: 'Trauma Center', 8.0: 'Other'
    })

    st.markdown('### 🏥 Hospital Stay Details')
    time_in_hospital = st.number_input('Time in Hospital (days)', 1.0, 30.0)
    num_lab_procedures = st.number_input('Number of Lab Procedures', 0.0)
    num_medications = st.number_input('Number of Medications', 0.0)
    number_inpatient = st.number_input('Number of Inpatient Visits', 0.0)

    st.markdown('### 🧬 Diagnosis Codes')
    diag_1 = st.number_input('Primary Diagnosis Code (ICD-9)')
    diag_2 = st.number_input('Secondary Diagnosis Code (ICD-9)')
    diag_3 = st.number_input('Additional Diagnosis Code (ICD-9)')

    st.markdown('### 💊 Medications & Treatment')
    metformin = st.radio('Metformin Use', ['No (0)', 'Yes (1)'])
    metformin = 0.0 if 'No' in metformin else 1.0

    insulin = st.selectbox('Insulin Use', {1.0: 'No', 2.0: 'Up', 3.0: 'Steady'})
    change = st.radio('Change in Medications', ['No (0)', 'Yes (1)'])
    change = 0.0 if 'No' in change else 1.0

    diabetesMed = st.radio('On Diabetes Medication', ['No (0)', 'Yes (1)'])
    diabetesMed = 0.0 if 'No' in diabetesMed else 1.0

    discharged_to = st.number_input('Discharge Destination Code (1-30)', 1.0, 30.0)

    # Input list for model
    input_list = [[
        gender, age, float(admission_type_id), time_in_hospital,
        num_lab_procedures, num_medications, number_inpatient,
        diag_1, diag_2, diag_3, metformin, float(insulin),
        change, diabetesMed, discharged_to
    ]]

    # Prediction button
    if st.button('🔍 Predict Readmission Risk'):
        with st.spinner('Analyzing patient data...'):
            response = prediction(input_list)
            st.success(response)

if __name__ == '__main__':
    main()
