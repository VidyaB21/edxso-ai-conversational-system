# Edxso AI Conversational System

A microservice-based AI Conversational System that classifies user intents using Hugging Face Transformers and serves predictions through FastAPI APIs. The project follows a production-inspired architecture with separate API Gateway and ML Service components, along with a data processing and model training pipeline.

---

## Project Overview

This project demonstrates how conversational AI systems can be built using a microservice architecture. User requests are routed through an API Gateway, which communicates with an ML Service responsible for intent classification using a Hugging Face Transformer model.

The system supports intents such as:

* Password Reset
* Order Tracking
* Cancel Order
* Refund Request

---

## Architecture

```text
                ┌─────────────────┐
                │      User       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   API Gateway   │
                │   FastAPI       │
                │   Port: 8000    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   ML Service    │
                │   FastAPI       │
                │   Port: 8001    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Hugging Face    │
                │ Transformers    │
                └─────────────────┘
```

---

## Features

* Microservice-based architecture
* FastAPI API Gateway
* FastAPI ML Service
* Hugging Face Transformers integration
* Zero-Shot Intent Classification
* Data preprocessing pipeline
* Model training pipeline
* Accuracy, Precision, and Recall evaluation
* MLflow experiment tracking
* REST API endpoints
* Interactive Swagger documentation

---

## Project Structure

```text
edxso-ai-conversational-system/
│
├── api_gateway/
│   ├── app.py
│   ├── routes.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml_service/
│   ├── app.py
│   ├── model.py
│   ├── predict.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── data_pipeline/
│   ├── dataset.csv
│   ├── preprocess.py
│   ├── train.py
│   ├── mlflow_tracking.py
│   └── requirements.txt
│
├── docker-compose.yml
├── architecture.png
└── README.md
```

---

## Technologies Used

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning

* Hugging Face Transformers
* Facebook BART Large MNLI
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Experiment Tracking

* MLflow

### DevOps

* Docker
* Docker Compose

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/edxso-ai-conversational-system.git

cd edxso-ai-conversational-system
```

---

## Install Dependencies

### API Gateway

```bash
cd api_gateway

pip install -r requirements.txt
```

### ML Service

```bash
cd ../ml_service

pip install -r requirements.txt
```

### Data Pipeline

```bash
cd ../data_pipeline

pip install -r requirements.txt
```

---

## Run Data Pipeline

### Preprocessing

```bash
python preprocess.py
```

### Training

```bash
python train.py
```

### MLflow Tracking

```bash
python mlflow_tracking.py
```

---

## Run Services

### Start ML Service

```bash
cd ml_service

uvicorn app:app --reload --port 8001
```

### Start API Gateway

```bash
cd api_gateway

uvicorn app:app --reload --port 8000
```

---

## API Documentation

### API Gateway

```text
http://127.0.0.1:8000/docs
```

### ML Service

```text
http://127.0.0.1:8001/docs
```

---

## Example Request

### Endpoint

```http
POST /chat
```

### Request Body

```json
{
  "message": "I forgot my password"
}
```

### Response

```json
{
  "user_query": "I forgot my password",
  "prediction": {
    "intent": "password_reset",
    "confidence": 0.4377
  }
}
```

---

## Model Information

### Model Used

```text
facebook/bart-large-mnli
```

### Classification Approach

```text
Zero-Shot Classification
```

Supported Labels:

* password_reset
* order_tracking
* cancel_order
* refund_request

---

## Performance Metrics

The project includes evaluation metrics using Scikit-Learn:

* Accuracy
* Precision
* Recall

These metrics are generated through the training pipeline and tracked using MLflow.

---

## Docker Support

Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

---

## Future Improvements

* Fine-tuned intent classification model
* Larger training dataset
* User authentication
* Database integration
* Kubernetes deployment
* CI/CD pipeline
* Real-time monitoring and logging

---

## Learning Outcomes

This project demonstrates:

* Microservice architecture design
* REST API development with FastAPI
* Transformer-based NLP applications
* Intent classification systems
* ML experiment tracking
* Model serving and deployment workflows
* End-to-end AI application development

---

## Author

**Vidya Bag**

AI Engineer | Machine Learning Enthusiast | Generative AI Developer

GitHub: https://github.com/VidyaB21
