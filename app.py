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
    st.set_page_config(page_title="Diabetes Readmission Prediction", layout="centered")

    # Add a banner image
    st.image("image.webp", use_column_width=True)

    # App title and description
    st.title("🏥 Early Readmission Prediction for Diabetic Patients")
    st.markdown("This app predicts if a diabetic patient is at **high risk of early readmission (within 30 days)**.")

    # Compact layout using columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔢 Basic Information")
        gender = st.selectbox('Gender', [0.0, 1.0], format_func=lambda x: 'Male' if x == 0.0 else 'Female')
        age = st.slider('Age Group', 1, 10)
        admission_type_id = st.selectbox('Admission Type', range(1, 9))
        time_in_hospital = st.slider('Hospital Stay (Days)', 1, 30)
        num_lab_procedures = st.number_input('Lab Procedures', min_value=0, step=1)
        num_medications = st.number_input('Medications', min_value=0, step=1)
        number_inpatient = st.number_input('Previous Inpatient Visits', min_value=0, step=1)

    with col2:
        st.subheader("📌 Additional Details")
        with st.expander("Click to enter diagnosis & medication details"):
            diag_1 = st.number_input('Primary Diagnosis Code', step=1)
            diag_2 = st.number_input('Secondary Diagnosis Code', step=1)
            diag_3 = st.number_input('Additional Diagnosis Code', step=1)
            metformin = st.selectbox('Metformin Use', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
            insulin = st.selectbox('Insulin Use', [1.0, 2.0, 3.0], format_func=lambda x: {1.0: 'No', 2.0: 'Up', 3.0: 'Steady'}[x])
            change = st.selectbox('Change in Medications', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
            diabetesMed = st.selectbox('Diabetes Medication', [0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
            discharged_to = st.slider('Discharge Destination Code', 1, 30)

    input_list = [[gender, age, admission_type_id, time_in_hospital, num_lab_procedures,
                   num_medications, number_inpatient, diag_1, diag_2, diag_3, metformin,
                   insulin, change, diabetesMed, discharged_to]]

    # Prediction Button
    if st.button("🔍 Predict Readmission Risk"):
        response, advice = prediction(input_list)
        st.success(f"**{response}**")
        st.info(advice)

    # Use Cases & Suggestions (Collapsible)
    with st.expander("📊 Use Cases & Recommendations"):
        st.subheader("🔹 Use Cases of Readmission Prediction")
        st.markdown("""
        - **Hospital Management:** Allocate resources for high-risk patients.
        - **Improved Patient Care:** Alerts healthcare providers for extra care.
        - **Cost Reduction:** Prevents avoidable readmissions, reducing costs.
        - **Insurance Optimization:** Helps insurers assess patient risk.
        """)
        
        st.subheader("💡 Recommendations for High-Risk Patients")
        st.markdown("""
        - **Monitor Blood Sugar Levels:** Keep glucose levels stable.
        - **Follow Medications Strictly:** Avoid skipping doses.
        - **Healthy Lifestyle:** Exercise, eat well, manage stress.
        - **Regular Follow-Ups:** Attend post-hospitalization checkups.
        """)

# Run the app
if __name__ == "__main__":
    main()
