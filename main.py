import streamlit as st
from app.translate import handle_translation_request, load_translation_pipeline
from app.sentiment import handle_sentiment_analysis_request, load_sentiment_analysis_pipeline

def setup_page():
    st.markdown("""
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">
        </head>
    """, unsafe_allow_html=True)

    st.title('Poltranslot')
    st.image('./resources/images/translation-image.jpeg')
    st.markdown('''
    <div style="background-color: #7FFFD4; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
        <h1 style="color: #333;">Welcome to Poltranslot!</h1>
        <p style="color: #333;">Poltranslot is designed to bridge language barriers and uncover the underlying emotions in texts.</p>
        <ul style="color: #333;">
            <li><strong>Text Translation</strong>: Instantly convert English sentences into German with state-of-the-art accuracy.</li>
            <li><strong>Sentiment Analysis</strong>: Uncover the emotional tone of English texts, from joyful to sorrowful, with a single click.</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)
    st.divider()

def display_footer():
    st.divider()
    st.markdown('''
    <footer style="text-align: center; margin-top: 20px;">
        <p>Created by s21651</p>
    </footer>
    ''', unsafe_allow_html=True)

def main():
    setup_page()
    translation_pipeline = load_translation_pipeline()
    sentiment_classifier = load_sentiment_analysis_pipeline()

    selected_option = st.selectbox(
        "Options",
        ["Text translation from English to German", "Sentiment analysis of text (eng)"]
    )

    if selected_option == "Text translation from English to German":
        handle_translation_request(translation_pipeline)
    elif selected_option == "Sentiment analysis of text (eng)":
        handle_sentiment_analysis_request(sentiment_classifier)

    display_footer()

if __name__ == "__main__":
    main()
