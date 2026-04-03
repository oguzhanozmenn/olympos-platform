FROM python:3.9-slim

WORKDIR /app

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir uvicorn fastapi  # Temel paketleri garantiye alalım
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı kopyala
COPY ./app ./app

# Çalıştırılacak komutu dosya yoluyla (absolute path) verelim
CMD ["/usr/local/bin/python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]