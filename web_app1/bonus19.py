import streamlit as st
from PIL import Image

st.subheader("Color to grayScale Converter")

upload_img = st.file_uploader("Upload Image")


with st.expander("Start Camera"):

    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image
    img = Image.open(camera_image)

    # convert the image to grey
    gray_img = img.convert("L")

    # Render the pillow image to gray
    st.image(gray_img)

    if upload_img:
        img =Image.open(upload_img)
        gray_uploaded_img = img.convert("L")
        st.image(gray_uploaded_img)












