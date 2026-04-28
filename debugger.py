#video 7.3

import streamlit as st
from api_calling_for_debugger import debug_generator
from PIL import Image


st.title("Debugger")
st.markdown("Upload screenshot of your bug program")
st.divider()

with st.sidebar:
    st.header("Controls")

    #img
    images = st.file_uploader (
        "Upload the photos of your program error",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    
    

PIL_images = []
    if images:
        #converting Streamlit img to PIL image
        for img in images:
            pil_img = Image.open(img)
            PIL_images.append(pil_img)
        if(len(images)>3):
            st.error("Upload at max 3 images")
        else:
            st.subheader("uploaded images")
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                   st.image(img) 
        
    
    #difficulty
    selected_option = st.selectbox(
        "What do you want? Hint or solution",
        ["Hint","solution"],
        index=None
    )
    # if selected_option:
    #     st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
    # else:
    #     st.error("You must select an difficulty")


    #btn
    pressed = st.button("Click the button to initiate AI",type="primary")
# video 7.4
if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("you must select a preference")
    
    if images and selected_option:
        # Note Summary
        with st.container(border=True):
            st.subheader(f"Your {selected_option}")

            with st.spinner("AI is debugging your code"):
                debug = debug_generator(PIL_images,selected_option)
                #Will be replaced by API call
                st.markdown(debug)
            
            
#         #Audio transcript
#         with st.container(border=True):
#             with st.spinner("Preparing the Audio"):
#                 st.subheader("Audio transcription")
#                 #Will be replaced by API call
#                 cleaned_text = Cleaner_text(generated_notes)
#                 audio_transcript(cleaned_text)

                            
# #Video 7.5


