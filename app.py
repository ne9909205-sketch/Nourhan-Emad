import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. إعدادات الصفحة والهيدر باسمك
st.set_page_config(page_title="Diabetes AI System | Eng. Nourhan", page_icon="🔬", layout="wide")

st.markdown("""
    <div style="background-color:#004d4d;padding:25px;border-radius:15px;border: 2px solid #e0f2f1;margin-bottom:20px">
    <h1 style="color:white;text-align:center;font-family:Arial;">Diabetes Risk Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Developed by: Eng. Nourhan Emad El-Din Mohamed</h3>
    <p style="color:#b2dfdb;text-align:center;">Graduation Project - Machine Learning Edition</p>
    </div>
    """, unsafe_allow_html=True)

# 2. تحميل الموديل وملف التشفير
@st.cache_resource
def load_models():
    try:
        model = joblib.load('diabetes_model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_models()

# 3. واجهة المدخلات (الـ 17 عمود بناءً على الداتا بتاعتك)
if model:
    st.subheader("📋 Patient Clinical & Lifestyle Data")
    
    # تقسيم المدخلات لـ 3 أعمدة عشان الشكل يكون "Elegant"
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', 1, 120, 25)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        bmi = st.number_input('Body Mass Index (BMI)', 10.0, 70.0, 24.0)
        bp = st.number_input('Blood Pressure (mm/Hg)', 50, 250, 120)
        glucose = st.number_input('Fasting Glucose (mg/dL)', 50, 400, 100)
        insulin = st.number_input('Insulin Level (mu U/ml)', 0.0, 600.0, 80.0)

    with col2:
        hba1c = st.number_input('HbA1c Level', 3.0, 18.0, 5.5)
        chol = st.number_input('Cholesterol (mg/dL)', 100, 500, 200)
        tri = st.number_input('Triglycerides (mg/dL)', 50, 500, 150)
        activity = st.selectbox('Physical Activity', ['Low', 'Moderate', 'High'])
        diet = st.selectbox('Diet Quality', ['Poor', 'Average', 'Good'])
        sleep = st.number_input('Sleep Hours', 1, 24, 7)

    with col3:
        stress = st.selectbox('Stress Level', ['Low', 'Moderate', 'High'])
        family = st.selectbox('Family History of Diabetes', ['No', 'Yes'])
        waist
