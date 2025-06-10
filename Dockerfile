FROM jbarlow83/ocrmypdf-ubuntu:latest

# Install pip3 (if not already present)
RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app

# PEP 668 fix: allow pip install in this container
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY app.py /app/app.py

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
