modelo_chatbot.py

import requests
import textwrap

def chat_continuo():
    url = "http://localhost:8000/chat"
    print("--- Chatbot Activo (Escribe 'salir' para terminar) ---")
    
    # El bucle while mantiene el chat abierto
    while True:
        mensaje_usuario = input("\nTu: ")
        
        # Opción para cerrar el programa manualmente
        if mensaje_usuario.lower() in ["salir", "exit", "quit"]:
            print("Finalizando Chat...")
            break
            
        payload = {"message": mensaje_usuario}
        
        try:
            # Petición al servidor FastAPI
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                # Obtenemos la respuesta y aplicamos formato de texto
                respuesta_bruta = response.json().get('reply')
                
                # Configuramos el ancho de 80 caracteres para evitar saltos bruscos
                wrapper = textwrap.TextWrapper(width=80) 
                texto_formateado = wrapper.fill(text=str(respuesta_bruta))
                
                print(f"\nChatbot: {texto_formateado}\n")
            else:
                print(f"\nError {response.status_code}: {response.text}\n")
                
        except Exception as e:
            print(f"\nError de conexión: {e}\n")
            # Decidimos no hacer 'break' aquí para que el bot no se cierre si falla una vez
            continue

if __name__ == "__main__":
    chat_continuo()