import os

HISTORIAL_FILE = "historial.txt"

def guardar_mensaje(rol, contenido):
    """Guarda cada mensaje en el archivo de texto."""
    with open(HISTORIAL_FILE, "a", encoding="utf-8") as f:
        f.write(f"{rol}: {contenido}\n")

def leer_historial():
    """Lee el historial completo para que el bot tenga contexto."""
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""
