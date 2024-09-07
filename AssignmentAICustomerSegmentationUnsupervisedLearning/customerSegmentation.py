import streamlit as st
import joblib
import numpy as np

#load the model
model = load('km_model.joblib')

#create a simple user input
user_input = st.number_input('Enter Annual Income:')

#rephrase the input for the model
input_array = np.array([[annual_income, spending_score]])

if st.button('Check'):
    predicted_cluster = model.predict(input_array)
    st.write(f"The Result is: {predicted_cluster[0]}")