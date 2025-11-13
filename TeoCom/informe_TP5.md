 # Punto 1 
 1) Características de MQTT

Protocolo: Message Queuing Telemetry Transport (MQTT).
Diseño: Es un protocolo de mensajería ligero, diseñado para dispositivos con recursos limitados y redes de baja calidad (alto latencia/bajo ancho de banda).
Modelo: Sigue el patrón Publish/Subscribe (Pub/Sub).

Ventajas: Bajo consumo de energía, uso eficiente del ancho de banda, baja sobrecarga (overhead), confiabilidad definida por niveles de QoS.

Desventajas: Dependencia de un broker central, no está diseñado para el intercambio de grandes volúmenes de datos.

Usos Principales: Internet de las Cosas (IoT), telemetría, sistemas de monitoreo y control remoto, aplicaciones móviles.


#### ¿Qué es el patrón de diseño Pub/Sub?
Es un modelo de comunicación asíncrona.
Los remitentes de los mensajes (Publishers) no se programan para enviar sus mensajes a receptores específicos. Los mensajes son publicados en categorías conocidas como tópicos.
Los receptores (Subscribers) expresan interés en uno o más tópicos. Un componente intermedio (Broker) filtra los mensajes según los tópicos y los distribuye a los Subscribers.
Se diferencia del modelo tradicional Cliente-Servidor en que el remitente y el receptor no tienen conocimiento directo entre sí (desacoplamiento)

2) Instalar y Ejecutar un Broker

Requerimiento: Debes configurar y ejecutar un broker MQTT (puedes usar HiveMQ, Mosquitto o EMQX).

## Insertar imagenes
<img width="1312" height="578" alt="image" src="https://github.com/user-attachments/assets/b07b401e-1a70-4245-8d6a-842e3f2b406e" />
<img width="689" height="564" alt="image" src="https://github.com/user-attachments/assets/0fd88cdc-48a4-409a-a270-c133f39ef7c4" />



Detalles del ejemplo (HiveMQ Cloud):
URL: 42914cf0bb8a4cf690bb8f26149dc983.s1.eu.hivemq.cloud 
Port: 8883 
WebSocket Port: 8884 
Estos datos son los necesarios para que tus clientes se conecten al broker.

3) Verificar Funcionamiento (Conexión Cliente)
Paso: Instalar un cliente MQTT (Python, Java, Node.js, etc.) y conectarlo al broker.
Verificación: Suscribirte a un tópico (ejemplo: test) y publicar un mensaje (ejemplo: Hola Mundo!) para confirmar que el broker lo recibe y lo reenvía.

Ejemplo en imagen: Muestra un cliente web conectado (The WebClient is connected) y recibiendo un mensaje en el tópico test.
## poner las capturas de pantalla
<img width="1363" height="704" alt="Captura de pantalla 2025-11-13 104659" src="https://github.com/user-attachments/assets/88783e17-6b18-41d3-a15d-72a0ef5c496c" />



4) Arquitectura Funcional
4a) Comunicación Directa (Punto a Punto simulado):
Crea el Dispositivo A que publica en el tópico lan/deviceA/status.
Crea el Dispositivo B que se suscribe al tópico lan/deviceA/status y muestra los mensajes.

4b) Broadcasting:

Crea el tópico general lan/broadcast/# (el # es un comodín de múltiples niveles).
Configura al menos dos clientes para suscribirse a lan/broadcast/#.
Desde un cliente "central", publica mensajes en lan/broadcast/all.
Ambos clientes suscritos a lan/broadcast/# recibirán el mensaje publicado en lan/broadcast/all.


## Imagenes del punto 4
<img width="1361" height="706" alt="Captura de pantalla 2025-11-13 110355" src="https://github.com/user-attachments/assets/632e0d8f-fd02-4be6-a8ed-f81605f0e75e" />

<img width="1365" height="715" alt="Captura de pantalla 2025-11-13 110422" src="https://github.com/user-attachments/assets/f9591b50-466f-411d-8f27-1584fda0b0cc" />


