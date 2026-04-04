import streamlit as st
import joblib

# Load model
model = joblib.load("housing_model(1).pkl")

st.title("🏠 House Price Prediction")

st.write("Enter values (use 0/1/2 as per encoding):")

# Numeric inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

mainroad = st.number_input("Main Road (1 = Yes, 0 = No)", min_value=0, max_value=1)
guestroom = st.number_input("Guest Room (1 = Yes, 0 = No)", min_value=0, max_value=1)
basement = st.number_input("Basement (1 = Yes, 0 = No)", min_value=0, max_value=1)
airconditioning = st.number_input("Air Conditioning (1 = Yes, 0 = No)", min_value=0, max_value=1)
prefarea = st.number_input("Preferred Area (1 = Yes, 0 = No)", min_value=0, max_value=1)

furnishingstatus = st.number_input(
    "Furnishing Status (0 = Furnished, 1 = Semi-Furnished, 2 = Unfurnished)",
    min_value=0,
    max_value=2
)

# Prediction
if st.button("Predict Price"):
    features = [[
        area, bedrooms, bathrooms, stories,
        mainroad, guestroom, basement, airconditioning,
        parking, prefarea, furnishingstatus
    ]]
    
    result = model.predict(features)
    st.success(f"🏡 Predicted Price: {result[0]}")
