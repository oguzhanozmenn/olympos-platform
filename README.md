🏗️ Olympos Platform: Advanced Kubernetes Observability Stack
Bu depo, modern mikroservis mimarilerinde Gözlemlenebilirlik (Observability) prensiplerini uygulamak amacıyla inşa edilmiş, uçtan uca bir altyapı projesidir. Proje, bir FastAPI uygulamasının konteynerleştirilmesinden başlayarak, Kubernetes üzerinde orkestra edilmesini ve Prometheus/Grafana ikilisiyle derinlemesine izlenmesini kapsar.

🎯 Proje Hedefleri ve Mimari Yaklaşım
Projenin ana odağı, sistemin "kara kutu" olmaktan çıkarılıp her bir bileşeninin izlenebilir hale getirilmesidir.

Konteyner Stratejisi: Uygulamanın hafif, güvenli ve ölçeklenebilir bir Docker imajı haline getirilmesi.

Cluster Orkestrasyonu: olympos-platform namespace'i ile kaynakların mantıksal olarak izole edilmesi.

Veri Odaklı Karar Mekanizması: Sezgilerle değil, PromQL sorgularıyla (CPU rate, Memory saturation) sistem sağlığının analizi.

🛠️ Teknik Stack & Bileşenler
Dil & Framework: Python 3.x / FastAPI (Asenkron API yapısı).

Altyapı Yönetimi: * Docker: İmaj versiyonlama ve Docker Hub entegrasyonu.

Kubernetes (K8s): Deployment, Service ve Ingress yönetimi.

Helm: Prometheus Stack kurulumu için paket yönetimi.

İzleme Araçları:

Prometheus: ServiceMonitor aracılığıyla metrik toplama (Scraping).

Grafana: Dinamik dashboarding ve görselleştirme.

🚀 Uygulama ve Devreye Alma Süreci (Deep Dive)
1. Konteynırlaştırma ve CI/CD Hazırlığı
Uygulama, CI/CD süreçlerine uyumlu olması için versiyonlanmış imajlar halinde paketlendi. Geliştirme sırasında Docker Hub yetkilendirmesi v1.0.8 sürümüyle stabilize edilerek imajların Kubernetes cluster'ına güvenli bir şekilde çekilmesi sağlandı.

2. Kubernetes Kaynak Yönetimi
Uygulamanın cluster içindeki yaşam döngüsü şu bileşenlerle yönetilmektedir:

Deployment: hypertrophy-app pod'larının yönetimi ve rolling update stratejisi.

Service: Pod'lar arası iletişimi sağlayan iç ağ katmanı.

ServiceMonitor: Prometheus'un uygulamayı otomatik olarak keşfedip (Service Discovery) /metrics uç noktasından veri çekmesini sağlayan CRD (Custom Resource Definition).

3. Monitoring Pipeline: Prometheus Entegrasyonu
Sistem metrikleri, Prometheus'un "Target" listesine başarıyla eklendi ve UP statüsünde doğrulanarak sürekli veri akışı sağlandı.

4. Veri Analizi ve Görselleştirme (Grafana)
Projenin en kritik aşamasında, ham metrikler anlamlı içgörülere dönüştürüldü:

Resident Memory Usage: Uygulamanın fiziksel RAM kullanımı (RSS) izlenerek bellek sızıntısı (leak) kontrolü yapıldı (Ortalama: 44.2 MB).

CPU Load Rate: rate(process_cpu_seconds_total[1m]) sorgusu kullanılarak, saniyede atılan 5 istek (curl stress test) sonrası sistemin tepki hızı ve işlemci üzerindeki yük dalgalanması kanıtlandı.

📈 Proje Çıktıları ve Analiz
Metrik Doğruluğu: Prometheus hedefleri %100 başarıyla taranmaktadır.

Görsel Kanıt: Sisteme yük bindirildiğinde (Stress Test) Grafana üzerindeki grafiklerin anlık olarak tetiklendiği ve veri kaybı yaşanmadığı gözlemlenmiştir.

Geliştirici: Oğuzhan Özmen

Rol: Cloud & DevOps Engineering Student

Tarih: Nisan 2026