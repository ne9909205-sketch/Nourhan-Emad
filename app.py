import streamlit as st
import numpy as np

# 1. إعدادات الصفحة والتنسيق (الأبيض والأخضر الهادئ)
st.set_page_config(page_title="Diabetes Prediction System", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .header-box {
        background-color: #f1f8e9;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #c8e6c9;
        margin-bottom: 40px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .main-title { color: #2e7d32; font-weight: bold; font-size: 2.8rem; margin:0; }
    .eng-name { color: #546e7a; font-size: 1.4rem; margin-top: 10px; font-style: italic; }
    label { color: #2e7d32 !important; font-weight: bold !important; font-size: 1.05rem; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        height: 3.5em;
        border-radius: 12px;
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1b5e20; border: none; }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر الخاص بكِ
st.markdown("""
    <div class="header-box">
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="eng-name">Prepared by: Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# 3. تنظيم المدخلات (الـ 17 باراميتر)
col1, col2, col3 = st.columns(3)

with col1:
    v1 = st.number_input("1. Age / العمر", 1, 100, 40)
    v2 = st.selectbox("2. Gender / النوع", [0, 1], format_func=lambda x: "Male / ذكر" if x==1 else "Female / أنثى")
    v3 = st.selectbox("3. Polyuria / كثرة التبول", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v4 = st.selectbox("4. Polydipsia / العطش الدائم", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v5 = st.selectbox("5. Sudden Weight Loss / نقص الوزن", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v6 = st.selectbox("6. Weakness / الضعف العام", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")

with col2:
    v7 = st.selectbox("7. Polyphagia / زيادة الشهية", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v8 = st.selectbox("8. Genital Thrush / مشاكل تناسلية", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v9 = st.selectbox("9. Visual Blurring / زغللة العين", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v10 = st.selectbox("10. Itching / حكة جلدية", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v11 = st.selectbox("11. Irritability / العصبية", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v12 = st.selectbox("12. Delayed Healing / تأخر التئام الجروح", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")

with col3:
    v13 = st.selectbox("13. Partial Paresis / ضعف جزئي", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v14 = st.selectbox("14. Muscle Stiffness / تصلب عضلات", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v15 = st.selectbox("15. Alopecia / تساقط الشعر", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v16 = st.selectbox("16. Obesity / السمنة", [0, 1], format_func=lambda x: "Yes / نعم" if x==1 else "No / لا")
    v17 = st.number_input("17. Blood Sugar Level / مستوى السكر", 50, 400, 100)

st.markdown("<br>", unsafe_allow_html=True)

# 4. زر التوقع وحساب النتيجة
if st.button("Predict Diagnosis / التنبؤ بالتشخيص"):
    # حساب "نقاط الخطر" بناءً على الأعراض المدخلة (Logic)
    # كثرة التبول والعطش ونقص الوزن هم الأعلى وزناً في التشخيص
    risk_score = (v3 * 2.5) + (v4 * 2.5) + (v5 * 2.0) + (v12 * 1.5) + (v9 * 1.0) + (v17/150)
    
    st.markdown("---")
    if risk_score >= 4.5:
        st.error("### Diagnosis Result: Positive (High Risk) ⚠️")
        st.info("النتيجة تشير إلى احتمالية عالية للإصابة. يُنصح بمراجعة الطبيب فوراً.")
    else:
        st.success("### Diagnosis Result: Negative (Low Risk) ✅")
        st.info("المؤشرات الحالية تقع في النطاق الآمن. حافظ على نمط حياة صحي.")
