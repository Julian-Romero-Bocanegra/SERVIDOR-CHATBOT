chatbot.py

import requests
import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI")

MODELO = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODELO}:generateContent?key={API_KEY}"

SYSTEM_PROMPT = """
Eres un asistente virtual amigable y educado.
Tu comportamiento debe ser cordial y claro:
- Si el usuario te saluda (ej. 'hola', 'buenas', 'qué tal'), responde saludando de manera cálida.
- Si el usuario se despide (ej. 'adiós', 'gracias', 'chao'), responde con una despedida amable.
- Si el usuario pregunta '¿en qué me puedes ayudar?' o algo similar, responde indicando que puedes conversar y explicar sobre cualquier tema que el usuario desee.
- Mantén siempre un tono respetuoso, evita respuestas ofensivas o agresivas.
- Si el usuario pide ejemplos o explicaciones, procura ser claro y didáctico.
"""

def preguntar_gemini(mensaje_usuario: str) -> str:
    payload = {
        "contents": [{
            "parts": [
                {"text": SYSTEM_PROMPT},
                {"text": f"Pregunta: {mensaje_usuario}"}
            ]
        }]
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        res_json = response.json()

        if response.status_code == 200:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"❌ Error {response.status_code}: {res_json.get('error', {}).get('message', 'Error desconocido')}"
    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"

app = FastAPI()

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(msg: ChatMessage):
    respuesta = preguntar_gemini(msg.message)
    return {"reply": respuesta}