import streamlit as st
import numpy as np
import pandas as pd
import pickle 

# Load the trained model
with open('final_model.pkl','rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    pred = model.predict(input_data)[0]
    
    if pred == 1:
        return 'High Risk of Readmission'
    else:
        return 'Low Risk of Readmission'

def main():
    st.title('Early Readmission Prediction for Diabetic Patients')
    st.subheader('This application predicts whether a diabetic patient is at high risk of early hospital readmission.')
    
    st.markdown('### Input Patient Data')
    st.markdown('Please enter the following details to get a prediction:')
    
    st.markdown('*Gender:* 0 - Male, 1 - Female')
    gender = st.selectbox('Select Gender', [0.0, 1.0])
    
    st.markdown('*Age Group:* Categorized (1: 0-10, 2: 10-20, ..., 10: 90-100)')
    age = st.number_input('Select Age Group', min_value=1.0, max_value=10.0)
    
    st.markdown('*Admission Type:* 1 - Emergency, 2 - Urgent, 3 - Elective, etc.')
    admission_type_id = st.selectbox('Select Admission Type', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
    
    st.markdown('*Time in Hospital (Days):* Number of days the patient stayed in the hospital')
    time_in_hospital = st.number_input('Enter Time in Hospital', min_value=1.0, max_value=30.0)
    
    st.markdown('*Number of Lab Procedures:* Total lab tests performed')
    num_lab_procedures = st.number_input('Enter Number of Lab Procedures', min_value=0.0)
    
    st.markdown('*Number of Medications:* Total medications prescribed')
    num_medications = st.number_input('Enter Number of Medications', min_value=0.0)
    
    st.markdown('*Number of Inpatient Visits:* Previous inpatient visits')
    number_inpatient = st.number_input('Enter Number of Inpatient Visits', min_value=0.0)
    
    st.markdown('*Primary Diagnosis Code:* ICD-9 numerical code for primary diagnosis')
    diag_1 = st.number_input('Enter Primary Diagnosis Code')
    
    st.markdown('*Secondary Diagnosis Code:* ICD-9 numerical code for secondary diagnosis')
    diag_2 = st.number_input('Enter Secondary Diagnosis Code')
    
    st.markdown('*Additional Diagnosis Code:* ICD-9 numerical code for additional diagnosis')
    diag_3 = st.number_input('Enter Additional Diagnosis Code')
    
    st.markdown('*Metformin Use:* 0 - No, 1 - Yes')
    metformin = st.selectbox('Select Metformin Use', [0.0, 1.0])
    
    st.markdown('*Insulin Use:* 1 - No, 2 - Up, 3 - Steady')
    insulin = st.selectbox('Select Insulin Use', [1.0, 2.0, 3.0])
    
    st.markdown('*Change in Medications:* 0 - No, 1 - Yes')
    change = st.selectbox('Select Change in Medications', [0.0, 1.0])
    
    st.markdown('*Diabetes Medication:* 0 - No, 1 - Yes')
    diabetesMed = st.selectbox('Select Diabetes Medication', [0.0, 1.0])
    
    st.markdown('*Discharge Destination Code:* Numerical code representing discharge destination')
    discharged_to = st.number_input('Enter Discharge Destination Code', min_value=1.0, max_value=30.0)
    
    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]
    
    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)

if __name__ == '__main__':
    main()
