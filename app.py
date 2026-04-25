import streamlit as st

# إضافة تنسيقات مخصصة بالـ CSS
st.markdown("""
    <style>
    /* تغيير خلفية الصفحة بالكامل */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* تنسيق العنوان الرئيسي */
    .main-title {
        color: #2c3e50;
        text-align: center;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }

    /* جعل الكروت (Inputs) تظهر بشكل أرقى */
    div[data-baseweb="input"] {
        border-radius: 10px !important;
    }
    
    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# تطبيق العنوان
st.markdown('<div class="main-title"><h1>Diabetes Prediction System</h1><p>Eng. Nourhan Emad El-Din Mohamed</p></div>', unsafe_allow_html=True)
