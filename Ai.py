import streamlit as st

image_path = 'Inno_logo_.png'  # Replace with your actual PNG image file path

# Specify the desired width and height
st.image(image_path, width=400)

import google.generativeai as genai

genai.configure(api_key="AIzaSyA5Upb6djtVUb_gRP5vC12jDkPLidQ6JcA")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.title("Data Science AI Tutor App")

user_prompt = st.text_input("Enter your query:",
              placeholder="Type your query here...")

btn_click = st.button("Generate Response")

if btn_click==True:
    #generate responce, configure, call gemini or gpt model
    response = model.generate_content(user_prompt)
    st.write(response.text)