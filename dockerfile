
FROM continuumio/miniconda3
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*
COPY environment.yml .
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "suml4", "/bin/bash", "-c"]
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY polyglot_intro.py .
COPY translation.py .
COPY sentiment_analysis.py .
COPY translate.jpg .
EXPOSE 8501
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "suml4", "streamlit", "run", "polyglot_intro.py"]
