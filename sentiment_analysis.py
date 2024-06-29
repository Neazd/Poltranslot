import streamlit as st
from transformers import pipeline

def sentiment_analysis_app():
    text = st.text_area("Enter the text")
    if text:
        with st.spinner("Analyzing sentiment..."):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.write("Sentiment analysis result:", answer)
            except Exception as e:
                st.error(f"An error occurred during sentiment analysis: {e}")
