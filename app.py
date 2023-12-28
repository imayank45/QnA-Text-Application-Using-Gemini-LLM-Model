# Importing the dotenv library to load environment variables from a .env file
from dotenv import load_dotenv
# Calling the load_dotenv function to load environment variables
load_dotenv()

# Importing the Streamlit library for web application development
import streamlit as st

# Importing the os library to interact with the operating system
import os
# Importing a module from the google library specifically for generative AI functionality
import google.generativeai as genai

# Retrieving the value of the 'GOOGLE_API_KEY' environment variable
os.getenv("GOOGLE_API_KEY")
# Configuring the Google generative AI module with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Creating an instance of the GenerativeModel class with the model name 'gemini-pro'
model = genai.GenerativeModel('gemini-pro')

# Defining a function that takes a question and returns the response from the Gemini model
def get_gemini_response(question):
    # Generating content based on the input question using the model
    response = model.generate_content(question)
    # Returning the text part of the response
    return response.text

# Setting the configuration of the Streamlit page
st.set_page_config('Q N A')
# Adding a header to the Streamlit page
st.header('QnA Text ChatBot Using Gemini LLM Model')

# Creating a text input field on the Streamlit page for user input
input = st.text_input('Ask your question below: ', key='input', help="Please click again on 'Ask the question button' if error encountered")
# Creating a button on the Streamlit page
submit = st.button('Ask the question')

# Checking if the button is pressed
if submit:
    # If the button is pressed, get the response from the Gemini model
    response = get_gemini_response(input)
    # Adding a subheader to the Streamlit page
    st.subheader('The response is ....')
    # Displaying the response in a success message format
    st.success(response)
