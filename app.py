import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text



def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
    
    
st.set_page_config(page_title="Analyze")
st.sidebar.header("Image Descriptor")

uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""  
input="" 
submit=0
if uploaded_file is not None:
    st.subheader("Your Uploaded  image")
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    input=st.text_input("Ask the question related to uploaded image only*: ",key="input")
    submit=st.button("Start Analyzing")
    
else:
     st.header("Smart Image Descriptor System")
     st.markdown("---")
     st.markdown("Welcome to our Image Descriptor System! This cutting-edge tool is designed to analyze and provide detailed descriptions of images you upload. Whether you're curious about the contents of a photo or need a comprehensive analysis , Go for it.")
     st.markdown("Neeraj Kumar")
     col1, col2, col3 = st.columns([1,1,1])
     with col1:
        st.link_button("Linkdin", "https://www.linkedin.com/in/neeraj-kumar-9a75811a2") 
     with col2:
        st.link_button("Github", "https://github.com/neerajcodes888")
     with col3:
        st.link_button("Kaggle", "https://www.kaggle.com/neerajdata")
     st.markdown("---")
     st.info('Smart Image Descriptor - Describe your image now', icon=None)
     st.warning(' Upload  images  in (.jpg , .jpeg , .png)format Only')




input_prompt="""
You are an expert in giving description  where you need to see the  items from the image
               and  also provide the details of every  items with 
               is below format

               1. Item 1 -
               2. Item 2 - 
               ----
               ----
               
            give 1 recommendation regarding items

 and if question is not related to uploaded picture then simply tell out of context ,  do not provide wrong information. just say out of context
"""


if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
