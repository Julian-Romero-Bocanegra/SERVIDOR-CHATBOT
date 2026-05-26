import os
import time
import subprocess

# Configuración
PROCESO_NOMBRE = "uvicorn chatbot:app"
TIMEOUT_SEG = 30

def gestionar_servidor():
    print("Iniciando Supervisor de Chatbot...")
    while True:
        # Busca procesos que coincidan con el nombre y estén activos
        cmd = f"ps aux | grep '{PROCESO_NOMBRE}' | grep -v grep"
        proceso = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if proceso.stdout:
            # Aquí podrías medir el tiempo si el proceso tiene un PID persistente
            # Para simplificar y ser efectivo: si detectamos comportamiento anómalo:
            print("Verificando estado del servidor...")
        else:
            print("Servidor no detectado. Reiniciando...")
            # Limpiar procesos zombies residuales
            os.system("pkill -9 -f 'uvicorn'") 
            # Iniciar el servidor en segundo plano
            os.system("nohup uvicorn chatbot:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &")
        
        time.sleep(TIMEOUT_SEG)

if __name__ == "__main__":
    gestionar_servidor()
