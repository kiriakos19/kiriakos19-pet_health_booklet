# Deploy app with docker compose
docker-compose up --build
# Deploy prohect to kubernetes cluster

# Deploy postgresql with helm
microk8s.helm3 repo add bitnami https://charts.bitnami.com/bitnami
microk8s.helm3 install my-release bitnami/postgresql
# 
microk8s.kubectl install db -f values.yaml bitnami/postgresql

# Deploy fastapi
microk8s.kubectl apply -f k8s/fastapi/fastapi-deployment.yaml 
microk8s.kubectl apply -f k8s/fastapi/fastapi-deployment.yaml
microk8s.kubectl apply -f k8s/fastapi/fastapi-clim.yaml
microk8s.kubectl apply -f k8s/fastapi/fastapi-pvc.yaml
microk8s.kubectl apply -f k8s/fastapi/fastapi-ingress.yaml

# Deploy vue.js
microk8s.kubectl apply -f k8s/vue/vue-deployment.yaml 
microk8s.kubectl apply -f k8s/vue/vue-clim.yaml
microk8s.kubectl apply -f k8s/vue/vue-ingress.yaml

# Test accounts 
Username user@gmail.com, Password test123
Username doctor@gmail.com, Password test123
Pet names (Rex, Aria).
# Url 
http://kausonas.ddns.net/
http://pet-app.ddns.net/
