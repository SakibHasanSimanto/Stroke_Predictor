# -*- coding: utf-8 -*-
"""scratchpad

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/empty.ipynb
"""

import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title('Stroke Predictor 1.0')
st.write('Enter your input in the following fields')

# Input field for user
#input_data = st.text_input('Input your data here:') 
gender = st.text_input('Gender? (0: Male, 1: Female): ') 
age = st.text_input('Enter your age: ') 
hypertension = st.text_input('Do you suffer from hypertension: (0: No, 1: Yes)') 
hrt_dis = st.text_input('Do you have any heart disease: (0: No, 1: Yes)') 
married = st.text_input('Are you married: (0: No, 1: Yes)') 
work = st.text_input('Profession: (Govt_job: 0, Never_worked: 1, Private: 2, Self-employed: 3, children: 4)') 
res = st.text_input('Residence: (0: Rural, 1: Urban)') 
avg_gluc = st.text_input('Glucose level: ') 
bmi = st.text_input('BMI:') 
smoking = st.text_input('Smoking status: (formerly smoked: 1, never smoked: 2, smokes: 3)')



# Button to make predictions
if st.button('Predict'):
    
        try:
            # Convert input string into a list of numbers
            input_list = [gender, age, hypertension, hrt_dis, married, work, res, avg_gluc, bmi, smoking]
            prediction = model.predict([input_list])
            st.success(f'Prediction: {prediction[0]}')
        except Exception as e:
            st.error(f"Error: {e}")
    