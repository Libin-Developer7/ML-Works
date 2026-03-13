import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\project\\model.pkl")
scaler = joblib.load("C:\\Users\\libin_urv2w13\\Desktop\\mljourney\\project\\scaler.pkl")

st.title("California Housing Price Predictor")

st.write("Enter the housing details to predict the median house value.")

# Numerical inputs
total_rooms = st.number_input("Total Rooms", min_value=0.0)
population = st.number_input("Population", min_value=0.0)
households = st.number_input("Households", min_value=0.0)
median_income = st.number_input("Median Income", min_value=0.0)

# Ocean proximity dropdown
ocean = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR BAY", "OTHER"]
)

# Encode ocean proximity
ocean_1h = 1 if ocean == "<1H OCEAN" else 0
ocean_inland = 1 if ocean == "INLAND" else 0
ocean_nearbay = 1 if ocean == "NEAR BAY" else 0

# Prediction
if st.button("Predict Price"):

    features = np.array([[ 
        ocean_1h,
        ocean_inland,
        ocean_nearbay,
        total_rooms,
        population,
        households,
        median_income
    ]])

    prediction = model.predict(scaler.transform(features))

    st.success(f"Predicted Median House Value: ${prediction}")