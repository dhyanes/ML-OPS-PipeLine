# ML-OPS-PipeLine
# MLOps Pipeline using Kubernetes

## Overview
End-to-end ML pipeline with CI/CD and Kubernetes deployment.

## Tech Stack
- Python
- Docker
- Kubernetes
- Jenkins

## Steps
1. Train model
2. Build Docker image
3. Deploy to Kubernetes

## Architecture

## RUn Prometheus (Docker )

docker run -d \
  -p 9090:9090 \
  -v $(pwd)/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus

## graffana Setup

docker run -d -p 3000:3000 grafana/grafana

👉 Login:

user: admin
password: admin

👉 Add Data Source:

URL: http://prometheus:9090

