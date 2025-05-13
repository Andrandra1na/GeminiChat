import streamlit as st
from gemini_api import generate_response
from io import StringIO
import datetime
import os

# Configuration de la page
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="wide")

# Logo + Titre
with st.container():
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("assets/logo.jpg"):
            st.image("assets/logo.jpg", width=80)
    with col2:
        st.title("Gemini Chatbot 💬")
        st.caption("Assistant IA polyvalent avec Streamlit + Gemini")

# Initialisation de la session
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Barre latérale : paramètres utilisateur ---
with st.sidebar:
    st.markdown("## ⚙️ Paramètres")
    tone = st.selectbox("🎭 Ton de réponse", ["Professionnel", "Amical", "Court", "Formel"])
    translate = st.selectbox("🌐 Traduire la réponse", ["Aucune", "Français", "Anglais", "Espagnol", "Arabe",       
                                                       "Allemand", "Italien", "Portugais", "Néerlandais", "Russe", "Chinois", "Japonais", "Coréen", "Hindi"])
    show_dev = st.checkbox("🧪 Mode développeur")

    st.markdown("---")

    # Réinitialiser la conversation
    if st.button("🗑️ Nouvelle conversation"):
        st.session_state.messages = []

    # Télécharger la conversation
    if st.button("📥 Télécharger .txt"):
        chat_log = "\n".join(
            [f"Vous: {msg}" if i % 2 == 0 else f"Assistant: {msg}" for i, msg in enumerate(st.session_state.messages)]
        )
        st.download_button(
            label="💾 Télécharger conversation",
            data=chat_log,
            file_name=f"conversation_{datetime.datetime.now().isoformat()}.txt",
        )

    # Upload de fichier texte
    uploaded_file = st.file_uploader("📤 Envoyer un fichier (.txt)", type=["txt"])
    if uploaded_file:
        content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        st.session_state.messages.append(content)
        st.success("✅ Texte ajouté à la conversation.")

    # Résumer la conversation
    if st.button("🧠 Résumer la conversation"):
        summary = generate_response(st.session_state.messages, tone=tone, mode_resume=True)
        st.success(summary)

# --- Questions fréquentes ---
st.markdown("### 🧩 Questions fréquentes")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📄 Aide pour un CV"):
        st.session_state.messages.append("Peux-tu m'aider à rédiger un CV ?")
with col2:
    if st.button("✉️ Lettre de motivation"):
        st.session_state.messages.append("Comment écrire une lettre de motivation ?")
with col3:
    if st.button("🗓️ Plan de révision"):
        st.session_state.messages.append("Aide-moi à planifier mes révisions.")

st.divider()

# --- Zone de texte utilisateur ---
user_input = st.text_input("👤 Votre message :", placeholder="Écrivez ici...")

if user_input:
    st.session_state.messages.append(user_input)

# --- Affichage du chat ---
for i, msg in enumerate(st.session_state.messages):
    if i % 2 == 0:
        st.markdown(f"**🧑‍🎓 Vous** : {msg}")
    else:
        st.markdown(f"**🤖 Assistant** : {msg}")

# --- Génération de la réponse ---
if len(st.session_state.messages) % 2 == 1:
    response = generate_response(
        st.session_state.messages,
        tone=tone,
        translate=None if translate == "Aucune" else translate,
    )
    st.session_state.messages.append(response)
    st.success(f"**🤖 Assistant** : {response}")

    if show_dev:
        st.code(f"[Prompt système : Ton={tone}, Traduction={translate}]")
