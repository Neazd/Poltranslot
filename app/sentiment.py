from transformers import pipeline
import streamlit as st

def load_sentiment_analysis_pipeline():
    return pipeline("sentiment-analysis")

def perform_sentiment_analysis(sentiment_classifier, input_text):
    return sentiment_classifier(input_text)

def handle_sentiment_analysis_request(sentiment_classifier):
    user_input_text = st.text_area("Enter the text")
    if user_input_text:
        with st.spinner("Analyzing sentiment..."):
            try:
                sentiment_result = perform_sentiment_analysis(sentiment_classifier, user_input_text)
                st.markdown(f'<div style="margin-top: 20px;"><h2>Sentiment analysis result:</h2><p>{sentiment_result}</p></div>', unsafe_allow_html=True)
            except Exception as analysis_error:
                st.error(f"An error occurred during sentiment analysis: {analysis_error}")
