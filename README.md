
# books scraping app


## Test project for Workies
---
## Deploy VPC, EKS, K8S

***

> cd terraform/eks-cluster

> terraform init/plan/apply

> aws eks update-kubeconfig --region eu-west-1 --name sonik-eks-cluster

***

## Deploy helm chart of the app

***

> cd terraform/books-helm

> terraform init/plan/apply

> kubectl get svc -n books

<li>Get external IP of the service. 

<li>Open it in browser on port 5000, endpoint /books