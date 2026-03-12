# 📈 Real-Time Monitoring Project (Prometheus & Grafana)

This project demonstrates a full-stack observability solution for a Python application. It uses a **Prometheus** time-series database to scrape metrics from a **Flask** app and visualizes them through a **Grafana** dashboard.

## 🚀 Key Features
- **Custom Metrics:** The app exposes real-time data on request duration and error rates using the Prometheus Python client.
- **Dockerized Infrastructure:** The entire stack (App, Prometheus, Grafana) is orchestrated using Docker Compose for 1-command deployment.
- **Visual Dashboards:** Includes a Grafana dashboard showing the "Golden Signals" of Latency and Errors.

## 🛠 Tools Used
- **Backend:** Python (Flask)
- **Monitoring:** Prometheus
- **Visualization:** Grafana
- **Infrastructure:** Docker & Docker Compose

## 📁 Project Structure
- `app.py`: The Python application exposing `/metrics`.
- `docker-compose.yml`: Orchestration for the monitoring services.
- `prometheus.yml`: Scrape configuration for the Prometheus server.
- `Dockerfile`: Instructions to build the application image.

## ⚙️ Setup Instructions
1. **Launch the services:**
   ```bash
   docker compose up -d --build
