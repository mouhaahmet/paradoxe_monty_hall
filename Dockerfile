FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

#creer un repertoire pour les logs
RUN mkdir /app/logs

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "monty_hall_streamlit.py", "--server.port=8501", "--server.enableCORS=false"]
