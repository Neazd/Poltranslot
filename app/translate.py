from transformers import pipeline
import streamlit as st

def load_translation_pipeline():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")

def translate_english_to_german(translation_pipeline, input_text):
    return translation_pipeline(input_text)[0]['translation_text']

def handle_translation_request(translation_pipeline):
    user_input_text = st.text_area("Enter the text in English", max_chars=500)
    if user_input_text:
        with st.spinner("Translating..."):
            try:
                german_translation = translate_english_to_german(translation_pipeline, user_input_text)
                st.markdown(f'<div style="margin-top: 20px;"><h2>Translation to German:</h2><p>{german_translation}</p></div>', unsafe_allow_html=True)
                st.balloons()
            except Exception as translation_error:
                st.error(f"An error occurred during translation: {translation_error}")
