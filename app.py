import streamlit as st
import numpy as np
import pandas as pd
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

def get_age_group(age):
    if age < 10:
        return 1.0
    elif age < 20:
        return 2.0
    elif age < 30:
        return 3.0
    elif age < 40:
        return 4.0
    elif age < 50:
        return 5.0
    elif age < 60:
        return 6.0
    elif age < 70:
        return 7.0
    elif age < 80:
        return 8.0
    elif age < 90:
        return 9.0
    else:
        return 10.0

def main():
    st.title('Early Readmission Prediction for Diabetic Patients')
    st.subheader('Predicts whether a diabetic patient is at high risk of early hospital readmission.')
    
    st.markdown('### Input Patient Data')

    gender = st.radio('Gender (0: Male, 1: Female)', [0.0, 1.0], horizontal=True)
    age_input = st.number_input('Age', min_value=0, max_value=100, step=1)
    age = get_age_group(age_input)

    admission_type_id = st.selectbox('Admission Type (1: Emergency, 2: Urgent, 3: Elective, etc.)',
                                     [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    
    time_in_hospital = st.number_input('Time in Hospital (Days)', min_value=1.0, max_value=30.0, step=1.0)
    
    num_lab_procedures = st.number_input('Number of Lab Procedures', min_value=0.0)
    num_medications = st.number_input('Number of Medications', min_value=0.0)
    number_inpatient = st.number_input('Number of Inpatient Visits', min_value=0.0)
    
    diag_1 = st.number_input('Primary Diagnosis Code')
    diag_2 = st.number_input('Secondary Diagnosis Code')
    diag_3 = st.number_input('Additional Diagnosis Code')

    metformin = st.radio('Metformin Use (0: No, 1: Yes)', [0.0, 1.0], horizontal=True)

    insulin_map = {
        0: 'No',
        1: 'Up',
        2: 'Steady',
        3: 'Down'
    }
    insulin_label = st.radio('Insulin Use', list(insulin_map.values()), horizontal=True)
    insulin = float([k for k, v in insulin_map.items() if v == insulin_label][0])

    change = st.radio('Change in Medications (0: No, 1: Yes)', [0.0, 1.0], horizontal=True)
    diabetesMed = st.radio('Diabetes Medication (0: No, 1: Yes)', [0.0, 1.0], horizontal=True)

    discharged_to = st.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0, step=1.0)

    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
