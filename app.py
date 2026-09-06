import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="AI Healthcare Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Healthcare Analytics & Prediction Dashboard")
st.write("AI-powered healthcare screening and analytics system")

st.divider()

st.header("🩸 Diabetes Risk Prediction")

age = st.number_input("Age", min_value=1, max_value=120, value=30)

hypertension = st.selectbox(
    "Hypertension",
    ["No", "Yes"]
)

heart_disease = st.selectbox(
    "Heart Disease",
    ["No", "Yes"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=70.0,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=3.0,
    max_value=10.0,
    value=5.5
)

glucose = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)

smoking = st.selectbox(
    "Smoking History",
    ["never", "former", "current", "No Info", "ever", "not current"]
)

if st.button("🔍 Predict Diabetes Risk"):

    try:
        model = joblib.load("diabetes_model.pkl")

        input_data = pd.DataFrame({
            "age": [age],
            "hypertension": [1 if hypertension == "Yes" else 0],
            "heart_disease": [1 if heart_disease == "Yes" else 0],
            "bmi": [bmi],
            "HbA1c_level": [hba1c],
            "blood_glucose_level": [glucose],
            "gender_Male": [1 if gender == "Male" else 0],
            "gender_Other": [1 if gender == "Other" else 0],
            "smoking_history_current": [1 if smoking == "current" else 0],
            "smoking_history_ever": [1 if smoking == "ever" else 0],
            "smoking_history_former": [1 if smoking == "former" else 0],
            "smoking_history_never": [1 if smoking == "never" else 0],
            "smoking_history_not current": [1 if smoking == "not current" else 0]
        })

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ Higher Diabetes Risk")
        else:
            st.success("✅ Lower Diabetes Risk")

    except Exception as e:
        st.error(f"Error: {e}")