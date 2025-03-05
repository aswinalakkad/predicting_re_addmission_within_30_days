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

    # Add a banner image
    st.image("hospital_banner.jpg", use_column_width=True)

    # App title and description
    st.title("🏥 Early Readmission Prediction for Diabetic Patients")
    st.markdown("This application helps predict whether a diabetic patient is at **high risk of early hospital readmission (within 30 days)**.")

    # Professional layout using columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔢 Enter Patient Data")
        
        gender = st.selectbox('Gender (0 - Male, 1 - Female)', [0.0, 1.0])
        age = st.number_input('Age Group (1: 0-10, ..., 10: 90-100)', min_value=1.0, max_value=10.0)
        admission_type_id = st.selectbox('Admission Type', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        time_in_hospital = st.number_input('Time in Hospital (Days)', min_value=1.0, max_value=30.0)
        num_lab_procedures = st.number_input('Number of Lab Procedures', min_value=0.0)
        num_medications = st.number_input('Number of Medications', min_value=0.0)
        number_inpatient = st.number_input('Number of Inpatient Visits', min_value=0.0)

    with col2:
        st.subheader("📌 Additional Details")

        diag_1 = st.number_input('Primary Diagnosis Code')
        diag_2 = st.number_input('Secondary Diagnosis Code')
        diag_3 = st.number_input('Additional Diagnosis Code')
        metformin = st.selectbox('Metformin Use (0 - No, 1 - Yes)', [0.0, 1.0])
        insulin = st.selectbox('Insulin Use (1 - No, 2 - Up, 3 - Steady)', [1.0, 2.0, 3.0])
        change = st.selectbox('Change in Medications (0 - No, 1 - Yes)', [0.0, 1.0])
        diabetesMed = st.selectbox('Diabetes Medication (0 - No, 1 - Yes)', [0.0, 1.0])
        discharged_to = st.number_input('Discharge Destination Code', min_value=1.0, max_value=30.0)

    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    # Prediction Button
    if st.button("🔍 Predict Readmission Risk"):
        response, advice = prediction(input_list)
        st.subheader("🛑 Prediction Result")
        st.write(f"**{response}**")
        st.info(advice)

    # Use Cases Section
    st.markdown("---")
    st.subheader("📊 Use Cases of Readmission Prediction")
    st.markdown("""
    - **Hospital Management:** Helps hospitals allocate resources for high-risk patients.
    - **Patient Care Improvement:** Alerts healthcare providers to offer extra care.
    - **Reducing Costs:** Prevents avoidable readmissions, reducing healthcare costs.
    - **Insurance Optimization:** Helps insurance companies assess patient risk.
    """)

    # Suggestions for Patients
    st.subheader("💡 Recommendations for Patients at High Risk")
    st.markdown("""
    - **Monitor Blood Sugar Levels:** Keep glucose levels in check.
    - **Follow Prescribed Medications:** Avoid skipping or changing medications without consulting a doctor.
    - **Healthy Lifestyle:** Exercise, eat a balanced diet, and manage stress.
    - **Regular Follow-Ups:** Attend post-hospitalization checkups to prevent complications.
    """)

# Run the app
if __name__ == "__main__":
    main()
