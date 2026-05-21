# SERVIDOR CON MODELO CHATBOT

## Documentación Técnica: Arquitectura de Chatbot con FastAPI y Gemini

Este proyecto implementa una arquitectura desacoplada Cliente-Servidor en un entorno Linux (Ubuntu Server). El backend gestiona de forma segura la comunicación con la API de Google Gemini mediante solicitudes HTTP asíncronas, mientras que el frontend actúa como una interfaz interactiva y ligera en la terminal para el usuario final. 

### Tener en cuenta

Si vas a desplegar el proyecto del chatbot en una máquina virtual (VM), es importante configurar el entorno correctamente para que el servidor y el cliente se comuniquen sin problemas. Aquí tienes las recomendaciones clave:

#### Configuración de Red (Modo Puente o NAT):

Si utilizas NAT (la opción por defecto en muchas plataformas), asegúrate de configurar el Reenvío de Puertos (Port Forwarding) en la configuración de red de la máquina virtual. Debes mapear el puerto 8000 de la máquina virtual al puerto 8000 de tu máquina anfitriona para poder acceder al chat desde tu sistema operativo principal.

Si utilizas Modo Puente (Bridged), la máquina virtual obtendrá una IP propia en tu red local (como si fuera otro dispositivo físico). Esto facilita la conexión, ya que simplemente apuntas el url en tu cliente al IP asignado a la VM.

#### Gestión de Memoria y CPU:

Aunque el chatbot y FastAPI son ligeros, recuerda asignar al menos 1 GB de RAM y 1 núcleo de CPU dedicado a la máquina virtual para garantizar estabilidad. Un sistema Ubuntu Server mínimo corre bien con estos recursos.

#### Nota
También existe la posibilidad de descargar directamente Ubuntu en la máquina en la cual se está trabajando.

### Estrcutura del proyecto

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/01a66534-b867-4fe8-a986-1f449d33aa80" />

#### ¿Cómo interactúan entre sí?
Para entender cómo fluye la información en tu sistema, este esquema te muestra la relación entre los archivos que hemos creado:
1.	El Cliente (modelo_chatbot.py) envía tu mensaje al Servidor (chatbot.py).
2.	El Servidor utiliza el Gestor (chat_history.py) para registrar la pregunta en el Almacenamiento (historial.txt).
3.	El Servidor consulta a Gemini y recibe una respuesta.
4.	El Servidor registra la respuesta en el Almacenamiento y la devuelve al Cliente para que la veas en pantalla.
5.	El Supervisor (supervisor.py) vigila constantemente que todo este flujo no se detenga.

### Fase 1: Configuración Inicial del Servidor
Ejecuta los siguientes comandos en la terminal de tu Ubuntu Server para preparar el entorno de dependencias y asegurar el acceso remoto seguro.

1. Actualizar los repositorios e índices de paquetes del sistema
`sudo apt update && sudo apt upgrade -y`
<img width="921" height="35" alt="image" src="https://github.com/user-attachments/assets/a5f8c78e-22d3-45b4-af42-387bb5f22b5b" />

2. Instalar el editor de texto Nano para la gestión de archivos en consola
`sudo apt install nano -y`
<img width="921" height="140" alt="image" src="https://github.com/user-attachments/assets/0e205d6a-23b4-44d0-96ba-b4ef1bdd91f8" />

3. Consultar la dirección IP asignada al servidor para futuras conexiones externas
`ip a`
<img width="921" height="227" alt="image" src="https://github.com/user-attachments/assets/379ead87-6a74-4370-9697-f4a8dfebfce2" />

4. Instalar el entorno de ejecución Python 3, su gestor de paquetes (pip) y el módulo de entornos virtuales
`sudo apt install python3 python3-pip -y`
<img width="921" height="172" alt="image" src="https://github.com/user-attachments/assets/e008ec5e-5f64-49be-8222-8d80e4e838c8" />

`sudo apt install python3-venv -y`
<img width="921" height="141" alt="image" src="https://github.com/user-attachments/assets/8ab3d37b-3a71-4b32-8dd3-d0fddcbd232d" />

### Fase 2: Entorno Virtualizado y Despliegue del Código
Para garantizar la portabilidad y evitar conflictos con las librerías globales de Python, aislamos el proyecto en un entorno virtualizado (venv)

1. Inicialización del Entorno
Crear el directorio de trabajo y posicionarse en él
`mkdir ubuntu_chatbot && cd ubuntu_chatbot`
<img width="921" height="35" alt="image" src="https://github.com/user-attachments/assets/6dd5447a-f5e1-47f2-a1c7-2f112d73b3ff" />

Generar el entorno virtual aislado
`python3 -m venv venv`
<img width="921" height="29" alt="image" src="https://github.com/user-attachments/assets/33042490-3b3e-418a-b60e-e754ade992a1" />

Activar el entorno virtual (notarás el prefijo '(venv)' en tu prompt)
`source venv/bin/activate`
<img width="921" height="31" alt="image" src="https://github.com/user-attachments/assets/c597f4dc-3f55-416c-bef4-63863438482d" />

Instalar las librerías necesarias especificadas en tu arquitectura
`pip install fastapi uvicorn python-dotenv requests`
<img width="921" height="78" alt="image" src="https://github.com/user-attachments/assets/47ed12c5-a7b9-4dcd-a89d-61b7c696b8ac" />

2. Creación de los Archivos de Configuración y Lógica
Crea cada archivo utilizando nano <nombre_del_archivo> y copia el código correspondiente que tienes desarrollado: 
`.env`
Servidor Backend (nano chatbot.py):
Aquí el backend se encarga de estructurar el payload JSON requerido por la API de Google, concatenando el SYSTEM_PROMPT para moldear la personalidad cordial y didáctica del bot. 
`Chatbot.py`
Cliente de Consola (nano modelo_chatbot.py): 
Consume localmente el endpoint expuesto por FastAPI y maneja las interrupciones o la salida controlada del programa. 
`Modelo_chatboy.py`

HACE FALTA

<img width="921" height="89" alt="image" src="https://github.com/user-attachments/assets/8d3f400f-fc3d-4404-9830-44b491118481" />

Fase 3: Pruebas de Funcionamiento e Interacción
Para validar el flujo completo de datos, abre dos instancias de terminal independientes en tu servidor (o utiliza un multiplexor como tmux): 

Paso 1: Inicializar el Backend (Terminal 1)
Dentro del entorno virtual, ejecuta el servidor ASGI Uvicorn. El parámetro --host 0.0.0.0 es clave, ya que mapea el servicio para escuchar peticiones en cualquier interfaz de red del servidor, no solo en local. 
`source venv/bin/activate`
`uvicorn chatbot:app --host 0.0.0.0 --port 8000`
<img width="921" height="130" alt="image" src="https://github.com/user-attachments/assets/2077a260-db2d-433a-9d95-c6957b94a39a" />

Paso 2: Ejecutar la Interfaz de Usuario (Terminal 2)
En la otra ventana de terminal, arranca el script cliente para iniciar el canal de conversación estructurado: 
`source venv/bin/activate`
`python modelo_chatbot.py`
<img width="921" height="149" alt="image" src="https://github.com/user-attachments/assets/ec567cb8-a485-4639-9fac-d73b565312df" />















