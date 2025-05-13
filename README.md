
💬 Gemini Chatbot avec Streamlit

Un assistant intelligent basé sur Gemini 2 (Google Generative AI) avec une interface moderne en Streamlit.  
Il vous permet de discuter, résumer, traduire et bien plus.

---

## ✨ Fonctionnalités

- 💬 Chat en continu avec mémoire de contexte
- 🎭 Choix du ton de réponse (Professionnel, Amical, etc.)
- 🌍 Traduction automatique dans plusieurs langues
- 🧠 Résumé automatique de la conversation
- 📤 Envoi de fichiers texte
- 💾 Téléchargement du chat au format `.txt`
- 🧪 Mode développeur (affiche les prompts système)
- 💡 Suggestions rapides : CV, Lettre de motivation, Révision

---

## ⚙️ Installation & Lancement

### 1. Cloner le projet

```bash
git clone https://github.com/Andrandra1na/GeminiChat.git
cd GeminiChat
````

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Ajouter votre clé API Gemini

Obtenez une clé ici : [https://makersuite.google.com/app]
Puis créez un fichier `.env` à la racine du projet :

```
GEMINI_API_KEY=ta_clé_api
```

Et ajoute cette ligne en haut de `app.py` si tu veux charger automatiquement :

```python
from dotenv import load_dotenv
load_dotenv()
```

Sinon, exporte-la manuellement :

```bash
export GEMINI_API_KEY="ta_clé_api"  # Linux/Mac
set GEMINI_API_KEY="ta_clé_api"     # Windows (cmd)
```

### 5. Lancer l’application

```bash
streamlit run app.py
```

---

## 📝 Exemple d'utilisation

* **Entrée** : "Peux-tu m’aider à rédiger une lettre de motivation ?"
* **Sortie** : Une lettre personnalisée avec le ton choisi, traduisible automatiquement

---

## 🧠 À propos

Ce projet utilise :

* [Streamlit](https://streamlit.io) pour l’interface web
* [Google Generative AI](https://ai.google.dev) pour le moteur conversationnel
* [deep-translator](https://github.com/nidhaloff/deep-translator) pour la traduction

---

## 📃 Licence

MIT — libre d’usage, améliorez-le à votre façon 🎉





