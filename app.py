import streamlit as st
import pickle # أو joblib حسب ما حفظتي الموديل

# 1. تحميل الموديل (تأكدي أن الملف في نفس مجلد الكود)
try:
    model = pickle.load(open('diabetes_model.sav', 'rb'))
except:
    st.error("ملف الموديل غير موجود، تأكدي من تسميته diabetes_model.sav")

# ... (هنا كود الـ 17 خانة اللي بعتهولك المرة اللي فاتت) ...

# 2. تعديل جزء زر التوقع عشان يطلع النتيجة الحقيقية
if st.button("Predict Diagnosis", use_container_width=True):
    # تجميع الـ 17 قيمة
    input_data = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17]
    
    # عمل التوقع
    prediction = model.predict([input_data])
    
    st.markdown("---")
    # عرض النتيجة بشكل احترافي ومريح للعين
    if prediction[0] == 1:
        st.error("### Result: Positive (Diabetes Risk) ⚠️")
        st.write("النتيجة تشير إلى احتمالية الإصابة، يرجى مراجعة الطبيب.")
    else:
        st.success("### Result: Negative (Healthy) ✅")
        st.write("النتيجة تشير إلى عدم وجود إصابة. حافظ على نمط حياتك الصحي!")
