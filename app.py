import streamlit as st
from transformers import pipeline
from gtts import gTTS
import os

# Title
st.title("Title to Story + Voiceover AI")

# User Input
story_title = st.text_input("Enter Story Title:")

if st.button("Generate Story"):
    if story_title.strip():
        # AI Model se Story Generate karna
        story_generator = pipeline("text-generation", model="gpt2")
        story = story_generator(f"{story_title} -", max_length=100, num_return_sequences=1)[0]['generated_text']

        # Display Story
        st.subheader("Generated Story")
        st.write(story)

        # Voiceover Generate karna
        tts = gTTS(text=story, lang='en')
        audio_file = "story.mp3"
        tts.save(audio_file)

        # Play Audio in Streamlit
        st.audio(audio_file, format="audio/mp3")

        # Download Button
        with open(audio_file, "rb") as file:
            st.download_button("Download Voiceover", file, file_name="story.mp3")

    else:
        st.error("Please enter a story title!")

