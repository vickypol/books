
# books scraping app


## exam project
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

> terraform init/plan/apply -var="tag=a713b22"

> kubectl get svc -n books

<li>Get external IP of the service. 

<li>Open it in browser http://ip:5000/1 for page 1 etc.
