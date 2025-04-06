import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to convert age to age group
def get_age_group(age):
    if age < 0:
        return 1.0
    elif age >= 100:
        return 10.0
    return float((age // 10) + 1)

# Prediction function
def prediction(input_data):
    pred = model.predict(input_data)[0]
    if pred == 1:
        return '⚠️ High Risk of Readmission'
    else:
        return '✅ Low Risk of Readmission'

# Main UI
def main():
    st.title('🧬 Early Readmission Risk Prediction')
    st.subheader('For Diabetic Patients')
    st.markdown('This tool predicts the **likelihood of early hospital readmission** for diabetic patients based on input features.')

    st.markdown('---')
    st.header('🔍 Patient Information')

    gender = st.radio('Gender:', ['Male', 'Female'])
    gender = 0.0 if gender == 'Male' else 1.0

    age = st.number_input('Age (in years):', min_value=0, max_value=120, step=1)
    age_group = get_age_group(age)

    admission_type_id = st.selectbox('Admission Type:', {
        1.0: 'Emergency',
        2.0: 'Urgent',
        3.0: 'Elective',
        4.0: 'Newborn',
        5.0: 'Not Available',
        6.0: 'NULL',
        7.0: 'Trauma Center',
        8.0: 'Not Mapped'
    }.items(), format_func=lambda x: x[1])[0]

    time_in_hospital = st.number_input(
    '🛏️ Time in Hospital (Days)',
    min_value=1,
    max_value=30,
    value=3,
    step=1,
    help='Enter the number of days the patient was hospitalized (1–30 days)'
    )
    num_lab_procedures = st.number_input('Number of Lab Procedures:', min_value=0)
    num_medications = st.number_input('Number of Medications:', min_value=0)
    number_inpatient = st.number_input('Number of Inpatient Visits:', min_value=0)

    diag_1 = st.number_input('Primary Diagnosis Code (ICD-9):')
    diag_2 = st.number_input('Secondary Diagnosis Code (ICD-9):')
    diag_3 = st.number_input('Additional Diagnosis Code (ICD-9):')

    metformin = st.radio('Metformin Use:', ['No', 'Yes'])
    metformin = 0.0 if metformin == 'No' else 1.0

    insulin = st.selectbox('Insulin Use:', {
        1.0: 'No',
        2.0: 'Up',
        3.0: 'Steady'
    }.items(), format_func=lambda x: x[1])[0]

    change = st.radio('Change in Medications:', ['No', 'Yes'])
    change = 0.0 if change == 'No' else 1.0

    diabetesMed = st.radio('Diabetes Medication:', ['No', 'Yes'])
    diabetesMed = 0.0 if diabetesMed == 'No' else 1.0

    discharged_to = st.number_input('Discharge Destination Code:', min_value=1.0, max_value=30.0)

    input_list = [[gender, age_group, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    if st.button('🔮 Predict Readmission Risk'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
