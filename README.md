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





