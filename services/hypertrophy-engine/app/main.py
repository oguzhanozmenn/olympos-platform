from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Uygulamanı başlat
app = FastAPI(title="Hypertrophy Engine API")

# SİHİRLİ DOKUNUŞ: Prometheus metriklerini uygulamaya bağla ve /metrics endpoint'ini otomatik oluştur
Instrumentator().instrument(app).expose(app)

# Senin mevcut sistem kontrol (health-check) endpoint'in
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "hypertrophy-engine"}


# --- DİĞER KODLAR ---
# Buranın altına uygulamanın asıl işini yapan diğer tüm endpoint'lerini
# (antrenman programı hesaplama, veritabanı işlemleri vb.) ekleyebilirsin.