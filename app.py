import streamlit as st
import numpy as np
import tensorflow as tf
from joblib import load

# Load the trained SVM model
model = load('svm_model.joblib')
scaler = load('scaler.joblib')

# Load the trained ANN model
# model = tf.keras.models.load_model("Ann_intrusion_model.keras")


st.title("Intrusion Detection System ")

st.markdown("Enter the feature values below to check if the traffic is normal or an anomaly.")

# Replace these with the actual number of features your model was trained on
# For demo: 6 sample features
f1 = st.number_input("Wrong Fragment", value=0)
f2 = st.number_input("Source Bytes", value=2499)
f3 = st.number_input("Destination Bytes", value=3410)
f4 = st.number_input("Protocol Type (tcp)", value=1)
f5 = st.number_input("Protocol Type (udp)", value=1)
f6 = st.number_input("Flag (REJ	)", value=0)
f7 = st.number_input("Flag (RSTO)", value=0)
f8 = st.number_input("Flag (RSTOS0)", value=0)
f9 = st.number_input("Flag (RSTR)", value=0)
f10 = st.number_input("Flag (S0	)", value=0)
f11 = st.number_input("Flag (S1	)", value=0)
f12 = st.number_input("Flag (S2)", value=0)
f13 = st.number_input("Flag (S3	)", value=0)
f14 = st.number_input("Flag (SF)", value=0)
f15 = st.number_input("Flag (SH)", value=0)

if st.button("Predict"):
    input_data = np.array([[f1, f2, f3, f4, f5, f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]])  # Make sure order matches training
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    # if prediction[0][0] > 0.8:
    #     st.error("⚠️ Anomaly Detected!")
    # else:
    #     st.success("✅ Normal Traffic")
    if prediction[0] == 1:
        st.error("⚠️ Anomaly Detected!")
    else:
        st.success("✅ Normal Traffic")