import streamlit as st
import pickle
import numpy as np

# 1. إعدادات الصفحة والتصميم الفاتح
st.set_page_config(page_title="Diabetes Prediction", layout="wide")

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
    .main-title { color: #2e7d32; font-weight: bold; margin-bottom: 10px; }
    .eng-name { color: #546e7a; font-size: 1.2rem; }
    label { color: #2e7d32 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. العنوان
st.markdown("""
    <div class="header-box">
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# 3. تحميل الموديل بحذر
model = None
try:
    with open('diabetes_model.sav', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("⚠️ خطأ: ملف الموديل 'diabetes_model.sav' غير موجود في المجلد. يرجى رفعه ليعمل التوقع.")

# 4. تقسيم الـ 17 خانة (3 أعمدة)
col1, col2, col3 = st.columns(3)

with col1:
    v1 = st.number_input("1. العمر", value=40)
    v2 = st.selectbox("2. النوع", [0, 1], format_func=lambda x: "ذكر" if x==1 else "أنثى")
    v3 = st.selectbox("3. كثرة التبول", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v4 = st.selectbox("4. العطش الشديد", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v5 = st.selectbox("5. فقدان وزن مفاجئ", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v6 = st.selectbox("6. الإجهاد / نقاط الضعف", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")

with col2:
    v7 = st.selectbox("7. زيادة الشهية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v8 = st.selectbox("8. مشاكل تناسلية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v9 = st.selectbox("9. تشوش الرؤية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v10 = st.selectbox("10. الحكة", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v11 = st.selectbox("11. العصبية", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v12 = st.selectbox("12. تأخر التئام الجروح", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")

with col3:
    v13 = st.selectbox("13. ضعف جزئي", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v14 = st.selectbox("14. تصلب العضلات", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v15 = st.selectbox("15. تساقط الشعر", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v16 = st.selectbox("16. السمنة", [0, 1], format_func=lambda x: "نعم" if x==1 else "لا")
    v17 = st.number_input("17. مستوى السكر (أو ميزة إضافية)", value=100)

# 5. زر التوقع والنتيجة
st.markdown("<br>", unsafe_allow_html=True)
if st.button("التنبؤ بالتشخيص", use_container_width=True):
    if model is not None:
        try:
            # تجميع المدخلات في مصفوفة واحدة
            input_data = np.array([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17]])
            prediction = model.predict(input_data)
            
            st.markdown("---")
            if prediction[0] == 1:
                st.error("### النتيجة: إيجابي (احتمال وجود سكري) ⚠️")
            else:
                st.success("### النتيجة: سلبي (بصحة جيدة) ✅")
        except Exception as e:
            st.error(f"حدث خطأ أثناء التوقع: {e}")
    else:
        st.warning("لا يمكن إجراء التوقع بدون ملف الموديل.")
