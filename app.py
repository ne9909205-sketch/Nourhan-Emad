import streamlit as st
import pickle
import numpy as np

# 1. إعدادات الصفحة والشكل (Theme)
st.set_page_config(page_title="Diabetes Prediction", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .header-container {
        background-color: #f1f8e9;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #c8e6c9;
        margin-bottom: 30px;
    }
    .main-title { color: #2e7d32; font-weight: bold; }
    .eng-name { color: #546e7a; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. تحميل الموديل (تأكدي أن الملف بجانب الكود بنفس الاسم)
try:
    with open('diabetes_model.sav', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ ملف الموديل 'diabetes_model.sav' غير موجود في المجلد.")

# 3. العنوان
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# 4. توزيع الـ 17 خانة في 3 أعمدة
col1, col2, col3 = st.columns(3)

with col1:
    v1 = st.number_input("1. العمر (Age)", value=40)
    v2 = st.selectbox("2. النوع (Gender)", [0, 1], format_func=lambda x: "ذكر" if x==1 else "أنثى")
    v3 = st.selectbox("3. كثرة التبول", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v4 = st.selectbox("4. العطش الشديد", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v5 = st.selectbox("5. فقدان وزن مفاجئ", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v6 = st.selectbox("6. الإجهاد", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")

with col2:
    v7 = st.selectbox("7. زيادة الشهية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v8 = st.selectbox("8. مشاكل تناسلية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v9 = st.selectbox("9. تشوش الرؤية", [0,
