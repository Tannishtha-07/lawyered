import streamlit as st
from PIL import Image
import google.generativeai as genai
import os



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
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

# Streamlit setup
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")


name = " "
age = " "
aadharno =" "

checkbox_placeholder = st.empty()

checkbox_placeholder2 = st.empty()
checkbox_placeholder3 = st.empty()
show = st.checkbox("Show ", value=False)



uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

input_prompt_default = """

               """
if submit:

    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(name, image_data, input_prompt_default)
    response2 = get_gemini_response(age, image_data, input_prompt_default)
    response3 = get_gemini_response(aadharno, image_data, input_prompt_default)

    name2 = "what is name on adharcard"
    response_name = get_gemini_response(name2, image_data, input_prompt_default)
    age2 = "what is year of birth on adharcard"
    response_name2 = get_gemini_response(age2, image_data, input_prompt_default)
    aadharno2 = "what is aadhar no"
    response_name3 = get_gemini_response(aadharno2, image_data, input_prompt_default)

    if show:
        checkbox_placeholder.checkbox(f"Name: {response_name}", value=True)
        checkbox_placeholder2.checkbox(f"Year: {response_name2}", value=True)
        checkbox_placeholder3.checkbox(f"Aadhar Number: {response_name3}", value=True)
    else:
        checkbox_placeholder.checkbox("Show name", value=False)
        checkbox_placeholder2.checkbox("Show name", value=False)
        checkbox_placeholder2.checkbox("Show name", value=False)


