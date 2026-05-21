# SERVIDOR-CON-MODELO-CHATBOT-IA-GEMINI

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



