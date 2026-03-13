# Projet IA – Analyse de sentiment (Application Web)

Ce projet consiste à intégrer un modèle d'intelligence artificielle dans une application web afin d’analyser automatiquement le sentiment d’un texte saisi par l’utilisateur.

L’application permet de détecter si un message est **positif ou négatif**, et d'afficher le **niveau de confiance du modèle**.

Ce projet a été réalisé dans le cadre d’un projet de développement web intégrant de l’IA.

---

# Objectif du projet

L’objectif est de montrer comment intégrer un modèle de **Machine Learning / NLP (Natural Language Processing)** dans une application web.

L’utilisateur peut :
- écrire un message
- envoyer le message
- obtenir une analyse automatique du sentiment

Le système utilise un modèle pré-entraîné via la bibliothèque **Transformers** de HuggingFace.

---

# Technologies utilisées

- Python
- Flask
- Transformers (HuggingFace)
- PyTorch
- HTML
- CSS

---

# Fonctionnement

1. L’utilisateur saisit un texte dans l’interface web.
2. Le texte est envoyé au serveur Flask.
3. Le modèle d’IA analyse le texte.
4. L’application retourne :
   - le sentiment détecté (positif / négatif)
   - le pourcentage de confiance
5. Le résultat est affiché dans l’interface avec un historique des analyses.

---

# Structure du projet
projet_integration_ia_site_web
│
├── run.py
├── requirements.txt
│
├── app_analyse_sentiment
│ ├── views.py
│ ├── data.json
│ ├── templates
│ │ └── index.html
│ └── static
│
├── app_assistant_ia
│ ├── views.py
│ ├── data.json
│ ├── templates
│ │ └── chat.html
│ └── static


---

# Installation

Cloner le projet :

```bash
git clone https://github.com/WazabiH/projet_integration_ia_site_web.git
cd projet_integration_ia_site_web

Installer les dépendances :

pip install -r requirements.txt

Lancer l'application :

python run.py

Puis ouvrir dans le navigateur :

http://127.0.0.1:5000
