# Poltranslot

Poltranslot is a Streamlit application designed to bridge language barriers and uncover the underlying emotions in texts. It provides functionalities for text translation from English to German and sentiment analysis of English texts.

## Features

* **Text Translation**: Instantly convert English sentences into German with state-of-the-art accuracy.
* **Sentiment Analysis**: Uncover the emotional tone of English texts, from joyful to sorrowful, with a single click.

## Installation





1. **Clone the repository:**

   ```bash
   git clone https://github.com/neazd/poltranslot.git
   cd poltranslot
   ```
2. **Set up a virtual environment:**
   Using `conda`:

   ```bash
   conda create --name poltranslot python=3.9
   conda activate poltranslot
   ```
3. **Install the dependencies:**
   Using `conda`:

   ```bash
   conda env create -f environment.yml
   conda activate poltranslot
   ```

Usage





1. **Run the Streamlit application:**

   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to `http://localhost:8501` to view the application.

## Project Structure

```
poltranslot/
│
├── app/
│   ├── __init__.py
│   ├── main.py         # Main Streamlit application file
│   ├── translation.py  # Functions related to translation
│   └── sentiment.py    # Functions related to sentiment analysis
│
├── resources/
│   ├── images/
│   │  └── translation-image.jpeg  # Image used in the application
|
├── .gitignore
├── README.md
└── environment.yml
```

## Customization

### Adding Custom Fonts

To add custom fonts, update the `styles.css` file located in the `resources/styles/` directory and link it in the `main.py` file:

```html
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="./resources/styles/styles.css">
</head>
```

## Dependencies

* Streamlit
* Transformers
* TensorFlow or PyTorch (Choose one compatible with your setup)
* SentencePiece

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [TensorFlow](https://www.tensorflow.org/) / [PyTorch](https://pytorch.org/)


