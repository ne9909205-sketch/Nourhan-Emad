import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# --- تنسيق CSS لتحويل الشكل لنظام فاتح واحترافي ---
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق للأبيض */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* تنسيق الحاوية العلوية (العنوان) */
    .header-style {
        background-color: #f1f8e9; /* أخضر فاتح جداً */
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #c8e6c9;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .main-title {
        color: #2e7d32; /* أخضر غامق احترافي */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 0;
    }
    
    .eng-name {
        color: #546e7a;
        font-size: 1.2rem;
        font-weight: 500;
        margin-top: 5px;
    }

    /* تنسيق العناوين الفرعية */
    .section-title {
        color: #1b5e20;
        border-bottom: 2px solid #a5d6a7;
        padding-bottom: 5px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    </style>
    
    <div class="header-style">
        <h1 class="main-title">Diabetes Prediction System</h1>
        <p class="eng-name">Eng. Nourhan Emad El-Din Mohamed</p>
    </div>
    """, unsafe_allow_html=True)

# --- قسم مدخلات البيانات ---
st.markdown('<p class="section-title">Patient Clinical Data</p>', unsafe_allow_html=True)

# تقسيم الصفحة لعمودين
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    hba1c = st.number_input("HbA1c Level", value=5.50, step=0.1)
    cholesterol = st.number_input("Cholesterol", value=200, step=1)
    triglycerides = st.number_input("Triglycerides", value=150, step=1)
    activity = st.slider("Activity Level (0-2)", 0, 2,
    
