# infrastructure/terraform/main.tf

resource "helm_release" "hypertrophy_engine" {
  name       = "hypertrophy-app"
  repository = "../../infrastructure/k8s/helm/hypertrophy-chart" # Lokal Chart yolu
  chart      = "hypertrophy-chart"
  namespace  = "olympos-platform"
  create_namespace = true

  # Uygulama versiyonunu buradan yönetiyoruz (Single Source of Truth)
  set {
    name  = "image.tag"
    value = "v1.0.4"
  }
}