import streamlit as st
import numpy as np

# 1. إعداد الصفحة وتنسيق الألوان الفاتحة (Professional Light Theme)
st.set_page_config(page_title="Diabetes Prediction", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-title { color: #2e7d32; text-align: center; font-size: 2.8rem; font-weight: bold; margin-bottom: 0px; }
    .eng-name { color: #546e7a; text-align: center; font-size: 1.2rem; margin-bottom: 20px; }
    .stNumberInput label, .stSelectbox label, .stSlider label {
        color: #2e7d32 !important; font-weight: bold !important;
    }
    div[data-baseweb="input"] { border-radius: 10px !important; }
    hr { border: 0; height: 1px; background: #e0e0e0; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# العنوان
st.markdown('<h1 class="main-title">Diabetes Prediction System</h1>', unsafe_allow_html=True)
st.markdown('<p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# 2. إنشاء الـ 17 خانة وتوزيعهم في 3 أعمدة عشان الزحمة
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📍 General Info")
    v1 = st.number_input("1. Age", value=40)
    v2 = st.selectbox("2. Gender", [0, 1], format_func=lambda x: "Male" if x==1 else "Female")
    v3 = st.selectbox("3. Polyuria", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v4 = st.selectbox("4. Polydipsia", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v5 = st.selectbox("5. Sudden Weight Loss", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v6 = st.selectbox("6. Weakness", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")

with col2:
    st.info("🧪 Clinical Symptoms")
    v7 = st.selectbox("7. Polyphagia", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v8 = st.selectbox("8. Genital Thrush", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v9 = st.selectbox("9. Visual Blurring", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v10 = st.selectbox("10. Itching", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v11 = st.selectbox("11. Irritability", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v12 = st.selectbox("12. Delayed Healing", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")

with col3:
    st.info("📉 Medical Indicators")
    v13 = st.selectbox("13. Partial Paresis", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v14 = st.selectbox("14. Muscle Stiffness", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v15 = st.selectbox("15. Alopecia", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v16 = st.selectbox("16. Obesity", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    v17 = st.number_input("17. Blood Glucose Level", value=100)

st.markdown('<hr>', unsafe_allow_html=True)

# 3. زر التوقع والنتيجة
if st.button("Predict Diagnosis", use_container_width=True):
    # تجميع الـ 17 قيمة في مصفوفة واحدة للموديل
    input_data = np.array([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17]])
    
    # ملاحظة: هنا لازم يكون عندك الموديل محمّل عشان يعمل predict
    # st.write(model.predict(input_data)) 
    
    st.success("Analysis Complete. The system is ready to process the 17 parameters.")
    st.balloons() # حركة احتفالية بسيطة عند الضغط
