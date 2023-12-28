from dotenv import load_dotenv
load_dotenv()

import streamlit as st

import os
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    
    return response.text


st.set_page_config('Q N A')
st.header('QnA Text Application Using Gemini LLM Model')

input = st.text_input('Ask your question below: ', key='input')
submit = st.button('Ask the question')


if submit:
    response = get_gemini_response(input)
    st.subheader('The response is ....')
    st.success(response)
    