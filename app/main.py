from fastapi import FastAPI
from app.schemas import NewsRequest
from app.predictor import predict_news

app = FastAPI(title="Fake News Detection API")

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: NewsRequest):
    return predict_news(data.text)
