# 🧠 Fake News Detection System (AI + API + Frontend Ready)

A production-ready Fake News Detection system built using Deep Learning (BiLSTM) and deployed via a scalable API architecture. This project transforms an experimental Jupyter Notebook model into a real-world inference service with API integration and frontend compatibility.

---

# 🚀 Project Overview

This system classifies news text as **Fake** or **Real** using a trained deep learning model. It exposes the model through a REST API, enabling integration with web or mobile applications.

---

# 🏗️ Architecture


Client (React / Web UI)
↓
REST API (FastAPI)
↓
Preprocessing Layer
↓
Tokenizer + Padding
↓
BiLSTM Model (TensorFlow/Keras)
↓
Prediction (Fake / Real + Confidence)


---

# 📁 Project Structure


fake-news-detector/
│── app/
│ ├── main.py # FastAPI entry point
│ ├── model_loader.py # Load model + tokenizer
│ ├── preprocess.py # Text preprocessing
│ ├── predictor.py # Prediction logic
│ └── schemas.py # API schemas
│
│── model/
│ ├── fake_news_model.keras # Trained model
│ └── tokenizer.joblib # Tokenizer
│
│── requirements.txt
│── Dockerfile
│── README.md


---

# ⚙️ Tech Stack

### 🔹 Backend
- FastAPI
- TensorFlow / Keras
- Scikit-learn
- Joblib

### 🔹 Frontend
- React

### 🔹 Model
- BiLSTM (Bidirectional LSTM)
- Tokenization + Padding
- Binary Classification

### 🔹 Deployment
- Docker
- Cloud-ready (Render / Railway / AWS / VPS)

---

# 📊 Model Details

- Architecture: BiLSTM
- Input: News text
- Output:
  - Label: `Fake` / `Real`
  - Confidence Score (0–1)

---

# 🧪 API Usage

## 🔹 Base URL

http://localhost:8000


---

## 🔹 Health Check

GET /


### Response:
```json
{
  "status": "API is running"
}
---

🔹 Prediction Endpoint
POST /predict
Request:
{
  "text": "Breaking news content goes here..."
}
Response:
{
  "confidence": 0.87,
  "label": "Fake"
}
🔹 Interactive API Docs
http://localhost:8000/docs


