FROM jbarlow83/ocrmypdf-ubuntu:latest

# Install pip and the German Tesseract language pack (deu)
RUN apt-get update && \
    apt-get install -y python3-pip tesseract-ocr-deu

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY app.py /app/app.py

EXPOSE 2016
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
