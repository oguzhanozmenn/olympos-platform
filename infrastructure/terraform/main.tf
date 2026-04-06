# infrastructure/terraform/main.tf

terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
    }
  }
}

# Hatanın çözümü tam olarak buradaki '=' işaretinde:
provider "helm" {
  kubernetes = {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "hypertrophy_engine" {
  name       = "hypertrophy-app"
  chart      = "./k8s/hypertrophy-chart"
  namespace  = "olympos-platform"
  create_namespace = true

  # Değerleri doğrudan liste içinde gönderiyoruz
  values = [
    yamlencode({
      image = {
        repository = "ozii4333/olympos-platform" # Burayı güncelledik
        tag        = "v1.0.7"
      }
    })
  ]
}