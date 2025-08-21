# 🔹 Purpose: Streamlit app to detect smells based on input values.
# virtual_nose_app.py
import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Streamlit UI
st.set_page_config(page_title="AI Virtual Nose 👃", layout="centered")
st.title("👃 AI-Powered Virtual Nose")
st.markdown("Simulated smell detection using AI and MQ sensor values")

# Sliders for input
mq2 = st.slider("MQ2 Sensor Value", 100, 1100, step=10)
mq3 = st.slider("MQ3 Sensor Value", 100, 1100, step=10)
mq135 = st.slider("MQ135 Sensor Value", 100, 1100, step=10)

# Predict
if st.button("🔍 Detect Smell"):
    input_data = np.array([[mq2, mq3, mq135]])
    prediction = model.predict(input_data)[0]
    st.success(f"Detected Smell: **{prediction}**")
