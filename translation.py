import streamlit as st
from transformers import pipeline

if option == "Text translation from English to German":
    text = st.text_area("Enter the text in English", max_chars=500)
    if text:
        with st.spinner("Translating..."):
            try:
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text)
                st.write('Translation to German:')
                st.text(translation[0]['translation_text'])
                st.balloons()
            except Exception as e:
                st.error(f"An error occurred during translation: {e}")
