 # Trabajo Practico N°5

**Nombres**

- Constanza Medran  
- Fabian N Hidalgo  
- Juan I Vizgarra  
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba - Facultad de Ciencias Exactas Fisicas y Naturales**  

**Comunicaciones de Datos** 

**Santiago M. Henn - Miguel Solinas** 

**16/11/2025**

---

### Información de los autores

* **Información de contacto**: *victoria.castro@mi.unc.edu.ar - fabian.hidalgo@mi.unc.edu.ar - constanza.medran@mi.unc.edu.ar - juan.vizgarra@mi.unc.edu.ar*

---

## Resumen

En este trabajo práctico se implementa y analiza el funcionamiento del protocolo MQTT dentro de una red local simulada, empleando el modelo de comunicación Publish/Subscribe. 

Se despliega un broker MQTT —local o cloud— y se configuran múltiples clientes que actúan como dispositivos IoT, publicando y recibiendo información en distintos tópicos jerárquicos. 

Se experimenta con publicaciones directas, broadcasting mediante comodines y recolección centralizada de datos en un gateway. 

Además, se capturan paquetes de red para estudiar la estructura del protocolo y se evalúan aspectos de integridad, disponibilidad, confidencialidad y QoS. 

El objetivo final es comprender el comportamiento de sistemas IoT basados en mensajería ligera y su aplicación en arquitecturas distribuidas.

**Palabras clave:** *MQTT, IoT, publish/subscribe, broker, tópicos, QoS, mensajería ligera, simulación de red, protocolos IoT, captura de paquetes.*

---

## Introducción

El rápido crecimiento del Internet de las Cosas (IoT) ha impulsado la necesidad de protocolos de comunicación eficientes, ligeros y escalables. En este contexto, MQTT (Message Queuing Telemetry Transport) se ha consolidado como uno de los estándares más utilizados debido a su bajo consumo de ancho de banda, su simplicidad y su orientación a escenarios donde los dispositivos poseen recursos limitados.

Este trabajo práctico tiene como finalidad introducir el uso de MQTT en una red local simulada, utilizando un broker como punto central de mensajería y distintos clientes que actúan como publicadores y suscriptores. Mediante esta práctica se experimenta con tópicos jerárquicos, comodines, niveles de QoS y captura de paquetes, permitiendo observar el comportamiento real del protocolo en una arquitectura pub/sub.

Asimismo, se busca desarrollar criterios para evaluar las ventajas y limitaciones del modelo Publish/Subscribe frente al modelo cliente-servidor tradicional, especialmente en lo referido a escalabilidad, desacoplamiento, fiabilidad y seguridad. De este modo, el trabajo permite comprender los fundamentos técnicos que sustentan gran parte de las plataformas IoT modernas.

---

## Marco Teorico

### MQTT y el modelo Publish/Subscribe

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero orientado al transporte eficiente de datos entre dispositivos IoT que utiliza el patrón Publish/Subscribe (Pub/Sub). Está diseñado para funcionar sobre redes inestables o con bajo ancho de banda, lo que lo convierte en una opción ideal para sensores, actuadores y sistemas embebidos.

### Broker MQTT

El broker actúa como intermediario en la comunicación y es responsable de gestionar las suscripciones, recibir y reenviar mensajes, aplicar los niveles de QoS, mantener sesiones persistentes, controlar permisos y autenticación.

### Tópicos, Jerarquías y Comodines

Los tópicos representan canales lógicos de comunicación y están organizados en estructuras jerárquicas (por ejemplo: lan/sala1/sensor/temp). MQTT permite:
- Comodín “+” → Matchea un nivel único de la jerarquía.
- Comodín “#” → Matchea todos los niveles inferiores.

Esto facilita la implementación de broadcast y routing lógico dentro de una red.

### QoS – Quality of Service

MQTT define tres niveles de fiabilidad:
- QoS 0: "At most once" – sin confirmación.
- QoS 1: "At least once" – recibe confirmación, puede haber duplicados.
- QoS 2: "Exactly once" – evita duplicados, mayor costo.

El nivel de QoS seleccionado influye directamente en la confiabilidad de la comunicación y en la carga del broker.

---

## Resultados
 
### Características de MQTT

Protocolo: Message Queuing Telemetry Transport (MQTT).

Diseño: Es un protocolo de mensajería ligero, diseñado para dispositivos con recursos limitados y redes de baja calidad (alto latencia/bajo ancho de banda).

Modelo: Sigue el patrón Publish/Subscribe (Pub/Sub).

Ventajas: Bajo consumo de energía, uso eficiente del ancho de banda, baja sobrecarga (overhead), confiabilidad definida por niveles de QoS.

Desventajas: Dependencia de un broker central, no está diseñado para el intercambio de grandes volúmenes de datos.

Usos Principales: Internet de las Cosas (IoT), telemetría, sistemas de monitoreo y control remoto, aplicaciones móviles.

#### ¿Qué es el patrón de diseño Pub/Sub?

Es un modelo de comunicación asíncrona donde los remitentes de los mensajes (Publishers) no se programan para enviar sus mensajes a receptores específicos.

En este patron los mensajes son publicados en categorías conocidas como tópicos y los receptores (Subscribers) expresan interés en uno o más tópicos. 

Un componente intermedio (Broker) filtra los mensajes según los tópicos y los distribuye a los Subscribers.

Se diferencia del modelo tradicional Cliente-Servidor en que el remitente y el receptor no tienen conocimiento directo entre sí (desacoplamiento)

### Instalar y Ejecutar un Broker

Configuramos y ejecutamos un broker MQTT con HiveMQ:

<img width="1312" height="578" alt="image" src="https://github.com/user-attachments/assets/b07b401e-1a70-4245-8d6a-842e3f2b406e" />
<img width="689" height="564" alt="image" src="https://github.com/user-attachments/assets/0fd88cdc-48a4-409a-a270-c133f39ef7c4" />

Para el cual tenemos los siguientes detalles de la conexión:
- URL: af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud 
- Port: 8883 
- WebSocket Port: 8884 

Estos datos son los necesarios para que tus clientes se conecten al broker.

### Verificar Funcionamiento (Conexión Cliente)

Instalamos un cliente MQTT en python y lo conectamos al broker, intentado suscribirnos a un tópico y publicar un mensaje para confirmar que el broker lo recibe y lo reenvía.

<img width="1363" height="704" alt="Captura de pantalla 2025-11-13 104659" src="https://github.com/user-attachments/assets/88783e17-6b18-41d3-a15d-72a0ef5c496c" />

En la imagen podemos observar un cliente web conectado (The WebClient is connected) y recibiendo un mensaje en el tópico test.

### Arquitectura Funcional

#### Comunicación Directa (Punto a Punto simulado):

- Creamos el Dispositivo A que publica en el tópico lan/deviceA/status.
- Creamos el Dispositivo B que se suscribe al tópico lan/deviceA/status y muestra los mensajes.

<img width="1300" height="297" alt="image" src="https://github.com/user-attachments/assets/36c675cd-718e-4eb6-9fb9-6c5e29e0c7d0" />
<img width="1363" height="698" alt="image" src="https://github.com/user-attachments/assets/e7fa13e3-bcd3-4c79-abbf-a2fa903dab70" />

#### Broadcasting:

- Creamos el tópico general lan/broadcast/# (el # es un comodín de múltiples niveles).
- Configuramos dos clientes para suscribirse a lan/broadcast/#.
- Desde un cliente "central", publicamos mensajes en lan/broadcast/all.
- Ambos clientes suscritos a lan/broadcast/# reciben el mensaje publicado en lan/broadcast/all.

<img width="1296" height="297" alt="image" src="https://github.com/user-attachments/assets/3a6f0a7e-a4a2-4db9-bdbb-a5213eaf3a11" />
<img width="1414" height="777" alt="image" src="https://github.com/user-attachments/assets/87f388a7-e6e9-47ff-b02d-9a55d82baf59" />
<img width="1416" height="778" alt="image" src="https://github.com/user-attachments/assets/a9564b0c-9905-414b-9b72-fed651cc6bcd" />


### Jerarquia de Topicos

A continuacion implementamos una jerarquia de topicos para registrar datos (simulados) de temperatura y humedad en distintas salas:
- lan/sala1/sensor/temp
- lan/sala1/sensor/hum
- lan/sala2/sensor/temp

Para esto generamos publishers que simulan sensores que toman datos de temperatura o humedad y los publican a su topico correspondiente, particularmente:
- temperature_sensor: lan/sala1/sensor/temp
- temperature_sensor: lan/sala2/sensor/temp
- humidity_sensor: lan/sala1/sensor/hum

Estos datos son recibidos en un gateway que obtiene los datos de todas las salas y todos los sensores, para lo cual nos subscribimos al topico jerarquico:
- lan/+/sensor/+

Este gateway registra los datos en un csv para su posterior visualizacion en Grafana.

### Q&A

a) ¿Sobre qué protocolos de capa de transporte están trabajando en esta actividad?

...

b) ¿Qué pueden decir sobre la garantía de Integridad, Confidencialidad y Disponibilidad en esta
arquitectura?

...

c) ¿Qué rol juegan los niveles de QoS en la fiabilidad de los mensajes?

...

d) ¿Qué ventajas ofrece el modelo pub/sub frente al modelo cliente-servidor?

...

e) ¿Qué limitaciones tiene MQTT respecto a una red LAN real?

...

f) ¿Qué implicaciones tiene depender de un broker central para la comunicación?

...

---

## Discusión y conclusiones

---

## Referencias
