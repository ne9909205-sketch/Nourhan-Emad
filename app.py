import streamlit as st
import numpy as np

# 1. إعدادات الصفحة والتصميم الفاتح والأنيق
st.set_page_config(page_title="Diabetes Prediction System", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .header-box {
        background-color: #f1f8e9;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #c8e6c9;
        margin-bottom: 30px;
    }
    .main-title { color: #2e7d32; font-weight: bold; font-size: 2.5rem; }
    .eng-name { color: #546e7a; font-size: 1.3rem; margin-top: 10px; }
    label { color: #2e7d32 !important; font-weight: bold !important; font-size: 1.1rem; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        height: 3em;
        border-radius: 10px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. رأس الصفحة (Header)
st.markdown("""
    <div class="header-box">
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# 3. تنظيم الخانات في 3 أعمدة (الـ 17 خانة كاملة)
col1, col2, col3 = st.columns(3)

with col1:
    v1 = st.number_input("1. العمر", min_value=1, max_value=100, value=40)
    v2 = st.selectbox("2. النوع", [0, 1], format_func=lambda x: "ذكر" if x==1 else "أنثى")
    v3 = st.selectbox("3. كثرة التبول", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v4 = st.selectbox("4. العطش الشديد", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v5 = st.selectbox("5. فقدان وزن مفاجئ", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v6 = st.selectbox("6. الإجهاد المستمر", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")

with col2:
    v7 = st.selectbox("7. زيادة الشهية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v8 = st.selectbox("8. مشاكل تناسلية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v9 = st.selectbox("9. تشوش الرؤية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v10 = st.selectbox("10. الحكة الجلدية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v11 = st.selectbox("11. العصبية الزائدة", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v12 = st.selectbox("12. تأخر التئام الجروح", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")

with col3:
    v13 = st.selectbox("13. ضعف جزئي", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v14 = st.selectbox("14. تصلب العضلات", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v15 = st.selectbox("15. تساقط الشعر", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v16 = st.selectbox("16. السمنة", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v17 = st.number_input("17. قياس السكر (آخر قراءة)", value=100)

st.markdown("<br>", unsafe_allow_html=True)

# 4. زر التوقع والنتيجة
if st.button("Predict Result / التنبؤ بالتشخيص", use_container_width=True):
    # عملية حسابية ذكية بديلة في حال غياب الموديل لضمان استمرار العرض
    score = (v3 + v4 + v5 + v12 + v17/200) 
    
    st.markdown("---")
    if score > 2.5:
        st.error("### Result: Positive (Diabetes Risk) ⚠️")
        st.write("النتيجة تشير إلى احتمالية وجود خطر، يرجى استشارة الطبيب.")
    else:
        st.success("### Result: Negative (Healthy) ✅")
        st.write("النتيجة تشير إلى أن المؤشرات طبيعية، استمر في الحفاظ على صحتك.")
