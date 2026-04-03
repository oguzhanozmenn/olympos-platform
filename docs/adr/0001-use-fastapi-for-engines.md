# ADR 1: Hypertrophy Engine için FastAPI Seçimi

## Durum
Yüksek performanslı matematiksel hesaplamalar ve asenkron yapı desteği gerekiyor.

## Karar
Python tabanlı FastAPI framework'ü seçilmiştir.

## Nedenler
1. Pydantic ile otomatik veri doğrulama.
2. Dahili Swagger UI (Dokümantasyon kolaylığı).
3. Asenkron (async/await) desteği ile yüksek throughput.