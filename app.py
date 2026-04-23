import streamlit as st
import pandas as pd
import joblib
import numpy as np

# إعدادات الصفحة باسمك
st.set_page_config(page_title="Diabetes System | Eng. Nourhan", layout="centered")

st.markdown("""
    <div style="background-color:#004d4d;padding:15px;border-radius:10px;">
    <h2 style="color:white;text-align:center;">Diabetes Prediction System</h2>
    <h4 style="color:#e0f2f1;text-align:center;">Eng. Nourhan Emad El-Din Mohamed</h4>
    </div>
    """, unsafe_allow_html=True)

# تحميل الموديل
@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

model = load_model()

# المدخلات الـ 9 الأساسية للموديل
st.write("### Patient Information")
age = st.number_input('Age', 1, 100, 25)
gender = st.selectbox('Gender', ['Male', 'Female'])
bmi = st.number_input('BMI', 10.0, 50.0, 24.0)
glucose = st.number_input('Glucose Level', 50, 300, 100)
hba1c = st.number_input('HbA1c Level', 3.0, 15.0, 5.5)
chol = st.number_input('Cholesterol', 100, 400, 200)
bp = st.number_input('Blood Pressure', 60, 200, 120)
smoking = st.selectbox('Smoking', ['No', 'Yes'])
family_history = st.selectbox('Family History', ['No', 'Yes'])

# تحويل البيانات لأرقام
gen_val = 1 if gender == 'Male' else 0
smoke_val = 1 if smoking == 'Yes' else 0
fam_val = 1 if family_history == 'Yes' else 0

# ترتيب البيانات الـ 9 المظبوط
features = np.array([[age, gen_val, bmi, glucose, hba1c, chol, bp, smoke_val, fam_val]])

if st.button('Predict'):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk / Healthy")

st.markdown("---")
st.caption("Developed by: Eng. Nourhan Emad El-Din Mohamed")
