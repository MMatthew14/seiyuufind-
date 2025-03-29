import streamlit as st
import os

st.title("SEIYUUFIND")
st.subheader("A reverse search engine for voice actors")

# To add images
# st.image(os.path.join(os.getcwd(), "static", "<IMAGE>"))

user_name = st.text_input("Enter the director's or anime character's name to search.")

name_pressed = st.button("Search by name")

user_record = st.audio_input("Or you can record audio.")

record_pressed = st.button("Search by audio")

# To use the audio
if record_pressed:
    st.audio(user_record)
