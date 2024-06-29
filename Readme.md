# Polyglot Streamlit Application

Polyglot is a Streamlit-based application designed to bridge language barriers and uncover the underlying emotions in texts. This application provides functionalities for text translation from English to German and sentiment analysis of English texts.

## Features

* **Text Translation**: Instantly convert English sentences into German with state-of-the-art accuracy.
* **Sentiment Analysis**: Uncover the emotional tone of English texts, from joyful to sorrowful, with a single click.

## File Structure

* `polyglot_intro.py`: Introduction and options selection for the application.
* `translation.py`: Handles the text translation from English to German.
* `sentiment_analysis.py`: Handles the sentiment analysis of English text.
* `translate.jpg`: Image used in the application.

## Setup and Installation

### Prerequisites

* Docker installed on your machine.

### Build the Docker Image


1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Build the Docker image:

   ```sh
   docker build -t polyglot-app .
   ```

### Run the Docker Container


1. Run the Docker container:

   ```sh
   docker run -p 8501:8501 polyglot-app
   ```
2. Open your web browser and navigate to `http://localhost:8501` to access the Polyglot application.

## Running the Application in Docker

To run the application using Docker, follow these steps:


1. Ensure Docker is installed on your machine.
2. Clone the repository and navigate into the directory:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
3. Build the Docker image:

   ```sh
   docker build -t polyglot-app .
   ```
4. Run the Docker container:

   ```sh
   docker run -p 8501:8501 polyglot-app
   ```
5. Open your web browser and go to `http://localhost:8501` to access the application.

## Development

If you want to contribute to the project or make modifications, follow these steps:


1. Ensure you have Conda installed.
2. Create the Conda environment:

   ```sh
   conda env create -f environment.yml
   ```
3. Activate the environment:

   ```sh
   conda activate suml4
   ```
4. Install additional dependencies:

   ```sh
   pip install -r requirements.txt
   ```
5. Run the application locally:

   ```sh
   streamlit run polyglot_intro.py
   ```

## License

This project is licensed under the MIT License.