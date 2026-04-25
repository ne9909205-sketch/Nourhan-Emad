import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Diabetes Prediction System", layout="wide")

# تنسيق الألوان (النمط الفاتح)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-title { color: #2e7d32; text-align: center; font-size: 2.5rem; font-weight: bold; margin-bottom: 5px; }
    .sub-title { color: #546e7a; text-align: center; font-size: 1.2rem; margin-bottom: 30px; }
    .stNumberInput, .stSelectbox, .stSlider { margin-bottom: 10px; }
    hr { margin-top: 20px; margin-bottom: 20px; }
    </style>
    <div>
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="sub-title">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    <hr>
    """, unsafe_allow_html=True)

# تقسيم الـ 17 خانة على 3 أعمدة عشان الشكل يكون مريح والعين تشوفهم كلهم
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧬 Demographics")
    age = st.number_input("1. Age", value=45)
    gender = st.selectbox("2. Gender", [0, 1], format_func=lambda x: "Male" if x==1 else "Female")
    bmi = st.number_input("3. BMI", value=25.0)
    waist = st.number_input("4. Waist (cm)", value=85)
    family_hist = st.selectbox("5. Family History", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    ethnicity = st.selectbox("6. Ethnicity", [0, 1, 2, 3]) # عدلي الاختيارات حسب الداتا

with col2:
    st.markdown("### 📊 Clinical Labs")
    hba1c = st.number_input("7. HbA1c Level", value=5.5)
    blood_glucose = st.number_input("8. Blood Glucose", value=100)
    cholesterol = st.number_input("9. Cholesterol", value=200)
    triglycerides = st.number_input("10. Triglycerides", value=150)
    systolic_bp = st.number_input("11. Systolic BP", value=120)
    diastolic_bp = st.number_input("12. Diastolic BP", value=80)

with col3:
    st.markdown("### 🏃 Lifestyle")
    activity = st.slider("13. Activity Level", 0, 2, 1)
    stress = st.slider("14. Stress Level", 0, 2, 1)
    smoking = st.selectbox("15. Smoking Status", [0, 1], format_func=lambda x: "Smoker" if x==1 else "Non-Smoker")
    diet_score = st.slider("16. Diet Quality (0-10)", 0, 10, 5)
    sleep_hours = st.number_input("17. Sleep Hours", value=7)

st.markdown("<hr>", unsafe_allow_html=True)

# زر التوقع
if st.button("Predict Result", use_container_width=True):
    # هنا بقى بتجمعي ال
