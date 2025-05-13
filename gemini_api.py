import os
from google import genai
from google.genai import types
from deep_translator import GoogleTranslator

# Initialisation de Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model_name = "gemini-2.0-flash"

# Dictionnaire de langue pour la traduction
LANG_CODE = {
    "Français": "fr",
    "Anglais": "en",
    "Espagnol": "es",
    "Arabe": "ar"
}

def generate_response(history, tone="Professionnel", translate=None, mode_resume=False):
    contents = []

    if mode_resume:
        # Résumé de l'historique
        history_text = "\n".join([f"{'Utilisateur' if i % 2 == 0 else 'Assistant'}: {msg}" for i, msg in enumerate(history)])
        prompt = f"Peux-tu me faire un résumé de cette conversation :\n{history_text}"
        contents.append(types.Content(role="user", parts=[types.Part.from_text(text=prompt)]))
    else:
        for i, msg in enumerate(history):
            role = "user" if i % 2 == 0 else "model"
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg)]))

    # Instructions système selon le ton choisi
    instruction_ton = {
        "Professionnel": "Réponds de manière claire et professionnelle.",
        "Amical": "Réponds comme un ami avec un ton chaleureux.",
        "Court": "Réponds de façon concise et directe.",
        "Formel": "Utilise un langage formel et respectueux."
    }

    system_instruction = [types.Part.from_text(text=instruction_ton.get(tone, ""))]

    response_text = ""
    config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=system_instruction
    )

    try:
        for chunk in client.models.generate_content_stream(
            model=model_name,
            contents=contents,
            config=config,
        ):
            response_text += chunk.text
    except Exception as e:
        response_text = f"Erreur : {e}"

    # Traduction (optionnelle)
    if translate:
        try:
            lang_code = LANG_CODE.get(translate)
            if not lang_code:
                raise ValueError(f"Langue non supportée : {translate}")
            response_text = GoogleTranslator(source='auto', target=lang_code).translate(response_text)
        except Exception as e:
            response_text = f"Erreur de traduction : {e}"

    return response_text
