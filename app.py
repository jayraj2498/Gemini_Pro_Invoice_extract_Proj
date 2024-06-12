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
        image_parts = [{
            "mime_type": uploaded_file.type, 
            "data": bytes_data}]
        
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Invoice Application")

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










# import os
# from dotenv import load_dotenv  

# load_dotenv()   # < -- it will load all environmnet variables from .env 

# import streamlit as st 
# from PIL import Image 
# import google.generativeai as genai  

# genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) 

# # we are loading model gemini pro vision 
# model = genai.GenerativeModel('gemini-pro-vision')  

# def get_gemini_response(input,image,prompt):
#     response=model.generate_content([input,image[0],prompt])    # <-- it takes values in list 
#     return response.text 


# def input_image_setup(uploaded_file) : 
    
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue() 
        
#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
        
#         return image_parts  
#     else:
#         raise FileNotFoundError("No file uploaded..")




# # streamlit 
# st.set_page_config(page_title="Multilanguage Invoice Extracter") 

# st.header("Multilanguage Invoice Extracter")

# input = st.text_input("input prompt: " , key="input")
# uploaded_file = st.file_uploader("Choose an image of Invoice.." , type=["jpg","jpeg","png"]) 

# image=" " 

# if uploaded_file is not None : 
#     image=Image.open(uploaded_file) 
#     st.image(image, caption="Uploaded file" , use_column_width=True) 
    
    
# submit= st.button("Tell Me About Invoice")     

# input_prompt = """
#                You are an expert in understanding invoices.
#                You will receive input images as invoices &
#                you will have to answer any questions based on the input image
#                """
    
    
# # if submit buton click 

# if submit: 
#     image_data=input_image_setup(uploaded_file)
#     response=get_gemini_response(input,image_data,input_prompt)
#     st.subheader("your respone is") 
#     st.write(response)