from app.model_loader import get_model
from app.preprocess import clean_text, tokenize_text

model, tokenizer = get_model()

def predict_news(text: str):
    cleaned = clean_text(text)
    processed = tokenize_text(cleaned, tokenizer, 40)

    prediction = model.predict(processed)[0][0]

    return {
        "confidence": float(prediction),
        "label": "Fake" if prediction > 0.5 else "Real"
    }
