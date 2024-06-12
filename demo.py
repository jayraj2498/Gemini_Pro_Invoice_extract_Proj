import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('''how we can solve error with respect to gemini pro am getting error proj_image_gemini.jpeg
AxiosError: Request failed with status code 403 

my code is  

import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image

load_dotenv()  # Load environment variables from .env

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

def get_gemini_response(input_text, image, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input_text, image[0], prompt])
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        st.error(f"Error: {e}")
        raise

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image
"""

if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")

''' )

print(response.text)