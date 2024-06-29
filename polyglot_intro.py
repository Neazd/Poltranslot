import streamlit as st
import tensorflow as tf  # Import TensorFlow first
from transformers import pipeline

st.title('Polyglot')
st.divider()
st.image('translate.jpg')

st.write('''
Polyglot is designed to bridge language barriers and uncover the underlying emotions in texts.

- **Text Translation**: Instantly convert English sentences into German with state-of-the-art accuracy.
- **Sentiment Analysis**: Uncover the emotional tone of English texts, from joyful to sorrowful, with a single click.
''')

st.divider()

option = st.selectbox(
    "Options",
    [
        "Text translation from English to German",
        "Sentiment analysis of text (eng)",
    ]
)
