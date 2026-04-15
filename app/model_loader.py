import joblib
from tensorflow.keras.models import load_model

MODEL_PATH = "model/fake_news_model.keras"
TOKENIZER_PATH = "model/tokenizer.joblib"

model = load_model(MODEL_PATH)
tokenizer = joblib.load(TOKENIZER_PATH)

MAX_LEN = 40

def get_model():
    return model, tokenizer
