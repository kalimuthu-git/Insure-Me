## 🛡️ InsureMe — Cloud-Native Insurance Management Application

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![AWS](https://img.shields.io/badge/AWS-ECS%20Fargate-FF9900?logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-CodePipeline-green?logo=amazonaws)

> A cloud-based insurance policy management application with a fully automated DevOps CI/CD pipeline on AWS.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Technologies Used](#-technologies-used)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [CI/CD Pipeline](#-cicd-pipeline)
- [AWS Infrastructure Setup](#-aws-infrastructure-setup)
- [Deployment](#-deployment)
- [Live Demo](#-live-demo)

---

## 📌 Project Overview

**InsureMe** is a cloud-based insurance management application designed to demonstrate a complete DevOps CI/CD pipeline using modern tools and AWS services.

The application is built with **Python (Flask)** and exposes REST APIs for managing insurance policies — create, view, update, and delete. It is containerized with **Docker**, stored in **Amazon ECR**, and deployed on **AWS ECS (Fargate)** — all automated through **AWS CodePipeline**.

Every code push to GitHub automatically triggers the pipeline: build → containerize → push to ECR → deploy to ECS. No manual steps required.

---

## 🏗️ Architecture

```
Developer (GitHub Push)
        │
        ▼
  AWS CodePipeline
        │
   ┌────┴────┐
   │ Source  │ ← GitHub Repository
   └────┬────┘
        │
   ┌────┴────┐
   │  Build  │ ← AWS CodeBuild (buildspec.yml)
   │         │   → Docker Image built
   │         │   → Image pushed to Amazon ECR
   └────┬────┘
        │
   ┌────┴────┐
   │ Deploy  │ ← Amazon ECS (Fargate)
   │         │   → Task Definition updated
   │         │   → Service re-deployed
   └────┬────┘
        │
        ▼
Application Load Balancer (ALB)
        │
        ▼
   End Users 🌐
```

---

## 🛠️ Technologies Used

| Category | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask + Flask-SQLAlchemy |
| Server | Gunicorn |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Amazon ECS (Fargate) |
| CI/CD | AWS CodePipeline + CodeBuild |
| Load Balancer | AWS Application Load Balancer (ALB) |
| Source Control | GitHub |

---

## ✨ Features

- ✅ Full **CRUD REST API** for insurance policy management
- ✅ **Automated CI/CD pipeline** — triggered on every GitHub push
- ✅ **Dockerized** application for consistent environments
- ✅ **Serverless containers** using AWS Fargate (no EC2 management)
- ✅ **High availability** via Application Load Balancer
- ✅ **Scalable** deployment on Amazon ECS
- ✅ Frontend UI (index.html) included

---

## 📁 Project Structure

```
insure-me/
│
├── app.py                  # Flask application & REST APIs
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image configuration
├── buildspec.yml           # AWS CodeBuild build specification
├── templates/
│   └── index.html          # Frontend UI
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker
- AWS CLI configured
- GitHub account

### Run Locally

```bash
# Clone the repository
git clone https://github.com/kalimuthu-git/insure-me.git
cd insure-me

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

App will be available at: `http://localhost:5000`

### Run with Docker

```bash
# Build the image
docker build -t insure-me .

# Run the container
docker run -p 5000:5000 insure-me
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Frontend UI / Health check |
| `POST` | `/policy` | Create a new insurance policy |
| `GET` | `/policy/1` | View a specific policy |
| `PUT` | `/policy/2` | Update an existing policy |
| `DELETE` | `/policy/3` | Delete a policy |

---

## 🔄 CI/CD Pipeline

The pipeline is configured using `buildspec.yml` and triggered automatically on every push to the `main` branch.

### Pipeline Stages

```
1. Source  →  GitHub (code push triggers pipeline)
2. Build   →  AWS CodeBuild
               - Login to Amazon ECR
               - Build Docker image
               - Push image to ECR
               - Generate imagedefinitions.json
3. Deploy  →  Amazon ECS (Fargate)
               - Pull new image from ECR
               - Update running service
```

### buildspec.yml Summary

```yaml
version: 0.2
phases:
  pre_build:   # Login to ECR
  build:       # Build Docker image
  post_build:  # Push image, create imagedefinitions.json
artifacts:
  files:
    - imagedefinitions.json
```

---

## ☁️ AWS Infrastructure Setup

### 1. Amazon ECR

- Repository: `project/insure-me`
- Stores Docker images for each build

### 2. AWS CodeBuild

- Connected to GitHub repository
- Uses `buildspec.yml` for build instructions
- Docker enabled

### 3. AWS CodePipeline

| Stage | Provider |
|---|---|
| Source | GitHub |
| Build | AWS CodeBuild |
| Deploy | Amazon ECS |

### 4. Amazon ECS (Fargate)

- **Cluster:** `Insure-me-cluster`
- **Task Definition:** `Insure-me-task`
- **Container Name:** `insure-me-container`
- **Port:** `5000`
- **Service:** `Insure-me-task-service-alka3ho2`

### 5. Application Load Balancer

- **Type:** Application Load Balancer (ALB)
- **Listener:** HTTP (Port 80)
- **Target:** ECS container (Port 5000)

---

## 📦 Deployment

Push to GitHub to trigger the pipeline:

```bash
git add .
git commit -m "your commit message"
git push origin main
```

The pipeline will automatically:
1. Pull the latest code
2. Build a new Docker image
3. Push to Amazon ECR
4. Deploy the updated image to ECS Fargate

---

## 🌐 Live Demo

Application is accessible via the Load Balancer URL:

```
http://insure-me-alb-207979398.ap-south-1.elb.amazonaws.com/
```

---

## 📸 Screenshots

### Application Deployed Successfully
<img width="1918" height="1078" alt="deployed successfully" src="https://github.com/user-attachments/assets/e0e899ce-53c7-4b63-a844-f51419c59ad7" />

### CI/CD Pipeline Success
<img width="1918" height="1078" alt="deployed success" src="https://github.com/user-attachments/assets/8efd7aba-8555-4b7e-8187-222652fff49e" />

### ECS Service Running
<img width="1918" height="1078" alt="ECS-Running Status" src="https://github.com/user-attachments/assets/16a2a517-c4d3-4ae3-8fc7-b1edb9a3bf6f" />

---
---

## 📝 Conclusion

InsureMe demonstrates a real-world DevOps pipeline using AWS services, providing hands-on experience in:

- Application containerization with Docker
- Infrastructure automation on AWS
- CI/CD pipeline design and implementation
- Cloud-native deployment with ECS Fargate

---



> **Author:** Kalimuthu A | **Date:** 10th April 2026
