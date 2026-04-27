from gtts import gTTS
from google import genai
from dotenv import load_dotenv
import streamlit as st
import os
import io
import string

# loading the environment variable
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

#INITIALING  A client
client = genai.Client(api_key=api_key)


#note generator
def debug_generator(images, selected_option):

    prompt = f"""Uploaded pictures are the screenshots of bug in program, given the user. now give {selected_option} in proper way"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images, prompt ]
    )
    return response.text

# def audio_transcript(text):
#     speech = gTTS(text, lang = 'bn', slow= False)
#     # speech.save("welcome.mp3")# this gives the command to save the audio in the local harddisk storage. But this will be bulky when we execute program multiple times.
#     #so to overcome the issue , we are going to use the RAM of this device. so , this audio file will be volatile, when execution ends. 
#     audio_buffer = io.BytesIO()#takes a space from RAM for the generated audio file
#     speech.write_to_fp(audio_buffer)#saves the audio file to that space
#     return st.audio(audio_buffer)


# def Cleaner_text(text):
#     clean_text = text.translate(str.maketrans('','',string.punctuation))
#     return clean_text


# def quiz_generator(image, difficulty):
#     prompt = f"Generate 3 quizzes based on the {difficulty}. make sure to add markdown to differentiate the options "
#     response_for_quiz = client.models.generate_content(
#         model = "gemini-3-flash-preview",
#         contents=[image, prompt ]
#     )
#     return response_for_quiz