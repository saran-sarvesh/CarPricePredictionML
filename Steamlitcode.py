import streamlit as st
import pickle
import pandas as pd
import numpy as np
import pickle

# Load your trained model
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🚗 Car Price Predictor")

# Input fields
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
year_of_manufacture = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
model_year = st.number_input("Model Year", min_value=1990, max_value=2025, step=1)
gear_box_clean = st.number_input("Gear Box Clean (number of gears)", min_value=0, max_value=10, step=1)
city = st.selectbox("City", ["kolkata", "jaipur", "delhi", "chennai", "hyderabad", "bangalore"])
insurance = st.selectbox("Insurance Validity", ["Comprehensive", "Third Party", "Third Party insurance"])
ownership = st.selectbox("Ownership", ["First Owner", "Second Owner", "Third Owner"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
kms_driven = st.number_input("Kms Driven", min_value=0)
bt = st.selectbox("Body Type", ["Sedan", "Hatchback", "SUV", "MUV", "Coupe", "Convertibles", "Minivans", "Pickup Trucks", "Wagon", "Hybrids"])
mileage = st.number_input("Mileage", min_value=0)

# Predict button
if st.button("Predict Price"):
    # Create input row
    input_data = {
        "transmission": transmission,
        "Year of Manufacture": year_of_manufacture,
        "modelYear": model_year,
        "Gear Box Clean": gear_box_clean,
        "city": city,
        "Insurance Validity": insurance,
        "Ownership": ownership,
        "Fuel Type": fuel_type,
        "Kms Driven": kms_driven,
        "bt": bt,
        "Mileage": mileage
    }

    # You must transform this input using the same preprocessing steps (scaling/encoding)
    # Here we assume you used a pipeline while training

    try:
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        st.success(f"Estimated Car Price: ₹ {int(prediction[0]):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
