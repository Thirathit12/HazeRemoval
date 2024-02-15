import streamlit as st
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



 #def plot_histogram():
    
 #   hist = cv2.calcHist([uploaded_file], [0], None, [256], [0, 256])
 #   plt.figure()
 #   plt.title("Image Histogram")
  #  plt.xlabel("Pixel Value")
 #   plt.ylabel("% of Pixels")
 #   plt.plot(hist)
   # plt.xlim([0, 256])
   # st.pyplot()



#Welcome 
st.markdown("## :rainbow[Welcome to Haze Removal Image Enhancement Perspective for IoT device]")
st.markdown("Choose a camera or upload image to enhance the picture.")
    
tab2, tab3 = st.tabs(['Camera', 'Upload image'])


#Camera
with tab2:
    cols = st.columns(2)
    st.markdown("## Take a picture")
    image_camerainp = st.camera_input(' Take a picture')

    if image_camerainp :
        with cols[0] :
            st.markdown("## Before ")
            image_inp = st.image(image_camerainp)

           

        with cols[1] :
            st.markdown("## After ")
            image_inp = st.image(image_camerainp)
            image_A = st.image(image_inp)
        #    plt.imshow(cv2.cvtColor(image_A, cv2.COLOR_GRAY2BGR))
       #     plt.figure()
         #   plt.title("Image Histogram")
          #  plt.xlabel("Pixel Value")
        #    plt.ylabel("% of Pixels")
       #     plt.plot(image_A)
       #     plt.xlim([0, 256])
       #     st.pyplot(image_A)





#Upload
with tab3:
    cols = st.columns(2)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    # Check if an image has been uploaded
    if uploaded_file:
        # Display the uploaded image
        with cols[0] :
            image = Image.open(uploaded_file)
            st.markdown("## Before ")
            st.image(image, use_column_width=True)
          #  plot_histogram(np.array(image))

        with cols[1] :
            image = Image.open(uploaded_file)
           #imageHaze = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, use_column_width=True)
            st.markdown("## After ")
            st.image(image)
        #    plot_histogram(np.array(imageHaze))

