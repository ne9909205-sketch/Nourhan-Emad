import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Diabetes Prediction", layout="wide")

# 2. كود التنسيق الجمالي (CSS) - لتحويل الموقع للون فاتح ومريح
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
    .header-box {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e9ecef;
        margin-bottom: 40px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    h1 { color: #2c3e50 !important; font-family: 'Trebuchet MS', sans-serif; }
    p.eng-name { color: #7f8c8d !important; font-size: 1.2rem; }
    .stNumberInput, .stSelectbox { margin-bottom: 20px; }
    </style>
    
    <div class="header-box">
        <h1>Diabetes Prediction System</h1>
        <p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# 3. تنظيم الخانات (Inputs) في أعمدة عشان تظهر كلها
st.subheader("Patient Clinical Data (Full Parameters)")

# هنقسم الصفحة لـ 3 أعمدة عشان الخانات تكون مريحة للعين ومترتبة
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    hba1c = st.number_input("HbA1c", value=5.50, format="%.2f")
    cholesterol = st.number_input("Cholesterol", value=200)

with col2:
    smoking = st.selectbox("Smoking", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    triglycerides = st.number_input("Triglycerides", value=150)
    stress = st.slider("Stress Level (0-2)", 0, 2, 1)

with col3:
    family_history = st.selectbox("Family History", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    waist = st.number_input("Waist (cm)", value=85)
    activity = st.slider("Activity Level (0-2)", 0, 2, 1)

# إضافة خانة ضغط الدم لو كانت موجودة عندك
blood_pressure = st.number_input("Blood Pressure", value=120)

st.markdown("---")

# 4. زر التوقع والنتيجة
col_btn, col_res = st.columns([1, 2])
with col_btn:
    if st.button("Predict Result", use_container_width=True):
        # هنا هتحطي الكود بتاع الموديل بتاعك (Model Prediction)
        # مثال: result = model.predict([[...]])
        st.info("Result will appear here") # ده مكان النتيجة
