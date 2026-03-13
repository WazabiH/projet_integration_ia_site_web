from flask import Flask, render_template, request, redirect
from transformers import pipeline
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

app = Flask(__name__)

# Chargement du modèle de sentiment
classifier = pipeline("sentiment-analysis")

def load_messages():
    if not os.path.exists(DATA_DIR):
        return []
    with open(DATA_DIR, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_messages(messages):
    with open(DATA_DIR, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

@app.route("/", methods=["GET", "POST"])
@app.route("/sentiment/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        messages = load_messages()

        message = request.form["message"].strip()
        if message:
            messages.append({"role": "user", "content": message})

            result = classifier(message)[0]
            label = result["label"]
            score = round(result["score"] * 100, 2)

            # Adaptation simple des labels
            if label.upper() == "POSITIVE":
                sentiment = f"Sentiment détecté : positif ({score}%)"
            elif label.upper() == "NEGATIVE":
                sentiment = f"Sentiment détecté : négatif ({score}%)"
            else:
                sentiment = f"Sentiment détecté : {label} ({score}%)"

            messages.append({"role": "assistant", "content": sentiment})
            save_messages(messages)

        return redirect("/sentiment/")

    messages = load_messages()
    return render_template("index.html", messages=messages)