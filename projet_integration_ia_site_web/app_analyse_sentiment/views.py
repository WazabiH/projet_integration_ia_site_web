from flask import Flask, render_template, request
from transformers import pipeline
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

app = Flask(__name__)

classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def load_history():
    if not os.path.exists(DATA_DIR):
        return []
    with open(DATA_DIR, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(history):
    with open(DATA_DIR, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def convert_label(label):
    stars = int(label[0])
    if stars <= 2:
        return "Négatif"
    elif stars == 3:
        return "Neutre"
    else:
        return "Positif"

def heuristic_fix(message, predicted_sentiment):
    text = message.lower().strip()

    negative_keywords = [
        "j'en ai marre", "jen ai marre", "marre",
        "pas bien", "triste", "déçu", "decu", "nul",
        "horrible", "catastrophe", "mauvais", "mal",
        "je vais mal", "ça va mal", "sa va mal"
    ]

    positive_keywords = [
        "heureux", "heureuse", "joyeux", "joyeuse",
        "j'aime", "j’adore", "j'adore", "trop bien",
        "incroyable", "super", "génial", "genial",
        "meilleure vie", "joie de vivre", "content", "contente"
    ]

    for word in negative_keywords:
        if word in text:
            return "Négatif"

    for word in positive_keywords:
        if word in text:
            return "Positif"

    return predicted_sentiment

@app.route("/", methods=["GET", "POST"])
@app.route("/sentiment/", methods=["GET", "POST"])
def index():
    result = None
    history = load_history()

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            prediction = classifier(message.lower())[0]
            sentiment = convert_label(prediction["label"])
            sentiment = heuristic_fix(message, sentiment)
            score = round(prediction["score"] * 100, 2)

            result = {
                "text": message,
                "sentiment": sentiment,
                "score": score
            }

            history.insert(0, result)
            save_history(history)

    return render_template("index.html", result=result, history=history[:10])