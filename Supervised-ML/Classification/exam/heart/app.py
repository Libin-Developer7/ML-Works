import streamlit as st
import joblib
st.title(":red[Heart Disease Prediction]")
model = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\Supervised-ML\\Classification\\exam\\heart\\model.pkl")
scaler = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\Supervised-ML\\Classification\\exam\\heart\\scaler.pkl")
age = st.number_input("enter age")
ejection_fraction = st.number_input("enter ejection_fraction")
serum_creatinine = st.number_input("enter serum_creatinine")
serum_sodium = st.number_input("enter serum_sodium")
time = st.number_input("enter time")
if st.button('PREDICT DISEASE'):
    test_data = [[age,ejection_fraction,serum_creatinine,serum_sodium,time]]
    result = model.predict(scaler.transform(test_data))[0]
    heart_disease_map = {0:"survival",1:"non_survival"}
    st.write(heart_disease_map.get(result))
