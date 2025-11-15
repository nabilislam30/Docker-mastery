# 🚀 Redis Counter App

A simple **Flask + Redis** web application containerized with **Docker Compose** and fronted by **NGINX** for load balancing.  
Each refresh increments a visit counter stored in Redis, demonstrating a scalable multi-container architecture.

---

## 🧠 Overview

This project is part of the **Docker-mastery** repository and showcases:
- A Python **Flask web application**
- A **Redis** key-value store for persistent counting
- An **NGINX** reverse proxy for load balancing multiple Flask containers
- Docker Compose orchestration for a clean, reproducible setup

---

## 🏗️ Architecture


---

## 🚀 How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/nabilislam30/Docker-mastery.git
cd Docker-mastery/redis-counter-app
docker compose up --build -d
docker compose up -d --scale web=3
Visit in your browser: http://localhost:5050
