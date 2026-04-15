import re
from tensorflow.keras.preprocessing.sequence import pad_sequences

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

def tokenize_text(text, tokenizer, max_len):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    return padded
