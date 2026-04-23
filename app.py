import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. إعدادات الصفحة والشكل العام
st.set_page_config(page_title="Diabetes AI System", page_icon="🔬", layout="wide")

# 2. تصميم الواجهة الأمامية (Header)
st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Diabetes Risk Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Project by: Eng. Nourhan Emad El-Din Mohamed</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("") # مسافة

# 3. تحميل الموديل المحفوظ
try:
    model = joblib.load('diabetes_model.pkl')
    le = joblib.load('label_encoder.pkl')
except:
    st.error("Model file not found! Please run the training code first.")

# 4. تقسيم الصفحة لعمودين (بيانات المدخلات - والنتائج)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Patient Biological Data")
    
    with st.container():
        age = st.slider('Select Age', 1, 100, 25)
        gender = st.selectbox('Gender', ('Female', 'Male'))
        bmi = st.number_input('Body Mass Index (BMI)', 10.0, 60.0, 22.0)
        bp = st.number_input('Blood Pressure (mmHg)', 50, 200, 120)
        glucose = st.number_input('Fasting Glucose Level', 50, 300, 100)
        hba1c = st.number_input('HbA1c Level (%)', 3.0, 15.0, 5.5)
        activity = st.selectbox('Physical Activity Level', ('Low', 'Moderate', 'High'))

# 5. معالجة البيانات للتوقع
# تحويل النصوص لأرقام يدويًا أو بالـ encoder لضمان الدقة
gender_num = 0 if gender == 'Female' else 1
activity_map = {'Low': 0, 'Moderate': 1, 'High': 2}
activity_num = activity_map[activity]

input_data = np.array([[age, gender_num, bmi, bp, glucose, hba1c, activity_num]])

with col2:
    st.subheader("🎯 Prediction Result")
    st.write("Click the button below to analyze the data.")
    
    if st.button('Predict My Risk'):
        prediction = model.predict(input_data)
        result = prediction[0]
        
        # عرض النتيجة بألوان وتنسيق مختلف حسب الفئة
        if result == 'High Risk':
            st.error(f"Prediction: {result}")
            st.warning("⚠️ Recommendation: Urgent medical check-up is advised.")
        elif result == 'Prediabetes':
            st.warning(f"Prediction: {result}")
            st.info("💡 Recommendation: Improve diet and increase physical activity.")
        else:
            st.success(f"Prediction: {result}")
            st.balloons()
            st.write("🌟 Recommendation: Your markers are within healthy limits.")

# 6. تذييل الصفحة (Footer)
st.markdown("---")
st.markdown("""
    <div style="text-align:center">
    <p>© 2026 Graduation Project | <b>Eng. Nourhan Emad El-Din Mohamed</b></p>
    </div>
    """, unsafe_allow_html=True)
