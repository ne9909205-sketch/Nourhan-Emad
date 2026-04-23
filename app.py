import streamlit as st
import pandas as pd
import joblib
import numpy as np

# إعداد الصفحة باسمك
st.set_page_config(page_title="Diabetes AI | Eng. Nourhan", layout="wide")

st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:15px;border: 2px solid #e0f2f1;">
    <h1 style="color:white;text-align:center;">Diabetes Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Eng. Nourhan Emad El-Din Mohamed</h3>
    </div>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

model = load_model()

# عرض الـ 17 خانة كاملة
st.write("### Patient Clinical Data (Full Parameters)")
col1, col2, col3 = st.columns(3)

with col1:
    v1 = st.number_input('Age', 1, 100, 25)
    v2 = st.selectbox('Gender (Male=1, Female=0)', [1, 0])
    v3 = st.number_input('BMI', 10.0, 60.0, 24.5)
    v4 = st.number_input('Blood Pressure', 60, 200, 120)
    v5 = st.number_input('Glucose', 50, 400, 100)
    v6 = st.number_input('Insulin', 0.0, 500.0, 80.0)

with col2:
    v7 = st.number_input('HbA1c', 3.0, 15.0, 5.5)
    v8 = st.number_input('Cholesterol', 100, 500, 200)
    v9 = st.number_input('Triglycerides', 50, 500, 150)
    v10 = st.number_input('Activity Level (0-2)', 0, 2, 1)
    v11 = st.number_input('Diet Quality (0-2)', 0, 2, 1)
    v12 = st.number_input('Sleep Hours', 1, 12, 7)

with col3:
    v13 = st.number_input('Stress Level (0-2)', 0, 2, 1)
    v14 = st.selectbox('Family History (Yes=1, No=0)', [1, 0])
    v15 = st.number_input('Waist (cm)', 40, 160, 85)
    v16 = st.selectbox('Smoking (Yes=1, No=0)', [1, 0])
    v17 = st.selectbox('Alcohol (Yes=1, No=0)', [1, 0])

# تجميع البيانات
all_features = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17]

# التأكد من عدد الأعمدة المطلوب للموديل لمنع الـ ValueError
n_required = model.n_features_in_
final_features = np.array(all_features[:n_required]).reshape(1, -1)

if st.button('Predict Now'):
    prediction = model.predict(final_features)
    if prediction[0] == 1:
        st.error("⚠️ Result: High Risk")
    else:
        st.success("✅ Result: Healthy / Low Risk")

st.markdown("---")
st.caption("Developed by: Eng. Nourhan Emad El-Din Mohamed")
