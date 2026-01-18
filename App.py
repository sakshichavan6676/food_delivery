import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("food_delivery_time.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Food Delivery Time Prediction", layout="centered")

st.title("🍔 Food Delivery Time Prediction")
st.write("Enter order details to predict delivery time")

# ---------- USER INPUT UI ----------
distance = st.number_input("Distance (km)", min_value=0.0, step=0.1)

weather = st.selectbox(
    "Weather",
    ["Clear", "Rainy", "Foggy", "Windy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

prep_time = st.number_input(
    "Preparation Time (minutes)", min_value=0, step=1
)

experience = st.number_input(
    "Courier Experience (years)", min_value=0.0, step=0.5
)

# ---------- ENCODING ----------
weather_map = {"Clear": 0, "Rainy": 1, "Foggy": 2, "Windy": 3}
traffic_map = {"Low": 0, "Medium": 1, "High": 2}
time_map = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}
vehicle_map = {"Bike": 0, "Scooter": 1, "Car": 2}

input_data = pd.DataFrame([[
    distance,
    weather_map[weather],
    traffic_map[traffic],
    time_map[time_of_day],
    vehicle_map[vehicle],
    prep_time,
    experience
]], columns=[
    "Distance_km",
    "Weather",
    "Traffic_Level",
    "Time_of_Day",
    "Vehicle_Type",
    "Preparation_Time_min",
    "Courier_Experience_yrs"
])

# ---------- PREDICTION ----------
if st.button("🚀 Predict Delivery Time"):
    prediction = model.predict(input_data)
    st.success(f"⏱ Estimated Delivery Time: **{int(prediction[0])} minutes**")
