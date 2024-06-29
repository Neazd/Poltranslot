# Use the official Conda image as a parent image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the environment.yml file
COPY environment.yml .

# Create the Conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "suml4", "/bin/bash", "-c"]

# Install additional pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit application and the image
COPY streamlit_app.py .
COPY sprechen_sie_deutsch.jpg .

# Expose the Streamlit port
EXPOSE 8501

# Run Streamlit
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "suml4", "streamlit", "run", "streamlit_app.py"]
