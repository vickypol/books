terraform {
  backend "local" {}
}

provider "kubernetes" {
  config_path    = "~/.kube/config"

}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

locals {
  cluster_name = "sonik-eks-cluster"
}

resource "kubernetes_namespace" "books" {
  metadata {
    name = "books"
  }
}

resource "helm_release" "books" {
  name       = "books"
  chart      = "${path.module}/../../helm/books"
  namespace   = "books"
  values = [
    "${file("${path.module}/../../helm/books/values.yaml")}"
  ]
  set {
    name  = "image.tag"
    value = var.tag
  }
}
