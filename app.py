import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. إعدادات الصفحة والهيدر باسمك
st.set_page_config(page_title="Diabetes AI System | Eng. Nourhan", layout="wide")

st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:10px;border: 2px solid #e0f2f1;">
    <h1 style="color:white;text-align:center;">Diabetes Risk Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Project by: Eng. Nourhan Emad El-Din Mohamed</h3>
    </div>
    """, unsafe_allow_html=True)

# 2. تحميل الموديل
@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

model = load_model()

# 3. واجهة المدخلات (الـ 17 عمود)
st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', 1, 100, 25)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    bmi = st.number_input('BMI', 10.0, 50.0, 22.0)
    bp = st.number_input('Blood Pressure', 60, 200, 120)
    glucose = st.number_input('Glucose', 50, 300, 100)
    insulin = st.number_input('Insulin', 0.0, 500.0, 80.0)

with col2:
    hba1c = st.number_input('HbA1c', 3.0, 15.0, 5.5)
    chol = st.number_input('Cholesterol', 100, 400, 200)
    tri = st.number_input('Triglycerides', 50, 400, 150)
    activity = st.selectbox('Physical Activity', ['Low', 'Moderate', 'High'])
    diet = st.selectbox('Diet Quality', ['Poor', 'Average', 'Good'])
    sleep = st.number_input('Sleep Hours', 1, 12, 7)

with col3:
    stress = st.selectbox('Stress Level', ['Low', 'Moderate', 'High'])
    family = st.selectbox('Family History', ['No', 'Yes'])
    waist = st.number_input('Waist (cm)', 50, 150, 80)
    smoke = st.selectbox('Smoking', ['No', 'Yes'])
    alcohol = st.selectbox('Alcohol', ['No', 'Yes'])

# تحويل البيانات لأرقام
gen_val = 1 if gender == 'Male' else 0
act_map = {'Low': 0, 'Moderate': 1, 'High': 2}
diet_map = {'Poor': 0, 'Average': 1, 'Good': 2}
stress_map = {'Low': 0, 'Moderate': 1, 'High': 2}
bin_map = {'No': 0, 'Yes': 1}

# تجميع المدخلات
features = np.array([[age, gen_val, bmi, bp, glucose, insulin, hba1c, chol, tri, 
                      act_map[activity], diet_map[diet], sleep, stress_map[stress], 
                      bin_map[family], waist, bin_map[smoke], bin_map[alcohol]]])

# 4. زر التوقع والنتيجة
st.divider()
if st.button('Analyze Risk'):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ Result: High Risk of Diabetes")
    else:
        st.success("✅ Result: Low Risk / Healthy")

# 5. الفوتر
st.markdown("<p style='text-align:center;'>© Eng. Nourhan Emad El-Din Mohamed</p>", unsafe_allow_html=True)
