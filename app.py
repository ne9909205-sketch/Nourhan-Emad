import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. إعدادات الصفحة والهيدر الاحترافي باسمك
st.set_page_config(page_title="Diabetes AI System | Eng. Nourhan", layout="wide")

st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:10px;border: 2px solid #e0f2f1;margin-bottom:25px">
    <h1 style="color:white;text-align:center;font-family:Arial;">Diabetes Risk Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Final Project by: Eng. Nourhan Emad El-Din Mohamed</h3>
    </div>
    """, unsafe_allow_html=True)

# 2. تحميل الموديل (تأكدي أن اسم الملف diabetes_model.pkl)
@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model file: {e}")
    model = None

# 3. واجهة المدخلات (الـ 17 عمود حسب بياناتك)
if model:
    st.subheader("📋 Enter Patient Clinical Data")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', 1, 100, 25)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        bmi = st.number_input('Body Mass Index (BMI)', 10.0, 60.0, 24.5)
        bp = st.number_input('Blood Pressure (mm/Hg)', 60, 200, 120)
        glucose = st.number_input('Glucose Level', 50, 400, 100)
        insulin = st.number_input('Insulin Level', 0.0, 500.0, 80.0)

    with col2:
        hba1c = st.number_input('HbA1c Level', 3.0, 15.0, 5.5)
        chol = st.number_input('Cholesterol', 100, 500, 200)
        tri = st.number_input('Triglycerides', 50, 500, 150)
        activity = st.selectbox('Physical Activity', ['Low', 'Moderate', 'High'])
        diet = st.selectbox('Diet Quality', ['Poor', 'Average', 'Good'])
        sleep = st.number_input('Sleep Hours', 1, 12, 7)

    with col3:
        stress = st.selectbox('Stress Level', ['Low', 'Moderate', 'High'])
        family = st.selectbox('Family History', ['No', 'Yes'])
        waist = st.number_input('Waist (cm)', 40, 160, 85)
        smoke = st.selectbox('Smoking Status', ['No', 'Yes'])
        alcohol = st.selectbox('Alcohol Consumption', ['No', 'Yes'])

    # 4. تحويل الاختيارات لأرقام (Mapping)
    gen_val = 1 if gender == 'Male' else 0
    act_map = {'Low': 0, 'Moderate': 1, 'High': 2}
    diet_map = {'Poor': 0, 'Average': 1, 'Good': 2}
    stress_map = {'Low': 0, 'Moderate': 1, 'High': 2}
    bin_map = {'No': 0, 'Yes': 1}

    # تحضير المصفوفة للـ 17 عمود بالترتيب
    input_data = [
        age, gen_val, bmi, bp, glucose, insulin, hba1c, chol, tri,
        act_map[activity], diet_map[diet], sleep, stress_map[stress],
        bin_map[family], waist, bin_map[smoke], bin_map[alcohol]
    ]

    # 5. زر التوقع والنتيجة
    st.markdown("---")
    if st.button('Predict Diabetes Risk'):
        # تحويل البيانات لـ Numpy array وتغيير الشكل (Reshape)
        features = np.array(input_data).reshape(1, -1)
        
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ Prediction: High Risk of Diabetes")
        else:
            st.success("✅ Prediction: Low Risk / Healthy")

# الفوتر
st.markdown("---")
st.markdown(f"<p style='text-align:center; color:grey;'>Engineer: Nourhan Emad El-Din Mohamed | © 2026</p>", unsafe_allow_html=True)
