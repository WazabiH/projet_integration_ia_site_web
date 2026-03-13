from flask import Flask, render_template, request, redirect
import json, os, random


os.environ["HF_HUB_OFFLINE"] = "1"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
GENERATION_DUMMY_TEXT = ["Ceci est un texte de génération d'exemple.",
                        "Voici un autre exemple de texte généré par le modèle.",
                        "Le modèle de génération de texte fonctionne correctement.",
                        "L'intelligence artificielle est fascinante.",
                        "Les modèles de langage sont de plus en plus avancés."]


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/chat/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        
        with open(DATA_DIR, 'r') as f:
            messages = json.load(f)
        
        # Obtenir le message de l'utilisateur
        message = request.form["message"]    
        messages.append({"role": "user", "content": message})
    
        # Generate response (dummy for now)  
        response = random.choice(GENERATION_DUMMY_TEXT)
        messages.append({"role": "assistant", "content": response})
        
        with open(DATA_DIR, 'w') as f:
            json.dump(messages, f)
        return redirect('/chat/')
        
    else:    
        with open(DATA_DIR, 'r') as f:
            messages = json.load(f)
    return render_template(
    "chat.html", messages=messages)
    