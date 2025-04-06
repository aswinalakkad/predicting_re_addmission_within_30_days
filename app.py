import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    pred = model.predict(input_data)[0]
    if pred == 1:
        return 'High Risk of Readmission'
    else:
        return 'Low Risk of Readmission'

def convert_age_to_group(age):
    # Convert age to group: 0-10 → 1, 10-20 → 2, ..., 90-100 → 10
    return min(max(int(age // 10) + 1, 1), 10)

def main():
    st.title('🏥 Early Readmission Prediction for Diabetic Patients')
    st.subheader('Predicting if a diabetic patient is at high risk of early hospital readmission.')
    
    st.markdown('---')
    st.markdown('### 📝 Input Patient Data')

    # Gender
    gender = st.radio('Gender', options=[0.0, 1.0], format_func=lambda x: 'Male' if x == 0.0 else 'Female', horizontal=True)

    # Age (convert to group)
    age = st.number_input('Age (in years)', min_value=1, max_value=99, step=1)
    age_group = float(convert_age_to_group(age))

    # Admission Type
    admission_type_id = st.radio(
        'Admission Type',
        options=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
        format_func=lambda x: f'Type {int(x)}',
        horizontal=True
    )

    # Time in Hospital
    time_in_hospital = st.number_input('Time in Hospital (days)', min_value=1.0, max_value=30.0, step=1.0)

    # Lab Procedures
    num_lab_procedures = st.number_input('Number of Lab Procedures', min_value=0.0, step=1.0)

    # Medications
    num_medications = st.number_input('Number of Medications', min_value=0.0, step=1.0)

    # Inpatient Visits
    number_inpatient = st.number_input('Number of Inpatient Visits', min_value=0.0, step=1.0)

    # Diagnosis Codes
    diag_1 = st.number_input('Primary Diagnosis Code')
    diag_2 = st.number_input('Secondary Diagnosis Code')
    diag_3 = st.number_input('Additional Diagnosis Code')

    # Metformin
    metformin = st.radio('Metformin Use', options=[0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes', horizontal=True)

    # Insulin
    insulin = st.radio(
        'Insulin Use',
        options=[0, 1, 2, 3],
        format_func=lambda x: {0: 'No', 1: 'Up', 2: 'Steady', 3: 'Down'}[x],
        horizontal=True
    )

    # Change in Medications
    change = st.radio('Change in Medications', options=[0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes', horizontal=True)

    # Diabetes Medication
    diabetesMed = st.radio('Diabetes Medication', options=[0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes', horizontal=True)

    # Discharge Destination
    discharged_to = st.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0, step=1.0)

    input_list = [[gender, age_group, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    if st.button('🔍 Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
