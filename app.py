import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. تصميم الواجهة باسمك
st.set_page_config(page_title="Diabetes AI | Eng. Nourhan", layout="wide")

st.markdown("""
    <div style="background-color:#004d4d;padding:20px;border-radius:10px;border: 2px solid #e0f2f1;">
    <h1 style="color:white;text-align:center;">Diabetes Prediction System</h1>
    <h3 style="color:#e0f2f1;text-align:center;">Project by: Eng. Nourhan Emad El-Din Mohamed</h3>
    </div>
    """, unsafe_allow_html=True)

# 2. تحميل الموديل
@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

try:
    model = load_model()
    # معرفة عدد الأعمدة اللي الموديل متدرب عليها
    expected_features = model.n_features_in_
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# 3. عرض الخانات (الداتا الكاملة)
if model:
    st.write(f"### Please fill in the {expected_features} clinical parameters:")
    
    # توزيع الخانات في أعمدة عشان الشكل يكون "شيك"
    cols = st.columns(3)
    inputs = []
    
    # توليد الخانات تلقائياً بناءً على حاجة الموديل لمنع أي ValueError
    for i in range(expected_features):
        with cols[i % 3]:
            val = st.number_input(f"Parameter {i+1}", value=0.0, key=f"input_{i}")
            inputs.append(val)

    st.markdown("---")
    if st.button('Predict Diabetes Risk'):
        features = np.array(inputs).reshape(1, -1)
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ Result: High Risk of Diabetes")
        else:
            st.success("✅ Result: Low Risk / Healthy")

st.markdown("---")
st.caption("Developed by: Eng. Nourhan Emad El-Din Mohamed | Graduation Project 2026")
